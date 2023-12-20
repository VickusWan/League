# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:51:29 2023

@author: Victor
"""

import league_data
import pandas as pd
from tqdm import tqdm
import league_data

df = pd.read_csv('aram_games.csv', header=None)
aram_games = df[0].tolist()