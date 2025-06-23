#!/usr/bin/env python3
import os
import re


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
    lines = [f'<section id="toc-{directory}">', f'  <h2>{heading}</h2>', '  <ul>']
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
    header = f"""<!DOCTYPE html>
<html lang=\"de\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{heading}</title>
    <link rel=\"stylesheet\" href=\"../style.css\">
</head>
<body>
<header>
    <h1>{heading}</h1>
</header>
<main>
  <ul id=\"chapter-list\">
"""
    footer = """
  </ul>
  <p><a href=\"../index.html\">&larr; Zurück zur Übersicht</a></p>
</main>
</body>
</html>
"""
    lines = [header]
    for fname, title, desc in items:
        lines.append('    <li>')
        lines.append(f'      <a href="{fname}">')
        lines.append(f'        <h3>{title}</h3>')
        if desc:
            lines.append(f'        <p>{desc}</p>')
        lines.append('      </a>')
        lines.append('    </li>')
    lines.append(footer)
    with open(os.path.join(directory, 'index.html'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    header = """<!DOCTYPE html>
<html lang=\"de\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Lernplan: Programmieren 2 (C & C++)</title>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
<header>
    <h1>Programmieren 2</h1>
    <p>Dein interaktiver Lernpfad für C und C++</p>
</header>
<main>
"""
    footer = """
    <section id=\"pdf-downloads\">
        <h2>PDF-Materialien</h2>
        <p>Alle Foliensätze und Übungsblätter findest du im <a href=\"material/\">Ordner material</a>.</p>
    </section>
</main>
<footer>
    <p>&copy; 2025 - Dein persönlicher Programmier-Tutor</p>
</footer>
</body>
</html>
"""
    sections = []
    sections.append(build_section('c', 'Themenübersicht - Teil 1: C'))
    sections.append(build_section('cpp', 'Themenübersicht - Teil 2: C++'))
    content = header + '\n'.join(sections) + footer
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    write_sub_index('c', 'C Kapitel')
    write_sub_index('cpp', 'C++ Kapitel')


if __name__ == '__main__':
    main()
