from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern


class CiteExtension(Extension):
    CITE_RE = r'(""")(.*?)"""'

    def extendMarkdown(self, md):
        pattern = SimpleTagPattern(self.CITE_RE, 'cite')
        md.inlinePatterns.register(pattern, 'cite', 55)


def makeExtension(*args, **kwargs):
    return CiteExtension(*args, **kwargs)
