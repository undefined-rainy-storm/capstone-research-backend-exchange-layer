from flasgger import Schema, fields

class RecognizeRequest(Schema):
    content = fields.Str(required=True)
