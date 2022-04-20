# バックエンド仕様書

## 参考資料

[テーブル定義](https://drive.google.com/file/d/1SBlcqxVVnBg7FhLkjSUIEGMuT07aD1bL/view?usp=sharing)  
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
