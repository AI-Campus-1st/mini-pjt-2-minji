import streamlit as st
import pandas as pd

from repository import load_mart_data
from components import show_table
from components import show_top3_cards


st.set_page_config(
    page_title="메이크업 상품 프로모션 분석",
    layout="wide"
)

st.title('메이크업 상품 프로모션 분석')
st.write('최근 랭킹 변화와 소비자 반응을 기반으로 프로모션 우선 상품 탐색')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('[베이스 메이크업]'):
        st.session_state['category'] = 'foundation'

with col2:
    if st.button('[아이 메이크업]'):
        st.session_state['category'] = 'eyeshadow'

with col3:
    if st.button('[립 메이크업]'):
        st.session_state['category'] = 'lip'

if 'category' not in st.session_state:
    st.session_state.category = 'foundation'

# if st.session_state.category == 'foundation':
#     st.title('베이스 메이크업')

# elif st.session_state.category == 'eyeshadow':
#     st.title('아이 메이크업')

# elif st.session_state.category == 'lip':
#     st.title('립 메이크업')

df = load_mart_data()
#st.dataframe(df)

if st.session_state.category == 'foundation':
    category_id = 1

elif st.session_state.category == 'eyeshadow':
    category_id = 2

elif st.session_state.category == 'lip':
    category_id = 3

filtered_df = df[df['category_id'] == category_id]
#st.dataframe(filtered_df)
top3_df = filtered_df[filtered_df['rank_change'] > 0]
top3_df = top3_df.sort_values(by='score', ascending=False)
top3_df = top3_df[:3]

show_top3_cards(top3_df)
st.divider()
show_table(filtered_df)
