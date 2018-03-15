"""
This module contains a function which acts as a reader for the files generated by this library

FILE FORMAT:
  (Number of experiments, Best recorded?)
  [list of experiments]
  best result
"""
def read(filename):
  import cPickle as pk
  with open(filename,'rb') as f:
    num_exp,best_recorded = pk.load(f)
    exps = [pk.load(f) for _ in xrange(num_exp)]
    if best_recorded: best = pk.load(f)
  return (num_exp,best_recorded,best,exps)