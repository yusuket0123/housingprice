root
├── README.md
├── analysis # データの基礎分析
├── config # 環境設定など
├── data  # データの保管場所。loadingのところで行った整形データもここに入る
├── loading # データのクレンジングや、ロード、整形処理を行う
├── model # モデルの処理
│   ├── predict # 予測を行う処理
│   └── train # 学習を行う処理
├── report  # 報告用の綺麗な画像などを保存したり、そのための処理を書くところ
├── result   # ログとか、解析の結果を保存する場所
│   ├── analysis  # analysisで行った結果を保存する場所
│   ├── loading  # loadingで行ったログを保存する場所
│   ├── model  # モデルの結果を保存する場所
│   │   ├── predict   # 予測結果の保存する場所
│   │   └── train   # 学習結果の保存する場所
│   └── validation  # 検証の結果を保存する場所
└── validation  # 検証を行うための場所
