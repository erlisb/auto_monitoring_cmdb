import requests
import json


class Icinga(object):

    def __init__(self, url, port, username, password):
        """
        :param url:
        :param port:
        :param username:
        :param password:
        """
        self.url = url
        self.port = port
        self.username = username
        self.password = password

    @classmethod
    def construct_object(cls, name, data):

        variables = ['{} = "{}"'.format(i, j) for i, j in data.items() if j is not None]

        body = ','.join(variables)

        payload = {
            "files": {
                "conf.d/test.conf": "object Host \"{}\" {{ {} }}".format(name, body)
                }
            }

        d = json.dumps(payload)
        return d

    def create_object(self, name, data, endpoint, ssl_verify=False):

        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        headers = {
            "Accept": "application/json"
        }
        api_url = '{}:{}{}'.format(self.url, self.port, endpoint)
        request = requests.post(url=api_url,
                                auth=auth,
                                data=Icinga.construct_object(name=name, data=data),
                                headers=headers,
                                verify=ssl_verify)
        return request

