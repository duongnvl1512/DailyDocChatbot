from app.processors.html_cleaner import HtmlCleaner
from app.processors.markdown_converter import MarkdownConverter
from app.writers.markdown_writer import MarkdownWriter
from app.models.article import Article

class DocumentService:

    def __init__(self):
        self.cleaner = HtmlCleaner()
        self.converter = MarkdownConverter()
        self.writer = MarkdownWriter()

    def export(self, article: Article):

        html = self.cleaner.clean(article.body)
        markdown = self.converter.convert(html)
        self.writer.save(article, markdown)