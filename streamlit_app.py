import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="AI 활용 역량 진단",
    page_icon="🎯",
    layout="wide"
)

# CSS 스타일
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 사이드바
with st.sidebar:
    st.markdown("### 🎯 AI 역량 진단")
    st.markdown("---")
    
    if st.button("🏠 홈", use_container_width=True):
        st.session_state.page = 'home'
    
    if st.button("📝 진단하기", use_container_width=True):
        st.session_state.page = 'assessment'
    
    if st.button("📊 결과보기", use_container_width=True):
        st.session_state.page = 'result'
    
    st.markdown("---")
    st.markdown("**공공기관 AI 역량 평가**")
    st.markdown("- 소요시간: 10분")
    st.markdown("- 문항수: 15개")

# 홈 페이지
if st.session_state.page == 'home':
    st.markdown('<div class="main-header"><h1>🎯 AI 활용 역량 진단 시스템</h1><p>공공기관 근무자를 위한 AI 역량 평가</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 📊 진단 안내")
        st.info("""
        **소요 시간**: 약 10분
        
        **평가 내용**:
        - ✅ AI 기본 이해도
        - ✅ 업무 자동화 활용
        - ✅ 데이터 분석 및 의사결정
        - ✅ AI 도구 실무 활용
        - ✅ AI 윤리 및 보안 인식
        
        **결과 제공**:
        - 종합 점수 및 레벨
        - 영역별 상세 분석
        - 맞춤형 학습 추천
        """)
        
        if st.button("🚀 진단 시작하기", use_container_width=True, type="primary"):
            st.session_state.page = 'assessment'
            st.rerun()

# 진단 페이지
elif st.session_state.page == 'assessment':
    st.markdown('<div class="main-header"><h1>📝 AI 활용 역량 진단</h1></div>', unsafe_allow_html=True)
    
    # 기본 정보
    st.markdown("### 📋 기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("이름 *", placeholder="홍길동")
        department = st.text_input("소속 부서 *", placeholder="디지털혁신과")
    with col2:
        position = st.text_input("직위 *", placeholder="주무관")
    
    st.markdown("---")
    
    # 진단 문항
    st.markdown("### 📋 진단 문항 (15문항)")
    st.info("각 문항을 읽고 본인의 상황에 가장 가까운 점수를 선택해주세요.")
    
    # 영역 1: AI 기본 이해도
    with st.expander("**1️⃣ AI 기본 이해도** (3문항)", expanded=True):
        q1 = st.radio("Q1. AI(인공지능)의 기본 개념과 활용 분야를 이해하고 있다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q1')
        q2 = st.radio("Q2. 생성형 AI(ChatGPT, Gemini 등)의 작동 원리를 알고 있다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q2')
        q3 = st.radio("Q3. AI의 장점과 한계를 이해하고 적절히 활용할 수 있다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q3')
    
    # 영역 2: 업무 자동화
    with st.expander("**2️⃣ 업무 자동화 활용** (3문항)", expanded=False):
        q4 = st.radio("Q4. AI를 활용해 문서 작성 업무를 효율화하고 있다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q4')
        q5 = st.radio("Q5. 정형화된 민원 응대나 FAQ 작성에 AI를 활용한다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q5')
        q6 = st.radio("Q6. 회의록 정리, 요약 등 반복 업무에 AI를 활용한다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q6')
    
    # 영역 3: 데이터 분석
    with st.expander("**3️⃣ 데이터 분석 및 의사결정** (3문항)", expanded=False):
        q7 = st.radio("Q7. AI를 활용해 대량의 데이터를 분석하고 인사이트를 도출한다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q7')
        q8 = st.radio("Q8. 정책 수립이나 의사결정 시 AI의 분석 결과를 참고한다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q8')
        q9 = st.radio("Q9. 통계 자료나 보고서를 AI로 요약·분석하여 활용한다", 
                      [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                      horizontal=True, key='q9')
    
    # 영역 4: 실무 활용
    with st.expander("**4️⃣ AI 도구 실무 활용** (3문항)", expanded=False):
        q10 = st.radio("Q10. ChatGPT, Gemini, Copilot 등 생성형 AI를 실무에 활용한다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q10')
        q11 = st.radio("Q11. 프롬프트 엔지니어링(명령어 작성법)을 이해하고 활용한다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q11')
        q12 = st.radio("Q12. 업무에 필요한 AI 도구를 스스로 찾아 활용할 수 있다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q12')
    
    # 영역 5: 윤리 및 보안
    with st.expander("**5️⃣ AI 윤리 및 보안 인식** (3문항)", expanded=False):
        q13 = st.radio("Q13. AI 사용 시 개인정보 보호와 보안을 고려한다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q13')
        q14 = st.radio("Q14. AI 결과물의 정확성을 검증하고 책임감 있게 활용한다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q14')
        q15 = st.radio("Q15. AI 사용 관련 조직의 가이드라인과 규정을 이해하고 준수한다", 
                       [1,2,3,4,5], format_func=lambda x: f"{x} - {'전혀 그렇지 않다' if x==1 else '그렇지 않다' if x==2 else '보통이다' if x==3 else '그렇다' if x==4 else '매우 그렇다'}", 
                       horizontal=True, key='q15')
    
    st.markdown("---")
    
    # 진단 완료 버튼
    if name and department and position:
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("✅ 진단 완료", use_container_width=True, type="primary"):
                # 점수 계산
                total_score = q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15
                percentage = (total_score / 75) * 100
                
                # 레벨 판정
                if total_score >= 66:
                    level = "전문가"
                    color = "#96ceb4"
                elif total_score >= 51:
                    level = "고급"
                    color = "#45b7d1"
                elif total_score >= 31:
                    level = "중급"
                    color = "#4ecdc4"
                else:
                    level = "초급"
                    color = "#ff6b6b"
                
                # 영역별 점수
                basic = ((q1+q2+q3)/15)*100
                automation = ((q4+q5+q6)/15)*100
                data = ((q7+q8+q9)/15)*100
                tools = ((q10+q11+q12)/15)*100
                ethics = ((q13+q14+q15)/15)*100
                
                st.session_state.result = {
                    "name": name,
                    "department": department,
                    "position": position,
                    "total_score": total_score,
                    "percentage": percentage,
                    "level": level,
                    "color": color,
                    "basic": basic,
                    "automation": automation,
                    "data": data,
                    "tools": tools,
                    "ethics": ethics,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                st.success("✅ 진단이 완료되었습니다!")
                st.info("👈 왼쪽 사이드바에서 '결과보기'를 클릭하세요!")
    else:
        st.warning("⚠️ 기본 정보(이름, 부서, 직위)를 모두 입력해주세요!")

# 결과 페이지
elif st.session_state.page == 'result':
    if 'result' not in st.session_state:
        st.warning("⚠️ 아직 진단을 완료하지 않았습니다.")
        if st.button("📝 진단하러 가기"):
            st.session_state.page = 'assessment'
            st.rerun()
    else:
        result = st.session_state.result
        
        st.markdown('<div class="main-header"><h1>🎊 진단 결과</h1></div>', unsafe_allow_html=True)
        
        # 종합 점수
        st.markdown(f"""
        <div style="padding: 2rem; background: linear-gradient(135deg, {result['color']} 0%, {result['color']}dd 100%); 
                    color: white; border-radius: 15px; text-align: center; margin: 1rem 0;">
            <h2>{result['name']}님의 진단 결과</h2>
            <h1 style="font-size: 4em; margin: 20px 0;">{result['total_score']} / 75</h1>
            <h3>달성률: {result['percentage']:.1f}%</h3>
            <h2 style="margin-top: 20px;">🏆 {result['level']} 레벨</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # 영역별 점수
        st.markdown("### 📈 영역별 상세 점수")
        
        categories = [
            ("AI 기본 이해도", result['basic']),
            ("업무 자동화 활용", result['automation']),
            ("데이터 분석 및 의사결정", result['data']),
            ("AI 도구 실무 활용", result['tools']),
            ("AI 윤리 및 보안 인식", result['ethics'])
        ]
        
        for cat_name, cat_score in categories:
            st.markdown(f"**{cat_name}**")
            st.progress(cat_score/100)
            st.caption(f"{cat_score:.1f}%")
            st.markdown("")
        
        # 추천사항
        st.markdown("### 💡 맞춤형 추천사항")
        
        if result['level'] == "전문가":
            st.success("""
            🌟 **전문가 레벨 추천**
            - 조직의 AI 전략 수립에 참여하기
            - AI 교육 프로그램 설계 및 운영
            - 외부 전문가 네트워크 구축
            - AI 우수 사례 발표 및 공유
            """)
        elif result['level'] == "고급":
            st.info("""
            🚀 **고급 레벨 추천**
            - 조직 내 AI 활용 가이드 작성
            - AI 활용 워크숍 개최
            - 최신 AI 트렌드 지속 학습
            - 타 부서 AI 도입 컨설팅
            """)
        elif result['level'] == "중급":
            st.info("""
            📚 **중급 레벨 추천**
            - 프롬프트 엔지니어링 스킬 향상
            - 부서 내 AI 활용 사례 공유
            - 업무 프로세스별 AI 활용 방안 수립
            - AI 도구 고급 기능 학습
            """)
        else:
            st.warning("""
            🌱 **초급 레벨 추천**
            - 생성형 AI 기본 사용법 익히기
            - AI 활용 기초 강의 수강
            - 간단한 업무에 AI 적용해보기
            - AI 관련 유튜브 채널 구독
            """)
        
        # 버튼
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 다시 진단하기", use_container_width=True):
                del st.session_state.result
                st.session_state.page = 'assessment'
                st.rerun()
        with col2:
            if st.button("🏠 처음으로", use_container_width=True):
                st.session_state.page = 'home'
                st.rerun()

# 푸터
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #888; font-size: 0.9em;'>
© 2024 AI 활용 역량 진단 시스템 | 공공기관 근무자 대상
</p>
""", unsafe_allow_html=True)
