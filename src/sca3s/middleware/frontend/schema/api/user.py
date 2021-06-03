# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which
# can be found at https://opensource.org/licenses/MIT (or should be included
# as LICENSE.txt within the associated archive or repository).

import jsonschema

from classes.errors import OKException
from sca3s.middleware.share.status import Status


def add_credits(data):
    """
    Validator for the advertise api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'username': {'type': 'string'},
            'credits': {
                'type': 'integer',
                'minimum': 0
            }
        },
        "additionalProperties": False,
        "required": ['username', 'credits']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        print(e)
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)


def patch_job(data):
    """
    Validator for the advertise api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'status': {
                'anyOf': [
                    {
                        'type': 'integer'
                    },
                    {
                        'type': 'string',
                        'pattern': "0[xX][0-9a-fA-F]+"
                    }
                ]
            }
        },
        "additionalProperties": False,
        "required": ['status']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)


def validate_default(conf, schema):
    """
    Dan Page validation function to auto fill in default params.
    :param conf: config to validate.
    :param schema: schema to validate against.
    """

    def defaults(validator_class):
        validate_properties = validator_class.VALIDATORS['properties']

        def set_defaults(validator, properties, instance, schema):
            for (property, subschema) in properties.items():
                if ('default' in subschema):
                    instance.setdefault(property, subschema['default'])

            for error in validate_properties(validator, properties, instance, schema):
                yield error

        return jsonschema.validators.extend(validator_class, {'properties': set_defaults})

    validator = defaults(jsonschema.Draft6Validator)
    validator(schema).validate(conf)
