from jsonschema import validate, ValidationError
from classes.errors import OKException
from sca3s.middleware.share.status import Status

def update_ci(data):
    schema = {
        "type": "object",
        "properties": {
            "ci": {"type": "boolean"}
        },
        "additionalProperties": False
    }
    try:
        validate(data, schema)
    except ValidationError:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)