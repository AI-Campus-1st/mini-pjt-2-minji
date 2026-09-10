# 마리아d 적재 및 검증

import pandas as pd
import pymysql 
from dotenv import load_dotenv
from pymysql.cursors import DictCursor
import os


def load_data():
    df = pd.read_csv('data/raw/glowpick_20260906_clean.csv')
    load_dotenv()

    DB_CONFIG = {
        'host': os.environ.get('DB_HOST', '127.0.0.1'),
        'port': int(os.environ.get('DB_PORT', "3306")),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', ''),
        'database': os.environ.get('DB_NAME', 'beauty_db'),
        'charset': 'utf8mb4',
        'autocommit': False,
    }

    conn = pymysql. connect(cursorclass=DictCursor, **DB_CONFIG)


    sql_score = """
    UPDATE tb_ranking
    SET score = %s
    WHERE product_id = %s
    """

    with conn.cursor() as cur:
        for i in range(len(df)):
            row = df.iloc[i]

            product_id = i + 1
            score = row['score']

            print(product_id, score)  # 확인

            cur.execute(sql_score, (score, product_id))

    conn.commit()
    conn.close()