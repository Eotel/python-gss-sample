#!/usr/bin/python
# -*- coding: utf-8 -*-
"""GSS.

* Google Sheets API を利用して Google Spread Sheat を編集する

Todo:
    * API を認証する
    * API を実行する部分を別クラスに分離する
    * 

"""

import json
import os
import sys

from logging import getLogger
from logging.config import dictConfig

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main():

    logger = getLogger(__name__)

    # logger の設定ファイルを読み込む
    if os.path.exists("logging.json"):
        with open("logging.json", "r", encoding="utf-8") as f:
            dictConfig(json.load(f))
    else:
        logger.info("logging.json が見つかりません")

    settings = {}

    # 設定ファイルを読み込む
    if os.path.exists("settings.json"):
        with open("settings.json", "r", encoding="utf-8") as f:
            settings: dict = json.load(f)
    else:
        logger.error("settings.json が見つかりません")
        return 1

    scope = settings.get("scope")

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        settings.get("keyfile"), scope  # type: ignore
    )

    # OAuth2の資格情報を使用してGoogle APIにログインします。
    gc = gspread.authorize(credentials)

    # 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
    SPREADSHEET_KEY = settings.get("spreadsheet_key")

    # 共有設定したスプレッドシートのシート1を開く
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    # A1セルの値を受け取る
    import_value = int(worksheet.acell("A1").value)

    # A1セルの値に100加算した値をB1セルに表示させる
    export_value = import_value + 100
    worksheet.update_cell(1, 3, export_value)

    # 正常終了
    return 0


if __name__ == "__main__":
    sys.exit(main())
