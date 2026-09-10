import os
import pymysql
import pandas as pd
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

@st.cache_data(ttl=3600)
def load_mart_data():

    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    query = """
    SELECT
        p.product_id,
        p.category_id,
        p.brand,
        p.name,
        r.current_rank,
        r.previous_rank,
        r.rank_change,
        r.rating,
        r.review_count,
        r.price,
        r.score
    FROM tb_product p
    JOIN tb_ranking r
        ON p.product_id = r.product_id
    ORDER BY p.category_id, r.score DESC;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df