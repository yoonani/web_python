import streamlit as st
import pandas as pd
import numpy as np

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT title, description, table_name FROM data_info;', ttl="10m")
st.dataframe( df )

if st.button('추가'):
    with st.form("get_table_info") :
        title = st.text_input('데이터의 이름을 입력하세요', '')
        description = st.text_area('데이터에 대한 간략한 설명을 입력하세요', '')
        table_name = st.text_input('저정한 테이블의 이름을 입력하세요', '')
        submit = st.form_submit_button('데이터 정보 입력', type='secondary')
        sql = 'INSERT INTO data_info(title, description, table_name) VALUES(', title, "', '", description, "', '", table_name, "'"

    if submit:
        st.write( sql )
        conn.query( sql )

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.title} has a :{row.description}:")