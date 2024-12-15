class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://judge.me"

    def navigate(self, path=""):
        self.page.goto(f"{self.base_url}{path}")

    def wait_for_selector(self, selector, timeout=5000):
        return self.page.wait_for_selector(selector, timeout=timeout)




