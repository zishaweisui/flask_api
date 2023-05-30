import json
from flask import jsonify, Response
from infrastructure_exceptions import NotFoundException

class BaseHandler:
    def __init__(self, presenter=None):
        self.presenter = presenter 
        
    def execute(self, handler_func, *args, **kwargs):
        try: 
            data = handler_func(*args, **kwargs)
            if self.presenter:
                data = self.presenter(data).present()
            return jsonify(data), 200
        except NotFoundException:
            response = {"status": 404, "body": {}}
        return Response(
            response=json.dumps(response["body"]),
            status=response["status"],
            mimetype="application/json"
        )
