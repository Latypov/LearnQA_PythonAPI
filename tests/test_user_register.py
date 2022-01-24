import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

    excluded_params = [
        ("no_password"),
        ("no_username"),
        ("no_firstName"),
        ("no_lastName"),
        ("no_email"),
        ("invalid_email_format"),
        ("one_symbol_name"),
        ("250_symbols_name"),
        ("251_symbols_name")
    ]

    @pytest.mark.parametrize('condition', excluded_params)
    def test_create_user_with_missed_param(self, condition):

        email = self.prepare_registration_data()['email']
        url = "/user/"
        name250symbols = "_250__symbols__name__250__symbols__name__250__symbols__name__250__symbols__name_" \
                        "_250__symbols__name__250__symbols__name__250__symbols__name__250__symbols__name_" \
                        "_250__symbols__name__250__symbols__name__250__symbols__name__250__symbols__name__250__symb"

        if condition == "no_password":
            response = MyRequests.post(url, data={'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa',
                                                'email': 'email@email.ru'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The following required params are missed: password",\
                f"Unexpected response content '{response.content}'"

        elif condition == "no_username":
            response = MyRequests.post(url, data={'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa',
                                                'email': 'email@email.ru'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The following required params are missed: username", \
                f"Unexpected response content '{response.content}'"

        elif condition == "no_firstName":
            response = MyRequests.post(url, data={'password': '123', 'username': 'learnqa', 'lastName': 'learnqa',
                                                'email': 'email@email.ru'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The following required params are missed: firstName",\
                f"Unexpected response content '{response.content}'"

        elif condition == "no_lastName":
            response = MyRequests.post(url, data={'password': '123', 'username': 'learnqa', 'firstName': 'learnqa',
                                                'email': 'email@email.ru'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The following required params are missed: lastName",\
                f"Unexpected response content '{response.content}'"

        elif condition == "no_email":
            response = MyRequests.post(url, data={'password': '123', 'username': 'learnqa', 'firstName': 'learnqa',
                                                'lastName': 'learnqa'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The following required params are missed: email",\
                f"Unexpected response content '{response.content}'"

        elif condition == "invalid_email_format":
            response = MyRequests.post(url, data={'password': '123', 'username': 'learnqa', 'firstName': 'learnqa',
                                                'lastName': 'learnqa', 'email': 'vinkotovexample.com'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"Invalid email format",\
                f"Unexpected response content '{response.content}'"

        elif condition == "one_symbol_name":
            response = MyRequests.post(url, data={'password': '123', 'username': 'l', 'firstName': 'learnqa',
                                                'lastName': 'learnqa', 'email': 'email@email.ru'})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The value of 'username' field is too short",\
                f"Unexpected response content '{response.content}'"

        elif condition == "250_symbols_name":
            response = MyRequests.post(url, data={'password': '123', 'username': name250symbols, 'firstName': 'learnqa',
                                                'lastName': 'learnqa', 'email': email})
            Assertions.assert_code_status(response, 200)
            print(f"Response: '{response.content}'")
            Assertions.assert_json_has_key(response, "id")

        elif condition == "251_symbols_name":
            response = MyRequests.post(url, data={'password': '123', 'username': name250symbols + "1", 'firstName': 'learnqa',
                                                'lastName': 'learnqa', 'email': email})
            Assertions.assert_code_status(response, 400)
            print(f"Response: '{response.content}'")
            assert response.content.decode("utf-8") == f"The value of 'username' field is too long",\
                f"Unexpected response content '{response.content}'"


    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post(f"/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post(f"/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content '{response.content}'"
