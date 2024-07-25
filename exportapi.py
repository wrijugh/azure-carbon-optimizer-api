import requests

def get_carbon_emission_report(token, report_type, subscription_list, resource_group_list, carbon_scope_list, start_date, end_date):
    """
    Fetches the carbon emission report from Azure.

    Parameters:
    - token (str): Bearer token for authorization.
    - report_type (str): Type of the report.
    - subscription_list (list): List of subscription IDs.
    - carbon_scope_list (list): List of carbon scopes.
    - start_date (str): Start date for the report.
    - end_date (str): End date for the report.

    Returns:
    - dict: The carbon emission report.
    """
    url = "https://management.azure.com/providers/Microsoft.Carbon/carbonEmissionReports?api-version=2023-04-01-preview"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "reportType": report_type,
        "subscriptionList": subscription_list,
        "resourceGroupUrlList": resource_group_list,
        "carbonScopeList": carbon_scope_list,
        "dateRange": {
            "start": start_date,
            "end": end_date
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch carbon emission report: {response.text}")

