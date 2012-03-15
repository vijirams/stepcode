# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Builtin import *
from SCL.Rules import *
from SCL.Algorithms import *

schema_name = 'test_named_type'

schema_scope = sys.modules[__name__]

# Defined datatype measure
class measure(REAL):
	def __init__(self,*kargs):
		pass

# Defined datatype type2
class type2(INTEGER):
	def __init__(self,*kargs):
		pass

# Defined datatype type3
class type3(type2):
	def __init__(self,*kargs):
		pass


####################
 # ENTITY line #
####################
class line(BaseEntityClass):
	'''Entity line definition.

	:param line_length
	:type line_length:measure

	:param other_param
	:type other_param:type3

	:param and_another
	:type and_another:REAL
	'''
	def __init__( self , line_length,other_param,and_another, ):
		self.line_length = line_length
		self.other_param = other_param
		self.and_another = and_another

	@apply
	def line_length():
		def fget( self ):
			return self._line_length
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument line_length is mantatory and can not be set to None')
			if not check_type(value,measure):
				self._line_length = measure(value)
			else:
				self._line_length = value
		return property(**locals())

	@apply
	def other_param():
		def fget( self ):
			return self._other_param
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument other_param is mantatory and can not be set to None')
			if not check_type(value,type3):
				self._other_param = type3(value)
			else:
				self._other_param = value
		return property(**locals())

	@apply
	def and_another():
		def fget( self ):
			return self._and_another
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument and_another is mantatory and can not be set to None')
			if not check_type(value,REAL):
				self._and_another = REAL(value)
			else:
				self._and_another = value
		return property(**locals())
