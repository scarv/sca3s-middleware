# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

import json, jsonschema

SCHEMA_MANIFEST = {
  'definitions' : {
     'trace-spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
      'resolution-id'   : { 'type' :  'string', 'default' :    'max', 'enum' : [  'bit', 'min', 'max' ]                        },
      'resolution-spec' : { 'type' :  'number', 'default' :        8                                                           },

          'period-id'   : { 'type' :  'string', 'default' :   'auto', 'enum' : [ 'auto', 'interval', 'frequency', 'duration' ] },
          'period-spec' : { 'type' :  'number', 'default' :        0                                                           },

      'type'            : { 'type' :  'string', 'default' :   '<f8',  'enum' : [ '<f4', '<f8' ]                                },
      'count'           : { 'type' :  'number', 'default' :        1                                                           }
    }, 'required' : [] }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
       'job-version' : { 'type' :  'string' },
       'job-id'      : { 'type' :  'string' },

      'user-id'      : { 'type' :  'string' },

    'remark'         : { 'type' :  'string' },
    'status'         : { 'type' :  'number' },

    'driver-id'      : { 'type' :  'string' },
    'device-id'      : { 'type' :  'string' },
      
      'repo-id'      : { 'type' :  'string' },
      'depo-id'      : { 'type' :  'string' },

     'trace-spec'  : { '$ref' : '#/definitions/trace-spec' }
  }, 'required' : [ 'job-version', 'job-id', 'user-id', 'driver-id', 'device-id', 'repo-id', 'depo-id', 'trace-spec' ],
  'allOf' : [ {
    'oneOf' : [ { # options: driver-spec
      'properties' : {
        'driver-id'   : { 'enum' : [ 'block' ] },
        'driver-spec' : { 
          'verify'      : { 'type' : 'boolean', 'default' : True                                },

          'policy-id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user', 'tvla' ] },
          'policy-spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'tvla-mode'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'fvr-k', 'fvr-d', 'svr-d', 'rvr-d' ] },
            'tvla-round'  : { 'type' : 'integer', 'default' : 1                                                       },

            'user-select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' :  'all', 'enum' : [ 'all', 'each' ] },
              'm' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
              'c' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
            }, 'required' : [] },
            'user-value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' : '{$*|k|}'                          },
              'm' : { 'type' : 'string', 'default' : '{$*|m|}'                          },
              'c' : { 'type' : 'string', 'default' : '{$*|c|}'                          }
            }, 'required' : [] }
          } }
        },
         'trace-spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace-spec'  }, { 'properties' : { # extend  trace-spec w. driver-specific content options
            'content' : { 'type' :   'array', 'default' : [ 'trace/signal', 'crop/signal', 'm', 'c', 'k' ], 'items' : {
              'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'k', 'r', 'm', 'c' ]
            } }
          } } ]
        }
      }
    } ] }, { 
    'oneOf' : [ { # options:  board-spec
      'properties' : {
         'board-id'   : { 'enum' : [ 'scale/lpc1313fbd48' ] },
         'board-spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect-id'      : { 'type' : 'string'           },
                   'connect-timeout' : { 'type' : 'number'           },
  
                   'program-id'      : { 'type' : 'string'           },
                   'program-timeout' : { 'type' : 'number'           },
                   'program-mode'    : { 'enum' : [ 'usb', 'jlink' ] },
         }, 'required' : [ 'connect-id', 'connect-timeout', 'program-id', 'program-timeout', 'program-mode' ] },
         'board-path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
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
           } },
         }, 'required' : [ 'connect-id', 'connect-timeout', 'channel-trigger-id', 'channel-acquire-id' ] },
         'scope-path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
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
         }, 'required' : [ 'connect-id', 'connect-timeout', 'channel-trigger-id', 'channel-acquire-id' ] },
         'scope-path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
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
