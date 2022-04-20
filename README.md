# バックエンド仕様書

## 参考資料

[テーブル定義](https://drive.google.com/file/d/1SBlcqxVVnBg7FhLkjSUIEGMuT07aD1bL/view?usp=sharing)

## Excel データ を整形して csv 化する

```sh
$ \copy ledger from 'CSVファイルのパス' with CSV;
$ sed -i -e "s/,\$//" 'CSVファイルのパス'
```
