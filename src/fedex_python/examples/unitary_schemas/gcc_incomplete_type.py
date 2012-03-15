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

schema_name = 'gcc_incomplete_type'

schema_scope = sys.modules[__name__]

# Defined datatype maths_number
class maths_number(NUMBER):
	def __init__(self,*kargs):
		pass

# SELECT TYPE atom_based_value
atom_based_value = SELECT(
	'maths_number',
	'atom_based_tuple',
	scope = schema_scope)
atom_based_tuple = LIST(0,None,'atom_based_value', scope = schema_scope)
