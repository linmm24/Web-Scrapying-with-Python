import requests

params = {'username': 'Ryan', 'password': 'password'}
#params = {'zjh': '140604132', 'mm': '076134','v_yzm':'1234'}

r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("-----------")
print("Going to profile page...")
#通过cookie登陆
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)