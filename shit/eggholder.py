import numpy as np
import random
import tkinter as tk
import math
import plotly.graph_objects as go
import libs.genetic_all as ga


numgen = 1000
lpop = 50
lstring   = 20
B = [[0, 0], [77,68], [12,75], [32,17], [51,64], [20,19], [72,87], [80,37], [35,82], [2,15], [18,90], [33,50], [85,52], [97,27], [37,67], [20,82], [49,0], [62,14], [7,60], [100, 100]]
M = 500
Space = np.array([np.ones(lstring) * (-M), np.ones(lstring) * M])
Delta = Space[1, :] / 1000.0





def basicGA(Pop,Fit):
  Best, _ = ga.selbest(Pop,Fit, [1, 1, 1])
  Old, _ = ga.seltourn(Pop, Fit, 27)

  Sub_Pop1, _ = ga.selsus(Pop, Fit, 20)

  ga.crossov(Old, 2, 0)
  ga.mutx(Old, 0.10, Space)
  ga.muta(Old, 0.15, Delta, Space)

  ga.crossov(Sub_Pop1, 1, 0)
  ga.mutx(Sub_Pop1, 0.10, Space)
  ga.muta(Sub_Pop1, 0.14, Delta, Space)

  Pop = np.vstack((Old, Best))
  return Pop

for gen in range(1, numgen+1):

  Fit = ga.eggholder(Pop)

  evolution[gen] = min(Fit)

  Pop = basicGA(Pop, Fit)

generations = list(range(numgen + 1))