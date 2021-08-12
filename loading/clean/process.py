###
### processing data
###
import re
import mojimoji
import pandas as pd
import numpy as np

### Clean().clean_moyoriで使用
def get_ave(s):
    strs = re.findall(r"\d+", s)
    nums = [int(s) for s in strs]
    if len(strs) > 0:
        ave = sum(nums) / len(strs)
    else:
        ave = nums
    return ave

### Clean().mutate_madoriで使用
def get_ldkvalue(s, pattern): # s = '4LDK'
    s = str(s)
    val = 0
    if re.match(r'{}'.format(pattern), s):
        val = 1 * int(re.search(r'\d', s).group())
    else:
        val = 0
    return val

# 西暦に変換
def get_seireki(s):
    s = str(s)
    val = 0
    if s != '':
        if re.match(r'.*昭和.*' ,s):
            val = int(re.search(r'\d+', s).group()) + 1925
        elif re.match(r'.*平成.*' ,s):
            val = int(re.search(r'\d+', s).group()) + 1989
        elif re.match(r'.*令和.*' ,s):
            val = int(re.search(r'\d+', s).group()) + 2019
        elif re.match(r'.*戦前.*' ,s):
            val = 1945
        else:
            val = '想定外の元号'
    else:
        val = s

    return val

class Select():

    def __init__(self, df):
        self.mydf = df

    def select_cols(self, cols):
        df_new = self.mydf[cols]
        return df_new

class Clean():

    def __init__(self, df):
        self.mydf = df

    # 最寄駅からの距離のカラム作成
    def clean_moyori(self):
        f = lambda x: get_ave(str(x))
        self.mydf['dist_sta'] = self.mydf['最寄駅：距離（分）'].map(f, na_action= 'ignore')
        return self.mydf

    # 面積m2以上から数字部分だけ取り出す
    def clean_area(self):
        f = lambda x: int( re.sub(r'\D', '', str(x) ) )
        self.mydf['area'] = self.mydf['面積（㎡）'].map(f)
        return self.mydf

    # 間取り
    def mutate_madori(self):
        # LDKそれぞれ分ける
        for i in ['L', 'D', 'K']: #元の値は全角なのでmojimojiを使う
            pattern = '.*' + i + '.*'
            colname = 'madori_' + i
            f = lambda x: get_ldkvalue(s = mojimoji.zen_to_han(x), pattern = pattern) #数字以外は消去してnをかける
            self.mydf[colname] = self.mydf['間取り'].map(f, na_action= 'ignore')
        return self.mydf

    # 建築年を西暦に変換
    def transform_kenchiku(self):
        self.mydf['est_year'] = self.mydf['建築年'].map(get_seireki, na_action = 'ignore')
        return self.mydf

    # 改装ダミー
    def mutate_renov(self):
        f = lambda x: 1 if x == '改装済' else 0
        self.mydf['rnvtn'] = self.mydf['改装'].map(f, na_action = 'ignore')
        return self.mydf

    # 取引の事情等ダミー
    def mutate_deal(self):
        f = lambda x: 1 if x == False else 0
        self.mydf['deal'] = self.mydf['取引の事情等'].isna().map(f)
        return self.mydf

    # clean_moyori値取得（確認用）
    def check_moyori(self):
        uni_list_old = self.mydf['最寄駅：距離（分）'].unique()
        uni_list_new = self.mydf['dist_sta'].unique()
        print('before: \n {} \n after: \n {}'.format(uni_list_old, uni_list_new))
