import random
import streamlit as st

# 1. 페이지 기본 설정 및 제목/안내 문구
st.set_page_config(page_title="가위바위보 게임", page_icon="🎮", layout="centered")

st.title("🎮 컴퓨터와 함께하는 가위바위보 한판!")
st.write("아래 버튼 중 하나를 클릭하여 컴퓨터와 대결해 보세요!")
st.write("---")

# 가위바위보 옵션 및 이모지 매핑
options = ["가위", "바위", "보"]
emojis = {"가위": "✌️", "바위": "✊", "보": "✋"}

# 2. 버튼 3개를 나란히 배치 (st.columns 활용)
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "가위"

with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "바위"

with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "보"

# 3. 사용자가 버튼을 클릭했을 때 대결 진행
if user_choice:
    # 컴퓨터의 random.choice() 선택
    computer_choice = random.choice(options)
    
    st.write("### ⚔️ 대결 결과")
    
    # 선택 결과 출력
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.info(f"👤 **나의 선택:** {emojis[user_choice]} {user_choice}")
    with res_col2:
        st.info(f"🤖 **컴퓨터의 선택:** {emojis[computer_choice]} {computer_choice}")
    
    # 4. 승패 판정 및 결과 출력 (st.balloons, st.success, st.error, st.warning)
    if user_choice == computer_choice:
        st.warning("🤝 **무승부입니다!** 다시 한 번 도전해 보세요.")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        st.balloons()  # 승리 시 축하 풍선 효과
        st.success("🎉 **축하합니다! 당신이 승리했습니다!**")
    else:
        st.error("😭 **아쉽네요! 컴퓨터가 승리했습니다.**")
