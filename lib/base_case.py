import json
from datetime import datetime

import allure
from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        with allure.step(f"Assert '{response.cookies}' response cookies string contains'{cookie_name}' expected cookie name"):
            assert cookie_name in response.cookies, f"Cannot find cookie with name -{cookie_name} in the last response"
            return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        with allure.step(f"Assert '{response.headers}' response headers string contains expected '{headers_name}' header name"):
            assert headers_name in response.headers, f"Cannot find header with the name -{headers_name} in the last response"
            return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response. json()
        except json.decoder.JSONOecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        with allure.step(f"Assert '{response_as_dict}' response in json format and contains'{name}' expected key name"):
            assert name in response_as_dict, f"Response JSON doesn't have key -'{name}'"

        return response_as_dict[name]


    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

