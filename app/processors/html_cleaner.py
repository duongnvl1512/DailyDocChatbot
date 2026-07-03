from bs4 import BeautifulSoup


class HtmlCleaner:

    REMOVE_TAGS = {
        "script",
        "style",
        "iframe",
        "noscript",
    }

    def clean(self, html: str) -> str:

        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted tags
        for tag in self.REMOVE_TAGS:
            for element in soup.find_all(tag):
                element.decompose()

        # Remove unnecessary attributes
        for tag in soup.find_all(True):
            allowed = {}

            if tag.name == "a" and tag.has_attr("href"):
                allowed["href"] = tag["href"]

            elif tag.name == "img":
                if tag.has_attr("src"):
                    allowed["src"] = tag["src"]

                if tag.has_attr("alt"):
                    allowed["alt"] = tag["alt"]

            tag.attrs = allowed

        for a in soup.find_all("a"):
            if not a.attrs and not a.text.strip():
                a.decompose()
                
        for p in soup.find_all("p"):
            if not p.get_text(strip=True) and not p.find("img"):
                p.decompose()
                
        # return def clean       
        return str(soup)
        