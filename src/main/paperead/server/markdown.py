import pathlib
import re

from marko import Markdown
from marko.md_renderer import MarkdownRenderer

regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class CustomMDRenderer(MarkdownRenderer):
    def resolve_link_dest(self, dest: str) -> str:
        return dest

    def render_link(self, element):
        element.dest = self.resolve_link_dest(element.dest)

        return super().render_link(element)

    def render_auto_link(self, element):
        element.dest = self.resolve_link_dest(element.dest)

        return super().render_auto_link(element)

    def render_image(self, element):
        element.dest = self.resolve_link_dest(element.dest)

        return super().render_image(element)


def rewriteMarkdownWithBaseUrl(text: str, baseUrl: str) -> str:

    class MDRenderer(CustomMDRenderer):
        def resolve_link_dest(self, dest: str) -> str:
            dest = dest.replace("\\", "/")

            if regex.match(dest) or pathlib.Path(dest).is_absolute():
                return dest

            dest = f"{baseUrl}/{dest}"
            return dest

    worker = Markdown(renderer=MDRenderer)
    return worker(text)


def rewriteBackMarkdownWithBaseUrl(text: str, baseUrl: str) -> str:

    class MDRenderer(CustomMDRenderer):
        def resolve_link_dest(self, dest: str) -> str:
            burl = f"{baseUrl}/"
            if dest.startswith(burl):
                return dest.replace(burl, "", 1)
            return dest

    worker = Markdown(renderer=MDRenderer)
    return worker(text)


if __name__ == "__main__":
    b = "http://localhost"
    r = rewriteMarkdownWithBaseUrl("""
![](a.py)
""", b)
    rb = rewriteBackMarkdownWithBaseUrl(r, b)

    print(r)
    print(rb)
