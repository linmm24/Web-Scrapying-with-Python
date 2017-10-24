import requests
cook={"Cookie":"a2475a5c917c11b2a63ea91472400c6b; SUB=_2A250sYQFDeRhGeRJ41QS9yvEzzyIHXVUXSxNrDV6PUJbkdAKLWegkW15MjMkf1ZDxOSKz3YlpG6oaFai4g..; SUHB=0cSW-_aCOqQXgS; SCF=ApZRjt_qP6D5_zz110aEfmkTMhrQl0Zpt_rwmMRMYa0B3I55Ey5igX0x6hXl5cTeh8PndF4u5W7DGCZzQpnmbgg.; SSOLoginState=1505096789"}
url="https://weibo.cn/?tf=5_009"
html=requests.get(url,cookies=cook)
print(html.text)