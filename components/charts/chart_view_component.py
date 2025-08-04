import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.identifier = identifier
        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible сhart view')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text(self.identifier.capitalize())

        self.chart.check_visible()

