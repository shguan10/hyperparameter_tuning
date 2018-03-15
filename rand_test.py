def bbox(a,b,c,d,e,f,g):
  return a+b+c+d+e+f+g

def compfun(res1,res2):
  if res1 > res2: return -1
  elif res2 > res1: return 1
  else: return 0

def main():
  from rand_search import RandSearcher as RS
  myrs = RS(bbox,compfun)
  ranges = {
    #c: (ord('a'),ord(c))
    c: (0,100)
    for c in 'abcdefg'
  }

  myrs.run(ranges,100,"test.pk")

  from opt_file_IO import read as opt_read
  (num_exp,best_recorded,best,exps) = opt_read("test.pk")
  assert(num_exp == 100)
  assert(best == myrs.best)
  assert(
    all([exps[expno] == myrs.results[expno] for expno in xrange(len(exps))])
    )
  return best
if __name__=='__main__': 
  from pprint import pprint as pp
  pp(main())