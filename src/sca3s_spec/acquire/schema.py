# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

import json, jsonschema

SCHEMA_MANIFEST = {
  'definitions' : {
     'trace-spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
           'period-id'   : { 'type' :  'string', 'default' : 'auto', 'enum' : [ 'auto', 'interval', 'frequency', 'duration' ] },
           'period-spec' : { 'type' :  'number', 'default' :      0                                                           },
       'resolution-id'   : { 'type' :  'string', 'default' : 'auto', 'enum' : [ 'auto', 'bit'                               ] },
       'resolution-spec' : { 'type' :  'number', 'default' :      0                                                           },
   
       'count'           : { 'type' :  'number', 'default' :      1                                                           },
       'crop'            : { 'type' : 'boolean', 'default' :   True                                                           }
    }, 'required' : [] }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'version'     : { 'type' :  'string' },
    'id'          : { 'type' :  'string' },
    'user_id'     : { 'type' :  'number' },

    'remark'      : { 'type' :  'string' },
    'status'      : { 'type' :  'number' },

    'driver-id'   : { 'type' :  'string' },
    'device-id'   : { 'type' :  'string' },
      
      'repo-id'   : { 'type' :  'string' },
      'depo-id'   : { 'type' :  'string' },

     'trace-spec' : { '$ref' : '#/definitions/trace-spec' }
  }, 'required' : [ 'version', 'id', 'user_id', 'repo-id', 'depo-id', 'driver-id', 'device-id', 'trace-spec' ],
  'allOf' : [ {
    'oneOf' : [ { # options: driver-spec
      'properties' : {
        'driver-id'   : { 'enum' : [ 'block/enc' ] },
        'driver-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'verify' : { 'type' : 'boolean', 'default' : True }
        } },
         'trace-spec' : { 
           'allOf' : [ { '$ref' : '#/definitions/trace-spec' }, { 'properties' : { # extend trace-spec w. driver-specific content options
             'content' : { 'type' :   'array', 'default' : [ 'signal', 'm', 'c', 'k' ], 'items' : {
               'enum' : [ 'trigger', 'signal', 'tsc', 'k', 'r', 'm', 'c' ]
            } },
          } } ]
        }
      } 
    }, {
      'properties' : {
        'driver-id'   : { 'enum' : [ 'block/dec' ] },
        'driver-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'verify' : { 'type' : 'boolean', 'default' : True }
        } },
         'trace-spec' : { 
           'allOf' : [ { '$ref' : '#/definitions/trace-spec' }, { 'properties' : { # extend trace-spec w. driver-specific content options
             'content' : { 'type' :   'array', 'default' : [ 'signal', 'c', 'm', 'k' ], 'items' : {
               'enum' : [ 'trigger', 'signal', 'tsc', 'k', 'r', 'm', 'c' ]
            } },
          } } ]
        }
      }
    } ] }, { 
    'oneOf' : [ { # options:  board-spec
      'properties' : {
         'board-id'   : { 'enum' : [ 'scale/lpc1313fbd48' ] },
         'board-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect-id'      : { 'type' : 'string' },
                   'connect-timeout' : { 'type' : 'number' },
  
                   'program-mode'    : { 'enum' : [ 'usb', 'jlink' ] },
                   'program-id'      : { 'type' : 'string' },
                   'program-timeout' : { 'type' : 'number' }
        }, 'required' : [ 'connect-id', 'connect-timeout', 'program-mode', 'program-id', 'program-timeout' ] }
      }
    } ] }, { 
    'oneOf' : [ { # options:  scope-spec
      'properties' : {
         'scope-id'   : { 'enum' : [ 'picoscope/ps2206b' ] },
         'scope-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect-id'      : { 'type' : 'string' },
                   'connect-timeout' : { 'type' : 'number' },

           'channel-trigger-id'      : { 
             'enum' : [ 'A', 'B' ] 
            },
           'channel-acquire-id'      : {
             'enum' : [ 'A', 'B' ]
            },
           'channel-disable-id'      : { 'type' :  'array', 'default' : [], 'items' : {
             'enum' : [ 'A', 'B' ]
           } }
        }, 'required' : [ 'connect-id', 'connect-timeout', 'channel-trigger-id', 'channel-acquire-id' ] }
      }
    }, {
      'properties' : {
         'scope-id'   : { 'enum' : [ 'picoscope/ps3406b' ] },
         'scope-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect-id'      : { 'type' : 'string' },
                   'connect-timeout' : { 'type' : 'number' },
  
           'channel-trigger-id'      : { 
             'enum' : [ 'A', 'B', 'C', 'D' ] 
            },
           'channel-acquire-id'      : {
             'enum' : [ 'A', 'B', 'C', 'D' ]
            },
           'channel-disable-id'      : { 'type' :  'array', 'default' : [], 'items' : {
             'enum' : [ 'A', 'B', 'C', 'D' ]
           } }
        }, 'required' : [ 'connect-id', 'connect-timeout', 'channel-trigger-id', 'channel-acquire-id' ] }
      }
    } ] }, { 
    'oneOf' : [ { # options:   repo-spec
      'properties' : {
          'repo-id'   : { 'enum' : [ 'git' ] },
          'repo-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
            'url'                     : { 'type' : 'string'                       },
            'tag'                     : { 'type' : 'string', 'default' : 'master' },
            'conf'                    : { 'type' : 'object', 'default' : {}       }
        }, 'required' : [ 'url' ] }
      }
    } ] }, { 
    'oneOf' : [ { # options:   depo-spec
      'properties' : {
          'depo-id'   : { 'enum' : [ 's3' ] },
          'depo-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {  
            'identity_id'             : { 'type' :     'string'                                 },
  
              'region-id'             : { 'type' :     'string', 'default' : 'eu-west-1'        },
              'bucket-id'             : { 'type' :     'string', 'default' : 'scarv-lab-traces' }
        }, 'required' : [] }
      }
    } ] }
  ]
}
