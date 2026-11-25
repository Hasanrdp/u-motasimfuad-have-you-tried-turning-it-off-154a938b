#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt.

The line: the agent "escalates" the case to Tier 2, which turns out to be
the same agent again, only with a deeper voice. The humour is the agent's
cheerful uselessness, never the customer; the customer's desperation is felt
in the escalation itself, not explained. 113 characters, one line, no
trailing newline, deterministic: the same bytes on every run.
"""

import hashlib
import os
import sys

LINE = "I completely understand, and I've escalated your case to Tier 2, which is just me again, but with a deeper voice."

EXPECTED_SHA256 = "9c2763082c8f3eea299ae9d4a9928736a23a9830c1c3fb48e27d5ab31dcfe7ac"
EXPECTED_BYTES = 113
EXPECTED_CHARS = 113

# The gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
# not only white space.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 199


def check_gate(line: str) -> None:
    """The competition gate: 1-199 UTF-8 characters, not only white space."""
    if not (GATE_MIN_CHARS <= len(line) <= GATE_MAX_CHARS):
        raise SystemExit("line fails the 1-199 character gate")
    if not line.strip():
        raise SystemExit("line is only white space")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")


def verify(line: str) -> bytes:
    """Check the line against its pinned hash and size before it is written."""
    data = line.encode("utf-8")
    if len(line) != EXPECTED_CHARS:
        raise SystemExit(f"line is {len(line)} chars, expected {EXPECTED_CHARS}")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(f"line is {len(data)} bytes, expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"line sha256 {digest} != expected {EXPECTED_SHA256}")
    check_gate(line)
    return data


def main() -> None:
    data = verify(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    sys.stdout.write(f"wrote {len(data)} bytes to {path}\n")


if __name__ == "__main__":
    main()
