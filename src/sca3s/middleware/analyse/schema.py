# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

from sca3s.middleware import acquire as acquire
from sca3s.middleware import analyse as analyse
from sca3s.middleware import share   as share

import json, jsonschema

MANIFEST_ACK = {
  'definitions' : {

  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'status'         : { 'type' : 'integer'                                               }
  }
}

MANIFEST_REQ = {
  'definitions' : {
     'trace_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
      'resolution_id'   : { 'type' :  'string', 'default' :  'max', 'enum' : [  'bit', 'min', 'max' ]                        },
      'resolution_spec' : { 'type' :  'number', 'default' :      8                                                           },

          'period_id'   : { 'type' :  'string', 'default' : 'auto', 'enum' : [ 'auto', 'interval', 'frequency', 'duration' ] },
          'period_spec' : { 'type' :  'number', 'default' :      0                                                           },

      'type'            : { 'type' :  'string', 'default' :  '<f8',  'enum' : [ '<f4', '<f8' ]                               },
      'count'           : { 'type' :  'number', 'default' :      1                                                           }
    }, 'required' : [] }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'status'         : { 'type' : 'integer'                                               }
  }
}
