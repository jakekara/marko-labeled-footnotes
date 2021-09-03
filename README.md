# Labeled footnotes for Marko

> An extension that adds labeled footnotes to the Python Markdown parser
> [Marko](https://github.com/frostming/marko/).

## Usage

There are two forms for the syntax fo a labeled footnote. You can use `[^label-text]` or [^label-id=label-text] where `label-id` is unique to the document.

```python
from marko import Markdown
markdown = Markdown()
markdown.use("labeled_footnote")

text = 'this is a labeled footnote[^10=Doe, 1998].\n\n[^10=Doe, 1998]: foo\n'
markdown = Markdown(extensions=['labeled_footnote'])
print(markdown(text))
```
