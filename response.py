from json import dumps
from flask import Response, jsonify
from config import Config

class JsonResponse(Response):

    j_status = 200
    message = None

    def __init__(self, data_group=None, extra_header=None, *args, **kwargs):
        data_group = data_group if data_group else {}
        response_data = {
            "message": self.message,
            **data_group
        }
        header = {"Access-Control-Allow-Origin": Config.Access_Control_Allow_Origin}
        if extra_header:
            header.update(extra_header)
        super().__init__(dumps(response_data, indent=2, separators=(", ", ": ")) + "\n", self.j_status, header, mimetype="application/json", *args, **kwargs)

class OKPage(JsonResponse):

    j_status = 200
    message = "OK"

    def __init__(self, data, data_count, page, limit, *args, **kwargs):
        super().__init__({"data": data, "data_count": data_count, "page": page, "limit": limit}, *args, **kwargs)

class OK(JsonResponse):

    j_status = 200
    message = "OK"

    def __init__(self, data, *args, **kwargs):
        super().__init__({"data": data}, *args, **kwargs)

class Created(JsonResponse):

    j_status = 201
    message = "Created"

    def __init__(self, data, *args, **kwargs):
        super().__init__({"data": data}, *args, **kwargs)

class BadRequest(JsonResponse):

    j_status = 400
    message = "BadRequest"

class Unauthorized(JsonResponse):

    j_status = 401
    message = "Unauthorized"

class Forbidden(JsonResponse):

    j_status = 403
    message = "Forbidden"

class NotFound(JsonResponse):

    j_status = 404
    message = "NotFound"

class MethodNotAllowed(JsonResponse):

    j_status = 405
    message = "MethodNotAllowed"

class TooManyRequest(JsonResponse):

    j_status = 429
    message = "TooManyRequest"

class InternalServerError(JsonResponse):

    j_status = 500
    message = "InternalServerError"

def return_error(error_class):
    def error(e):
        return error_class()
    return (error_class.j_status, error)

error_list = [return_error(i) for i in [BadRequest, Unauthorized, Forbidden, NotFound, MethodNotAllowed, TooManyRequest, InternalServerError]]
