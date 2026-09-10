# KPI 카드, 사이드바 필터
import pandas as pd
import streamlit as st

# 테이블 컬럼 이름 지정 
def show_table(filtered_df, category_name):

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
        },
        hide_index=True,
        use_container_width=True
    )

    # CSV 변환
    csv = display_df.to_csv(
        index=False
    ).encode('utf-8-sig')

    # CSV 다운로드
    st.download_button(
        label="파일 다운로드",
        data=csv,
        file_name=f"{category_name}_TOP20.csv",
        mime="text/csv"
    )

def show_top3_cards(top3_df):

    cols = st.columns(3)

    for i, (_, row) in enumerate(top3_df.iterrows()):

        with cols[i]:

            st.markdown(f"##### {row['brand']}")
            st.write(row['name'])
            st.write(f"score : {row['score']}")

            # 1번째 줄
            row1 = pd.DataFrame({
                "현재 순위": [f"{row['current_rank']}위"],
                "전주 순위": [f"{row['previous_rank']}위"],
                "순위 변화": [f"🔺 {row['rank_change']}"]
            })

            st.dataframe(
                row1,
                hide_index=True,
                use_container_width=True
            )

            # 2번째 줄
            row2 = pd.DataFrame({
                "평점": [f"⭐ {row['rating']}"],
                "리뷰 수": [f"{row['review_count']}개"],
                "가격": [f"{row['price']:,}원"]
            })

            st.dataframe(
                row2,
                hide_index=True,
                use_container_width=True
            )

            # 선정 이유
            if row['rank_change'] >= 10:
                reason = (
                    f"전주 대비 {row['rank_change']}단계 상승하며 "
                    f"최근 주목도가 크게 증가한 상품입니다."
                )

            elif row['current_rank'] <= 5:
                reason = (
                    f"현재 {row['current_rank']}위의 상위권에 위치하며 "
                    f"전주 대비 {row['rank_change']}단계 상승한 상품입니다."
                )

            else:
                reason = (
                    f"전주 대비 {row['rank_change']}단계 상승하고 "
                    f"평점 {row['rating']}점을 기록한 상품입니다."
                )

            st.caption(reason)


def show_kpi(filtered_df):
    rising_products = len(filtered_df[filtered_df["rank_change"] > 0])
    rising_ratio = (
        rising_products / len(filtered_df) * 100
        if len(filtered_df) > 0 else 0
    )

    c1, c2 = st.columns(2)

    c1.metric("순위 상승 상품 수", f"{rising_products}개")
    c2.metric("순위 상승 상품 비율", f"{rising_ratio:.1f}%")

def show_sidebar():
    with st.sidebar:
        st.header("차트 상세보기")

        selected_chart = st.radio(
            "페이지 선택",
            [
                "대시보드 홈",
                "순위 상승폭 TOP5",
                "주요 상품 순위 변화",
                "현재 순위별 평점 분포",
                "프로모션 후보 선정 기준"
            ]
        )

        st.divider()

        st.caption("데이터 출처: Glowpick")
        st.caption("데이터 기준일: 2026-09-06")

    return selected_chart

    
