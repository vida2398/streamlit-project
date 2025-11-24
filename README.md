# 📱 스마트폰 과의존 현상 분석 및 디지털 디톡스 가이드

## 🧩 데이터분석 프로젝트 설명
스마트폰 사용 증가와 코로나 시기를 중심으로 **스마트폰 과의존 현상**을 데이터로 분석한 프로젝트입니다.  

| 구분 | 내용 |
| :--- | :--- |
| **주제** | **스마트폰 과의존 현상 데이터 분석 및 디지털 디톡스 솔루션 제공 웹사이트** |
| **주제 선택 이유** | 사회적으로 심화되고 있는 스마트폰 과의존 문제를 데이터 분석과 시각화를 통해 객관적으로 진단하고, 사용자가 자신의 위험도를 테스트하며 실질적인 도움(디지털 디톡스 팁 및 상담 센터 안내)을 얻을 수 있는 **공익적 인터랙티브 웹 대시보드**를 구현하고자 했습니다. |
| **데이터 분석 내용** | - 뉴스 데이터를 기반으로 **과의존 위험군의 특징** 확인<br>- 연령대별 스마트폰 의존도 분석<br>- **콘텐츠 유형별 트래픽 현황** 분석<br>- 실업률과 스마트폰 의존도의 연관성 분석<br>- **디지털 디톡스** 실천을 위한 생활 팁 제시<br>- 전국 스마트 쉼 센터 위치 및 정보 안내 |

---

## 👥 팀원 소개 (Team Members)

| 이름 | 역할 | GitHub |
|------|------|------------------|
| 장혜미 | 팀장 · 개발자 | |
| 비다 | 개발자 | https://github.com/vida2398 |


---

## 🚀 웹사이트 실행 정보 및 링크

   * https://fred.stlouisfed.org/series/LRUNTTTTKRM156S
     
   * https://www.itstat.go.kr/itstat/main.html
     
   * https://www.itstat.go.kr/statHtml/statHtml.do?orgId=006&tblId=DT_127006_C005&vw_cd=undefined&list_id=undefined&scrId=&seqNo=&language=ko&obj_var_id=undefined&itm_id=undefined&conn_path=I2&path=
     
   * https://www.itstat.go.kr/statHtml/statHtml.do?orgId=006&tblId=DT_ITSTAT_A000004&vw_cd=undefined&list_id=undefined&scrId=&seqNo=&language=ko&obj_var_id=undefined&itm_id=undefined&conn_path=I2&path=

---

## 📝 코드 및 실행 환경

### 1. 사용 기술 및 라이브러리

* **Python**
* **Streamlit** (메인 웹 대시보드 프레임워크)
* **Pandas, NumPy** (데이터 처리 및 분석)
* **Plotly Express** (인터랙티브 시각화)
* **Folium, Streamlit-Folium** (전국 스마트쉼센터 지도 구현)
* **Seaborn, Matplotlib** (시각화)

### 2. 프로젝트 파일 목록 및 `requirements.txt`

이 프로젝트를 실행하려면 다음 파일들이 필요합니다.

1.  **`extream.py`** (또는 프로젝트 코드 파일명): Streamlit 애플리케이션 코드
2.  **`requirements.txt`** (필수 라이브러리 목록)
3.  **데이터 파일**: `smtphone.csv`, `unemployment.csv`, `콘텐츠_유형별_트래픽_현황_최종.csv`
4.  **이미지 파일**: `news.jpg`, `help.jpg`, 및 기타 사용된 이미지

> **💡 `requirements.txt` 내용
>
> ```text
> streamlit
> pandas
> seaborn
> numpy
> matplotlib
> plotly-express
> folium
> streamlit-folium
> ```

### 3. 웹사이트 실행 방법

1.  **저장소 복제 및 이동:**
    ```bash
    git clone [Your GitHub Repository URL]
    cd [repository-folder-name]
    ```
2.  **환경 설정:**
    * Follium 라이브러리 설치:
    ```bash
       pip install streamlit pydeck folium streamlit-folium
    ```

3.  **Streamlit 실행:** 
    ```bash
    streamlit run extream.py
    ```

