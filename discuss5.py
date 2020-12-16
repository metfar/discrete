#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  discuss5.py
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
from os import system;
try:
	raw_input;
	input=raw_input;#if python2, redefine input as raw_input (str_input)
except:
	raw_input=input;#only if anyone want to use raw_input in python3

ESC=chr(27);

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
			print("Dividing "+str(i)+" by 2: "+str(out));
	else:
		out=int(3*i+1);
		if(interact):
			print("Multiplying "+str(i)+" by 3 and adding one: "+str(out));
	return(out);

def main(args):
	APP=args.pop(0);#first argument is the name of this script
	RecursionLimit=300;
	if(len(args)<1 or (args[0].lower() in ["-?","-h","--help"])):#help
		print("""
HELP
====

%s  requires at least one argument


%s -?|-h|--help       Shows this help

%s -i|--interactive   Enter into interactive mode (ask for input)

%s 0 1 2 3            Batch process all the values as function input

		""" % tuple([APP]*4));
		exit(1);
		
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
			counter=0;#to count steps
			sequence=[num];#to save the sequence
			finishThis=False;#condition of trapped in 4 2 1 sequence
			while(counter<RecursionLimit and not finishThis):
								#until it reaches the recursion limit 
				#run the algorithm with last number  of the sequence
				sequence.append(function(sequence[-1],interact=True));
										#interactive mode prints steps
				#if last two values are the same,  finish
				finishThis=(sequence[-1]==sequence[-2]);
				if (	sequence[-3:]==[4,2,1] 
					or 	sequence[-2:]==[-2,-1]
					or
						(len(set(sequence))>2 and set(sequence[:-3])==set(sequence))
						):#repeating pattern
					finishThis=True;
				counter+=1;
			print(sequence);
			resp=input("\nDo you want to try with another number? (Yes/no)\n");
			out="n" in resp.lower(); #if there is an N in your answer, it will exit
		exit(0);
	else:#non-interactive process
		while (len(args)>0):
			num=int(toNum(args.pop(0))); #take first argument off array
			counter=0;
			sequence=[num];
			finishThis=False;#condition of trapped in 4 2 1 sequence
			while(counter<RecursionLimit and not finishThis):
				sequence.append(function(sequence[-1]));
				finishThis=(sequence[-1]==sequence[-2]);#if last two values are the same,  finish
				if (	sequence[-3:]==[4,2,1] 
					or 	sequence[-2:]==[-2,-1]
					or
						(len(set(sequence))>2 and set(sequence[:-3])==set(sequence))
						):#repeating pattern
					finishThis=True;
				counter+=1;
			print("F("+str(sequence[0])+"):",sequence[1:]," #",len(sequence)-1);
		exit(0);
	return(0);

if __name__ == '__main__':
	sys.exit(main(sys.argv));
