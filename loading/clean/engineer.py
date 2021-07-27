###
### engineering features
###

import re
import mojimoji
import pandas as pd
import numpy as np

class Engineer():

    def __init__(self, df):
        self.mydf = df

    def combine_purpose(self): # '用途' '今後の利用目的'
        list_purpose = []
        df_current = self.mydf['用途'].isnull()
        df_future = self.mydf['今後の利用目的'].isnull()
        for idx in self.mydf.index:

            # print(df_tiny['用途'].isnull().iloc[idx])
            if df_current.iloc[idx] == False:
                list_purpose.append(self.mydf['用途'].iloc[idx])
            elif df_future.iloc[idx] == False:
                list_purpose.append(self.mydf['今後の利用目的'].iloc[idx])
            else:
                list_purpose.append(np.nan)

        self.mydf['purpose'] = list_purpose
        print('unique_value: \n{}'.format(self.mydf['purpose'].unique())) #['住宅' nan '事務所' 'その他' '店舗' '住宅、店舗' '駐車場' '住宅、その他' '住宅、事務所' '住宅、駐車場' '店舗、その他' '事務所、店舗' '駐車場、店舗' '倉庫' '住宅、事務所、駐車場、店舗' '倉庫、駐車場' '倉庫、店舗']

        return self.mydf
