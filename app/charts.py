# 그래프 함수
import pandas as pd
import plotly.express as px
import streamlit as st

from colors import (
    PASTEL_BLUE,
    PASTEL_PINK,
    PASTEL_MINT,
    PASTEL_COLORS
)


def show_rank_change_top5(filtered_df):
    top5_df = filtered_df[filtered_df['rank_change'] > 0]
    top5_df = top5_df.sort_values(by='rank_change', ascending=False)
    top5_df = top5_df[:5]

    fig = px.bar(
        top5_df,
        x='rank_change',
        y='name',
        title='전주 대비 순위 상승폭 TOP5',
        labels={
            'rank_change': '상승폭',
            'name': '상품명'
        },
        text='rank_change',
        color_discrete_sequence=[PASTEL_BLUE]
    )

    fig.update_yaxes(categoryorder='total ascending')

    st.plotly_chart(fig)


def show_rank_comparison(filtered_df):

    top3_df = filtered_df[filtered_df['rank_change'] > 0]

    top3_df = top3_df.sort_values(
        by='rank_change',
        ascending=False
    )

    top3_df = top3_df[:3]

    rank_df = pd.melt(
        top3_df,
        id_vars=['name'],
        value_vars=['previous_rank', 'current_rank'],
        var_name='week',
        value_name='rank'
    )

    rank_df['week'] = rank_df['week'].replace({
        'previous_rank': '전주',
        'current_rank': '이번 주'
    })

    fig = px.line(
        rank_df,
        x='week',
        y='rank',
        color='name',
        markers=True,
        title='주요 상품 순위 변화',
        labels={
            'week': '',
            'rank': '순위',
            'name': '상품명'
        },
        text='rank',
        color_discrete_sequence=PASTEL_COLORS
    )

    fig.update_yaxes(autorange='reversed')

    st.plotly_chart(fig, theme='streamlit')


def show_rating_review(filtered_df, top3_df):

    filtered_df = filtered_df.copy()

    filtered_df['group'] = filtered_df['name'].apply(
        lambda x: '프로모션 TOP3'
        if x in top3_df['name'].values
        else '전체 상품'
    )

    fig = px.scatter(
        filtered_df,
        x='current_rank',
        y='rating',
        color='group',
        title='현재 순위별 평점 분포',
        labels={
            'current_rank': '현재 순위',
            'rating': '평점',
            'group': ''
        },
        hover_name='name',
        color_discrete_map={
            '프로모션 TOP3': PASTEL_PINK,
            '전체 상품': PASTEL_BLUE
        }
    )

    st.plotly_chart(fig)



def show_promotion_criteria():

    st.header("프로모션 후보 선정 기준")

    selected_score = st.radio(
        "점수 기준 선택",
        [
            "순위 상승폭 · 40점",
            "현재 순위 · 30점",
            "평점 · 30점",
            "최종 점수"
        ],
        horizontal=True
    )

    st.divider()

    if selected_score == "순위 상승폭 · 40점":
        st.subheader("순위 상승폭 · 40점")
        st.write("전주 대비 순위가 많이 상승할수록 높은 점수를 부여합니다.")

        st.code("""
            순위 상승폭 점수
            = (상품의 순위 상승폭 / 전체 상품 중 최대 상승폭) * 40
        """)

    elif selected_score == "현재 순위 · 30점":
        st.subheader("현재 순위 · 30점")
        st.write("현재 순위가 높을수록 높은 점수를 부여합니다.")

        st.code("""
            현재 순위 점수
            = ((20 - 현재 순위) / 19) * 30
        """)

    elif selected_score == "평점 · 30점":
        st.subheader("평점 · 30점")
        st.write("전체 상품의 최소·최대 평점을 기준으로 0~30점으로 환산합니다.")

        st.code("""
            평점 점수
            = ((상품 평점 - 최소 평점)
            / (최대 평점 - 최소 평점)) * 30
        """)

    elif selected_score == "최종 점수":
        st.subheader("최종 점수")

        st.code("""
            최종 점수
            = 순위 상승폭 점수
            + 현재 순위 점수
            + 평점 점수
        """)

        st.write("최종 점수는 100점 만점입니다.")