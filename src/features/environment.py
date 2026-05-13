from playwright.sync_api import sync_playwright

# Runs before any scenarios
def before_all(context):
    # Start Playwright and the browser - close it in after_all
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)

# Runs at the start of each scenario
def before_scenario(context, scenario):
    # The scenario fixture is created from a feature file, we don't typically need it for anything.
    # Open a new page, to prevent cookies to leak between tests. Set default timeout to something appropriate. Close the page in after_scenario.
    context.page = context.browser.new_page()
    context.page.set_default_timeout(100)
    context.base_url = "https://forverkliga.se/JavaScript/whose-turn/"

# Runs directly after each scenario - clean up to avoid memory leaks
def after_scenario(context, scenario):
    if context.page:
        context.page.close()

# Runs after all scenarios have finished - clean up
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()