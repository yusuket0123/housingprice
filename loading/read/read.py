####################
### read csv files
####################

import numpy as np
import pandas as pd
import os

class Read:

    def __init__(self, path): # インスタンスかメソッド
        self.mypath = path
        self.files = []

    ### check files in the directory
    def get_files(self):
        f = os.listdir(self.mypath)
        self.files = f
        print("num_pref: " + str(len(self.files)) + "\n" + str(self.files))

    ### read and merge csv files
    def read_files(self):
        for f in self.files:
            fpath = self.mypath + '/' + f
            if f == self.files[0]:
                df = pd.read_csv(fpath)
            else:
                df_by_pref = pd.read_csv(fpath)
                df = pd.concat([df, df_by_pref], axis = 0) # vertically merge files

        return df
