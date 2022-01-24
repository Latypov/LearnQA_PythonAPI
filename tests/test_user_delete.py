import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_value(response1, "user_id")


    def test_delete_user(self):
        #Try to DELETE existing user
        response1 = MyRequests.delete(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )

        Assertions.assert_code_status(response1, 400)
        assert response1.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
            f"Unexpected server response: '{response1.text}'"


        #REGISTER
        register_data = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        user_id = self.get_json_value(response2, "id")

        email = register_data['email']
        password = register_data['password']


        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        #Try to DELETE another user
        another_user_id = int(user_id) - 1

        response4 = MyRequests.delete(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response4, 200)
        assert response4.text == "", f"Unexpected server response: '{response4.text}'"

        #DELETE user
        response5 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response5, 200)
        assert response5.text == "", f"Unexpected server response: '{response5.text}'"

        response6 = MyRequests.get(
           f"/user/{user_id}",
           headers={"x-csrf-token": self.token},
           cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_code_status(response5, 200)
        assert response6.text == "User not found", f"Unexpected server response: '{response6.text}'"
