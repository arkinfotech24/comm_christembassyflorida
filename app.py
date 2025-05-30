import streamlit as st
from message_generator import generate_devotional
from twilio_sms import send_sms

st.title("📖 Christ Embassy Devotional Manager")

topic = st.text_input("Enter Devotional Topic", "Walking in Divine Health")

if st.button("Generate Devotional"):
    devotional = generate_devotional(topic)
    st.text_area("Generated Message", devotional, height=300)

    if st.button("Send SMS"):
        short_msg = f"Join us at Christ Embassy this Sunday: '{topic}'"
        send_sms(short_msg)
        st.success("SMS Sent!")