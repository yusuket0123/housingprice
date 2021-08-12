###
### engineering features
###

import re
import mojimoji
import pandas as pd
import numpy as np
import datetime as dt
import statistics as stc

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

    # 築年数
    def transform_bldgyrs(self):
        f = lambda x: dt.date.today().year - float(x)
        self.mydf['bldgyrs'] = self.mydf['est_year'].map(f)
        return self.mydf

    # ダミーでない変数を正規化
    def transform_std(self):
        # カラムのリストを取得
        colnames = self.mydf.columns

        # IDとダミー変数のカラムをリストから除外
        for i in range(len(colnames)):
            col = colnames[i]
            unique_vals = self.mydf[col].unique()
            print('{} \n {}'.format(col, unique_vals))

            # 処理をスキップ ID|市区町村コード|最寄駅：距離（分）|間取り|面積（㎡）|建築年

            string = ''.join(str(v) for v in unique_vals)
            print('changed: {} \n {}\n\n\n'.format(col, re.sub(r'(\d)|(\.)|(-)|(nan)', '', string)))

            condition_1 = "len(re.sub(r'(\d)|(\.)|(-)|(nan)', '', string)) > 0" # 文字列のカテゴリカル変数（get_dummiesする前）
            condition_2 = "np.nanmax(unique_vals) == 1 and np.nanmin(unique_vals) == 0" # ダミー変数
            condition_3 = "re.match(r'(ID)|(市区町村コード)', col)" # ID or 市区町村コード

            if eval(condition_1) or eval(condition_2) or eval(condition_3):
                continue

            ### calculate z score
            mu = np.nanmean(self.mydf[col])
            sigma = np.nanstd(self.mydf[col])
            f = lambda x: (x - mu) / sigma

            # 処理
            new_name = 'std_' + col
            self.mydf[new_name] = self.mydf[col].map(f)
            print('standardized column {} to {}'.format(col, new_name))

        return self.mydf
