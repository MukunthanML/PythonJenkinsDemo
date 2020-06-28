import json
import jsonpath
import pytest
import requests

# @pytest.fixture()
# def read_url():
#     with open("../urls.json", "r") as file:
#         urls = json.load(file)
#         return urls

@pytest.fixture()
def hit_api_get():
    response = requests.get('http://api.zippopotam.us/us/90210')
    return response

@pytest.fixture()
def response_to_json(hit_api_get):

    return hit_api_get.json()


def test_save_resp_jsonfile(response_to_json):
    print(response_to_json)
    with open("Result_response.json", "a") as Result_response_file:
        Result_response_file.write('\n')
        json.dump(response_to_json, Result_response_file)

# Assert status code
def test_status_code(hit_api_get):
    print('status code of response:' + str(hit_api_get.status_code))
    assert 200 == hit_api_get.status_code

# Assert response time
def test_response_time(hit_api_get):
    print('Response Time:', hit_api_get.elapsed.total_seconds())
    assert hit_api_get.elapsed.total_seconds() < 1.5

# Assert response body content type
def test_response_content_type(hit_api_get):
    print('Response Content Type:', hit_api_get.headers['content-type'])
    assert hit_api_get.headers['content-type'] == 'application/json'

# Assert the response body’s field “state” value
def test_response_field_state(hit_api_get):
    json_response = json.loads(hit_api_get.content)
    state = jsonpath.jsonpath(json_response, "places[0].state")
    print('Response Field State Value:', state[0])
    assert state[0] == 'California'