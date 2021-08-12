/root<br>
|-- README.md<br>
|-- analysis # データの基礎分析<br>
|-- config # 環境設定など<br>
|-- data  # データの保管場所。loadingのところで行った整形データもここに入る<br>
|-- loading # データのクレンジングや、ロード、整形処理を行う<br>
|-- model # モデルの処理<br>
|   |-- predict # 予測を行う処理<br>
|   |-- train # 学習を行う処理<br>
|-- report  # 報告用の綺麗な画像などを保存したり、そのための処理を書くところ<br>
|-- result   # ログとか、解析の結果を保存する場所<br>
|   |-- analysis  # analysisで行った結果を保存する場所<br>
|   |-- loading  # loadingで行ったログを保存する場所<br>
|   |-- model  # モデルの結果を保存する場所<br>
|   |   |-- predict   # 予測結果の保存する場所<br>
|   |   |-- train   # 学習結果の保存する場所<br>
|   |-- validation  # 検証の結果を保存する場所<br>
|-- validation  # 検証を行うための場所<br>
