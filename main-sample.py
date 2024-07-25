import os 
from dotenv import load_dotenv
load_dotenv()

import gettoken

client_id = os.getenv('client_id') 
client_secret = os.getenv('client_secret')  
tetnant_id = os.getenv('tetnant_id') 
subscription_id = os.getenv('subscription_id')
resource_group_id = os.getenv('resource_group_id')

token_url = 'https://login.microsoftonline.com/'+ tetnant_id +'/oauth2/token'
resouce= 'https://management.azure.com'

# Obtain a bearer token
token = gettoken.get_bearer_token(client_id, client_secret, token_url, resouce)

# print(token)

# Example usage
token = token
report_type = "MonthlySummaryReport" # https://learn.microsoft.com/en-us/azure/carbon-optimization/export-data?tabs=RESTAPI#report-types
subscription_list = [subscription_id]
resource_group_list = [resource_group_id] 
carbon_scope_list = ["Scope1", "Scope2", "Scope3"]
start_date = "2024-01-01"
end_date = "2024-01-01"

import exportapi
# Fetch the report
try:
    report = exportapi.get_carbon_emission_report(token, report_type, 
                                                  subscription_list, 
                                                  resource_group_list, 
                                                  carbon_scope_list, start_date, end_date)
    print(report)
except Exception as e:
    print(e)