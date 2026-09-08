import streamlit as st
import pandas as pd


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

if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
    st.title('메인')
    