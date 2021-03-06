import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("GET method cases")
class TestUserGet(BaseCase):

    @allure.description("This test as non authorized user try get user data")
    def test_get_user_details_not_auth(self):

        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")


    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("This test as an authorized user gets user data")
    def test_get_user_details_auth_as_same_user(self):

        response2 = MyRequests.get(
           f"/user/{self.user_id_from_auth_method}",
           headers={"x-csrf-token": self.token},
           cookies={"auth_sid": self.auth_sid}
        )

        expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)


    @allure.description("This test as an authorized user try to get another user's data")
    def test_get_user_details_auth_as_other_user(self):

        response2 = MyRequests.get(
           f"/user/1",
           headers={"x-csrf-token": self.token},
           cookies={"auth_sid": self.auth_sid}
        )

        print(f"Resp: '{response2.content}'")
        Assertions.assert_json_has_key(response2, "username")
        not_expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_no_keys(response2, not_expected_fields)

        response3 = MyRequests.get(f"/user/1")

        print(f"Resp: '{response3.content}'")
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_no_keys(response3, not_expected_fields)