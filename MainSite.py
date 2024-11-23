import streamlit as st
from st_keyup import st_keyup


#this is the main site of the application for the rental car GUI
st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center;'>Rent a Car at hackatum Check24 Challenge</h1>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Pick-up & Return")
        pickup_location = st_keyup("Pick-up Location", "Airport, city or address")
        return_location = st_keyup("Return Location", "Airport, city or address")

        

    
    with col2:
        st.subheader("Pick-up Date & Time")
        pickup_date = st.date_input("Pick-up Date")
        pickup_time = st.time_input("Pick-up Time")

    with col3:
        st.subheader("Return Date & Time")
        return_date = st.date_input("Return Date")
        return_time = st.time_input("Return Time")

    
    if st.button("Show Cars"):
        st.write(f"Searching cars for pick-up at {pickup_location} on {pickup_date} at {pickup_time} and return at {return_location} on {return_date} at {return_time}")

if __name__ == "__main__":
    main()