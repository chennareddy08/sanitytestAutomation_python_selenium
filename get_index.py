import requests

class Transcation(object):

    def run(self):
        r=requests.get("https://www.handstandapp.com")
        r.raw.read(0)