"""
Footnotes extension
~~~~~~~~~~~~~~~~~~~

Enable footnotes parsing and renderering in Marko.

Usage::

    from marko import Markdown

    text = 'Foo[^1=footnote-1]\\n\\n[^1=footnote-1]: This is a footnote.\\n'
    markdown = Markdown(extensions=['footnote'])
    print(markdown(text))

"""
import re
from marko import block, inline, helpers
from urllib.parse import unquote


class Document(block.Document):
    def __init__(self, text):
        self.footnotes = {}
        super().__init__(text)


class FootnoteDef(block.BlockElement):

    pattern = re.compile(r" {,3}\[\^([^\]]+)\]:[^\n\S]*(?=\S| {4})")
    priority = 6

    def __init__(self, match):
        raw_label = helpers.normalize_label(match.group(1))
        if "=" in raw_label:
            id, display_label = match.group(1).split("=")
            display_label = unquote(display_label)
            id = helpers.normalize_label(id)

        else:
            display_label = raw_label
            id = raw_label
        self.label = raw_label
        self.display = display_label
        self.id = id

        self._prefix = re.escape(match.group())
        self._second_prefix = r" {1,4}"

    @classmethod
    def match(cls, source):
        return source.expect_re(cls.pattern)

    @classmethod
    def parse(cls, source):
        state = cls(source.match)
        with source.under_state(state):
            state.children = block.parser.parse(source)
        source.root.footnotes[state.label] = state
        return state


class FootnoteRef(inline.InlineElement):

    pattern = re.compile(r"\[\^([^\]]+)\]")
    priority = 6

    def __init__(self, match):

        raw_label = helpers.normalize_label(match.group(1))
        if "=" in raw_label:
            id, display_label = match.group(1).split("=")
            display_label = unquote(display_label)
            id = helpers.normalize_label(id)
        else:
            display_label = raw_label
            id = raw_label

        self.label = raw_label
        self.display = display_label
        self.id = id

    @classmethod
    def find(cls, text):
        for match in super().find(text):
            label = helpers.normalize_label(match.group(1))
            if label in inline._root_node.footnotes:
                yield match


class FootnoteRendererMixin:
    def __init__(self):
        super().__init__()
        self.footnotes = []

    def render_footnote_ref(self, element):

        if element.label not in self.footnotes:
            self.footnotes.append(element.label)

        return (
            '<sup class="footnote-ref" id="fnref-{id}">'
            '<a href="#fn-{id}">{lab}</a></sup>'.format(
                lab=element.display, id=self.escape_url(element.id)
            )
        )

    def render_footnote_def(self, element):
        return ""

    def _render_footnote_def(self, element):
        children = self.render_children(element).rstrip()
        back = f'<a href="#fnref-{element.id}" class="footnote">&#8617;</a>'
        if children.endswith("</p>"):
            children = re.sub(r"</p>$", f"{back}</p>", children)
        else:
            children = f"{children}<p>{back}</p>\n"
        return '<li id="fn-{}" data-label="{}">\n{}</li>\n'.format(
            self.escape_url(element.id), self.escape_url(element.display), children
        )

    def render_document(self, element):
        text = self.render_children(element)
        items = [self.root_node.footnotes[label] for label in self.footnotes]
        if not items:
            return text
        children = "".join(self._render_footnote_def(item) for item in items)
        footnotes = f'<div class="footnotes">\n<ol>\n{children}</ol>\n</div>\n'
        self.footnotes = []
        return text + footnotes


class LabeledFootnote:
    elements = [Document, FootnoteDef, FootnoteRef]
    renderer_mixins = [FootnoteRendererMixin]


def make_extension():
    return LabeledFootnote()
