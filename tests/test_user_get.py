import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserGet(BaseCase):

    def test_get_user_details_not_auth(self):

        response = requests.get("https://playground.learnqa.ru/api/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")


    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_get_user_details_auth_as_same_user(self):

        response2 = requests.get(
           f"https://playground.learnqa.ru/api/user/{self.user_id_from_auth_method}",
           headers={"x-csrf-token": self.token},
           cookies={"auth_sid": self.auth_sid}
        )

        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)


    def test_get_user_details_auth_as_other_user(self):

        response2 = requests.get(
           f"https://playground.learnqa.ru/api/user/1",
           headers={"x-csrf-token": self.token},
           cookies={"auth_sid": self.auth_sid}
        )

        print(f"Resp: '{response2.content}'")
        Assertions.assert_json_has_key(response2, "username")
        not_expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_no_keys(response2, not_expected_fields)

        response3 = requests.get(f"https://playground.learnqa.ru/api/user/1")

        print(f"Resp: '{response3.content}'")
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_no_keys(response3, not_expected_fields)