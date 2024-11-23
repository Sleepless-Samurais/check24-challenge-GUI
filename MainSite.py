import streamlit as st
from st_keyup import st_keyup


#this is the main site of the application for the rental car GUI
st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center;'>Rent a Car at hackatum Check24 Challenge</h1>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Pick-up & Return")
        pickup_location = st.text_input("Pick-up Location","Munich")
        return_location = st.text_input("Return Location","Munich")

        

    
    with col2:
        st.subheader("Pick-up Date & Time")
        pickup_date = st.date_input("Pick-up Date")
        pickup_time = st.time_input("Pick-up Time")

    with col3:
        st.subheader("Return Date & Time")
        return_date = st.date_input("Return Date")
        return_time = st.time_input("Return Time")

    
    if st.button("Show Cars"):
        if pickup_location == return_location:
            st.write(f"Searching cars for pick-up at {pickup_location} on {pickup_date} at {pickup_time} and return at {return_location} on {return_date} at {return_time}")
        else:
            #forwarding to carVisuals.py
            import pages.carVisuals
            sourceLatitude = 11.5820
            sourceLongitude = 48.1351
            targetLatitude = 9.2109
            targetLongitude = 49.1427
            pages.carVisuals.main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude)

if __name__ == "__main__":
    main()