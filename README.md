# バックエンド仕様書

## 参考資料

[テーブル定義](https://drive.google.com/file/d/1SBlcqxVVnBg7FhLkjSUIEGMuT07aD1bL/view?usp=sharing)

## CSV ファイルを整形する

```sh
$ \copy ledger from 'CSVファイルのパス' with CSV;
$ sed -i -e "s/,\$//" 'CSVファイルのパス'
```
