from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import psycopg2
import pandas as pd

# PostgreSQL 데이터베이스에 연결
def connect_to_db():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PWD")
    )
    return conn

# 테이블 데이터 표시 함수
def display_table_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_info")
    data = cursor.fetchall()
    conn.close()

    # 데이터를 DataFrame으로 표시
    df = pd.DataFrame(data)  # 실제 열 이름으로 변경
    st.write(df)

# 새로운 행 삽입 함수
def insert_new_row():
    conn = connect_to_db()
    cursor = conn.cursor()

    # 사용자 입력으로 새로운 행 값 가져오기
    title = st.text_input("저장한 데이터의 이름을 입력하세요")
    description = st.text_area("저장한 데이터에 대한 설명을 입력하세요")
    table_name = st.text_input("DB에 저장한 테이블 이름을 입력하세요")

    if st.button("table 정보 저장"):
        cursor.execute("INSERT INTO data_info ( title, description, table_name) VALUES (%s, %s, %s)",
                       (title, description, table_name))  # 실제 테이블 이름과 열 이름으로 변경
        conn.commit()
        st.success("새로운 정보를 저장했습니다.")


    conn.close()


# 메인 Streamlit 앱
def main():
    st.title("Q's Data")
#    st.write("PostgreSQL 테이블을 보고 데이터를 삽입하세요.")

    # 기존 테이블 데이터 표시
    st.write("## 저장한 데이터")
    display_table_data()

    # 새로운 행 삽입
    st.write("## 새로운 데이터를 입력하세요")
    insert_new_row()

if __name__ == "__main__":
    main()