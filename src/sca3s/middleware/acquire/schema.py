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
    # trace spec.  generic fields
    'trace_spec_generic'           : { 'type' :  'object', 'default' : {}, 'properties' : {
      'resolution_id'     : { 'type' :  'string', 'default' :  'max', 'enum' : [ 'bit', 'min', 'max' ]                         },
      'resolution_spec'   : { 'type' :  'number', 'default' :      8                                                           },

          'period_id'     : { 'type' :  'string', 'default' : 'auto', 'enum' : [ 'auto', 'interval', 'frequency', 'duration' ] },
          'period_spec'   : { 'type' :  'number', 'default' :      0                                                           },

       'calibrate_trials' : { 'type' :  'number', 'default' :     10                                                           },
       'calibrate_margin' : { 'type' :  'number', 'default' :     10                                                           },

      'type'              : { 'type' :  'string', 'default' :  '<f8', 'enum' : [ '<f4', '<f8' ]                                },
      'count'             : { 'type' :  'number', 'default' :      1                                                           }
    }, 'required' : [] },
    # trace spec. specific fields: kernel = aead     
    'trace_spec_specific_aead'     : { 'type' :  'object', 'default' : {}, 'properties' : {
      'content' : { 'type' : 'array', 'default' : [ 'trace/signal', 'crop/signal', 'k', 'a', 'm', 'c' ], 'items' : {
        'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'k', 'a', 'm', 'c' ]
      } }
    } },
    # trace spec. specific fields: kernel = block    
    'trace_spec_specific_block'    : { 'type' :  'object', 'default' : {}, 'properties' : {
      'content' : { 'type' : 'array', 'default' : [ 'trace/signal', 'crop/signal', 'k',      'm', 'c' ], 'items' : {
        'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'k',      'm', 'c' ]
      } }
    } },
    # trace spec. specific fields: kernel = function 
    'trace_spec_specific_function' : { 'type' :  'object', 'default' : {}, 'properties' : {
      'content' : { 'type' : 'array', 'default' : [ 'trace/signal', 'crop/signal', 'x', 'r'           ], 'items' : {
        'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'x', 'r'           ]
      } }
    } },
    # trace spec. specific fields: kernel = hash     
    'trace_spec_specific_hash'     : { 'type' :  'object', 'default' : {}, 'properties' : {
      'content' : { 'type' : 'array', 'default' : [ 'trace/signal', 'crop/signal', 'm', 'd'           ], 'items' : {
        'enum'  : [ 'trace/trigger', 'trace/signal', 'crop/trigger', 'crop/signal', 'perf/cycle', 'perf/duration', 'tvla/lhs', 'tvla/rhs', 'm', 'd'           ]
      } }
    } }
  },
  'type' : 'object', 'default' : {}, 'properties' : {
    'status'         : { 'type' :  'string'                                       },

      'user_id'      : { 'type' : 'integer'                                       },

       'job_type'    : { 'type' :  'string', 'enum' : [ 'user', 'ci', 'contest' ] },
       'job_id'      : { 'type' :  'string'                                       },
       'job_version' : { 'type' :  'string'                                       },

   'contest_id'      : { 'type' :  'string'                                       },
   'contest_spec'    : { 'type' :  'object', 'default' : {}                       },

    'driver_id'      : { 'type' :  'string'                                       },
    'device_id'      : { 'type' :  'string'                                       },
      
      'repo_id'      : { 'type' :  'string'                                       },
      'depo_id'      : { 'type' :  'string'                                       },
  }, 'required' : [ 'user_id', 'job_type', 'job_id', 'job_version', 'trace_spec', 'driver_id', 'device_id', 'repo_id', 'depo_id' ],
  'allOf' : [ {
    'oneOf' : [ { # options: driver_spec
      'type' : 'object', 'default' : {}, 'properties' : {    
        'driver_id'   : { 'enum' : [ 'aead'     ] }, # kernel = aead
        'driver_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'policy_id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user'         ] },
          'policy_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'user_select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' :  'all', 'enum' : [ 'all', 'each' ] },
              'a' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
              'm' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
              'c' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] }
            }, 'required' : [] },
            'user_value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' : '{$*|k|}'                          },
              'a' : { 'type' : 'string', 'default' : '{$*|a|}'                          },
              'm' : { 'type' : 'string', 'default' : '{$*|m|}'                          },
              'c' : { 'type' : 'string', 'default' : '{$*|c|}'                          }
            }, 'required' : [] }
          } }
        } },
         'trace_spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace_spec_generic' }, { '$ref' : '#/definitions/trace_spec_specific_aead'     } ]
        }
      }
    }, {
      'type' : 'object', 'default' : {}, 'properties' : {    
        'driver_id'   : { 'enum' : [ 'block'    ] }, # kernel = block
        'driver_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'policy_id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user', 'tvla' ] },
          'policy_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'user_select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' :  'all', 'enum' : [ 'all', 'each' ] },
              'm' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] },
              'c' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] }
            }, 'required' : [] },
            'user_value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'k' : { 'type' : 'string', 'default' : '{$*|k|}'                          },
              'm' : { 'type' : 'string', 'default' : '{$*|m|}'                          },
              'c' : { 'type' : 'string', 'default' : '{$*|c|}'                          }
            }, 'required' : [] }
          } }
        } },
         'trace_spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace_spec_generic' }, { '$ref' : '#/definitions/trace_spec_specific_block'    } ]
        }
      }
    }, {
      'type' : 'object', 'default' : {}, 'properties' : {    
        'driver_id'   : { 'enum' : [ 'function' ] }, # kernel = function
        'driver_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'policy_id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user'         ] },
          'policy_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'user_select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'x' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] }
            }, 'required' : [] },
            'user_value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'x' : { 'type' : 'string', 'default' : '{$*|x|}'                          }
            }, 'required' : [] }
          } }
        } },
         'trace_spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace_spec_generic' }, { '$ref' : '#/definitions/trace_spec_specific_function' } ]
        }
      }
    }, {
      'type' : 'object', 'default' : {}, 'properties' : {    
        'driver_id'   : { 'enum' : [ 'hash'     ] }, # kernel = hash
        'driver_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
          'policy_id'   : { 'type' :  'string', 'default' : 'user', 'enum' : [ 'user'         ] },
          'policy_spec' : { 'type' :  'object', 'default' : {}, 'properties' : {
            'user_select' : { 'type' :  'object', 'default' : {}, 'properties' : {
              'm' : { 'type' : 'string', 'default' : 'each', 'enum' : [ 'all', 'each' ] }
            }, 'required' : [] },
            'user_value'  : { 'type' :  'object', 'default' : {}, 'properties' : {
              'm' : { 'type' : 'string', 'default' : '{$*|m|}'                          }
            }, 'required' : [] }
          } }
        } },
         'trace_spec' : { 
          'allOf' : [ { '$ref' : '#/definitions/trace_spec_generic' }, { '$ref' : '#/definitions/trace_spec_specific_hash'     } ]
        }
      }
    } ] 
  }, { 
    'oneOf' : [ { # options:   repo_spec
      'type' : 'object', 'default' : {}, 'properties' : {
          'repo_id'   : { 'enum' : [ 'git'  ] },
          'repo_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
            'url'       : { 'type' : 'string'                              },
            'tag'       : { 'type' : 'string', 'default' : 'master'        },

            'conf'      : { 'type' :  'array', 'default' : [], 'items' : {
                'type' : 'string'
            } }
        }, 'required' : [ 'url'  ] }
      }
    } ] 
  }, { 
    'oneOf' : [ { # options:   depo_spec
      'type' : 'object', 'default' : {}, 'properties' : {
          'depo_id'   : { 'enum' : [ 's3'   ] },
          'depo_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {  
            'region_id' : { 'type' : 'string', 'default' : 'eu-west-1'     },
            'bucket_id' : { 'type' : 'string', 'default' : 'sca3s-acquire' }
        }, 'required' : [] }
      }
    }, {
      'type' : 'object', 'default' : {}, 'properties' : {
          'depo_id'   : { 'enum' : [ 'null' ] },
          'depo_spec' : { 'type' : 'object', 'default' : {}, 'properties' : {
            'foo' : { 'type' : 'string', 'default' : 'bar' }
        }, 'required' : [] }
      }
    } ] 
  } ]
}
