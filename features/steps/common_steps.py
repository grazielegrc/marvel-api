import requests
from behave import *
from utils import params
from utils import config
from utils import headers

api_key = params.public_key
api_hash = params.hash_key

@given('I have an access token')
def step_impl(context):
    global api_key
    global api_hash

@when('I perform a GET operation for "{endpoint}"')
def step_impl(context, endpoint):
    global api_key
    global api_hash
    url = config.api_url
    endpoint = endpoint
    api_url = url + endpoint
    ts = params.ts
    limit = params.limit
    payload = {"ts": ts, "apikey": api_key, "hash": api_hash, "limit": limit}
    context.response = requests.get(url=api_url, params=payload, headers=headers.content_json)


@then('I verify the response code is "{code}"')
def step_impl(context, code):
    code = int(code)
    context.json_response = context.response.json()
    assert context.json_response['code'] == code
