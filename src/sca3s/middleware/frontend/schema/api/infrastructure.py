import jsonschema

from classes.errors import OKException
from sca3s.middleware.share.status import Status


def revoke_token(data):
    """
    Validator for the advertise api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'token': {
                'type': 'string'
            }
        },
        "additionalProperties": False,
        "required": ['token']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)


def create_token(data):
    """
    Validator for the advertise api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'name': {
                'type': 'string'
            }
        },
        "additionalProperties": False,
        "required": ['name']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)
