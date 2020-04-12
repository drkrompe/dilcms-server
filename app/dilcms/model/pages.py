import uuid
import json

from .page import Page

class Pages():

    def __init__(self):
        self._pages = {}

    def add_page(self, page: Page):
        self._pages[page._page_path] = page

    def get_pages(self):
        return self._pages

    def get_page(self, page_path: str) -> Page:
        return self._pages[page_path]