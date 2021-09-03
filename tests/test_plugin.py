#! -*- coding: utf-8 -*-

from marko import Markdown


class TestLabeledFootnote:
    def setup_method(self):
        self.markdown = Markdown()
        self.markdown.use("labeled_footnote")

    def test_basic_example_renders(self):
        result = self.markdown(
            "this is a labeled footnote[^10=Doe, 1998].\n\n[^10=Doe, 1998]: foo\n"
        )
        assert '<sup class="footnote-ref"' in result
        assert 'href="#fn-10">Doe, 1998</a' in result
        assert 'id="fnref-10"' in result
        assert 'foo<a href="#fnref-10" class="footnote">&#8617;</a>' in result
