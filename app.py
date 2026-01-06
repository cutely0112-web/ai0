import streamlit as st

# 페이지 설정
st.set_page_config(page_title="쉰바이브 AI 다이어트 처방전", page_icon="💊")

# 스타일링 (중년 시청자를 위해 폰트를 키우고 깔끔하게 구성)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    h1 { color: #003366; font-family: 'Nanum Gothic', sans-serif; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #00c4b4; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("💊 쉰바이브 AI 다이어트 처방전")
st.subheader("남들 다 한다고 따라 하지 마세요. 당신에게 '진짜' 필요한 것만 골라드립니다.")
st.write("---")

# 질문 섹션
st.info("💡 몇 가지 질문에 답하시면 '쉰바이브'만의 독한 처방전을 내려드립니다.")

col1, col2 = st.columns(2)

with col1:
    job = st.selectbox("1. 현재 하시는 일은 무엇인가요?", 
                      ["사무직 직장인", "자영업자/소상공인", "은퇴자/무직", "주부"])
    time = st.selectbox("2. 하루에 AI에 투자할 수 있는 시간은?", 
                       ["30분 미만", "1시간 내외", "3시간 이상"])

with col2:
    skill = st.selectbox("3. 디지털 도구 숙련도는 어떤가요?", 
                        ["기본적인 검색만 가능", "엑셀/문서 작업 가능", "새로운 툴 배우는 게 즐거움"])
    goal = st.selectbox("4. AI를 배우려는 진짜 목적은?", 
                       ["업무 시간 단축", "추가 수익 창출(부업)", "삶의 활력/취미", "자녀/가족과 대화"])

# 결과 도출 로직
if st.button("내 처방전 확인하기"):
    st.write("---")
    st.balloons()
    
    # 로직에 따른 처방전 구성
    if time == "30분 미만" and goal == "추가 수익 창출(부업)":
        st.error("🚨 [긴급 처방] 지금은 AI 부업을 시작할 때가 아닙니다.")
        st.write("**이유:** 하루 30분으로는 AI 학습조차 불가능합니다. 유료 강의 결제하지 마세요. 돈만 날립니다.")
        st.write("**추천:** 차라리 그 시간에 가족과 30분 더 산책하세요. 그게 남는 겁니다.")
        
    elif job == "사무직 직장인" and goal == "업무 시간 단축":
        st.success("✅ [맞춤 처방] 챗GPT '요약'과 '초안 작성' 딱 하나만 파세요.")
        st.write("**이유:** 다른 화려한 툴은 시간 낭비입니다. 메일 작성과 보고서 요약만 해도 퇴근이 30분 빨라집니다.")
        st.write("**추천 도구:** ChatGPT (유료 결제도 필요 없습니다. 무료 버전이면 충분합니다.)")
        
    elif job == "은퇴자/무직" or goal == "삶의 활력/취미":
        st.info("🎨 [즐거움 처방] 이미지 생성 AI로 '나만의 갤러리'를 만들어보세요.")
        st.write("**이유:** 수익화의 압박에서 벗어나 창작의 즐거움을 느끼는 것이 정신 건강에 최고입니다.")
        st.write("**추천 도구:** Midjourney 또는 캔바(Canva) AI 기능")
        
    else:
        st.warning("🧐 [신중 처방] 기본기부터 천천히, 도구보다 '질문하는 법'을 익히세요.")
        st.write("**이유:** 조급함이 화를 부릅니다. 유료 툴부터 구독하지 마시고, 무료 툴로 '말 거는 법'부터 연습하세요.")
        st.write("**추천:** 쉰바이브의 다음 영상 '질문의 기술' 편을 기다려주세요.")

st.write("---")
st.caption("본 결과는 '쉰바이브'의 현실적인 철학을 바탕으로 제작되었습니다. 기술보다 당신의 삶이 먼저입니다.")