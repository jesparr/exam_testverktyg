from behave import given, when, then
from playwright.sync_api import expect

@given(u'att jag är på sidan för att lägga till böcker')
def step_impl(context):
    context.page.goto(context.base_url)
    context.page.get_by_test_id('add-book').click()
    expect(context.page.locator('.form')).to_be_visible()

@when(u'jag fyller i titel och författare och klickar på spara')
def step_impl(context):
    context.page.get_by_test_id("add-input-title").fill("Automatisera")
    context.page.get_by_test_id("add-input-author").fill("Jesper Svensson")
    # Klicka på submitknappen
    context.page.get_by_test_id("add-submit").click()

@then(u'vill jag att boken skall läggas till under "Mina böcker"')
def step_impl(context):
    context.page.get_by_test_id("catalog").click()
    expect(context.page.locator('.catalog')).to_contain_text('Automatisera')
