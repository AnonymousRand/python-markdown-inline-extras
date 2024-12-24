from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor


class StrikethroughExtension(Extension):
    def extendMarkdown(self, md):
        """
        Strikes through text.
        
        Usage:
            ```
            ~~<text>~~
            ```
        """
        regex = r"()~~([\S\s]+?)~~"
        md.inlinePatterns.register(SimpleTagInlineProcessor(regex, "del"), "strikethrough", 2)
