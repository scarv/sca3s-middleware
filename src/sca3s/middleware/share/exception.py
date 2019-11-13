# Copyright (C) 2018 SCARV project <info@scarv.org>
#
# Use of this source code is restricted per the MIT license, a copy of which 
# can be found at https://opensource.org/licenses/MIT (or should be included 
# as LICENSE.txt within the associated archive or repository).

import abc, sys, traceback

class SCA3SException( Exception ) :
  def __init__( self, message = None, exception = None ):
    super().__init__( message )

    self.exception = exception

  @abc.abstractmethod
  def _translate( self ) :
    raise NotImplementedError()

  def __str__( self ):
    if   (       self.message   == None ) :
      t = "unknown"
    elif ( type( self.message ) == str  ) :
      t =                  self.message
    elif ( type( self.message ) == int  ) :
      t = self._translate( self.message )

    return t

class FrontEndException( SCA3SException ) :
  def __init__( self, message = None, exception = None ):
    super().__init__( message = message, exception = exception )

class  BackEndException( SCA3SException ) :
  def __init__( self, message = None, exception = None ):
    super().__init__( message = message, exception = exception )






