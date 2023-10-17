import numpy as np
import matplotlib.pyplot as plt
import pyomo.environ as pyo
import pandas as pd
from ast import literal_eval as make_tuple
import networkx as nx

from pyomo.environ import SolverFactory
SOLVER = SolverFactory('glpk')
# opt = SolverFactory('glpk')

from idaes.core import FlowsheetBlock