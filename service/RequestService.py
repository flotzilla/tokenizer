import requests

from error.CommunicationError import CommunicationError


class RequestService:

    # Simple implementation
    def postJSONRequest(self, url, data):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        try:
            res = requests.post(url, data=data, headers=headers)
            if res.status_code == 200:
                return res.text
        except Exception as e:
            raise CommunicationError("Please, try again later", status_code=503)
