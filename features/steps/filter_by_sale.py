from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open()
    sleep(5)


@when('log in to the page')
def log_in(context):
    context.app.login_page.login()


@when('Click on "off plan" at the left side menu')
def click_off_plan(context):
    context.app.filter_by_sale_page.click_off_plan()


@when('Verify the right page opens')
def verify_text(context):
    context.app.filter_by_sale_page.verify_text()


@when('Click on Filters')
def click_filters(context):
    context.app.filter_by_sale_page.click_filters()


# "High demand" was not an option in filters. I had to choose "Location/Bali" instead.
@when('Filter by sale status of "High Demand"')
def click_bali(context):
    context.app.filter_by_sale_page.click_bali()


# Product will contain "Bali" instead of "High Demand"
@then('Verify each product contains the High Demand tag')
def verify_text(context):
    context.app.filter_by_sale_page.verify_location()
