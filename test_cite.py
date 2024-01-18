import markdown
import pytest
from mdx_cite import CiteExtension


def _mark_down(md_str):
    return markdown.markdown(md_str, extensions=[CiteExtension()])

def test_no_citation():
    md = _mark_down('foo bar')
    assert md =='<p>foo bar</p>'