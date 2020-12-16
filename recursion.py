#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  recursion.py
#  
#  Copyright 2020 William Martinez Bas <metfar@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys;
import inspect;

def recurse(name,firstIndex,lastIndex,firstValue,expression,verbose=True):
	"""
		recurse("c",1,4,5,"c[n]=c[n-1]+3")
		
		or
		
		recurse("c",1,4,5,"c[n-1]+3")
		
		"""
	step=name+"=[0.0]*(lastIndex+1);";
	exec(step);
	step=name+"["+str(firstIndex)+"]="+str(firstValue);
	exec(step);
	if(verbose):
		print(name,"[",firstIndex,"]=",eval(name+"[firstIndex]"));
	for n in range(firstIndex+1,lastIndex+1):
		if("=" in expression):
			step=expression;
		else:
			step=name+"[n]="+expression+";";
		exec(step);
		if(verbose):
			print(name,"[",n,"]=",eval(name+"[n]"));
		
	return(eval(name+"["+str(firstIndex)+":]"));
	
	
def main(args):
	print(recurse(name="c",firstIndex=1,lastIndex=4,firstValue=-5,expression="c[n]=c[n-1]+9",verbose=True));
	
	arithmeticExplicit=lambda n: 199-3*(n-1);#A+B(n-1)
	#print(inspect.getsource(arithmeticExplicit).strip());
	print(arithmeticExplicit(124));
	
	firstTerm=5;
	term10th=59;
	#Equation?
	#S=5+B(9)   59=5+B(9)   54=9B  b=54/9  B=6
	S=lambda n: 5+6*(n-1);#A+B(n-1)
	print(S(10));
	print("..................................");
	
	print(recurse(name="A",firstIndex=0,lastIndex=7,firstValue=-1,expression="3*A[n-1]-2*n +7",verbose=True));
	
	return(0);

if __name__ == '__main__':
	sys.exit(main(sys.argv));
