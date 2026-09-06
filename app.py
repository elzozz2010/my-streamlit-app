import  os
import streamlit as st
import random
st.set_page_config(page_title="اهلا بيك في موقعي", layout="wide")

dark_mode = st.toggle("🌙 الوضع الليلي / ☀️ الوضع الساطع", value=False)

if dark_mode:
    bg_color = "#0E1117"
    text_color = "#FAFAFA"
    primary_color = "#FF4B4B"
else:
    bg_color = "#FFFFFF"
    primary_color = "#0066CC"
st.title("🚀 اهلا بيك في موقعي")
st.write ("اهلا بيك في الموقع", "streamlit")

# 2. سؤال الاسم + التفاعل
name = st.text_input("اكتب اسمك")
if name:
    fav_color = st.color_picker("اختار لونك المفضل", "#00f900")

if name:
    st.write(f".اهلا {name} 👋")
    st.markdown(f"<h3 style='color:{fav_color}'>ده اللون اللي انت اخترته</h3>", unsafe_allow_html=True)
    st.write(f"اهلا {name} 👋 نورت الموقع")
else:
    st.warning("اكتب اسمك الاول")

st.markdown("---")

# 3. العداد بتاع الزوار
st.subheader("📊 احصائيات الموقع")

file_name = "visits.txt"
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("0")

with open(file_name, "r") as f:
    visits = int(f.read())

visits += 1

with open(file_name, "w") as f:
    f.write(str(visits))

st.metric("عدد الزوار", visits)

# 4. معرض الاراء
st.markdown("---")
st.subheader("💬 سيب رايك")

comment = st.text_area("اكتب رايك هنا")
if st.button("انشر الراي", use_container_width=True):
    if comment:
        with open("comments.txt", "a", encoding="utf-8") as f:
            f.write(comment + "\n")
        st.success("تم النشر ❤️")
    else:
        st.warning("اكتب حاجة الاول")

st.markdown("### اراء الناس:")
if os.path.exists("comments.txt"):
    with open("comments.txt", "r", encoding="utf-8") as f:
        comments = f.readlines()
        for c in comments[::-1]:  # الجديد الاول
            st.write(f"🗨️ {c}")
else:
    st.info("لسه مفيش اراء. كن اول واحد")

# 5. اله حاسبة ملونة
st.markdown("---")
st.subheader("🧮 اله حاسبة ملونة")

col1, col2, col3 = st.columns([2,1,2])
with col1:
    num1 = st.number_input("الرقم الاول", value=0, key="n1")
with col2:
    op = st.selectbox(" ", ["+", "-", "*", "/"], key="op")
with col3:
    num2 = st.number_input("الرقم التاني", value=0, key="n2")

if st.button("احسب = ", use_container_width=True, type="primary"):
    try:
        if op == "+": result = num1 + num2
        if op == "-": result = num1 - num2  
        if op == "*": result = num1 * num2
        if op == "/": result = num1 / num2
        st.success(f"الناتج: {result} ✅")
    except:
        st.error("مينفعش تقسم على صفر 😅")

# 6. رمي النرد ملون
st.markdown("---")
st.subheader("🎲 رمي الزهر")

if st.button("دوس وارمي الزهر 🎲", use_container_width=True, type="secondary"):
    roll = random.randint(1,6)
    st.balloons()
    dice_emojis = ["⚀","⚁","⚂","⚃","⚄","⚅"]
    st.markdown(f"<h1 style='text-align:center; font-size:120px; color:#FF4B4B'>{dice_emojis[roll-1]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center'>طلعلك: {roll}</h2>", unsafe_allow_html=True)



st.markdown(f"""
    <style>


    
 [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        else:
            st.session_state.snake.pop()

grid_html = "<div style='display: grid; grid-template-columns: repeat(20, 20px); gap: 1px; background: black; padding: 5px;'>"
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        if [x, y] in st.session_state.snake:
            color = "limegreen"
        elif [x, y] == st.session_state.apple:
            color = "red"
        else:
            color = "#
grid_html += f"<div style='width:20px; height:20px; background:{color};'></div>"
grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)
st.write(f"### النقاط: {st.session_state.score}")

if st.session_state.game_over:
    st.error(f"خسرت! النقاط النهائية: {st.session_state.score}")
    if st.button("اعادة اللعب"):
        st.session_state.snake = [[10, 10]]
        st.session_state.direction = "RIGHT"

[random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
else:
    time.sleep(0.2)
    st.rerun()

    .stApp {{ background-color: {bg_color}; color: {text_color}; }}
    h1, h2, h3 {{ color: {primary_color}; }}
    </style>
""", unsafe_allow_html=True)
