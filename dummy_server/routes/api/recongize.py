from flask import request, make_response
from flasgger import SwaggerView

from . import api_bp
from ...schemata.requests.recognize import RecognizeRequest
from ...entities.responses.response_enum import ResponseState
from ...schemata.responses.response_base import Response, ResponseOnSuccessSchema, ResponseOnFailedSchema
from ...controllers.recognize import RecognizeController

class RecognizeApiView(SwaggerView):
    parameters = RecognizeRequest
    responses = {
        200: {
            'description': 'Response on success',
            'schema': ResponseOnSuccessSchema
        },
        400: {
            'description': 'Response on failed',
            'schema': ResponseOnFailedSchema
        }
    }
    validation = True

    def post(self):
        '''
        Example using marshmallow Schema
        validation=True forces validation of parameters in body
        ---
        # This value overwrites the attributes above
        '''
        w, h = RecognizeController.handle_request(request.json)
        response = Response(
            ResponseState.success,
            f'Image({w}, {h})'
        )
        schema = ResponseOnSuccessSchema()
        return make_response(
            schema.dump(response), 200
        )

api_bp.add_url_rule(
    '/recognize',
    view_func=RecognizeApiView.as_view('api/recongize'),
    methods=['POST']
)
