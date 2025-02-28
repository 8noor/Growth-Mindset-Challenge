import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Growth Challenges",
    page_icon="🌱🌟",
    layout="centered"
)

# Ensure session state is initialized for motivation
if "motivation" not in st.session_state:
    st.session_state["motivation"] = "🌟 Every small win adds up to success! Keep going! 🚀"

# Custom Styling
st.markdown(
    """
    <style>
        .big-font { font-size:24px !important; font-weight: bold; }
        .highlight { color: #FF5733; font-weight: bold; }
        .success-box { background-color: #DFF2BF; padding: 10px; border-radius: 10px; }
        .motivation-box { background-color: #E3F2FD; padding: 10px; border-radius: 10px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Introduction
st.title("🌟 Growth Mindset Challenge 🌟")
st.subheader("🚀 Welcome to Your Growth Journey!")
st.write("Take on challenges, learn from setbacks, and unlock your full potential. This **AI-powered app** helps you build a growth mindset through **reflection, challenges, and achievements.**")

# Daily Quote Section
st.divider()
st.header("🌟 Daily Inspiration 🌟")
st.markdown("> ❝Success is not final, failure is not fatal: It is the courage to continue that counts.❞ - **Winston Churchill**")

# User Challenge Input
st.divider()
st.header("🛠️ What’s Your Challenge Today?")
user_input = st.text_input("Share a challenge you're currently facing:")

if user_input:
    st.success(f"🙌 You've acknowledged your challenge: **{user_input}**. Facing it is the first step to growth! 🚀")
else:
    st.info("💡 Take a moment to reflect. What's challenging you today?")

# Reflection Section
st.divider()
st.header("🌱 Reflect on Your Learning")
reflection = st.text_area("How can you overcome this challenge with a growth mindset?")

if reflection:
    st.markdown(f'<div class="success-box">🚀 Your reflection is valuable: <span class="highlight">{reflection}</span> 🌟 Keep pushing forward! 🌱</div>', unsafe_allow_html=True)
else:
    st.warning("💭 Looking back on past experiences helps you grow. Share your thoughts!")

# Achievements Section
st.divider()
st.header("🎉 Celebrate Your Wins!")
achievements = st.text_input("Tell us about something you've recently achieved or collected! ✨")

if achievements:
    st.success(f"🎉 Amazing! You've achieved: **{achievements}**. Keep up the great work! 🏆")
else:
    st.info("🏆 Small or big, every win matters! What have you accomplished lately?")

# 🔥 Motivation Section
st.markdown("### 💡 Need More Motivation?")
motivation_quotes = [
    "🌟 Every challenge is an opportunity to grow!",
    "💪 Keep pushing! Progress happens one step at a time.",
    "🚀 Believe in yourself. You are stronger than you think!",
    "🔥 Growth begins at the end of your comfort zone.",
    "🌱 Mistakes are proof that you're trying. Keep going!"
]

st.markdown(
    f'<div class="motivation-box">{st.session_state["motivation"]}</div>',
    unsafe_allow_html=True
)

if st.button("🔄 Get More Motivation!"):
    st.session_state["motivation"] = random.choice(motivation_quotes)
    st.experimental_rerun()  # Rerun the script to update the motivation text dynamically

# Footer
st.divider()
st.write("🌟 Keep learning, keep growing, and embrace challenges! 🚀")
st.markdown("**© Created by Anum Rajput**")
