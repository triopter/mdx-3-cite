# Cite Extension for Python-Markdown v3

Meant to replace the original [mdx_cite](https://github.com/aleray/mdx_cite) extension, which is not maintaine, nor compatible with python-markown v3+

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






