import yaml


class Config(object):

    def __init__(self, config_file):
        self.config_file = config_file

        with open(self.config_file) as cf:

            config_dict = yaml.safe_load(cf)

            self.icinga2_url = config_dict.get('icinga2_rest_api').get('icinga2_url')

            self.icinga2_api_port = config_dict.get('icinga2_rest_api').get('icinga2_api_port')

            self.username = config_dict.get('icinga2_rest_api').get('username')

            self.password = config_dict.get('icinga2_rest_api').get('password')

            self.package_endpoint = config_dict.get('icinga2_rest_endpoints').get('package_endpoint')

            self.stage_endpoint = config_dict.get('icinga2_rest_endpoints').get('stage_endpoint')

