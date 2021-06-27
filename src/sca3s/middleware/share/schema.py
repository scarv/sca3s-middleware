# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which
# can be found at https://opensource.org/licenses/MIT (or should be included
# as LICENSE.txt within the associated archive or repository).

import json, jsonschema

# In the jsonschema FAQ [1], there's a recipe which extends a validator with
# the ability to (recursively) apply the default values in a given schema to
# an associated instance *before* then validating it.  On the whole, this is
# good enough for most purposes; it fails, however, for allOf, oneOf, etc.
# The function populate is a limited replacement therefore.  It's basic, and
# so likely only useful for the specific schema and idioms we use, but does
# the right thing in the cases the jsonschema recipe doesn't.
#
# [1] https://python-jsonschema.readthedocs.io/en/stable/faq

def validate( schema, instance ) :
  jsonschema.Draft7Validator( schema ).validate( instance )

def populate( schema, instance, definitions = dict() ) :
  for key in schema.keys() :
    # remember definitions for later use

    if   ( key == 'definitions' ) :
      definitions = schema[ key ]

    # base cases

    elif ( key == 'type'        ) :
      pass
    elif ( key == 'default'     ) :
      pass
    elif ( key == 'required'    ) :
      pass

    # more complex recursive cases

    elif ( key == 'allOf'       ) :
      for subschema in schema[ key ] :
          populate( subschema, instance, definitions = definitions )
    elif ( key == 'oneOf'       ) :
      for subschema in schema[ key ] :
        if ( jsonschema.Draft7Validator( { 'definitions' : definitions, **subschema } ).is_valid( instance ) ) :
          populate( subschema, instance, definitions = definitions )

    # less complex recursive cases

    elif ( key == '$ref'        ) : 
      _schema   = definitions[ schema[ key ][ len( '#/definitions/' ) : ] ]
      _instance = instance

      populate( _schema, _instance, definitions = definitions )
    elif ( key == 'properties'  ) :
      _schema   =              schema[ key ]
      _instance = instance

      populate( _schema, _instance, definitions = definitions )

    # default case

    else :
      if ( not ( key in instance ) ) :
        if ( 'default' in schema[ key ] ) :
          instance[ key ] = schema[ key ][ 'default' ]

      if (       key in instance   ) :
        populate( schema[ key ], instance[ key ], definitions = definitions )

