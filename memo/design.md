# 分析設計

## 読み込み
都道府県ごとにファイルが分かれているので、読み込んだのち突合する

## 加工

### 元の列
['ID' '種類' '地域' '市区町村コード' '都道府県名' '市区町村名' '地区名' '最寄駅：名称' '最寄駅：距離（分）' '間取り'
 '面積（㎡）' '土地の形状' '間口' '延床面積（㎡）' '建築年' '建物の構造' '用途' '今後の利用目的' '前面道路：方位'
 '前面道路：種類' '前面道路：幅員（ｍ）' '都市計画' '建ぺい率（％）' '容積率（％）' '取引時点' '改装' '取引の事情等'
 '取引価格（総額）_log']

### 変数定義
* ID: string(categorical)
* 市区町村コード: string(categorical)
* 最寄駅：距離（分）: numeric
* 間取り: int
* 面積（㎡）: numeric
* 建築年: int -> 築年数: int
* 建物の構造: string(categorical)
* 用途, 今後の利用目的 -> 用途+今後の利用目的: string(categorical)
* 都市計画: string(categorical)'
* 建ぺい率（％）: numeric
* 容積率（％）: numeric
* 取引時点: int
* 改装: dummy
* 取引の事情等: dummy
* 取引価格（総額）_log: numeric

### 削除列
種類, 地域, 都道府県, 市区町村, 地区名, 最寄駅（名称）, 土地の形状, 間口, 延べ床面積, 前面道路(３列)

### 加工列
* 市区町村コード: str(categ)
* 最寄駅：文字列として認識する場合のユニークな値を取得し、パターンごとに正規表現で処理（2つ値が入っている場合は中央値で処理?）cl
* 間取り：L/D/Kダミーをそれぞれ作り"nLDK"のnの値をそれぞれのダミーに掛け合わせる cl/en
* 建築年: 西暦に変換 cl
* 建物の構造: ユニークな値を確認->ダミー作成
* 用途+今後の利用目的: 用途をベースとして用いる、 用途がNULL&今後の利用目的がNULLでない場合今後の利用目的を使う、用途と今後の利用目的が一致しない場合は用途を優先
* 取引時点: 年ダミー
* 改装: 未改装=0, 改装済=1
* 取引の事情等: 調停ダミー作成（NULLを0に）

### 参考情報
#### 建物構造
* 木造（W造）
* 軽量鉄骨造(S造)
* 重量鉄骨造(S造)
* 鉄筋コンクリート造(RC造）
* 鉄骨鉄筋コンクリート造(SRC造）
* アルミ造(AL造)
* コンクリート充填鋼管構造(CFT造)
* コンクリートブロック造(CB造)

### 加工工程
1. クリーニング(process.py)
  1. カラム選択
  2. 変数定義に合うように各カラムをクレンジング
    1. 最寄駅
    2. 間取り
    3. 建築年
    4. 改装
    5. 取引の事情等
    6. 面積
2. エンジニアリング(engineer.py)
  1. 新しくカラムを作成
    1. 用途+今後の利用目的
  2. そのままでも分析に使用できるカラムを加工
    1. 建築年を築年数に
    2. ダミーでない特徴量を正規化
3. 最終化
  1. 列名変更
  2. 列選択（分析に使うもののみ。データ加工のために残していた列も消す）

### オブジェクト命名
* 読み込んだdf: df_raw
* 加工途中のdf
   * main関数: df_tiny
   * 中間処理の関数: df_c# (#は番号)
* 最終加工後のdf: df_use

## モデル選択
* exboost

## モデル学習
* get_dummiesする
