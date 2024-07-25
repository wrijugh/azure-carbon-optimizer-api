import requests

def get_bearer_token(client_id, client_secret, token_url, resource):
    """
    Obtain a bearer token using OAuth client credentials flow.

    Parameters:
    - client_id (str): The client ID issued to the client during the registration process.
    - client_secret (str): The client secret issued to the client during the registration process.
    - token_url (str): The URL to obtain the token from the OAuth server.

    Returns:
    - str: The obtained bearer token or None if an error occurred.
    """
    # Define the payload for the token request
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': resource
    }

    # Send a POST request to the token URL
    try:
        response = requests.post(token_url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Extract the token from the response
        token = response.json().get('access_token')
        return token
    except requests.RequestException as e:
        print(f"Error obtaining token: {e}")
        return None