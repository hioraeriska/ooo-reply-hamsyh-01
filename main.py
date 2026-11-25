"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single out-of-office auto-reply line to /output/entry.txt.
The reply is a fresh turn on the usual away message: no beach, no inbox,
no limited-email line — just a to-do list that has moved on.
"""

import os

REPLY = "I'm out of office until Monday. My to-do list and I have agreed to see other people."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def check_reply(text: str) -> None:
    """Enforce the bounty gate before writing: 1-160 chars, one line."""
    if not 1 <= len(text) <= 160:
        raise ValueError(f"reply is {len(text)} chars, gate needs 1-160")
    if text.strip() == "":
        raise ValueError("reply must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")


def main() -> int:
    check_reply(REPLY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REPLY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
