import streamlit as st
from streamlit.components.v1 import html

cities = {
    "München": {"latitude": 48.1351, "longitude": 11.5820},
    "Heilbronn": {"latitude": 49.1427, "longitude": 9.2109},
    "Augsburg": {"latitude": 48.3705, "longitude": 10.8978},
    "Nuremberg": {"latitude": 49.4521, "longitude": 11.0767},
    "Stuttgart": {"latitude": 48.7758, "longitude": 9.1829},
    "Regensburg": {"latitude": 49.0134, "longitude": 12.1016},
    "Ingolstadt": {"latitude": 48.7651, "longitude": 11.4237},
    "Ulm": {"latitude": 48.4011, "longitude": 9.9876},
    "Würzburg": {"latitude": 49.7913, "longitude": 9.9534},
    "Erlangen": {"latitude": 49.5897, "longitude": 11.0049},
    "Bamberg": {"latitude": 49.8988, "longitude": 10.9028},
    "Schweinfurt": {"latitude": 50.0489, "longitude": 10.2217},
    "Rosenheim": {"latitude": 47.8561, "longitude": 12.1225},
    "Landshut": {"latitude": 48.5442, "longitude": 12.1469},
    "Freising": {"latitude": 48.4029, "longitude": 11.7481},
    "Fürth": {"latitude": 49.4774, "longitude": 10.9886},
    "Bayreuth": {"latitude": 49.9456, "longitude": 11.5713},
    "Weiden in der Oberpfalz": {"latitude": 49.6767, "longitude": 12.1566},
    "Kempten": {"latitude": 47.7267, "longitude": 10.3139},
    "Lindau": {"latitude": 47.5460, "longitude": 9.6849},
    "Memmingen": {"latitude": 47.9839, "longitude": 10.1812},
    "Passau": {"latitude": 48.5660, "longitude": 13.4319},
    "Coburg": {"latitude": 50.2590, "longitude": 10.9642},
    "Schwabach": {"latitude": 49.3296, "longitude": 11.0236},
    "Hof": {"latitude": 50.3176, "longitude": 11.9215},
    "Ansbach": {"latitude": 49.3007, "longitude": 10.5710},
    "Deggendorf": {"latitude": 48.8408, "longitude": 12.9608},
    "Aschaffenburg": {"latitude": 49.9737, "longitude": 9.1473},
    "Amberg": {"latitude": 49.4428, "longitude": 11.8631},
    "Bad Kissingen": {"latitude": 50.2011, "longitude": 10.0773},
    "Garmisch-Partenkirchen": {"latitude": 47.4922, "longitude": 11.0955},
    "Dachau": {"latitude": 48.2606, "longitude": 11.4346},
    "Neu-Ulm": {"latitude": 48.3921, "longitude": 10.0106},
    "Biberach an der Riß": {"latitude": 48.0958, "longitude": 9.7939},
    "Landsberg am Lech": {"latitude": 48.0506, "longitude": 10.8793},
    "Neumarkt in der Oberpfalz": {"latitude": 49.2807, "longitude": 11.4621},
    "Ebersberg": {"latitude": 48.0793, "longitude": 11.9691},
    "Pfaffenhofen an der Ilm": {"latitude": 48.5336, "longitude": 11.5007},
    "Bad Tölz": {"latitude": 47.7617, "longitude": 11.5586},
    "Wangen im Allgäu": {"latitude": 47.6909, "longitude": 9.8324},
    "Donauwörth": {"latitude": 48.7186, "longitude": 10.7801},
    "Günzburg": {"latitude": 48.4552, "longitude": 10.2738},
    "Dillingen an der Donau": {"latitude": 48.5778, "longitude": 10.4946},
    "Aalen": {"latitude": 48.8378, "longitude": 10.0933},
    "Ellwangen": {"latitude": 48.9637, "longitude": 10.1303},
    "Göppingen": {"latitude": 48.7031, "longitude": 9.6505},
    "Friedrichshafen": {"latitude": 47.6563, "longitude": 9.4750},
    "Böblingen": {"latitude": 48.6824, "longitude": 9.0098},
    "Leonberg": {"latitude": 48.8015, "longitude": 9.0065},
    "Ludwigsburg": {"latitude": 48.8974, "longitude": 9.1916},
    "Heidenheim an der Brenz": {"latitude": 48.6782, "longitude": 10.1529},
    "Tübingen": {"latitude": 48.5216, "longitude": 9.0576},
    "Esslingen am Neckar": {"latitude": 48.7429, "longitude": 9.3098},
    "Reutlingen": {"latitude": 48.4918, "longitude": 9.2115},
    "Sindelfingen": {"latitude": 48.7052, "longitude": 9.0167},
    "Karlsruhe": {"latitude": 49.0069, "longitude": 8.4037},
    "Pforzheim": {"latitude": 48.8842, "longitude": 8.6989},
    "Baden-Baden": {"latitude": 48.7601, "longitude": 8.2398},
    "Offenburg": {"latitude": 48.4723, "longitude": 7.9425},
    "Kehl": {"latitude": 48.5745, "longitude": 7.8158},
    "Lörrach": {"latitude": 47.6141, "longitude": 7.6617},
    "Freiburg im Breisgau": {"latitude": 47.9990, "longitude": 7.8421},
    "Konstanz": {"latitude": 47.6779, "longitude": 9.1732},
    "Singen": {"latitude": 47.7590, "longitude": 8.8333},
    "Radolfzell": {"latitude": 47.7455, "longitude": 8.9706},
    "Weil am Rhein": {"latitude": 47.5934, "longitude": 7.6163},
    "Überlingen": {"latitude": 47.7717, "longitude": 9.1594},
    "Ravensburg": {"latitude": 47.7819, "longitude": 9.6104},
    "Biberach": {"latitude": 48.0935, "longitude": 9.7866},
    "Füssen": {"latitude": 47.5714, "longitude": 10.7017},
    "Oberstdorf": {"latitude": 47.4087, "longitude": 10.2793},
    "Kaufbeuren": {"latitude": 47.8801, "longitude": 10.6216},
    "Peiting": {"latitude": 47.7962, "longitude": 10.9293},
    "Mittenwald": {"latitude": 47.4411, "longitude": 11.2637},
    "Bad Wörishofen": {"latitude": 48.0112, "longitude": 10.5968},
    "Schongau": {"latitude": 47.8128, "longitude": 10.8963},
    "Weilheim in Oberbayern": {"latitude": 47.8418, "longitude": 11.1488},
    "Miesbach": {"latitude": 47.7892, "longitude": 11.8322},
    "Holzkirchen": {"latitude": 47.8743, "longitude": 11.7011},
    "Erding": {"latitude": 48.3050, "longitude": 11.9071},
    "Wolfratshausen": {"latitude": 47.9128, "longitude": 11.4198},
    "Bad Aibling": {"latitude": 47.8634, "longitude": 12.0096},
    "Bad Reichenhall": {"latitude": 47.7290, "longitude": 12.8761},
    "Traunstein": {"latitude": 47.8688, "longitude": 12.6434},
    "Burghausen": {"latitude": 48.1701, "longitude": 12.8318},
    "Altötting": {"latitude": 48.2261, "longitude": 12.6767},
    "Trostberg": {"latitude": 48.0327, "longitude": 12.5575},
    "Waging am See": {"latitude": 47.9392, "longitude": 12.7256},
    "Simbach am Inn": {"latitude": 48.2656, "longitude": 13.0274},
    "Eggenfelden": {"latitude": 48.3953, "longitude": 12.7528},
    "Mühldorf am Inn": {"latitude": 48.2470, "longitude": 12.5221},
    "Traunreut": {"latitude": 47.9648, "longitude": 12.5997}
}

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
    st.markdown("<h1 style='text-align: center;'>Rent a Car🚙 @ hackaTUM Check24 Challenge</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pick-up Details🧳")
        pickup_location =  st.selectbox("Pick-up Location",
            tuple(list(cities)), index=0)
        pickup_date = st.date_input("Pick-up Date")
        pickup_time = st.time_input("Pick-up Time")
    
    with col2:
        st.subheader("Return Details🏠")
        return_location = st.selectbox("Return Location",
            tuple(list(cities)), index=1)
        return_date = st.date_input("Return Date")
        return_time = st.time_input("Return Time")
    
    if st.button("Show Cars 🚗💨"):
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
        st.session_state['pickup_location'] = pickup_location
        st.session_state['pickupLongitude'] = cities[pickup_location]["longitude"]
        st.session_state['pickupLatitude'] = cities[pickup_location]["latitude"]
        st.session_state['return_location'] = return_location
        st.session_state['returnLongitude'] = cities[return_location]["longitude"]
        st.session_state['returnLatitude'] = cities[return_location]["latitude"]
        st.session_state['pickup_date'] = pickup_date
        st.session_state['pickup_time'] = pickup_time
        st.session_state['return_date'] = return_date
        st.session_state['return_time'] = return_time

    st.markdown('<style>footer{visibility: hidden;}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()