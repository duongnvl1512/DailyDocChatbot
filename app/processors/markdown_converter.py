from markdownify import markdownify


class MarkdownConverter:
    """
    Convert clean HTML to Markdown.
    """

    def convert(self, html: str) -> str:

        markdown = markdownify(
            html,
            heading_style="ATX",
        )

        return markdown.strip()