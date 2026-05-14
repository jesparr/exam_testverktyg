from behave import given, when, then
from playwright.sync_api import expect


@given(u'att jag är på sidan katalog')
def step_impl(context):

    context.page.goto(context.base_url)
    catalog_btn = context.page.get_by_test_id("catalog")
    expect(catalog_btn).to_be_visible()

@when(u'jag klickar på hjärt-ikonen på en bok')
def step_impl(context):

   heart_btn = context.page.get_by_test_id("star-The Pragmatic Procrastinator")
   heart_btn.click()

@then(u'vill jag att boken sparas som favorit och hamnar under "Mina böcker"')
def step_impl(context):
    # Gå till favoritsidan
    context.page.get_by_test_id("favorites").click()
    # Verifiera att rätt bok är favoritmarkerad
    expect(context.page.get_by_test_id("book-list")).to_contain_text("The Pragmatic Procrastinator")



@then(u'ska siffran för favoritmarkerade böcker öka med 1 på sidan "Statistik"')
def step_impl(context):

    context.page.get_by_test_id("statistics").click()
    stats_container = context.page.locator("main")
    expect(stats_container).to_contain_text("1")