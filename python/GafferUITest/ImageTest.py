##########################################################################
#
#  Copyright (c) 2011-2012, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import os
import unittest

import imath

import GafferUI
import GafferUITest

class ImageTest( GafferUITest.TestCase ) :

	def testPNGLoad( self ) :

		i = GafferUI.Image._qtPixmapFromFile( "arrowRight10.png" )

		self.assertEqual( i.width(), 10 )
		self.assertEqual( i.height(), 10 )

		i2 = GafferUI.Image._qtPixmapFromFile( "arrowRight10.png" )

		self.assertEqual( i2.width(), 10 )
		self.assertEqual( i2.height(), 10 )

		self.assertTrue( i is i2 )

	def testLoadMissing( self ) :

		self.assertRaises( Exception, GafferUI.Image, "iAmNotAFile" )

	def testUnicode( self ) :

		i = GafferUI.Image( u"info.png" )

	def testCreateSwatch( self ) :

		s = GafferUI.Image.createSwatch( imath.Color3f( 1, 0, 0 ) )

		self.assertEqual( s._qtPixmap().width(), 10 )
		self.assertEqual( s._qtPixmap().height(), 10 )

if __name__ == "__main__":
	unittest.main()
