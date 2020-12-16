#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plotting.py
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

from sequence import *
import numpy as np;
import matplotlib.pyplot as plt;
import os;
import pandas as pd;

def main(args):
	if (len(args)<2):
		print(args[0]+" requires one filename as argument! ");
		return(1);
	name=args[1];
	if (not (os.path.exists(name) and os.path.isfile(name))):
		print("Couldn't open "+name+" or it doesn't  exist!");
		return(2);
	arch=open(name,"r");
	dat=[int(f) for f in arch.read().strip().split()];
	data=pd.DataFrame(dat);
	arch.close();
	data.plot(kind="line");
	#plt.plot(data);
	plt.savefig(name+".png");
	#plt.show();
	
	print("               Filename: ",name);
	print("            Data Length:",len(data));
	print("           Data Average:",np.average(data));
	print("Data Standard Deviation:",np.std(data[0]));
	print("                Graphic: ",name+".png");
	return(0)

if __name__ == '__main__':
	out=main(sys.argv);
	print(Greetings);
	sys.exit(out);
