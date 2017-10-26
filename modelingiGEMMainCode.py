#!/usr/bin/env python

#Modelling TODO
__author__      = "Renato Augusto Correa dos Santos"
__copyright__   = "Copyright 2017"
__license__     = "GPL v3.0"
__maintainer__  = "Renato Augusto Correa dos Santos"
__email__       = "renatoacsantos@gmail.com"

"""This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
from PyDSTool import *

parser = argparse.ArgumentParser(description='iGEM USP-SP 2017: Modelling ', add_help=True) #TODO: description of the script
parser.add_argument('-v','--version', action='version', version=version)
parser.add_argument('-o','--out', dest='out', metavar='file', type=str, help='Output', required=True) # TODO: improve description of output file(s)
parser.add_argument('-t','--temperature', dest='runTemp', choices=[20,25,30,37], help='Describe it. If user does not inform it, it is assumed 37 Celsius', required=False, type=int) # TODO: improve description of this parameter; check the paper about temperature inside the mosquito

args = parser.parse_args()
bamOBJ = args.bam
tempPar = args.runTemp
baseOut = args.out
outOBJ = open(fileHistOut,"w")

## declarations of symbolic objects
## Based on example: http://www.ni.gsu.edu/~rclewley/PyDSTool/Tutorial/Tutorial_SymbolicJac.html
# Variables:
# Na = P. agglomerans populations
# theta = Translation/Secretion rate
# mT = Toehold switch mRNA []
# mR = mRNA
# miP = protein degradation rate
# P = protein []
# alpha = mR-mT complex “Releasing” rate
#

y0 = Var('y0')
y1 = Var('y1')
y2 = Var('y2')
t = Var('t')

# Set temperature to value informed by user. If user does not pass it, assume the temperature is 37 Celsius.
if(args.runTemp):
 t = args.runTemp
else:
 t = 37

## Equations
## Based on example: http://www.ni.gsu.edu/~rclewley/PyDSTool/Tutorial/Tutorial_SymbolicJac.html
## Toehold-Switch
ydot0 = Fun(Na * (theta * mT * mR * (alpha - miP) * P), [Na,alpha,theta,mT,mR,miP,P], 'ydot0')
