#!/usr/bin/env python3
import os
import re
import datetime
from string import Template


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


def load_template(name: str) -> Template:
    with open(os.path.join(TEMPLATE_DIR, name), encoding="utf-8") as f:
        return Template(f.read())


def parse_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    title_match = re.search(r'<h1>(.*?)</h1>', text, re.S)
    desc_match = re.search(r'<h1>.*?</h1>\s*<p>(.*?)</p>', text, re.S)
    title = title_match.group(1).strip() if title_match else os.path.basename(path)
    desc = desc_match.group(1).strip() if desc_match else ''
    return title, desc


def build_list(directory):
    def sort_key(name: str) -> int:
        m = re.search(r"(\d+)", name)
        return int(m.group(1)) if m else 0

    items = []
    for filename in sorted(os.listdir(directory), key=sort_key):
        if filename.endswith(".html") and filename != "index.html":
            title, desc = parse_file(os.path.join(directory, filename))
            items.append((filename, title, desc))
    return items


def build_section(directory, heading):
    items = build_list(directory)
    lines = [f'<section id="toc-{directory}">', f'  <h2>{heading}</h2>', '  <ul class="chapter-list">']
    for fname, title, desc in items:
        lines.append('    <li>')
        lines.append(f'      <a href="{directory}/{fname}">')
        lines.append(f'        <h3>{title}</h3>')
        if desc:
            lines.append(f'        <p>{desc}</p>')
        lines.append('      </a>')
        lines.append('    </li>')
    lines.append('  </ul>')
    lines.append('</section>')
    return '\n'.join(lines)


def write_sub_index(directory, heading):
    items = build_list(directory)
    li_lines = []
    for fname, title, desc in items:
        li_lines.append('    <li>')
        li_lines.append(f'      <a href="{fname}">')
        li_lines.append(f'        <h3>{title}</h3>')
        if desc:
            li_lines.append(f'        <p>{desc}</p>')
        li_lines.append('      </a>')
        li_lines.append('    </li>')

    tpl = load_template('sub_index.html')
    html = tpl.substitute(heading=heading, items='\n'.join(li_lines))
    with open(os.path.join(directory, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    sections = []
    sections.append(build_section('c', 'Themenübersicht - Teil 1: C'))
    sections.append(build_section('cpp', 'Themenübersicht - Teil 2: C++'))
    tpl = load_template('index.html')
    year = datetime.date.today().year
    html = tpl.substitute(sections='\n'.join(sections), year=year)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    write_sub_index('c', 'C Kapitel')
    write_sub_index('cpp', 'C++ Kapitel')


if __name__ == '__main__':
    main()
