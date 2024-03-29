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
    'status'         : { 'type' :  'string'                                       },
    'response'       : { 'type' :  'object', 'default' : {}                       }
  }, 'required' : [ 'status' ]
}

MANIFEST_REQ = {
  'definitions' : {
     'trace_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
      'url' : { 'type' :  'string' }
    }, 'required' : [] }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'status'         : { 'type' :  'string'                                       },

       'job_id'      : { 'type' :  'string'                                       },
       'job_type'    : { 'type' :  'string', 'enum' : [ 'user', 'ci', 'contest' ] },
       'job_version' : { 'type' :  'string'                                       },

      'user_id'      : { 'type' : 'integer'                                       },

     'trace_spec'    : { '$ref' : '#/definitions/trace_spec'                      }
  }, 'required' : [ 'user_id', 'job_type', 'job_id', 'job_version', 'trace_spec' ]
}
