import streamlit as st
from streamlit.components.v1 import html

#https://github.com/streamlit/streamlit/issues/4832
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


#this is the main site of the application for the rental car GUI
if "done_init" not in st.session_state:
    st.session_state["done_init"] = True
    st.set_page_config(
        initial_sidebar_state="collapsed",
        layout="wide"
    )
    st.markdown(
        """
    <style>
        .st-emotion-cache-yfhhig.ef3psqc5 {
            display: none;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

def main():
    st.markdown("<h1 style='text-align: center;'>Rent a Car at hackatum Check24 Challenge</h1>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Pick-up & Return")
        pickup_location = st.text_input("Pick-up Location","Munich")
        return_location = st.text_input("Return Location","Heilbronn")

        

    
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
            #pages.carVisuals.main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude)

            nav_page("carVisuals")
    st.markdown('<style>footer{visibility: hidden;}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()