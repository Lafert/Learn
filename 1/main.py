import requests
# from urllib.parse import urlencode
from api_key import API_Token


data = {
	"custname": "user",
	"custtel": "05430480",
	"custemail": "user@user.com",
	"size": "small",
	"topping": "bacon",
	"delivery": "",
	"comments": ""
}
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "X-Amzn-Trace-Id": "Root=1-646e3216-2d135c49678532dd0f049163"
}

# url = 'https://httpbin.org/#/Request_inspection/get_headers' + urlencode(headers)

variable = requests.Session()
s = variable.get('https://httpbin.org/form/post')
r = variable.post('https://httpbin.org/post' , headers=headers, data=data)
print(r.status_code)
# with open('my_site.html', 'w', encoding='utf-8')as file:
#     file.write(r.text)

print(r.text)