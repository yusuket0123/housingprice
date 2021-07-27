###
### 実行用ファイル（housingpriceディレクトリ直下）
###

from loading.read import read
from loading.clean import process
from loading.clean import engineer

### 処理
def main():
    df_raw = read_data()
    #df_use = clean(df)
    print(df_raw.columns.values)
    df_tiny = clean(df = df_raw)
    print(df_tiny)
    print(df_tiny['deal'])

### データ読み込み
def read_data():
    files = read.Read(path = 'data/train') # path指定
    files.get_files() # ファイル名取得
    df_raw = files.read_files() # ファイル読み込み(dataframe)
    return df_raw

### データ加工
def clean(df):
    # カラム選択
    df_c1 = process.Select(df)
    cols = ['ID', '市区町村コード', '最寄駅：距離（分）', '間取り', '面積（㎡）', '建築年', '建物の構造', '用途', '今後の利用目的', '都市計画', '建ぺい率（％）', '容積率（％）', '取引時点', '改装', '取引の事情等', '取引価格（総額）_log']
    df_c1 = df_c1.select_cols(cols=cols)
    # 最寄
    df_c2 = process.Clean(df = df_c1).clean_moyori()
    df_c3 = process.Clean(df = df_c2).mutate_madori()
    df_c4 = process.Clean(df = df_c3).transform_kenchiku()
    df_c5 = process.Clean(df = df_c4).mutate_renov()
    df_c6 = process.Clean(df = df_c5).mutate_deal()
    return df_c6

### モデリング

### 結果出力

if __name__ == "__main__":
    main()
