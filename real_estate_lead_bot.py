
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Real Estate Lead Bot", page_icon="🏡", layout="centered")

st.title("🏡 Real Estate Assistant")
st.subheader("Let’s help you find the perfect property!")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.lead_data = {}

# Step 1: Property Purpose
if st.session_state.step == 1:
    purpose = st.radio("What are you looking for?", ["Buy", "Rent"])
    if st.button("Next"):
        st.session_state.lead_data["Purpose"] = purpose
        st.session_state.step = 2

# Step 2: Property Type
elif st.session_state.step == 2:
    ptype = st.selectbox("Property Type", ["Apartment", "Villa", "Plot", "Commercial"])
    if st.button("Next"):
        st.session_state.lead_data["Property Type"] = ptype
        st.session_state.step = 3

# Step 3: Location
elif st.session_state.step == 3:
    location = st.text_input("Preferred location or city")
    if st.button("Next") and location:
        st.session_state.lead_data["Location"] = location
        st.session_state.step = 4

# Step 4: Budget
elif st.session_state.step == 4:
    budget = st.text_input("What’s your budget? (e.g. ₹50 lakhs, ₹1 Cr)")
    if st.button("Next") and budget:
        st.session_state.lead_data["Budget"] = budget
        st.session_state.step = 5

# Step 5: Contact Info
elif st.session_state.step == 5:
    name = st.text_input("Your name")
    phone = st.text_input("Phone number")
    email = st.text_input("Email address (optional)")

    if st.button("Submit Lead") and name and phone:
        st.session_state.lead_data["Name"] = name
        st.session_state.lead_data["Phone"] = phone
        st.session_state.lead_data["Email"] = email
        st.session_state.lead_data["Submitted At"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        df = pd.DataFrame([st.session_state.lead_data])
        try:
            existing = pd.read_csv("leads.csv")
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_csv("leads.csv", index=False)

        st.success("✅ Thank you! Our team will reach out to you shortly.")
        st.balloons()
        st.session_state.step = 1
        st.session_state.lead_data = {}
