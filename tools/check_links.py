#!/usr/bin/env python3
"""Prüft alle lokalen Links in HTML-Dateien.

Das Skript durchläuft das übergebene Verzeichnis (standardmäßig das
Repository-Wurzelverzeichnis) und meldet nicht gefundene Dateien.
"""
import os
import sys
from html.parser import HTMLParser
from typing import List, Tuple

class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: List[str] = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.links.append(value)


def iter_html_files(root: str):
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".html"):
                yield os.path.join(dirpath, name)


def check_links(root: str) -> List[Tuple[str, str]]:
    broken: List[Tuple[str, str]] = []
    for html_file in iter_html_files(root):
        with open(html_file, encoding="utf-8") as f:
            parser = LinkCollector()
            parser.feed(f.read())
        for href in parser.links:
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(html_file), href))
            if not os.path.exists(target):
                broken.append((html_file, href))
    return broken


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    broken = check_links(root)
    if broken:
        print("Broken links found:")
        for html, href in broken:
            print(f"{html}: {href}")
        sys.exit(1)
    print("All links are valid.")


if __name__ == "__main__":
    main()
