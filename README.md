# Labeled footnotes for Marko

> An extension that adds labeled footnotes to the Python Markdown parser
> [Marko](https://github.com/frostming/marko/).

## Usage

```python
from marko import Markdown
markdown = Markdown()
markdown.use("labeled_footnote")

text = 'this is a labeled footnote[^10=Doe, 1998].\n\n[^10=Doe, 1998]: foo\n'
markdown = Markdown(extensions=['labeled_footnote'])
print(markdown(text))
```
