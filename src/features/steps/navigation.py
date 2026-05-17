from behave import given, when, then
from playwright.sync_api import expect

@given(u'att jag står på startsidan')
def step_impl(context):
    context.page.goto(context.base_url)
    # Verfierar katalogsidan
    expect(context.page.locator("div.catalog")).to_be_visible()

@when(u'jag använder länkarna i menyn')
def step_impl(context):
    # Osäker på om jag ens behöver använda den här?
    pass

@then(u'vill jag kunna växla mellan de olika sidorna för att se vad det finns för information')
def step_impl(context):
    # Gå till "Lägg till bok" och verifiera sidan
    context.page.get_by_test_id("add-book").click()
    expect(context.page.locator("div.form")).to_be_visible()
    # Gå till "Mina böcker"
    context.page.get_by_test_id("favorites").click()
    expect(context.page.locator("div.favorites")).to_be_visible()
    # Gå till "Statistik"
    context.page.get_by_test_id("statistics").click()
    expect(context.page.locator("div.stats")).to_be_visible()


