import streamlit as st
import time

def countdown(minutes):
    total_seconds = minutes * 60
    timer_placeholder = st.empty()  # Create an empty placeholder for the timer text

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer_text = f"⏳ **Time Left:** {mins:02d}:{secs:02d}"
        timer_placeholder.markdown(timer_text)
        time.sleep(1)
        total_seconds -= 1

    timer_placeholder.markdown("✅ **Time's up!**")

def pomodoro_session(work=25, short_break=5, long_break=15, sessions=4):
    # When the user clicks the Start button, run the pomodoro sessions
    if st.button("Start Pomodoro"):
        for i in range(1, sessions + 1):
            st.write(f"### Session {i}: Work for {work} minutes")
            countdown(work)
            
            # If it is not the last session, take a short break; else, take a long break
            if i < sessions:
                st.write(f"### Short Break: {short_break} minutes")
                countdown(short_break)
            else:
                st.write(f"### Long Break: {long_break} minutes")
                countdown(long_break)
        st.balloons()

# Streamlit page configuration
st.set_page_config(page_title="Pomodoro Timer", page_icon="🍅", layout="centered")
st.title("🍅 Pomodoro Timer")

# Explanation on the page
st.markdown("""
This is a simple Pomodoro Timer built with Streamlit.  
- **Work Session:** 25 minutes  
- **Short Break:** 5 minutes (after each session except the last)  
- **Long Break:** 15 minutes (after the final session)  

Click the button below to get started!
""")

# Start the session
pomodoro_session()
