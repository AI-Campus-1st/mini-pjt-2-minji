# KPI 카드, 사이드바 필터
import pandas as pd
import streamlit as st

# 테이블 컬럼 이름 지정 
def show_table(filtered_df):
    display_df = filtered_df.copy()
    display_df = display_df.drop(columns=['product_id'])
    display_df['category_id'] = display_df['category_id'].replace({
        1: '베이스 메이크업',
        2: '아이 메이크업',
        3: '립 메이크업'
    })

    st.dataframe(
        display_df,
        column_config={
            "category_id": st.column_config.Column("카테고리"),
            "brand": st.column_config.Column("브랜드"),
            "name": st.column_config.Column("상품명"),
            "current_rank": st.column_config.Column("현재 순위"),
            "previous_rank": st.column_config.Column("전주 순위"),
            "rank_change": st.column_config.Column("순위 변화"),
            "rating": st.column_config.Column("평점"),
            "review_count": st.column_config.Column("리뷰 수"),
            "price": st.column_config.Column("가격"),
            "score": st.column_config.Column("총 점수")
        }
    )

def show_top3_cards(top3_df):
    cols = st.columns(3)

    for i in range(3):
        product = top3_df.iloc[i]

        with cols[i]:
            product = top3_df.iloc[i]

            st.write(product['brand'])
            st.write(product['name'])
            st.write(f'score : {product['score']}')

            row1 = st.columns(3)

            with row1[0]:
                st.write('현재 순위')
                st.write(f'{product['current_rank']}위')
            with row1[1]:
                st.write('전주 순위')
                st.write(f'{product['previous_rank']}위')
            with row1[2]:
                st.write('순위 변화')
                st.write(f'🔺{product['rank_change']}')

            row2 = st.columns(3)

            with row2[0]:
                st.write('평점')
                st.write(f'⭐{product['rating']}')
            with row2[1]:
                st.write('리뷰 수')
                st.write(f'{product['review_count']}개')
            with row2[2]:
                st.write('가격')
                st.write(f'{product['price']}원')