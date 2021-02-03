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
    'status'         : { 'type' :  'string'                                                           },
    'result'         : { 'type' :  'object'                                                           }
  }
}

MANIFEST_REQ = {
  'definitions' : {
     'trace_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
      'url'               : { 'type' :  'string' }
    }, 'required' : [] }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'status'         : { 'type' :  'string'                                                           },

       'job_type'    : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user', 'ci', 'contest' ] },
       'job_version' : { 'type' :  'string'                                                           },
       'job_id'      : { 'type' :  'string'                                                           },

      'user_id'      : { 'type' : 'integer'                                                           },
   'contest_id'      : { 'type' :  'string'                                                           },

     'trace_spec'    : { '$ref' : '#/definitions/trace_spec' }
  }, 'required' : []
}
