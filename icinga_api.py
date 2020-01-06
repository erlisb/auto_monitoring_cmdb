import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Icinga(object):

    def __init__(self, url, port, username, password, package_endpoint, stage_endpoint):
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
        self.package_endpoint = package_endpoint
        self.stage_endpoint = stage_endpoint

    @classmethod
    def construct_object(cls, name, data):

        # data.pop('customer', None)
        variables = ['{} = "{}"'.format(i, j) for i, j in data.items() if j is not None and i != 'customer']

        body = ','.join(variables)

        payload = {
            "files": {
                "conf.d/test.conf": "object Host \"{}\" {{ {} }}".format(name, body)
                }
            }

        d = json.dumps(payload)
        return d

    def create_object(self, name, data, ssl_verify=False):

        auth = requests.auth.HTTPBasicAuth(self.username, self.password)
        headers = {"Accept": "application/json"}

        stage_api = '{}:{}{}{}'.format(self.url, self.port, self.stage_endpoint, data.get('customer'))

        package_api = '{}:{}{}{}'.format(self.url, self.port, self.package_endpoint, data.get('customer'))

        requests.post(url=package_api, auth=auth, headers=headers, verify=ssl_verify)

        request = requests.post(url=stage_api, auth=auth,
                                data=Icinga.construct_object(name=name, data=data),
                                headers=headers, verify=ssl_verify)
        return request

