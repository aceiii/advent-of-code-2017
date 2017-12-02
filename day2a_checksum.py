#!/usr/bin/env python
# pylint: disable=all

import sys


def spreadsheet_checksum(sheet):
    line_checks = []
    for line in sheet:
        cells = map(int, [c for c in line.strip().split(" ") if c != ''])
        line_checks.append((max(cells) - min(cells)) if len(cells) > 0 else 0)
    return sum(line_checks)


def main():
    print spreadsheet_checksum(sys.stdin)


if __name__ == "__main__":
    main()
