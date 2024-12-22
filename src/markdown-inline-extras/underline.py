from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor


class UnderlineExtension(Extension):
    def extendMarkdown(self, md):
        """
        Underlines text.

        Usage:
            ```
            __<text>__
            ```
        """
        regex = r"()__([\S\s]+?)__"
        md.inlinePatterns.register(SimpleTagInlineProcessor(regex, "u"), "underline", 105)
