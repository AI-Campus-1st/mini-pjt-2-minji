# 마리아d 적재 및 검증

import pandas as pd
import pymysql 
from dotenv import load_dotenv
from pymysql.cursors import DictCursor
import os


def load_data():
    df = pd.read_csv('../data/raw/glowpick_20260906_clean.csv')
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

    # sql_product = """
    # INSERT INTO tb_product (category_id, brand, name)
    #     VALUES (%s, %s, %s)
    # """
    # with conn.cursor() as cur:
    #     for i in range(len(df)):
    #         row = df.iloc[i]
    #         category_id = row['category_id']
    #         brand = row['brand']
    #         name = row['product_name']
    #         cur.execute(sql_product, (category_id, brand, name))
    # conn.commit()
    # conn.close()

    # sql_ranking = """
    # INSERT INTO tb_ranking (
    #     product_id,
    #     current_rank,
    #     previous_rank,
    #     rank_change,
    #     update_date,
    #     rating,
    #     review_count,
    #     price
    # )
    # VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    # """
    # with conn.cursor() as cur:
    #     for i in range(len(df)):
    #         row = df.iloc[i]
    #         product_id = i + 1 
    #         current_rank = row['current_rank']
    #         previous_rank = row['previous_rank']
    #         rank_change = row['rank_change_value']
    #         update_date = row['update_date']
    #         rating = row['rating']
    #         review_count = row['review_count']
    #         price = row['price']
    #         cur.execute(sql_ranking, (product_id,
    #             current_rank,
    #             previous_rank,
    #             rank_change,
    #             update_date,
    #             rating,
    #             review_count,
    #             price))
    # conn.commit()
    # conn.close()

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