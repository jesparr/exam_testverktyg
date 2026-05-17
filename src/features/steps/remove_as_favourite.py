from behave import given, when, then
from playwright.sync_api import expect
# BOOK = 'Playwright: Click It Till You Make It.'

@given(u'att jag är på sidan "Katalog"')
def step_impl(context):
    context.page.goto(context.base_url)
    # Verfiera att vi är på katalogsidan och att sidan laddat klart
    expect(context.page.locator('div.catalog')).to_be_visible()

@given('det finns böcker som är favoritmarkerade')
def step_impl(context):
    star_button = context.page.get_by_test_id('star-Playwright: Click It Till You Make It')
    # Favoritmarkerar boken
    star_button.click()
    # Verifierar att boken blivit favoritmarkerad
    expect(star_button).to_have_class('star selected')

@when('jag klickar på hjärtat på en redan favoritmarkerad bok')
def step_impl(context):
    # Klickar på samma stjärna igen för att ta bort den som favorit
    context.page.get_by_test_id('star-Playwright: Click It Till You Make It').click()

@then('ska boken försvinna från listan på "Mina böcker"')
def step_impl(context):
    # Öppna "Mina böcker"
    context.page.get_by_test_id("favorites").click()
    favorite_book = context.page.get_by_test_id("fav-Playwright: Click It Till You Make It")
    # Verifiera att boken är borttagen som favorit
    expect(favorite_book).not_to_be_visible()


