import os
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from tools import generate_index

def create_html(path, title="Title", desc="Desc"):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"<h1>{title}</h1>\n<p>{desc}</p>")

def test_build_list_and_parse(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    create_html(d / "01_test.html", "T1", "D1")
    create_html(d / "02_test.html", "T2", "D2")
    create_html(d / "index.html", "IDX", "Should be ignored")
    items = generate_index.build_list(str(d))
    assert items[0][0] == "01_test.html"
    assert items[0][1] == "T1"
    assert items[0][2] == "D1"
    # index.html should be ignored
    assert len(items) == 2

def test_write_sub_index(tmp_path):
    d = tmp_path / "chap"
    d.mkdir()
    create_html(d / "01.html", "A", "B")
    generate_index.write_sub_index(str(d), "Heading")
    index = (d / "index.html").read_text(encoding="utf-8")
    assert "Heading" in index
    assert "01.html" in index

