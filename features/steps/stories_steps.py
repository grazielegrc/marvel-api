from behave import *


@then('it was returned only 5 registers')
def step_impl(context):
    context.json_response = context.response.json()
    for i in range(len(context.json_response['data']['results'])):
        print(f'Title {i + 1}: ', context.json_response['data']['results'][i]['title'] + '\n')
    assert context.json_response['data']['limit'] == 5
