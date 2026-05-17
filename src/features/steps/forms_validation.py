from behave import given, when, then
from playwright.sync_api import expect

@given(u'att jag är på sidan "Lägg till bok"')
def step_impl(context):
    context.page.goto(context.base_url)
    # Gå till "Lägg till bok"
    context.page.get_by_test_id("add-book").click()
    # Verifiera att vi är på rätt sida
    expect(context.page.locator("div.form")).to_be_visible()

@when('jag inte har fyllt i alla fält')
def step_impl(context):
    title_input = context.page.get_by_test_id('add-input-title')
    author_input = context.page.get_by_test_id('add-input-author')

    # Lämnar ett av fälten tomma
    title_input.fill('Jeppes bok')
    author_input.fill('')

@then('vill jag att knappen "Lägg till ny bok" endast skall vara aktiv när alla fält är ifyllda')
def step_impl(context):
    # Hitta submitknappen
    submit_button = context.page.get_by_test_id('add-submit')
    # Verifiera att knappen är inaktiv
    expect(submit_button).to_be_disabled()

    # Fyll i det andra fältet och verifiera att knappen blir enablad
    context.page.get_by_test_id('add-input-author').fill('Bill Gates')

    # Verifiera att knappen ni är aktiv
    expect(submit_button).to_be_enabled()
