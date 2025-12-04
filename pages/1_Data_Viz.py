import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# 페이지 기본 설정
# ------------------------------
st.title("📊 데이터 시각화 페이지")
st.write("CSV 파일을 업로드하고, Plotly로 인터랙티브 차트를 시각화합니다.")


# ------------------------------
# 1) 데이터 업로드 영역
# ------------------------------
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 완료!")
    
    st.subheader("📄 데이터 미리보기")
    st.dataframe(df.head())

    # ------------------------------
    # 2) 컬럼 선택
    # ------------------------------
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) < 2:
        st.warning("시각화를 위해 숫자형 컬럼이 최소 2개 필요합니다.")
    else:
        x_col = st.selectbox("X축 컬럼 선택", numeric_cols)
        y_col = st.selectbox("Y축 컬럼 선택", numeric_cols)

        # ------------------------------
        # 3) Plotly 시각화
        # ------------------------------
        st.subheader("📈 인터랙티브 Plotly 차트")

        fig = px.scatter(df, x=x_col, y=y_col,
                         title=f"{x_col} vs {y_col} 산점도",
                         trendline="ols")

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("CSV 파일을 업로드하면 시각화를 진행할 수 있습니다.")