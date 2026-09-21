from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url