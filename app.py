import streamlit as st

# Page config
st.set_page_config(page_title="Employee Evaluation System", layout="centered")

# ------------------ STYLING ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #f0f0f0;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #f0f0f0;
    margin-bottom: 20px;
}

/* Made by styling */
.made-by {
    position: fixed;
    right: 30px;
    bottom: 25px;
    font-family: 'Poppins', sans-serif;
    font-size: 26px;
    font-weight: 600;
    background: linear-gradient(45deg, #ff6b6b, #5f27cd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">🚀 Employee Performance Evaluation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🤖 AI-Based Expert System</div>', unsafe_allow_html=True)

st.divider()

# ------------------ INPUT ------------------
st.subheader("📋 Enter Employee Details")

name = st.text_input("Employee Name")
role = st.text_input("Department / Role")

st.subheader("⭐ Rate Performance (1 = Poor, 5 = Excellent)")

teamwork = st.slider("🤝 Teamwork", 1, 5, 3)
punctuality = st.slider("⏰ Punctuality", 1, 5, 3)
task_completion = st.slider("📌 Task Completion", 1, 5, 3)
communication = st.slider("🗣️ Communication Skills", 1, 5, 3)
problem_solving = st.slider("🧠 Problem Solving", 1, 5, 3)
leadership = st.slider("👨‍💼 Leadership", 1, 5, 3)

st.divider()

# ------------------ EVALUATION ------------------
if st.button("🔍 Evaluate Performance"):

    total = teamwork + punctuality + task_completion + communication + problem_solving + leadership
    avg = total / 6

    # Overall performance + final recommendation
    if avg >= 4.5:
        remark = "🌟 Outstanding"
        final_action = "🚀 Consider for Promotion / Leadership Role"

    elif avg >= 3.5:
        remark = "👍 Good"
        final_action = "📈 Eligible for Appraisal / Increment"

    elif avg >= 2.5:
        remark = "⚖️ Average"
        final_action = "📚 Needs Training & Skill Development"

    else:
        remark = "⚠️ Below Average"
        final_action = "🛠️ Immediate Improvement Plan Required"

    # ------------------ SKILL-BASED SUGGESTIONS ------------------
    suggestions = []

    if teamwork <= 2:
        suggestions.append("🤝 Improve teamwork and collaboration")

    if punctuality <= 2:
        suggestions.append("⏰ Work on punctuality and time management")

    if task_completion <= 2:
        suggestions.append("📌 Focus on completing tasks on time")

    if communication <= 2:
        suggestions.append("🗣️ Improve communication skills")

    if problem_solving <= 2:
        suggestions.append("🧠 Enhance problem-solving ability")

    if leadership <= 2:
        suggestions.append("👨‍💼 Develop leadership qualities")

    # If all good
    if not suggestions:
        suggestions.append("🎉 Excellent performance! Keep it up!")

    # ------------------ OUTPUT ------------------
    st.success("✅ Evaluation Completed")

    st.subheader("📊 Performance Report")
    st.write(f"**👤 Employee Name:** {name}")
    st.write(f"**🏢 Department:** {role}")
    st.write(f"**📈 Average Score:** {avg:.2f} / 5")
    st.write(f"**🏆 Performance:** {remark}")
    st.write(f"**🎯 Recommendation:** {final_action}")

    st.subheader("💡 Suggestions")
    for s in suggestions:
        st.write(f"- {s}")

    # Progress bar
    st.progress(int(avg * 20))

# ------------------ FOOTER ------------------
st.markdown("""
<div class="made-by">
    ✨ Made by Vaishnavi❤️
</div>
""", unsafe_allow_html=True)