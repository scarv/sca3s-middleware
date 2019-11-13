# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

from sca3s.share import share   as share
from sca3s.share import acquire as acquire
from sca3s.share import analyse as analyse

import json, jsonschema

SCHEMA_MANIFEST = {
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
      'user_id'      : { 'type' : 'integer' },

       'job_version' : { 'type' : 'string'  },
       'job_id'      : { 'type' : 'string'  },

    'remark'         : { 'type' : 'string'  },
    'status'         : { 'type' : 'integer' },

    'driver_id'      : { 'type' : 'string'  },
    'device_id'      : { 'type' : 'string'  },
      
      'repo_id'      : { 'type' : 'string'  },
      'depo_id'      : { 'type' : 'string'  },

     'trace_spec'    : { '$ref' : '#/definitions/trace_spec' }
  }, 'required' : [ 'job_version', 'job_id', 'user_id', 'driver_id', 'device_id', 'repo_id', 'depo_id', 'trace_spec' ],
  'allOf' : [ {
    'oneOf' : [ { # options: driver_spec
      'properties' : {
        'driver_id'   : { 'enum' : [ 'block' ] },
        'driver_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'verify'      : { 'type' : 'boolean', 'default' : True                                },

          'policy_id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user', 'tvla' ] },
          'policy_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'tvla_mode'   : { 'type' :  'string', 'default' : 'fvr_d', 'enum' : [ 'fvr_k', 'fvr_d', 'svr_d', 'rvr_d' ] },
            'tvla_round'  : { 'type' : 'integer', 'default' : 1                                                        },

            'user_select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' :  'all', 'enum' : [ 'all', 'each' ] },
              'm' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
              'c' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
            }, 'required' : [] },
            'user_value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' : '{$*|k|}'                          },
              'm' : { 'type' : 'string', 'default' : '{$*|m|}'                          },
              'c' : { 'type' : 'string', 'default' : '{$*|c|}'                          }
            }, 'required' : [] }
          } }
        } },
         'trace_spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace_spec'  }, { 'properties' : { # extend  trace_spec w. driver_specific content options
            'content' : { 'type' : 'array', 'default' : [ 'trace/signal', 'crop/signal', 'm', 'c', 'k' ], 'items' : {
              'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'k', 'r', 'm', 'c' ]
            } }
          } } ]
        }
      }
    } ] }, { 
    'oneOf' : [ { # options:  board_spec
      'properties' : {
         'board_id'   : { 'enum' : [ 'scale/lpc1313fbd48' ] },
         'board_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect_id'      : { 'type' : 'string'           },
                   'connect_timeout' : { 'type' : 'number'           },
  
                   'program_id'      : { 'type' : 'string'           },
                   'program_timeout' : { 'type' : 'number'           },
                   'program_mode'    : { 'enum' : [ 'usb', 'jlink' ] },
         }, 'required' : [ 'connect_id', 'connect_timeout', 'program_id', 'program_timeout', 'program_mode' ] },
         'board_path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
      }
    } ] }, { 
    'oneOf' : [ { # options:  scope_spec
      'properties' : {
         'scope_id'   : { 'enum' : [ 'picoscope/ps2206b' ] },
         'scope_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect_id'      : { 'type' : 'string' },
                   'connect_timeout' : { 'type' : 'number' },

           'channel_trigger_id'      : { 
             'enum' : [ 'A', 'B' ] 
            },
           'channel_acquire_id'      : {
             'enum' : [ 'A', 'B' ]
            },
           'channel_disable_id'      : { 'type' :  'array', 'default' : [], 'items' : {
             'enum' : [ 'A', 'B' ]
           } },
         }, 'required' : [ 'connect_id', 'connect_timeout', 'channel_trigger_id', 'channel_acquire_id' ] },
         'scope_path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
      }
    }, {
      'properties' : {
         'scope_id'   : { 'enum' : [ 'picoscope/ps3406b' ] },
         'scope_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
                   'connect_id'      : { 'type' : 'string' },
                   'connect_timeout' : { 'type' : 'number' },
  
           'channel_trigger_id'      : { 
             'enum' : [ 'A', 'B', 'C', 'D' ] 
            },
           'channel_acquire_id'      : {
             'enum' : [ 'A', 'B', 'C', 'D' ]
            },
           'channel_disable_id'      : { 'type' :  'array', 'default' : [], 'items' : {
             'enum' : [ 'A', 'B', 'C', 'D' ]
           } }
         }, 'required' : [ 'connect_id', 'connect_timeout', 'channel_trigger_id', 'channel_acquire_id' ] },
         'scope_path' : { 'type' :  'array', 'default' : [], 'items' : { 
           'type' : 'string' 
         } }
      }
    } ] }, { 
    'oneOf' : [ { # options:   repo_spec
      'properties' : {
          'repo_id'   : { 'enum' : [ 'git' ] },
          'repo_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
            'url'                     : { 'type' : 'string'                       },
            'tag'                     : { 'type' : 'string', 'default' : 'master' },
            'conf'                    : { 'type' : 'object', 'default' : {}       }
        }, 'required' : [ 'url' ] }
      }
    } ] }, { 
    'oneOf' : [ { # options:   depo_spec
      'properties' : {
          'depo_id'   : { 'enum' : [ 's3' ] },
          'depo_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {  
            'identity_id'             : { 'type' :     'string'                                 },
  
              'region_id'             : { 'type' :     'string', 'default' : 'eu-west-1'        },
              'bucket_id'             : { 'type' :     'string', 'default' : 'scarv-lab-traces' }
        }, 'required' : [] }
      }
    } ] }
  ]
}
