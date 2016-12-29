import requests

from django.conf import settings


class GetBank(object):

    def __init__(self):
        self.API_KEY = settings.MONEY_WAVE_API_KEY
        self.SECRET = settings.MONEY_WAVE_SECRET
        self.MONEY_WAVE_TEST_URL = "https://moneywave.herokuapp.com/"
        self.commission_fee = settings.COMMISSION_FEE

    def get_all_banks(self):
        url = self.MONEY_WAVE_TEST_URL + "banks"
        req_data = requests.post(url)
        if req_data.status_code == 200:
            data = req_data.json()
            return data['data']
        return []

    def verify_merchant(self):
        url = self.MONEY_WAVE_TEST_URL + 'v1/merchant/verify'
        data = {
            'apiKey': self.API_KEY,
            'secret': self.SECRET
        }
        req_data = requests.post(url, data=data)
        if req_data.status_code == 200:
            data = req_data.json()
            return data['token']
        return ''

    def get_commission(self, amount):
        req_data = requests.post(MONEY_WAVE_TEST_URL + 'v1/get-charge', 
            data={"amount": amount, "fee": self.commission_fee}, headers=headers)
        return req_data.json()['data']

    def transfer_from_card_to_account(self, token, firstname, lastname, phonenumber,
     email, recipient_account_number, cvv, expiry_year, expiry_month, amount, redirecturl, card_no):
    data = {
        'apiKey': API_KEY,
        'secret': SECRET,
        'firstname': firstname,
        'lastname': lastname,
        'phonenumber': phonenumber,
        'email': email,
        'recipient_account_number': recipient_account_number,
        'cvv': cvv,
        'expiry_year': expiry_year,
        'expiry_month': expiry_month,
        'medium': 'web',
        'amount': amount,
        'redirecturl': redirecturl,
        'card_no': card_no
    }
    headers = {'Authorization': token}
    req_data = requests.post(self.MONEY_WAVE_TEST_URL + 'v1/transfer', data=data, headers=headers)
    return req_data.json()
