#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parts.py
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

def powerset(U):
	x = len(U);
	out=[];
	for i in range(1<< x):
		out.append([U[j] for j in range(x) if (i & (1<< j))]);
	return(out);
	
def main():
	U=[16,17,19,26,27,29];
	P_U=powerset(U);
	P_U.sort();
	flag=1;
	O=set(U);
	print("𝕌=",O,"\n");
	print("𝒫(𝕌)=","{",end="");
	for f in P_U:
		a=set(f);
		if(a==set()):
			a="{}";
		else:
			a=str(set(f));
		print(a,end="");
		if(flag<len(P_U)):
			print(", ",end="");
		flag+=1;
		
	print(" }\n#𝒫(𝕌)=",len(P_U));
				
	return(0);

if __name__ == '__main__':
	main()

