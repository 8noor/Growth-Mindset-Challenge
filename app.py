import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset Challenges",
    page_icon="🌱🌟",
    layout="centered"
)

# Initialize session state
if "motivation" not in st.session_state:
    st.session_state["motivation"] = "🌟 Every small win adds up to success! Keep going! 🚀"
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # Track button click state

# Motivation Quotes
motivation_quotes = [
    "🌟 Every challenge is an opportunity to grow!",
    "💪 Keep pushing! Progress happens one step at a time.",
    "🚀 Believe in yourself. You are stronger than you think!",
    "🔥 Growth begins at the end of your comfort zone.",
    "🌱 Mistakes are proof that you're trying. Keep going!"
]

# Custom Styling for Button
button_color = "#FFA07A" if st.session_state["button_clicked"] else "#ADD8E6"  # Light change on click
st.markdown(
    f"""
    <style>
        .motiv-button {{
            background-color: {button_color} !important;
            color: white !important;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }}
        .motiv-button:hover {{
            background-color: #FF7F50 !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Motivation Box
st.divider()
st.markdown("### 💡 Need More Motivation?")
st.markdown(
    f'<div style="background-color:#E3F2FD; padding:10px; border-radius:10px; font-weight:bold;">{st.session_state["motivation"]}</div>',
    unsafe_allow_html=True
)

# Spacing before button
st.write("")
st.write("")

# Button with Dynamic Color
if st.button("🔄 Get More Motivation!"):
    st.session_state["motivation"] = random.choice(motivation_quotes)
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]  # Toggle button state
    st.rerun()  # Refresh UI to apply color change

# Footer
st.divider()
st.write("🌟 Keep learning, keep growing, and embrace challenges! 🚀")
st.markdown("**© Created by Anum Rajput**")
