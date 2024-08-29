from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')
    sleep(5)


@when('log in to the page')
def log_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[placeholder='Email']").send_keys('sekoyahicks@gmail.com')
    context.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys('403d57ef')
    context.driver.find_element(By.CSS_SELECTOR, "[class='login-button w-button']").click()
    sleep(5)


@when('Click on "off plan" at the left side menu')
def click_off_plan(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-current='page']").click()
    sleep(5)


@when('Verify the right page opens')
def verify_text(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[aria-current='page']").text
    assert 'Off-plan' in actual_text, f'Expected Off-plan not in actual {actual_text}'


@when('Click on Filters')
def click_filters(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='filter-button w-inline-block']").click()
    sleep(5)


# "High demand" was not an option in filters. I had to choose "Location/Bali" instead.
@when('Filter by sale status of "High Demand"')
def click_bali(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='tag-properties']").click()
    sleep(4)


#Product will contain "Bali" instead of "High Demand"
@then('Verify each product contains the High Demand tag')
def verify_text(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[name='Location']").text
    assert 'Bali' in actual_text, f'Expected Bali not in actual {actual_text}'
    sleep(4)
