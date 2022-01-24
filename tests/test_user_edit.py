import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )


    invalid_params = [
        ('vinkotovexample.com'),
        ('l')
    ]

    @pytest.mark.parametrize('condition', invalid_params)
    def test_edit_user_data_negative(self, condition):
        #REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        if condition == 'vinkotovexample.com':
            data={'email': condition}
            error_message = 'Invalid email format'
        else:
            data = {'firstName': condition}
            error_message = '{"error":"Too short value for field firstName"}'

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=data
        )

        Assertions.assert_code_status(response3, 400)
        print(f"Response: '{response3.content}'")
        assert response3.content.decode("utf-8") == error_message, \
            f"Unexpected response content '{response3.content}'"

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            "Wrong name of the user after edit"
        )

        #Authorized user trying EDIT another user's data
        another_user_id = 23908
        response5 = MyRequests.put(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": "I" + first_name}
        )

        Assertions.assert_code_status(response5, 200)
        assert response5.text == "", f"Unexpected response content '{response5.text}'"

        #Unauthorized user trying EDIT another user's data
        response6 = MyRequests.get(f"/user/{another_user_id}")
        Assertions.assert_json_has_key(response6, "username")
        response7 = MyRequests.put(f"/user/{another_user_id}", data={"username": "new_name"})
        Assertions.assert_code_status(response7, 400)
        assert response7.text == "Auth token not supplied", f"Unexpected server response: '{response6.text}'"



