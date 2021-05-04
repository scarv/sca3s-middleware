# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which
# can be found at https://opensource.org/licenses/MIT (or should be included
# as LICENSE.txt within the associated archive or repository).

import jsonschema

from classes.errors import OKException
from sca3s.middleware.share.status import Status


def post_contest(data):
    """
    Validator for the post contest api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'id': {'type': 'string'},
            'description': {'type': 'string'}
        },
        "additionalProperties": False,
        "required": ['id', 'description']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)


def patch_contest(data):
    """
    Validator for the patch contest api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'id': {'type': 'string'},
            'description': {'type': 'string'},
            'settings' : {
                'type' : 'object',
                'properties' : {
                    'submission_cost' : {
                        'type' : 'integer',
                        "minimum": 0,
                        "maximum": 604800
                    },
                    'enrolment_grant': {
                        'type': 'integer',
                        "minimum": 0,
                        "maximum": 604800
                    },
                    "commit_link" : {'type' : 'boolean'}
                },
                "additionalProperties": False,
                "required": ['submission_cost', 'enrolment_grant', 'commit_link']
            }
        },
        "additionalProperties": False,
        "required": ['id', 'description', 'settings']
    }
    try:
        jsonschema.validate(data, schema)
    except Exception as e:
        raise OKException(Status.FAILURE_FE_API_SCHEMA_MISMATCH)


def delete_contest(data):
    """
    Validator for the delete contest api endpoint.
    """
    schema = {
        "type": "object",
        "properties": {
            'id': {'type': 'string'}
        },
        "additionalProperties": False,
        "required": ['id']
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
