#!/usr/bin/env python3
"""Native messaging host for Silo. Receives a URL from Firefox and opens it with Silo."""

import json
import struct
import subprocess
import sys


def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
    length = struct.unpack("@I", raw_length)[0]
    message = sys.stdin.buffer.read(length).decode("utf-8")
    return json.loads(message)


def main():
    msg = read_message()
    if msg and "url" in msg:
        # Try system install first, fall back to cargo build
        import shutil
        silo_bin = shutil.which("silo") or "/home/fred/projects/silo/target/release/silo"
        subprocess.Popen([silo_bin, msg["url"]])


if __name__ == "__main__":
    main()
