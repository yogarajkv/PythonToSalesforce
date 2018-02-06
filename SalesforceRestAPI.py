from simple_salesforce import Salesforce
import requests

session = requests.Session()

sf = Salesforce(
    username='userName',
    password='password',
    security_token='securityToken')

account = sf.Account.get('0017F00000LkvYHQAZ')


payload = {
    "name":"from Python"
    }
sf.apexecute('testRestServiceForAWS/test',method='POST', data=payload)
    
