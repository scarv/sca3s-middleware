from jsonschema import validate, ValidationError
from classes.errors import OKException
from sca3s.middleware.share.status import Status

def infrastructure_token(data):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        },
        "additionalProperties": False,
        "required" : ['name']
    }
    try:
        validate(data, schema)
    except ValidationError:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)