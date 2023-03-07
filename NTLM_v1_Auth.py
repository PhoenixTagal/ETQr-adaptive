import requests
from requests_ntlm import HttpNtlmAuth


# HttpNtlmAuth syntax
# requests.get("http://ntlm_protected_site.com",auth=HttpNtlmAuth('domain\\username','password'))


# ETQr DEV endpoint: https://adaptivebio.etq.com:8443/dev/rel/#/app/auth/login


# using connection pooling to avoid each request from completing its own NTLM challenge response
session = requests.Session()
session.auth = HttpNtlmAuth('reliance-ws-intgUser', 'adaptive321')
r = session.get('https://adaptivebio.etq.com:8443/dev/rel/#/app/auth/login')
print(r.status_code)





