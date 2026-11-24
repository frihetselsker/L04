"""Homework helpers: skill 3 (bug fixer), similar to what was at the lab"""
import ast
import os
import re
import shutil
import tempfile

from lab_helpers import S, ask, check, clean_code, sh, skill, split_reports


def _numbered(code):
    return "\n".join(f"{i:3d} | {l}" for i, l in enumerate(code.splitlines(), 1))


def _strip_numbers(code):
    """Removes '  3 | ' prefixes if the model copied the line numbers."""
    lines = code.splitlines()
    if lines and all(re.match(r"\s*\d+\s*\|", l) or not l.strip() for l in lines):
        lines = [re.sub(r"^\s*\d+\s*\| ?", "", l) for l in lines]
    return "\n".join(lines)


def fix_bugs(file):
    """Runs your bug-fixer skill on the bug reports and writes the fixed file.
    The original is kept in originals/<file> the first time."""
    name = file.replace(".py", "")
    path = f"reports/{name}.md"
    if not os.path.exists(path):
        return check("bug reports found", False, f'run find_bugs("{file}") first')
    os.makedirs("originals", exist_ok=True)
    if not os.path.exists(f"originals/{file}"):
        shutil.copy(file, f"originals/{file}")
    original = open(f"originals/{file}").read()
    reports = "\n\n".join(split_reports(open(path).read()))
    answer = ask(skill("bug-fixer"), f"## The file {file}\n{_numbered(original)}\n\n## Bug reports\n{reports}",
                 max_new_tokens=1500)
    fixed = _strip_numbers(clean_code(answer)).strip() + "\n"
    try:
        compile(fixed, file, "exec")
    except SyntaxError as e:
        print(fixed)
        return check("the fixed file is valid Python", False, f"{e}: improve your bug-fixer skill and run again")
    with open(file, "w") as f:
        f.write(fixed)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as t:
        t.write(original)
    print(sh(f"diff -u --label original --label fixed {t.name} {file}"))
    os.unlink(t.name)
    return check(f"fixed file written to {file} (original kept in originals/{file})", True)


# ---------------------------------------------------------------- final check

HIDDEN = {
    "celsius_to_fahrenheit": lambda m: m.celsius_to_fahrenheit(100) == 212 and m.celsius_to_fahrenheit(0) == 32,
    "is_teenager": lambda m: all(m.is_teenager(a) is v for a, v in [(12, False), (13, True), (19, True), (20, False)]),
    "max_of_list": lambda m: m.max_of_list([-3, -1, -7]) == -1 and m.max_of_list([1, 5, 2]) == 5,
    "last_n": lambda m: m.last_n([1, 2, 3], 0) == [] and m.last_n([1, 2, 3], 2) == [2, 3],
    "load_settings": lambda m: (m.load_settings('{"volume": 5, "dark": true}') == {"volume": 5, "dark": True}
                                and "eval(" not in open(m.__file__).read()),
}
LEVEL = {"celsius_to_fahrenheit": "easy", "is_teenager": "medium", "max_of_list": "medium",
         "last_n": "hard", "load_settings": "hard"}


def _functions(code):
    """{function name: (first line, last line)}"""
    return {n.name: (n.lineno, n.end_lineno) for n in ast.parse(code).body if isinstance(n, ast.FunctionDef)}


def _pytest_status(cwd, test_file):
    out = sh(f"python -m pytest {test_file} -q -rA --no-header -p no:cacheprovider", cwd=cwd)
    return {l.split(" ", 1)[1].split(" - ")[0].split("::")[-1]: l.split(" ", 1)[0] for l in out.splitlines()
            if l.startswith(("PASSED", "FAILED", "ERROR"))}


def check_homework(file="homework.py"):
    """For each function: did the AI find the bug, is the AI fix right, is the AI test good?
    Prints a summary and the rows for the Typst report."""
    import importlib, sys
    name = file.replace(".py", "")
    original = open(f"originals/{file}").read() if os.path.exists(f"originals/{file}") else None
    if original is None:
        return check("original kept", False, f'run fix_bugs("{file}") first')
    funcs = _functions(original)

    reports = split_reports(open(f"reports/{name}.md").read()) if os.path.exists(f"reports/{name}.md") else []
    report_fn = {}
    for k, r in enumerate(reports, 1):
        line = int(re.search(r"Line:\s*(\d+)", r).group(1))
        report_fn[k] = next((f for f, (a, b) in funcs.items() if a <= line <= b), None)

    sys.modules.pop(name, None)
    mod = importlib.import_module(name)

    before, after = {}, {}
    if os.path.exists(f"tests/test_{name}.py"):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree("tests", f"{tmp}/tests")
            open(f"{tmp}/{file}", "w").write(original)
            before = _pytest_status(tmp, f"tests/test_{name}.py")
        after = _pytest_status(".", f"tests/test_{name}.py")

    rows = []
    for fn in funcs:
        found = [k for k, f in report_fn.items() if f == fn]
        fixed = False
        try:
            fixed = bool(HIDDEN[fn](mod))
        except Exception:
            pass
        tests = [t for t in after if any(t.startswith(f"test_r{k}_") for k in found)]
        good = [t for t in tests if after[t] == "PASSED" and before.get(t) in ("FAILED", "ERROR")]
        rows.append((fn, LEVEL.get(fn, "?"), bool(found), fixed, f"{len(good)}/{len(tests)}" if tests else "0/0",
                     bool(tests) and len(good) == len(tests)))

    print(f"{'function':24}{'level':8}{'found':7}{'fixed':7}{'good tests'}")
    for fn, lv, fo, fx, gt, ok in rows:
        print(f"{fn:24}{lv:8}{'yes' if fo else 'NO':7}{'yes' if fx else 'NO':7}{gt}")
    extra = [k for k, f in report_fn.items() if f is None]
    if extra:
        print(f"\nreports outside any function: {extra}")
    print(f"\nbug reports: {len(reports)}   found: {sum(r[2] for r in rows)}/5   fixed: {sum(r[3] for r in rows)}/5"
          f"   good tests: {sum(r[5] for r in rows)}/5")
    return rows
