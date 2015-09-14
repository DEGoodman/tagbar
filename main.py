from instagram.client import InstagramAPI

access_token = "" # add IG access token
client_secret = "" # add IG client secret
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

def call_IG(tag=""):
    # RESTful api
    # https://instagram.com/developer/endpoints/tags/
    pass