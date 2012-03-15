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

schema_name = 'test_where_rule'

schema_scope = sys.modules[__name__]

# Defined datatype month
class month(INTEGER):
	def __init__(self,*kargs):
		pass
		self.unnamed_wr_0()
		self.unnamed_wr_1()

	def unnamed_wr_0(self):
		eval_unnamed_wr_0 = (self  <=  12)
		if not eval_unnamed_wr_0:
			raise AssertionError('Rule unnamed_wr_0 violated')
		else:
			return eval_unnamed_wr_0

	def unnamed_wr_1(self):
		eval_unnamed_wr_1 = (self  >=  1)
		if not eval_unnamed_wr_1:
			raise AssertionError('Rule unnamed_wr_1 violated')
		else:
			return eval_unnamed_wr_1

# Defined datatype positive
class positive(INTEGER):
	def __init__(self,*kargs):
		pass
		self.notnegative()

	def notnegative(self):
		eval_notnegative_wr = (self  >  0)
		if not eval_notnegative_wr:
			raise AssertionError('Rule notnegative violated')
		else:
			return eval_notnegative_wr

