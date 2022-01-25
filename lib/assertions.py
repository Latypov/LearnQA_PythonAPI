import allure
from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        with allure.step(f"Assert '{response_as_dict}' response in json format and contains expected '{name}' key name"):
            assert name in response_as_dict, f"Response JSON doesn't have '{name}' key."
            assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        with allure.step(f"Assert '{response_as_dict}' response in json format and contains expected '{name}' key name"):
            assert name in response_as_dict, f"Response JSON doesn't have '{name}' key."

    @staticmethod
    def assert_json_has_keys(response: Response, names:list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            with allure.step(
                    f"Assert '{response_as_dict}' response in json format and contains expected '{name}' key name"):
                assert name in response_as_dict, f"Response JSON doesn't have '{name}' key."

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        with allure.step(f"Assert '{response_as_dict}' response in json format and not contains '{name}' key name"):
            assert name not in response_as_dict, f"Response JSON shouldn't have '{name}' key. But it is present."

    @staticmethod
    def assert_json_has_no_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            with allure.step(f"Assert '{response_as_dict}' response in json format and not contains '{name}' key name"):
                assert name not in response_as_dict, f"Response JSON shouldn't have '{name}' key. But it is present."

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        with allure.step(f"Assert response with '{response.status_code}' status code"):
            assert response.status_code == expected_status_code, f"Unexpected status code! " \
                   f"Expected: '{expected_status_code}', Actual: '{response.status.code}'"