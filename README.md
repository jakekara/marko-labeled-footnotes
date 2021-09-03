# Labeled footnotes for Marko

> An extension that adds labeled footnotes to the Python Markdown parser
> [Marko](https://github.com/frostming/marko/).

![Unit test status](https://github.com/jakekara/marko-labeled-footnotes/actions/workflows/main.yml/badge.svg)

## Usage

There are two forms for the syntax fo a labeled footnote. You can use `[^label-text]` or `[^label-id=label-text]` where `label-id` is unique to the document.

```python
from marko import Markdown
markdown = Markdown()
markdown.use("labeled_footnote")

text = 'this is a labeled footnote[^10=Doe, 1998].\n\n[^10=Doe, 1998]: foo\n'
markdown = Markdown(extensions=['labeled_footnote'])
print(markdown(text))
```

## Development

To develop and run tests, use the following commands in your preferred
environment. I like to use venv.:

```bash
pip install -r dev_requirements
python setup.py develop
pytest
```
