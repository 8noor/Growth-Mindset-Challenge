import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset Challenges",
    page_icon="🌱🌟",
    layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
        .big-font { font-size:24px !important; font-weight: bold; }
        .highlight { color: #FF5733; font-weight: bold; }
        .success-box { background-color: #DFF2BF; padding: 10px; border-radius: 10px; }
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

# Footer
st.divider()
st.write("🌟 Keep learning, keep growing, and embrace challenges! 🚀")
st.markdown("**© Created by Anum Rajput**")
