from pages.base_page import Page


class FilterBySalePage(Page):

    def open(self):
        self.open_url('https://soft.reelly.io')
