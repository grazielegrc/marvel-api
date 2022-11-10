from behave import *

@then('it was returned the "{name}" character')
def step_impl(context, name):
    context.json_response = context.response.json()
    assert context.json_response['data']['results'][0]['name'] == name

@then('it was returned the message: "{message}"')
def step_impl(context, message):
    assert context.json_response['status'] == message