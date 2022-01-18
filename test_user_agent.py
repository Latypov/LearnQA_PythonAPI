import  requests
import pytest


class TestUserAgent:
    userAgents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('userAgent', userAgents)
    def test_user_agent(self, userAgent):
        i=0
        platform = "platform"
        browser = "browser"
        device = "device"

        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": userAgent})

        userAgentResp = response.text
        print(f"User Agent response: '{userAgentResp}'")
        userAgentHeader = response.json()

        platformValue = userAgentHeader[platform]
        browserValue = userAgentHeader[browser]
        deviceValue = userAgentHeader[device]

        if userAgent == ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
                         "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"):
            assert platformValue == 'Mobile', f"Unexpected platform value: '{platformValue}'"
            print(f"Response contains: '{platform}':'{platformValue}' value, as expected")
            assert browserValue == 'No', f"Unexpected browser value: '{browserValue}'"
            print(f"Response contains: '{browser}':'{browserValue}' value, as expected")
            assert deviceValue == 'Android', f"Unexpected device value: '{deviceValue}'"
            print(f"Response contains: '{device}':'{deviceValue}' value, as expected")

        if userAgent == ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                          "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"):
            assert platformValue == 'Mobile', f"Unexpected platform value: '{platformValue}'"
            print(f"Response contains: '{platform}':'{platformValue}' value, as expected")
            assert browserValue != 'Chrome', f"Known bug: '{browserValue}'!= 'Chrome'"
            print(f"Response contains: '{browser}':'{browserValue}' value, instead of 'Chrome' ")
            assert deviceValue == 'iOS', f"Unexpected device value: '{deviceValue}'"
            print(f"Response contains: '{device}':'{deviceValue}' value, as expected")

        if userAgent == ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"):
            assert platformValue != 'Googlebot', f"Known bug: '{platformValue}'!= 'Googlebot'"
            print(f"Response contains: '{platform}':'{platformValue}' value, instead of 'Googlebot'")
            assert browserValue == 'Unknown', f"Unexpected browser value: '{browserValue}'"
            print(f"Response contains: '{browser}':'{browserValue}' value, as expected")
            assert deviceValue == 'Unknown', f"Unexpected device value: '{deviceValue}'"
            print(f"Response contains: '{device}':'{deviceValue}' value, as expected")

        if userAgent == ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"):
            assert platformValue == 'Web', f"Unexpected platform value: '{platformValue}'"
            print(f"Response contains: '{platform}':'{platformValue}' value, as expected")
            assert browserValue == 'Chrome', f"Unexpected browser value: '{browserValue}'"
            print(f"Response contains: '{browser}':'{browserValue}' value, as expected")
            assert deviceValue == 'No', f"Unexpected device value: '{deviceValue}'"
            print(f"Response contains: '{device}':'{deviceValue}' value, as expected")

        if userAgent == ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"):
            assert platformValue == 'Mobile', f"Unexpected platform value: '{platformValue}'"
            print(f"Response contains: '{platform}':'{platformValue}' value, as expected")
            assert browserValue == 'No', f"Unexpected browser value: '{browserValue}'"
            print(f"Response contains: '{browser}':'{browserValue}' value, as expected")
            assert deviceValue != 'iPhone', f"Known bug: '{deviceValue}' != 'iPhone'"
            print(f"Response contains: '{device}':'{deviceValue}' value, instead of 'iPhone'")
