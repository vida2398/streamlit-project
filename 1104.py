
# cd streamlit
# streamlit run 1104.py
# ctrl + s
# print("hello")
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px # 인덱스 인지 못함..! as_index = False
def show_home():
    st.header("너는 HOME을 선택했다.")
    st.image("cat.jpg")
    # st.video("유튜브 URL 아무거나")

def show_car():
    st.header("너는 자동차 분석을 선택했다.")
    mpg = pd.read_csv("mpg.csv")
    st.subheader("자동차데이터입니다.")
    st.dataframe(mpg)

    #manufacturer 별로 cty의 평균을 구하고, 화면에 나타내다
    st.subheader("차동차 회사 별 도시평균 연비를 구하자")
    mpg = mpg.groupby("manufacturer", as_index=False).agg(cty평균 = ("cty","mean"))
    st.dataframe(mpg)

    # 그래프 그리자
    # import matplotlib.pyplot as plt
    # sns.barplot(data = mpg, x="manufacturer", y ="cty평균") -> 강 하면 안 됨
    fig1 = plt.figure()
    sns.barplot(data = mpg, x="manufacturer", y ="cty평균")
    st.pyplot(fig1)

    # import plotly.express as px
    c1 = px.bar(data_frame=mpg, x = "manufacturer", y = "cty평균")
    st.plotly_chart(c1)
def show_car_deep():

    st.header("너는 자동차 '심층'분석을 선택했다.")
    mpg = pd.read_csv("mpg.csv")
    # 1. 현대차 리스트를 보여줘라. (하드코딩 -> selectbox 입력받기)
    result2 = mpg.query("manufacturer == 'hyundai'")
    st.subheader(" #1. 현대차 리스트 = 하드코딩")
    st.dataframe(result2)

    # 2. 현대차 리스트 - 변수 처리
    company1 = 'hyundai'
    result3 = mpg.query("manufacturer == @company1")
    st.subheader(" #2. 현대차 리스트 - 변수처리")
    st.dataframe(result3)

    # 3. 회사를 사용자가 입력
    st.subheader(" #3 회사를 사용자가 입력")
    selectedCar = st.selectbox("자동차회사를 선택하시오", mpg['manufacturer'].unique().tolist())
    result4 = mpg.query("manufacturer == @selectedCar")
    st.dataframe(result4) # 여전히 하드 코딩 mpg['manufacturer'].unique().tolist() 로 해결

    # 4.마음대로 데이터를 분석하기( 사용자가 옵션 선택 )
    # 1) groupby ??? - 선택지            -input1(회사, 카테고리, 구동방식(drv), 출시년도(year))
    # 2) cty or hwy ???                 -input2
    # 3) 수학통계 ??? - 최대? 최소? mean?  -input3
    input1 =  st.selectbox("그룹핑 대상 고르기", mpg.columns)
    input2 =  st.selectbox("계산 대상 고르기", ['cty', 'hwy'])
    input3 =  st.selectbox("계산 방법 고르기", ["mean", "max", "min"])
  
    result5 = mpg.groupby(input1).agg(value = (input2, input3))
    st.subheader("마음대로 분석하기")
    st.text(input1 + " 을 그룹핑해서, " + input2 + " 의 " + input3 +"(으)로 계산했다.")
    st.dataframe(result5)






# st.sidebar.header("사이드 바 입니다.")
# st.sidebar.image("cat.jpg")
selectedmenu = st.sidebar.selectbox("메뉴제목입니다", ['HOME', '자동차분석', '자동차심층분석'])

if selectedmenu == 'HOME':
    show_home()
elif selectedmenu == '자동차분석':
    show_car()
elif selectedmenu == '자동차심층분석':
    show_car_deep()
else:
    st.header("나머지")
