from playwright.sync_api import expect
from behave import given, when, then

@given(u'att jag är på startsidan')
def step_impl(context):
    # Går till sidan
    context.page.goto(context.base_url)

@then(u'ska jag se en lista över alla böcker')
def step_impl(context):
    # Kollar efter catalog klassen
    catalog_container = context.page.locator('.catalog')

    # Förväntar sig catalog_container att synas
    expect(catalog_container).to_be_visible()

    # Räknar antalet element med klassen "book"
    books = context.page.locator('.book')
    expect(books).to_have_count(13)

@then(u'varje bok ska visa titel och författare')
def step_impl(context):
    first_book = context.page.locator('.book').first

    # Verifiera att de viktigaste delarna finns i diven
    expect(first_book).to_contain_text('Ormar på ett plan: En Python-berättelse')
    expect(first_book).to_contain_text('Guido van Rossum')
