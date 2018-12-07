""" This part of the package is for loading data of various types and then 
making traces.

Benjamin Barad
"""
from numpy import load
from scipy import stats
from trace import Trace
from pandas import read_table,DataFrame
import numpy as np
import re
# from table import table



def parse(filename):
    """Wrapper function for any loader functions that I may write besides 
    tpkl. Just passes through to the appropriate place based on the `mode` 
    variable."""
    if filename.endswith("dat"):
        return parse_dat(filename)
    else:
        raise TypeError('scattering data can only be read from the following filetypes: *.dat')

def parse_dat(filename):
    data = read_table(filename, delimiter="    ", engine='python', skiprows=1, names=['q','I','sigI'])
    q = data.q
    SA = data.I
    sigSA = data.sigI
    S = np.empty_like(data.q)
    sigS = np.empty_like(data.q)
    Nj = np.empty_like(data.q)
    return Trace(q, sigS, S, sigSA, SA, Nj)

dt = np.dtype({'names': ['q','S','sigS','SA','sigSA','Nj'],
                    'formats': ['<f8','<f8','<f8','<f8','<f8','<i8']})

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

def tryint(s):
    try:
        return int(s)
    except:
        return s
     
def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ] 

# Little stub for testing
if __name__ == "__main__":
	from sys import argv
	filename = argv[1]
	trace = parse(filename)
	print(trace)
