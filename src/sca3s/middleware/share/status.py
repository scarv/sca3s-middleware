# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

import enum, re

# status modes
MODE_SUCCESS = 0x0
MODE_FAILURE = 0x1

# status domain separators
DOMAIN_GENERIC = 0x0
DOMAIN_BE = 0x1
DOMAIN_FE = 0x2


class Status(enum.IntEnum):
    def encode(mode, domain, value):
        return ((mode & 0x1) << 31) | ((domain & 0x7) << 28) | ((value & 0xFFFF) << 0)

    @staticmethod
    def build(value):
        try:  # B10 Integer
            return Status(int(value))
        except ValueError:  # B16 Integer
            return Status(int(value, 16))

    # status values: generic
    SUCCESS = encode(MODE_SUCCESS, DOMAIN_GENERIC, 0x0000)
    # status values:  back-end
    FAILURE_BE_JOB_PROLOGUE = encode(MODE_FAILURE, DOMAIN_BE, 0x0000)
    FAILURE_BE_JOB_PROCESS = encode(MODE_FAILURE, DOMAIN_BE, 0x0001)
    FAILURE_BE_JOB_EPILOGUE = encode(MODE_FAILURE, DOMAIN_BE, 0x0002)
    # status values: front-end, job-related
    FAILURE_FE_JOB_UNKNOWN = encode(MODE_FAILURE, DOMAIN_FE, 0x0000)
    FAILURE_FE_JOB_INVALID = encode(MODE_FAILURE, DOMAIN_FE, 0x0001)
    # status values: front-end, API-related
    FAILURE_FE_API_QUEUE_EMPTY = encode(MODE_FAILURE, DOMAIN_FE, 0x0100)
    FAILURE_FE_API_QUEUE_FULL = encode(MODE_FAILURE, DOMAIN_FE, 0x0101)
    # status values: front-end, AWS-related
    FAILURE_FE_AWS_AUTH = encode(MODE_FAILURE, DOMAIN_FE, 0x0200)
    FAILURE_FE_AWS_URL = encode(MODE_FAILURE, DOMAIN_FE, 0x0201)

    def is_success(self):
        return ((self.value >> 31) & 0x1) == MODE_SUCCESS

    def is_failure(self):
        return ((self.value >> 31) & 0x1) == MODE_FAILURE

    def describe(self):
        if (self.value == self.SUCCESS):
            t = 'success'

        elif (self.value == self.FAILURE_BE_JOB_PROLOGUE):
            t = 'job failed during processing prologue (before processing, e.g.,   allocation of resources)'
        elif (self.value == self.FAILURE_BE_JOB_PROCESS):
            t = 'job failed during processing'
        elif (self.value == self.FAILURE_BE_JOB_EPILOGUE):
            t = 'job failed during processing epilogue (after  processing, e.g., deallocation of resources)'

        elif (self.value == self.FAILURE_FE_JOB_UNKNOWN):
            t = ''
        elif (self.value == self.FAILURE_FE_JOB_INVALID):
            t = ''
        elif (self.value == self.FAILURE_FE_API_QUEUE_EMPTY):
            t = ''
        elif (self.value == self.FAILURE_FE_API_QUEUE_FULL):
            t = ''
        elif (self.value == self.FAILURE_FE_AWS_AUTH):
            t = ''
        elif (self.value == self.FAILURE_FE_AWS_URL):
            t = ''

        return re.sub(r'\s\s+', ' ', t)

    def __repr__(self):
        return (self.name) + ' : ' + ('<' + '{0:08X}'.format(self.value) + '>')
