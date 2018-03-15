import random

"""
This module contains the RandSearcher class, which randomly searches the hyperparameter space of some black box function and reports its findings in a list of ((parameters),(results)) tuples
"""
class RandSearcher:
  def __init__(self,bboxfun,compfun=None):
    """
    ACCEPTS:
      bboxfun: blackbox function to search the parameter space of,
                  this function must ACCEPT
                    dictionary of float-valued parameters
                  and must RETURN
                    result that is comparable using the compfun function
      
      compfun: optional comparator function that compares the results to find which is best
        compfun(res1,res2)
        must ACCEPT:
          res1 and res2 are in same format as whatever bboxfun returns
        must RETURN:
          positive if res1 better than res2, negative if other way, 0 if same

    """
    self.bbox = bboxfun
    self.compfun = compfun
    self.best = None
    self.results = []

  def run(self,ranges,num_experiments, outfile=None):
    """
    Runs the RandSearcher over the specified ranges. Results will be recorded in self.results, and optionally saved to file outfile

    ACCEPTS:
      ranges: dictionary of tuples of (start,stop), dictionary is keyed by the names of the parameters
      
      num_experiments: number of function evaluations of self.bbox, with the parameters within the specified ranges

      outfile: optional file to write the results in 
        TODO, currently this is pickled

    RETURNS:
      self.results: a list of tuples of form ((params),(result))
    """
    if outfile: import cPickle as pk

    params = list(ranges.keys())

    #trials is list of param_dict to be fed into self.bbox
    trials = [
      {
        p: random.uniform(ranges[p][0], ranges[p][1])
        for p in params
      }
      for x in xrange(num_experiments)
    ]

    if outfile:
      with open(outfile,'ab') as f: 
        if self.compfun: pk.dump((len(trials),True),f)
        else: pk.dump((len(trials),False),f)

    for trial in trials:
      res = self.bbox(**trial)
      if outfile: 
        with open(outfile,'ab') as f:  pk.dump((trial,res),f)
      self.results.append((trial,res))      
      if self.compfun and (not self.best or self.compfun(self.best,res) < 1):
        self.best = res

    if outfile and self.compfun:
      with open(outfile,'ab') as f: pk.dump(self.best,f)

    return self.results