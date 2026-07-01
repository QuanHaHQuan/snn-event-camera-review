#!/usr/bin/env python3
"""Commit local changes and optionally push through Git over SSH.

This helper intentionally uses plain Git only. It does not use GitHub CLI and it
will not create a GitHub repository.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def has_changes(repo_root: Path) -> bool:
    result = run(["git", "status", "--porcelain"], repo_root)
    return bool(result.stdout.strip())


def remote_exists(repo_root: Path, remote: str) -> bool:
    result = run(["git", "remote"], repo_root)
    remotes = {line.strip() for line in result.stdout.splitlines() if line.strip()}
    return remote in remotes


def main() -> int:
    parser = argparse.ArgumentParser(description="Commit and optionally push workflow changes.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument("--message", default="Update literature review workflow", help="Commit message")
    parser.add_argument("--remote", default="origin", help="Git remote name")
    parser.add_argument("--branch", default="main", help="Branch to push")
    parser.add_argument("--remote-url", help="Optional SSH remote URL to add if the remote is absent")
    parser.add_argument("--push", action="store_true", help="Push after committing")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    if not (repo_root / ".git").exists():
        run(["git", "init", "-b", args.branch], repo_root)

    if args.remote_url and not remote_exists(repo_root, args.remote):
        run(["git", "remote", "add", args.remote, args.remote_url], repo_root)

    if has_changes(repo_root):
        run(["git", "add", "-A"], repo_root)
        run(["git", "commit", "-m", args.message], repo_root)
    else:
        print("No local changes to commit.")

    if args.push:
        if not remote_exists(repo_root, args.remote):
            raise SystemExit(f"Remote '{args.remote}' is not configured. Add an SSH remote first.")
        run(["git", "push", "-u", args.remote, args.branch], repo_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