### 4. 주요 코드 기능 요약

| 기능 (함수명) | 상세 설명 |
| :--- | :--- |
| **사이드바 테스트** | 5개의 과의존 테스트 체크박스 중 **3개 이상 체크 시**만 주요 메뉴(분석, 팁, 센터 안내)가 활성화되어 표시됩니다. |
| **`show_anl()`** | **과의존 위험도 분석**을 수행합니다. 연령대별 의존도와 연도별 실업률을 Plotly로 비교하며, 주요 의존도 증가 시기(2021년)의 원인을 기사 자료를 통해 분석합니다. |
| **`show_content_usage()`** | **콘텐츠 유형별 트래픽 현황 분석**을 Plotly 막대 그래프로 시각화하여, 주된 스마트폰 이용 콘텐츠 유형을 파악합니다. |
| **`tip()`** | **디지털 디톡스를 위한 5가지 실천 습관**을 시각 자료와 함께 제공하여 과의존 탈출을 돕습니다. |
| **`helper()`** | **전국 스마트쉼센터**의 누리집 및 소개 영상을 제공하고, Folium을 이용해 **전국의 센터 위치를 지도에 표시**하여 상담 안내를 돕습니다. |

---

## 📽️ 시연 동영상

[![데모 영상 보기](https://img.youtube.com/vi/66gp4Me4H1A/0.jpg)](https://www.youtube.com/66gp4Me4H1A)


---

### 💻 코드 (extream.py)
```python
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px # 인덱스 인지 못함..! as_index = False
import folium
from streamlit_folium import st_folium #pip install streamlit pydeck folium streamlit-folium

def show_main():
    st.header("스마트폰 과의존 현상: 특이점이 온 시기는?")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.write('"눈 뜨자마자 확인"...스마트폰 과의존 위험군, 아동층도 예외 없다? 출처 : KTV News 2025년 3월 28일')
    st.video("[https://www.youtube.com/watch?v=UYGZKnNmsuM](https://www.youtube.com/watch?v=UYGZKnNmsuM)")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.subheader("❓확인 해 볼 사항")
    st.markdown("""
        - 스마트폰 과의존도가 높아진 이유 -> 가설: 코로나 시기의 오프라인 활동이 줄었기 때문일 것이다 -> 코로나 시기의 데이터 확인
        - 위의 뉴스 정보 중 과의존 이용자와 일반 이용자의 주요 이용 콘텐츠 유형이 다르다는 자료 -> 콘텐츠 유형별 트래픽 데이터 분포 확인
          """)
    st.image("news.jpg")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.subheader("👈👈👈 데이터를 확인 하기 전 간단한 테스트를 해봅시다")


def show_anl():
    st.header("과의존 위험도 분석")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    smtph = pd.read_csv("smtphone.csv")
    st.write("## 스마트폰 의존도 데이터입니다.")
    selectedAge = st.selectbox("연령을 선택하시오", smtph['연령대별'].unique().tolist())
    result = smtph.query("연령대별 == @selectedAge")

    c1 = px.bar(data_frame=result, x="시점", y ="의존도")
    st.plotly_chart(c1)

    c2 = px.bar(data_frame=smtph, x="시점", y="의존도", color="연령대별", barmode="group")
    st.plotly_chart(c2)
    st.write("## 💡알수 있는 지점 2가지")
    st.write("### 1. 특정 연령만 의존도가 높아진 건 아니다")
    st.write("### 2. 청소년을 제외하고 모두 2021년에 의존도가 가장 높았다")
    st.write("### 👉 가설: 코로나 시기에 실업률이 늘어 의존도가 높아진 것이다.")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.write("## 월별 실업률 데이터를 살펴보자")
    fired = pd.read_csv("unemployment.csv")
    c3 = px.bar(data_frame=fired, x="date", y ="rate")
    st.plotly_chart(c3)

    

    st.subheader("실업률이 높았더 시기의 요인은?")
    st.write('한예경 / 강계만 기자. "1월 실업률 5%대로 껑충…청년실업률은 9.3%" 매일경제, 2010년 02월 11일')
    st.write("[https://www.mk.co.kr/news/economy/4684439](https://www.mk.co.kr/news/economy/4684439)")
    st.markdown("*이처럼 실업자가 급증한 것은 실직자 증가보다는 종래 실업자 통계에서" \
    " 잡히지 않던 비경제활동인구 중 상당수가 구직활동에 나선 것에 더 큰 영향을 받은 것으로 풀이된다.* (기사 원문 중)")
    st.write('이광호 기자. "8월 고용사정 최악…신규 취업 3000명 증가 그쳐(종합)", 2018년 09월 12일')
    st.write("[https://www.asiae.co.kr/article/2018091208515321517&mobile=Y](https://www.asiae.co.kr/article/2018091208515321517&mobile=Y)")
    st.markdown('*빈현준 통계청 고용통계과장은 "고용유발효과가 높은 자동차·조선업 부진이' \
    ' 계속되면서 도소매업 등 연관 산업에도 영향을 미쳐 취업자 수가 많이 둔화한 것으로 보인다"고 말했다.*(기사 원문 중)')
    st.write('구정모 기자. "한국 실업률 OECD보다 낮지만 급속 악화…21년만의 최고", 2021년 03월 14일')
    st.write("[https://www.yna.co.kr/view/AKR20210312125800009](https://www.yna.co.kr/view/AKR20210312125800009)")
    st.markdown('*한국의 1월 실업률은 5.4%로 전월보다 0.9%포인트' \
    ' 악화하면서 1999년 10월 이후 최고치를 기록했다.한국의 실업률은' \
    ' 작년 9월부터 악화 기조를 보여왔다.다행이라면 실업률의 절대적인 수준은' \
    ' 통계가 집계된 OECD 회원국 27개국 중 18위로 상대적으로는 낮은 편이라는 점이다.*(기사 원문 중)')
    st.subheader("특이점이 온 시기의 원인 요약")
    st.markdown("""
        - 2010년 1월: 기존 실업자 통계에 잡히지 않던 대상이 구직활동을 했기 때문
        - 2018년 8월: 특정 산업의 불황
        - 2021년 1월: 코로나(전세계적 동일)
            """)
    df = pd.DataFrame(fired)
    # 날짜 형식으로 변환
    df['date'] = pd.to_datetime(df['date'])
    # 'year' 컬럼 생성
    df['year'] = df['date'].dt.year
    # 년도별 평균 계산
    yearly_avg = df.groupby('year')['rate'].mean().reset_index()
    st.subheader("📊 년도별 평균 실업률")
    c4 = px.bar(data_frame=yearly_avg, x="year", y ="rate")
    st.plotly_chart(c4)
    st.subheader("❓ 년도별 실엽률과 의존도의 양상을 비교해보자 ")


def tip():
    st.header("💡 스마트폰 과의존 탈출 팁: 디지털 디톡스")
    st.markdown("---")
    
    st.subheader("일상에서 실천하는 5가지 습관")
    st.write("스마트폰으로부터 자유로워지기 위한 간단하지만 효과적인 생활 습관입니다.")
    st.write("")
    
    st.markdown("#### 1. 알림 관리: 방해 요소를 차단하세요.")
    st.image("[https://buildfire.com/wp-content/uploads/2024/09/why-users-mute-push-notifications-1.jpg](https://buildfire.com/wp-content/uploads/2024/09/why-users-mute-push-notifications-1.jpg)")
    st.write("- **불필요한 앱 알림**을 모두 끄고, 꼭 필요한 전화나 메시지만 남깁니다.")

    st.markdown("#### 2. 공간 분리: 손이 닿지 않는 곳에 두세요.")
    st.image("[https://thumbs.dreamstime.com/b/device-free-zone-icon-text-stop-using-smartphone-digital-devices-detox-creativity-family-fun-community-bonding-208768843.jpg](https://thumbs.dreamstime.com/b/device-free-zone-icon-text-stop-using-smartphone-digital-devices-detox-creativity-family-fun-community-bonding-208768843.jpg)")
    st.write("- 식사 시간이나 **취침 시**에는 스마트폰을 침실 밖 거실이나 부엌에 둡니다. (디지털 금식)")
    
    st.markdown("#### 3. 시간 제한 설정: 사용 시간을 눈으로 확인하세요.")
    st.image("[https://cdn.osxdaily.com/wp-content/uploads/2018/11/set-time-limit-social-media-use-ios-sceen-time.jpg](https://cdn.osxdaily.com/wp-content/uploads/2018/11/set-time-limit-social-media-use-ios-sceen-time.jpg)")
    st.write("- '동영상'과 같이 트래픽 비중이 높은 앱은 **하루 최대 사용 시간**을 설정하여 제한합니다.")
    
    st.markdown("#### 4. 새로운 취미: 대체 활동을 찾으세요.")
    st.image("[https://static.vecteezy.com/system/resources/thumbnails/002/987/395/small/various-hobbies-and-professions-icons-collection-vector.jpg](https://static.vecteezy.com/system/resources/thumbnails/002/987/395/small/various-hobbies-and-professions-icons-collection-vector.jpg)")
    st.write("- 스마트폰 사용을 대체할 수 있는 **독서, 운동, 그림 그리기** 등 오프라인 활동을 시작합니다.")
    
    st.markdown("#### 5. 스크린 타임 확인: 객관적인 현실을 마주하세요.")
    st.image("[https://static.vecteezy.com/system/resources/previews/029/917/318/non_2x/screen-time-time-control-on-smartphone-stock-illustration-vector.jpg](https://static.vecteezy.com/system/resources/previews/029/917/318/non_2x/screen-time-time-control-on-smartphone-stock-illustration-vector.jpg)")
    st.write("- 스마트폰의 **'스크린 타임'** 기능을 활용하여 자신이 얼마나 많은 시간을 썼는지 객관적으로 확인하고 경각심을 가집니다.")
    
    st.markdown("---")
    st.subheader("🌿 삶의 균형을 되찾으세요.")
    st.image("[https://www.shutterstock.com/shutterstock/photos/1643401516/display_1500/stock-vector-internet-addiction-and-digital-detox-infographic-what-are-the-effects-on-our-bodies-and-how-to-1643401516.jpg](https://www.shutterstock.com/shutterstock/photos/1643401516/display_1500/stock-vector-internet-addiction-and-digital-detox-infographic-what-are-the-effects-on-our-bodies-and-how-to-1643401516.jpg)", caption="디지털 디톡스로 찾는 평화")

def helper():
    st.header("💁 상담 센터 안내")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.write("## 👩‍⚕️스마트 쉼 센터")
    st.write("#### 전국의 스마트쉼센터를 통해 예방교육, 가정방문상담, 캠페인" \
    " 등 인터넷·스마트폰 과의존 문제를 해소하기 위해 다양한 정책과 사업을 추진하고 있습니다.")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.subheader("🔽누리집 링크")
    st.write("[https://www.iapc.or.kr/](https://www.iapc.or.kr/)")
    st.image("help.jpg")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.subheader("🔽스마트폰 과의존에 대한 이해 및 스마트쉼센터 소개영상(공식유튜브)")
    st.video("[https://www.youtube.com/watch?v=XKdl-iSC9wU](https://www.youtube.com/watch?v=XKdl-iSC9wU)")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.write("### 🗺️ 서울스마트쉼센터 위치📍") 
    # 지도 생성
    m = folium.Map(location=[37.568962, 126.978815], zoom_start=13)

    # 마커 추가
    folium.Marker([37.568962, 126.978815], tooltip="서울스마트쉼센터").add_to(m)
    folium.Marker([37.468839, 126.660727], tooltip="인천스마트쉼센터").add_to(m)
    folium.Marker([36.350305, 127.384860], tooltip="대전스마트쉼센터").add_to(m)
    folium.Marker([35.892669, 128.600464], tooltip="대구스마트쉼센터").add_to(m)
    folium.Marker([35.535141, 129.313776], tooltip="울산스마트쉼센터").add_to(m)
    folium.Marker([35.172989, 129.130739], tooltip="부산스마트쉼센터").add_to(m)
    folium.Marker([35.160123, 126.851296], tooltip="광주스마트쉼센터").add_to(m)
    folium.Marker([37.259353, 127.034118], tooltip="경기남부스마트쉼센터").add_to(m)
    folium.Marker([37.736268, 127.040721], tooltip="경기북부스마트쉼센터").add_to(m)
    folium.Marker([37.883138, 127.729069], tooltip="강원스마트쉼센터").add_to(m)
    folium.Marker([36.481536, 127.291477], tooltip="세종스마트쉼센터").add_to(m)
    folium.Marker([33.499411, 126.540246], tooltip="제주스마트쉼센터").add_to(m)
    folium.Marker([35.535105, 129.313673], tooltip="경남스마트쉼센터").add_to(m)
    folium.Marker([35.871564, 128.600781], tooltip="경북스마트쉼센터").add_to(m)
    folium.Marker([35.820550, 127.149203], tooltip="전북스마트쉼센터").add_to(m)
    folium.Marker([36.706454, 127.432056], tooltip="충북스마트쉼센터").add_to(m)
    folium.Marker([36.659521, 126.672880], tooltip="충남스마트쉼센터").add_to(m)
    
    # 스트림릿에 지도 표시
    st_folium(m, width=700, height=500)


def show_content_usage():
    st.header("📊 콘텐츠 유형별 트래픽 현황 분석(2015년 ~ 2025년)")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    df = pd.read_csv("콘텐츠_유형별_트래픽_현황_최종.csv", encoding='cp949')

    st.subheader("데이터 미리보기")
    st.dataframe(df)

    usage_summary = (
        df.groupby('콘텐츠유형', as_index=False)['점유율(%)']
        .sum()
        .sort_values(by='점유율(%)', ascending=False)
    )

    fig = px.bar(
        usage_summary,
        x='콘텐츠유형',
        y='점유율(%)',
        title='콘텐츠 유형별 총 트래픽 (TB)',
        color='콘텐츠유형',
        text='점유율(%)'
    )
    fig.update_layout(xaxis_title='콘텐츠 유형', yaxis_title='총 점유율(%)', showlegend=False)
    st.plotly_chart(fig)

    top_type = usage_summary.iloc[1]
    st.markdown("---")
    st.subheader("요약")
    st.write(
        f"가장 많은 트래픽을 사용하는 콘텐츠 유형은 **{top_type['콘텐츠유형']}**이며, "
        f"총 트래픽은 **{top_type['점유율(%)']:.1f} TB** 입니다."
    )
    st.write("이 유형은 사용자들이 가장 많이 이용하는 주요 콘텐츠로 볼 수 있습니다.")
    # -------------------------------------------
    st.markdown("---")
    # -------------------------------------------
    st.write("### 🔽 메인 화면의 뉴스 자료와 비교하기")
    st.image("news.jpg")


st.sidebar.title('📱 스마트폰 과의존 테스트')

# 체크박스 항목들
q1 = st.sidebar.checkbox('이용시간을 줄일려고 해도 힘들다')
q2 = st.sidebar.checkbox('일상생활에 지장을 느낀 적이 있다')
q3 = st.sidebar.checkbox('이용시간을 지키는 것이 어렵다')
q4 = st.sidebar.checkbox('스마트폰이 옆에 있으면 집중이 어렵다')
q5 = st.sidebar.checkbox('스마트폰 이용 때문에 타인과 갈등을 빚은 적이 있다')

# 체크된 항목 수 계산
checked_count = sum([q1, q2, q3, q4, q5])

# 조건에 따라 새로운 메뉴 추가
if checked_count >= 3:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 결과 보기")
    option = st.sidebar.selectbox(
    "다음 중 원하는 항목을 선택하세요:",
    ("과의존 위험도 분석", "콘텐츠 이용 현황 분석", "스마트폰 사용 줄이기 팁", "상담 센터 안내"))

    if option == '콘텐츠 이용 현황 분석':
        show_content_usage()
    if option == '과의존 위험도 분석':
        show_anl()
    elif option == '스마트폰 사용 줄이기 팁':
        tip()
    elif option == '상담 센터 안내':
        helper()
    else:
        st.header("")
else:
    show_main()
