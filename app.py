#streamlit 
import streamlit as st

st.set_page_config(page_title= "growth Mindset Challenges ", project_icon="🌱🌟")

st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome To Your Growth Journey Challenge!")
st.write("Take on challenges, learn from setbacks, and unlock your true potential! 🚀 This AI-powered app helps you develop a growth mindset through reflection, exciting challenges, and rewarding achievements.✨")

#Quote section
st.header("🌟 Daily Quote 🌟")
# st.write("❝Successfully completing a challenge is a great way to boost your confidence and develop a growth mindset. Here's a quote to inspire you today:❞")
st.write( "❝Success is not final, failure is not fatal: It is the courage to continue that counts.❞ - Winston Churchill")

st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Share a challenge you're currently facing.")


#condition 
if user_input:
    st.write(f"🙌👏👍🥇Congratulations! You've successfully: {user_input}. faced your challenge today. Keep up the great work!🚀 ���")
else:
    st.write("🤔 What challenge are you facing today? Share it with us!🌟")   

    #reflexing 
    st.write(f"🌟 Reflect on your learning!🌱")
    reflection = st.text_area("How can you overcome this challenge with a growth mindset?")
    if reflection:
        st.write(f"🚀🌟🌱 Your reflection has been saved! Keep up the great work and stay positive!: {reflection}🌟🌱🚀")
    else:
        st.info("💡 Looking back on past experiences helps you grow! Share your reflections with us! 🌱✨")

        #achievements
        st.header("🎉🏆🌟 Celebrate Your Wins! ")
        achievements = st.text_input("Tell us about something you've recently gathered or collected! ✨")

        if achievements:
            st.success(f"🌟🎉🏆 Congratulations on your achievement! 🌟🎉🏆: {achievements} Keep up the great work! 🚀🌱🌟")
        else:
            st.info("🌟🎉🏆 Celebrate your wins, no matter how small! Share your achievements with us! 🌟🎉🏆✨")

            #footer
            st.write("- - -")
            st.write("🌟🚀💡 Keep up the great work and stay positive! 🚀💡🌟")
            st.write("**© ⛔ Created by Anum Rajput**")
