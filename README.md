# バックエンド仕様書

## 参考資料

### 事前準備

- src ディレクトリと同階層に csv ディレクトリを作成し、csv ファイルを置いてください。
  - プライベートな情報が入っているため、git の管理から外しています。

[テーブル定義](https://drive.google.com/file/d/1SBlcqxVVnBg7FhLkjSUIEGMuT07aD1bL/view?usp=sharing)  
※仕様書では緯度・経度がメッシュテーブルの管理となっていますが、現在の実装上では台帳テーブルで一括管理しています。  
※DB は Heroku Postgres を利用しています。  
[フロントエンドリポジトリ](https://github.com/yud0uhu/road-map)

## CSV ファイルの整形とインポート

```sh
$ sed -i -e "s/,\$//" 'CSVファイルのパス'
# ledgerテーブルにcsvファイルをインポートする
$ \copy ledger from 'CSVファイルのパス' with CSV;
```

## 実行コマンド

```sh
$ uvicorn --port 5000 --host 127.0.0.1 main:app --reload
```
