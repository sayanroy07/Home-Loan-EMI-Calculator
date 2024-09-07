import streamlit as st
import time
import numpy as np

with st.sidebar:
    st.title("Description:")
    st.markdown("A Quick Home Loan Calculator for your Dream House.")
    st.markdown("You begin by providing 2 initial details & hit the Calculate button.")
    st.markdown("Then you can make changes to details provided below to get your exact EMI values.")
    st.title('Developed by Sayan Roy')
    st.write("https://github.com/sayanroy07")

# Loading the pre-trained ViT

st.title("🏡 Quick Home Loan Calculator 🏡")

with st.form(key='form1'):
    col1, col2 = st.columns([1, 1])
    with col1:
        a = st.text_input('Super Built Area (Sqft)',placeholder=1000,value=1000)
    with col2:
        b = st.text_input('Price Per Square Feet (INR)',placeholder=5000,value=5000)

    if st.form_submit_button('Calculate'):
        result = float(a) * float(b)
        st.write("Base Price of your House: Rs", f'{int(result):,}'," Lakhs")
        if result !=0:
            if result > 4500000:
                col1, col2, col3 = st.columns(3)
                with col1:
                    g = st.slider("GST Charge (%)", min_value=1, max_value=30, value=5)
                with col2:
                    r = st.slider("Registry Charge (%)", min_value=1, max_value=30, value=7)
                with col3:
                    l = st.slider("Lawyer Charge (%)", min_value=1, max_value=30, value=1)
                gst = result*(g/100)
                registry = result*(r/100)
                lawyer = result*(l/100)
                result1 = result + registry + lawyer + gst
                st.write("Final Price: Rs ",f'{int(result1):,}'," Lakhs (* ",g,"% GST, ",r,"% Registry & ",l,"% Lawyer Charges)")
                if result1 is not None:
                    down = st.slider("Down Payment (Min 15%)", min_value=15, max_value=60)
                    down1 = (down*result1)/100
                    st.write("Down Payment: Rs ",f'{int(down1):,}'," Lakhs")
                    loan = result1 - down1
                    st.write("Remaining Loan Amount: Rs ",f'{int(loan):,}')
                    st.write("Bank EMI Loan Calculator:")
                    col11, col21, col31 = st.columns(3)
                    with col11:
                        amount = st.number_input("Loan Amount:",value=loan)
                    with col21:
                        rate = st.number_input("Interest Rate:",value=9.75)
                    with col31:
                        year = st.slider("No of Years:", min_value=1, max_value=30, value=15)
                    rate1 = (rate/12/100)
                    year1 = (year*12)
                    emi = amount*rate1*(1+rate1)**year1/((1+rate1)**year1-1)
                    st.write("EMI = Rs ",f'{int(emi):,}')
