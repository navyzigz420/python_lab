# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 06:31:49 2018

@author: admin
"""

import pickle
game_data = {'data' : 'stuff',
        'more data' : ['more', 'stuff',"e altra ancora"],
        'money' : 500}

save_file = open('data.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('data.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()

print(loaded_game_data)