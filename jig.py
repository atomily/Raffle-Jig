import datetime
import time
from time import gmtime, strftime
from random import randint
import requests

def generate():
    print("For the UK FAM - ymeuniverse.com raffle jig\n")
    fname = input('What is the first name for the raffle entry? ')
    lname = input('What is the last name for the raffle entry? ')
    full_name = fname + ' ' + lname
    email = input('What is your email handle? (Gmail only, ex: promichael01) ')
    size = input('What size are you going for? (UK Sizes, ex: 10) ')
    city = input('What city are you from? ')
    sleeknote = '24494' # dont change this
    customerId = '3096' # dont change this
    signup = 'https://ymeuniverse.com/en/blog/2017/01/31/blackred-yeezy-boost-350-v2-will-release-february-11th/'
    useragent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    amount = 100
    i = 0

    base = 'https://mailchimp.sleeknote.com'

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
            'Host': 'https://mailchimp.sleeknote.com',
            'Referer': 'https://sleeknoteboxcontent.sleeknote.com/24494.html'
        })

        gen_email = email + '+' + str(randint(0, 999999999)) + '@gmail.com'

        r = s.post(base,
                   data={
                       'name': full_name,
                       'email': gen_email,
                       'Kid 20-27 or Unisex UK 4-12': size,
                       'Enter City': city,
                       'SleeknoteId': sleeknote,
                       'CustomerId': customerId,
                       'SignupPage': signup,
                       'UserAgent': useragent
                   },
                   verify=False)
        i = i + 1
        amount = amount + 1

        print(currentString + str(i) + ': ' + str(r.status_code) + ': Successfully entered raffle for ' + gen_email + '. Restarting in 3 seconds.')

        time.sleep(5)

generate()
