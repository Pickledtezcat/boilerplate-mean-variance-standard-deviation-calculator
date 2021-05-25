import numpy as np

#starting project

def calculate(number_list):

  calc = {}

  if len(number_list) < 9:
    raise ValueError("List must contain nine numbers.")  

  a = np.array(number_list)
  b = a.reshape(3,3)
  
  calc["mean"] = [b.mean(axis=0).tolist(), b.mean(axis=1).tolist(), a.mean()]
  calc["variance"] = [b.var(axis=0).tolist(), b.var(axis=1).tolist(), a.var()]
  calc["standard deviation"] = [b.std(axis=0).tolist(), b.std(axis=1).tolist(), a.std()]
  calc["max"] = [b.max(axis=0).tolist(), b.max(axis=1).tolist(), a.max().tolist()]
  calc["min"] = [b.min(axis=0).tolist(), b.min(axis=1).tolist(), a.min()]
  calc["sum"] = [b.sum(axis=0).tolist(), b.sum(axis=1).tolist(), a.sum()]
  
  return calc