import streamlit as st
import pandas as pd

# 서울 명소 위치
data = pd.DataFrame({
    'lat': [37.5665, 37.5700, 37.5796],
    'lon': [126.9780, 126.9920, 126.9770],
    'place': ['시청', '동대문', '경복궁']
})

st.map(data)

