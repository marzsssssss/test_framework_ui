import os

from dotenv import load_dotenv

load_dotenv()


class Links():

    HOST = os.getenv('HOST')
    BUSINESS_PAGE = f'{HOST}'
    print(BUSINESS_PAGE)
    PERSONAL_PAGE = f'{HOST}/personal'
    PRICING_PAGE = f'{HOST}/pricing'
    LOGIN_PAGE = f'{HOST}/login'
    BUSINESS_REGISTER = f'{HOST}/business/register/phone'
    PERSONAL_REGISTER = f'{HOST}/register/phone'
    