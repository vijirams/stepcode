# Copyright (c) 2011, Thomas Paviot (tpaviot@gmail.com)
# All rights reserved.

# This file is part StepClassLibrary (SCL).
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#   Neither the name of the <ORGANIZATION> nor the names of its contributors may
#   be used to endorse or promote products derived from this software without
#   specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import sys
sys.path.append('../examples/unitary_schemas')

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Expr import *

class TestSelectDataType(unittest.TestCase):
    '''
    unitary_schemas/test_select_data_type.py
    '''
    def test_import_schema_module(self):
        import test_select_data_type
    
    def test_schema(self):
        import test_select_data_type
        my_glue = test_select_data_type.glue(STRING("comp"),STRING("solvent"))
        wm = test_select_data_type.wall_mounting(STRING("mounting"),STRING("on"),my_glue)

class TestSingleInheritance(unittest.TestCase):
    '''
    unitary_schemas/test_single_inheritance.py
    '''
    def test_import_schema_module(self):
        import test_single_inheritance
    
    def test_schema(self):
        import test_single_inheritance
        my_base_shape = test_single_inheritance.shape(item_name = STRING("spherical shape"),number_of_sides = INTEGER(1))
        my_shape = test_single_inheritance.rectangle(shape__item_name = STRING("rect"),shape__number_of_sides = INTEGER(6), height = REAL(30.0), width = REAL(45.))


class TestSingleInheritanceMultiLevel(unittest.TestCase):
    '''
    unitary_schemas/test_single_inheritance_multi_level.py
    '''
    def test_import_schema_module(self):
        import test_single_inheritance_multi_level
    
    def test_schema(self):
        import test_single_inheritance_multi_level
        #my_base_shape = test_single_inheritance.shape(item_name = STRING("spherical shape"),number_of_sides = INTEGER(1))
        #my_shape = test_single_inheritance.rectangle(shape__item_name = STRING("rect"),shape__number_of_sides = INTEGER(6), height = REAL(30.0), width = REAL(45.))


class TestEnumEntityName(unittest.TestCase):
    '''
    unitary_schemas/test_enum_entity_name.py
    '''
    def test_import_schema_module(self):
        import test_enum_entity_name
    
    def test_schema(self):
        from test_enum_entity_name import *
        check_type(line,simple_datum_reference_modifier)
        checkt_type(translation,simple_datum_reference_modifier)

def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestSelectDataType))
   suite.addTest(unittest.makeSuite(TestSingleInheritance))
   suite.addTest(unittest.makeSuite(TestSingleInheritanceMultiLevel))
   suite.addTest(unittest.makeSuite(TestEnumEntityName))
   return suite

if __name__ == '__main__':
    unittest.main()


