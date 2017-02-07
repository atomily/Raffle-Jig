from time import gmtime, strftime
import time
from random import randint
import requests

base = 'https://hervia.typeform.com/app/form/result/token/Or8TZ9/default'

def generate():
    print("RAFFLE SPLASH FOR HERVIA - BY GLEB-IO\n")
    fname = input("First name: ")
    lname = input("Last name: ")
    email = input("Email handle (Gmail only): ")
    size = input("Size (Number only, UK Size): ")
    country = input("Country (Format: United States of America): ")

    amount = 1
    i = 0

    while (i < amount):
        current = strftime('%H:%M:%S', gmtime())
        currentString = "[" + current + "] "

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }

        s = requests.Session()
        s.headers.update(headers)

        s.headers.update({
            'Origin':'https://hervia.typeform.com',
            'Referer':'https://hervia.typeform.com/to/Or8TZ9?typeform-embed=popup-classic'
        })

        gen_email = email + '+' + str(randint(0, 999999999)) + '@gmail.com'

        r = s.post(base,
                   data={
                       'form[language]': 'en',
                       'form[textfield:42058146]': fname + ' ' + lname,
                       'form[textfield:42058161]': gen_email,
                       'form[dropdown:42058358]':  country,
                       'form[dropdown:42058616]': 'UK ' + size, # CHANGE SIZE HERE
                       'form[textfield:42139636]': '',
                       'form[textfield:42058638]': '',
                       'form[textfield:42058683]': '',
                       'form[token]': '60896cfca4d9ceff1e0af6cec811b61a'
                   },
                   verify=False)

        amount = amount + 1
        i = i + 1

        if(r.status_code == 200):
            print(currentString + 'Generated Account #' + str(i) + ' using email address: ' + gen_email + '. Restarting in 3 seconds.')
        else:
            print(currentString + 'Error: Server response: ' + str(r.status_code))

        time.sleep(3)

generate()
