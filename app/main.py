import streamlit as st

from repository import load_mart_data
from components import (
    show_table,
    show_top3_cards,
    show_sidebar
)
from charts import (
    show_rank_change_top5,
    show_rank_comparison,
    show_rating_review,
    show_promotion_criteria
)

st.set_page_config(
    page_title="메이크업 상품 프로모션 분석",
    layout="wide"
)

st.title("메이크업 상품 프로모션 분석")
st.write("최근 랭킹 변화와 소비자 반응을 기반으로 프로모션 우선 상품 탐색")

# 분석 대상 설명
st.info(
    "분석 대상은 베이스 메이크업의 파운데이션, "
    "아이 메이크업의 아이섀도우, "
    "립 메이크업의 립 틴트·라커입니다. "
    "Glowpick에서 각 세부 카테고리별로 독립적인 랭킹이 제공되기 때문에 "
    "동일한 기준으로 비교 가능한 세부 카테고리를 선정하여 "
    "각 카테고리 TOP20 상품을 분석했습니다."
)


# 카테고리 선택
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("[베이스 메이크업]"):
        st.session_state["category"] = "foundation"

with col2:
    if st.button("[아이 메이크업]"):
        st.session_state["category"] = "eyeshadow"

with col3:
    if st.button("[립 메이크업]"):
        st.session_state["category"] = "lip"


# 기본 카테고리 설정
if "category" not in st.session_state:
    st.session_state.category = "foundation"


# 데이터 불러오기
df = load_mart_data()


# 전체 데이터가 없는 경우
if df.empty:
    st.warning("불러올 데이터가 없습니다.")
    st.stop()


# 카테고리 설정
if st.session_state.category == "foundation":
    category_id = 1
    category_name = "베이스 메이크업 · 파운데이션"

elif st.session_state.category == "eyeshadow":
    category_id = 2
    category_name = "아이 메이크업 · 아이섀도우"

elif st.session_state.category == "lip":
    category_id = 3
    category_name = "립 메이크업 · 립 틴트·라커"


# 선택한 카테고리 데이터
filtered_df = df[df["category_id"] == category_id]


# 선택한 카테고리 데이터가 없는 경우
if filtered_df.empty:
    st.warning(f"{category_name} 데이터가 없습니다.")
    st.stop()


# 프로모션 TOP3 생성
top3_df = filtered_df[filtered_df["rank_change"] > 0]

top3_df = top3_df.sort_values(
    by="score",
    ascending=False
)

top3_df = top3_df[:3]


# 사이드바
selected_chart = show_sidebar()

st.divider()


# 화면 교체
if selected_chart == "대시보드 홈":

    # 핵심 결론 + KPI
    if not top3_df.empty:

        top_product = top3_df.iloc[0]

        rising_products = len(
            filtered_df[filtered_df["rank_change"] > 0]
        )

        rising_ratio = (
            rising_products / len(filtered_df) * 100
            if len(filtered_df) > 0 else 0
        )

        result_col, kpi_col1, kpi_col2 = st.columns(
            [3, 1, 1]
        )

        # 핵심 결론
        with result_col:
            st.subheader(
                f"{category_name}에서는 "
                f"{top_product['brand']}의 "
                f"'{top_product['name']}'이 "
                f"프로모션 우선 검토 1순위로 선정되었습니다."
            )

            st.write(
                f"현재 {top_product['current_rank']}위이며 "
                f"전주 대비 {top_product['rank_change']}단계 상승했고, "
                f"평점은 {top_product['rating']}점입니다."
            )

        # KPI 1
        with kpi_col1:
            st.metric(
                "순위 상승 상품 수",
                f"{rising_products}개"
            )

        # KPI 2
        with kpi_col2:
            st.metric(
                "순위 상승 상품 비율",
                f"{rising_ratio:.1f}%"
            )

    st.divider()


    # TOP3
    st.subheader(
        f"{category_name} 프로모션 우선 검토 TOP3"
    )

    if top3_df.empty:
        st.info(
            "현재 프로모션 우선 검토 대상 상품이 없습니다."
        )

    else:
        show_top3_cards(top3_df)


    st.divider()


    # 주요 분석 차트
    st.subheader("주요 분석 차트")

    columns = st.columns(3)

    with columns[0]:
        show_rank_change_top5(filtered_df)

    with columns[1]:
        show_rank_comparison(filtered_df)

    with columns[2]:
        show_rating_review(
            filtered_df,
            top3_df
        )


    st.divider()


    # TOP20 상세표
    st.subheader(
        f"{category_name} TOP20 상품 상세"
    )

    show_table(
        filtered_df,
        category_name
    )


elif selected_chart == "순위 상승폭 TOP5":

    st.subheader(
        f"{category_name} 순위 상승폭 TOP5"
    )

    show_rank_change_top5(filtered_df)


elif selected_chart == "주요 상품 순위 변화":

    st.subheader(
        f"{category_name} 주요 상품 순위 변화"
    )

    show_rank_comparison(filtered_df)


elif selected_chart == "현재 순위별 평점 분포":

    st.subheader(
        f"{category_name} 현재 순위별 평점 분포"
    )

    show_rating_review(
        filtered_df,
        top3_df
    )


elif selected_chart == "프로모션 후보 선정 기준":

    show_promotion_criteria()