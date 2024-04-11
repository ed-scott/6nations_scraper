import requests
import json
from bs4 import BeautifulSoup
csrf_url = "https://account.sixnationsrugby.com/api/auth/csrf"
callback_url = "https://account.sixnationsrugby.com/en/signin"
login_url = "https://account.sixnationsrugby.com/api/auth/callback/credentials"
login = "" 
password = ""
recaptcha_token = ""

# start request session
with requests.session() as s: 
    # Get csrf token
	req = s.get(csrf_url).text
	json_resp = json.loads(req)
	csrf_token = json_resp["csrfToken"]

    # post credentials
	payload = {
		"email" : login,
		"password": password,
		"recaptchaToken": recaptcha_token,
		"redirect": False,
		"csrfToken": csrf_token,
		"callbackUrl": callback_url
    }
	
    # send request
	res = s.post(login_url,data=
			  payload)
	print(res.url)