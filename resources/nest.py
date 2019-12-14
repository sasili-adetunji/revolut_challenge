from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from nest import read_input, parse_json


auth = HTTPBasicAuth()

CREDENTIALS = {
    'testUser': 'SuperSecretP@ssw0rd!'
}

#  verify if the user has access to the resource
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return CREDENTIALS.get(username) == password


class Nest(Resource):

    @auth.login_required
    def post(self):

        # get json from request body
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Provide an input data'}, 400

        # get nlevels from request params json
        request_params = request.args.get('nlevels')
        if not request_params:
               return {'message': 'Please provide nlevels as parameters'}, 400

        # convert the params tgo list
        nlevels = [i for i in request_params.split(',')]
        res = parse_json(json_data, nlevels)

        if res:
            return res, 201
        else:
            return {"message": 'nlevels must be one of the keys in the json array'}, 400
