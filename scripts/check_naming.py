"""Check tracked filenames, the branch name, and the PR title against NAMING.md."""

import os
import re
import subprocess
import sys
from fnmatch import fnmatch
from pathlib import Path

# Names mandated by a tool or convention we do not control.
EXEMPT_FILES = {
    "README.md", "README.txt", "README.adoc", "LICENSE", "NOTICE", "CLAUDE.md",
    "AGENTS.md", "NAMING.md", "BEHAVIOR.md", "OUTPUT.md", "CODING.md",
    "WRITING.md",
    "Makefile", "Makefile.am", "Dockerfile",
    "CODEOWNERS", "CITATION.cff",
}
COMMIT_TYPES = "feat|update|fix|lint|chore|refactor"
COMMIT_RE = re.compile(rf"^({COMMIT_TYPES})\([a-z0-9._/-]+\): \S.*[^.]$")
BRANCH_RE = re.compile(rf"^(({COMMIT_TYPES})|claude)/[a-z0-9-]+$")
SNAKE_RE = re.compile(r"^[a-z0-9_]+$")
BAD_DATE_RE = re.compile(r"(?<!\d)(19|20)\d{6}(?!\d)")
# A trailing " 2" or "(2)" is a download duplicate; "_2026" is a year field and legitimate.
JUNK_RE = re.compile(r"(?:^|[ _-])(copy|final|v\d+)(?:[ _.-]|$)|\(\d+\)| \d+\.", re.I)


def ignored(path, patterns):
    return any(fnmatch(path, p) for p in patterns)


def check_path(path):
    """Yield a message for each way this repo-relative path violates NAMING.md."""
    name = Path(path).name
    if name not in EXEMPT_FILES:
        if " " in path:
            yield "contains a space"
        if not path.isascii():
            yield "contains non-ASCII characters"
        if JUNK_RE.search(name):
            yield "carries a copy/version suffix — use a date field or git"
        if BAD_DATE_RE.search(name):
            yield "has a non-ISO date — use YYYY-MM-DD"
        if name != name.lower():
            yield "contains uppercase"

    if name.endswith((".py", ".m")) and not SNAKE_RE.match(Path(name).stem):
        yield f"{Path(name).suffix} files must be snake_case — a kebab module cannot be imported"


def package_dirs(paths):
    return {str(Path(p).parent) for p in paths if Path(p).name == "__init__.py"}


def check_dirs(paths):
    packages = package_dirs(paths)
    seen = set()
    for path in paths:
        parent = Path(path).parent
        for i in range(len(parent.parts)):
            d = str(Path(*parent.parts[: i + 1]))
            if d in seen or d.startswith("."):
                continue
            seen.add(d)
            if "_" in Path(d).name and d not in packages and not Path(d).name[0].isdigit():
                yield d, "directory is snake_case but is not an importable package"


def main():
    patterns = []
    if Path(".namingignore").exists():
        patterns = [l.strip() for l in Path(".namingignore").read_text().splitlines()
                    if l.strip() and not l.startswith("#")]

    # -z: a path containing a space is exactly what this script must not lose.
    tracked = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True,
                             check=True).stdout.split("\0")
    paths = [p for p in tracked if p and not ignored(p, patterns)]

    failures = []
    for path in paths:
        failures += [(path, m) for m in check_path(path)]
    failures += list(check_dirs(paths))

    branch = os.environ.get("BRANCH_NAME", "")
    if branch and branch != "main" and not BRANCH_RE.match(branch):
        failures.append((branch, f"branch must be <{COMMIT_TYPES}|claude>/<kebab-slug>"))

    title = os.environ.get("PR_TITLE", "")
    if title and not COMMIT_RE.match(title):
        failures.append((title, f"PR title must be <{COMMIT_TYPES}>(<scope>): <description>"))

    for subject, message in failures:
        print(f"{subject}: {message}")
    if failures:
        print(f"\n{len(failures)} naming violations. See volar-robotics/.github NAMING.md.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
