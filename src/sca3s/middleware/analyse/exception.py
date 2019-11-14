# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

from sca3s.middleware import acquire as acquire
from sca3s.middleware import analyse as analyse
from sca3s.middleware import share   as share

class AnalyseException( share.exception.FrontEndException ) :
  def __init__( self, message = None, exception = None ):
    super().__init__( message = message, exception = exception )

  def _translate( self ) :
    return ""
