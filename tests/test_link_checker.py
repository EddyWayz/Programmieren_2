import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from tools.check_links import check_links

def test_link_checker(tmp_path):
    html_dir = tmp_path / "html"
    html_dir.mkdir()
    target = html_dir / "target.html"
    target.write_text("<p>ok</p>", encoding="utf-8")
    valid = html_dir / "valid.html"
    valid.write_text('<a href="target.html">Good</a>', encoding='utf-8')
    invalid = html_dir / "invalid.html"
    invalid.write_text('<a href="missing.html">Bad</a>', encoding='utf-8')
    broken = check_links(str(tmp_path))
    assert (str(invalid), 'missing.html') in broken
    assert not any(b[0] == str(valid) for b in broken)
