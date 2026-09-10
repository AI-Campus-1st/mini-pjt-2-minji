import os
import pandas as pd
import pymysql
from dotenv import load_dotenv


load_dotenv()

# clean CSV 불러오기
df = pd.read_csv(
    'data/raw/glowpick_20260906_clean.csv'
)

# 날짜 형식 변환
df['update_date'] = pd.to_datetime(
    df['update_date'],
    format='%Y.%m.%d'
).dt.strftime('%Y-%m-%d')


# DB 연결
conn = pymysql.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    port=int(os.getenv('DB_PORT', '3306')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
    charset='utf8mb4'
)

cur = conn.cursor()


# score 업데이트
sql = """
UPDATE tb_ranking r
JOIN tb_product p
    ON r.product_id = p.product_id
SET r.score = %s
WHERE p.category_id = %s
  AND p.brand = %s
  AND p.name = %s
  AND r.update_date = %s
"""


for _, row in df.iterrows():

    cur.execute(
        sql,
        (
            row['score'],
            row['category_id'],
            row['brand'],
            row['product_name'],
            row['update_date']
        )
    )


conn.commit()

print(f"{len(df)}개 상품 score 업데이트 완료")


cur.close()
conn.close()