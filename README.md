# <cite> Extension for Python-Markdown v3

Dead-simple extension meant to replace the original [mdx_cite](https://github.com/aleray/mdx_cite) extension, which is not maintained, nor compatible with [python-markown](https://github.com/Python-Markdown/markdown) v3+

## Installation

```sh
pip install git+https://github.com/triopter/mdx-3-cite.git#egg=mdx_cite
```

## Usage

```python
>>> import markdown
>>> src = '"""Who Is Killing the Great Chefs of Europe?""" is the last movie I watched.'
>>> html = markdown.markdown(src, extensions=['mdx_cite'])
>>> print(html)
<p><cite>Who Is Killing the Great Chefs of Europe?</cite> is the last movie I watched.</p>
```






