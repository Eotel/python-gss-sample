# python-gss-sample

gss api を利用してスプレッドシートを操作するときのサンプル

---

## Install

```
poetry install
```

- settings.json を作成する


## Google Sheets Document

- https://developers.google.com/sheets/api

```
worksheet.add_cols(col)		#col数だけ列を増やす
worksheet.add_rows(row)		#row数だけ行を増やす
worksheet.col_count 		#選択したワークシートの列数を取得
worksheet.row_count 		#選択したワークシートの行数を取得
worksheet.delete_row(row) 	#選択した行を削除する
worksheet.clear() 			#選択したワークシートの値を全てクリアする
```
