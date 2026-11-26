#!/usr/bin/env python3
"""The Router Confesses (make.fun).

Writes the entry -- one original line -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = "I didn't drop your Wi-Fi during the climax out of spite — after three years of being unplugged, rebooted, and blamed for everything, I just wanted one dramatic exit."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
