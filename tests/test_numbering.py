import os
import re

def extract_numbers(names, pattern):
    nums = []
    for n in names:
        m = re.search(pattern, n)
        if m:
            nums.append(int(m.group(1)))
    return sorted(nums)


def test_sequential_chapter_numbers():
    c_files = [f for f in os.listdir('c') if f.endswith('.html') and f != 'index.html']
    cpp_files = [f for f in os.listdir('cpp') if f.endswith('.html') and f != 'index.html']
    c_nums = extract_numbers(c_files, r'^(\d+)')
    cpp_nums = extract_numbers(cpp_files, r'kapitel-(\d+)')
    assert c_nums == list(range(1, len(c_nums)+1))
    assert cpp_nums == list(range(1, len(cpp_nums)+1))


def test_pdf_material_available():
    c_pdfs = [f for f in os.listdir('material/c') if f.lower().endswith('.pdf')]
    cpp_pdfs = [f for f in os.listdir('material/cpp') if f.lower().endswith('.pdf')]
    c_nums = extract_numbers(c_pdfs, r'KE(\d{2})')
    cpp_nums = extract_numbers(cpp_pdfs, r'KE(\d{2})')
    for i in range(1, 13):
        assert i in c_nums
        assert i in cpp_nums
