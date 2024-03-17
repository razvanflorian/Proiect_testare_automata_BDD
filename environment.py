from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_page import HomePage
from pages.add_to_cart_page import AddPage
from pages.remove_item_page import RemovePage
from pages.comparison_page import ComparisonPage
from pages.review_page import ReviewPage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.search_page = HomePage()
    context.add_to_cart_page = AddPage()
    context.remove_item_page = RemovePage()
    context.comparison_page = ComparisonPage()
    context.review_page = ReviewPage()


def after_all(context):
    context.login_page.close()