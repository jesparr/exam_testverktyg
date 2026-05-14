from behave import given, when, then


@given(u'att jag står på startsidan')
def step_impl(context):
    context.page.goto(context.base_url)

@when(u'jag använder länkarna i menyn')
def step_impl(context):
    pass

@given(u'Vill jag kunna växla mellan de olika sidorna för att se vad det finns för information')
def step_impl(context):
    pass


