#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sequence.py
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
#  Thanks for using this! metfar@gmail.com
#


import sys;
from os import system;
import inspect;
try:
	raw_input;
	input=raw_input;#if python2, redefine input as raw_input (str_input)
except:
	raw_input=input;#only if anyone want to use raw_input in python3
#************************************************************************
#constants
RecursionLimit=10240;	#set this to low value if CutWhenPattern is off
						#suggested: 30-400
CutWhenPattern=True;#Flag to stop searching when pattern is recognized
CutSameValue=True;#if a number is repeated, the process ends

#************************************************************************


LF="\n";#enter
true=TRUE=True;#to avoid human error (mostly)
false=FALSE=False;
null=NULL=Nil=None;
#Greeting
_g=inspect.getsource(inspect.currentframe()).split(LF);
if (not("x" in sys.platform.lower())):
	LF+="\r";
Greetings=LF+_g[-2+_g.index("")][2:].strip()+LF;

HELP="""
%s  requires at least one argument

How to use it
-------------

%s -?|-h|--help       Shows this help

%s -i|--interactive   Enter into interactive mode (ask for input)

%s 0 1 2 3            Batch process all the values as function input

%s -r|--range 0 100   Process all numbers from 0 to 100

""";


def clrscr():
	system("cls | clear");#just call system cls or if it does not work, clear

def trimNotNumeric(x,allowed="-.0123456789"):
	""" Eliminate any non-numeric character from x and output it as 
		string;	take care that x=[-1,-2] =>  out="-1-2"
		"""
	
	out="";
	inp=str(x);
	for f in inp:
		if f in allowed:
			out+=f;
	return(out);
	
def toNum(x):
	""" Convert input into a floating point number """
	out=0.0;#default  value
	try:
		out=float(str(x));#try to convert it into a floating point 
	except:
		try:
			out=float(eval(trimNotNumeric(x)));#try trimming non-numeric
				# characters and then evaluate it because it could content operations
		except:
			pass; #we tried direct conversion and evaluated and it
				#  didn't work so give up
	return(out);

def function(i,interact=False):
	if(i%2 == 0):
		out=int(i/2);
		if(interact):
			print("Dividing "+str(i)+" by 2: "+str(out)+";",end="");
	else:
		out=int(3*i+1);
		if(interact):
			print("Multiplying "+str(i)+" by 3 and adding one: "+str(out),end="");
	if(interact):
		print(LF);
	return(out);

def processNum(num,interact=False):
	counter=0;
	sequence=[num];
	Cause="Recursion Limit";
	finishThis=False;#condition of trapped in 4 2 1 sequence
	while(counter<RecursionLimit and not finishThis):
		sequence.append(function(sequence[-1],interact));
		if(CutSameValue and  sequence[-1]==sequence[-2]):
			finishThis=True;#if last two values are the same,  finish (because 0)
			Cause="last=actual ("+str(sequence[-1])+"="+str(sequence[-2])+")";
			
		if (CutWhenPattern and				#flag to enable or disable pattern recognition
			(	sequence[-3:]==[4,2,1] 		#positive repetition sequence 
			or 	sequence[-2:]==[-2,-1]		#negative repetition sequence
			or	
				(len(set(sequence))>2 and set(sequence[:-3])==set(sequence))	
				)			#Set of results 3 steps before is same as now (repetition)
			):#repeating pattern
			finishThis=True;
			if(sequence[-3:]==[4,2,1]):
				Cause="Pattern [4,2,1]";
			if(sequence[-2:]==[-2,-1]):
				Cause="Pattern [-2,-1]";
			if (len(set(sequence))>2 and set(sequence[:-3])==set(sequence)):
				Cause="LoopStart "+str(sequence[-3:len(sequence)-2])
		counter+=1;
	return(sequence,Cause);
	
def main(args):
	APP=args.pop(0);#first argument is the name of this script
	if(len(args)<1 or (args[0].lower() in ["-?","-h","--help"])):#help
		print(HELP % tuple([APP]*HELP.count("%")));
		return(1);
		
	if(args[0].lower() in ["-i","--interactive"]): #if interactive mode
		out=False;
		while(not out):
			clrscr();
			num=int(				#we want an integer
					toNum(			#which must be a number (filter errors)
						input(		#received from the user
								"Give me a number: "
								)
						)
					);
			print();
			sequence,Cause=processNum(num,interact=True);
			print("F("+str(sequence[0])+"):",sequence[1:]," End:",Cause,"#",len(sequence)-1);
			resp=input("\nDo you want to try with another number? (Yes/no)\n");
			out="n" in resp.lower(); #if there is an N in your answer, it will exit
		return(0);
	if(args[0].lower() in ["-r","--range"]): #if interactive mode
		args.pop(0);
		try:
			_from=int(toNum(args.pop(0)));
			_to=int(toNum(args.pop(0)));
		except:
			print("\nPlease indicate two integers to mark the range to calculate\n");
			return(1);
		if(_from>_to):
			_from,_to=_to,_from;
		for f in range(_from,_to+1):
			sequence,Cause=processNum(f);
			print("F("+str(sequence[0])+"):",sequence[1:]," End:",Cause,"#",len(sequence)-1);
		return(0);
	else:#non-interactive process
		while (len(args)>0):
			num=int(toNum(args.pop(0))); #take first argument off array
			sequence,Cause=processNum(num);
			print("F("+str(sequence[0])+"):",sequence[1:]," End:",Cause,"#",len(sequence)-1);
		return(0);
	return(128);


if __name__ == '__main__':
	out=main(sys.argv);
	print(Greetings);
	sys.exit(out);
