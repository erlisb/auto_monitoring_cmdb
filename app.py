from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3
from config import Config
from icinga_api import Icinga

app = Flask(__name__)
api = Api(app)


config = Config(config_file='configs.yaml')
icinga_api = Icinga(url=config.icinga2_url,
                    port=config.icinga2_api_port,
                    username=config.username,
                    password=config.password,
                    package_endpoint=config.package_endpoint,
                    stage_endpoint=config.stage_endpoint)


class Health(Resource):
    def get(self):

        return {
            "message": "Hello Pyrana People :)"
        }, 200


class Hosts(Resource):
    TABLE_NAME = 'hosts'

    def get(self):

        connection = sqlite3.connect('cmdb.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)

        try:
            result = cursor.execute(query)
        except:
            return {"message": "An error occurred when selecting from the database."}, 503

        hosts = [
            {
                'customer': row[0],
                'host_id': row[1],
                'host_object_id': row[2],
                'display_name': row[3],
                'address': row[4],
                'check_interval': row[5],
                'check_command': row[6],
                'check_command_args': row[7],
                'status': row[8]
            } for row in result
        ]

        connection.close()

        return {'hosts': hosts}, 200 if not hosts else 404


class Host(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('address', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('check_interval', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('check_command', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('check_command_args', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('customer', type=str, required=True, help="This field cannot be left blank!")

    def post(self, name):
        data = Host.parser.parse_args()

        request = icinga_api.create_object(name=name, data=data)

        return {
            'name': name,
            'data': data,
            'json': request.json()
        }, 200


api.add_resource(Health, '/health')
api.add_resource(Hosts, '/hosts')
api.add_resource(Host, '/host/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
