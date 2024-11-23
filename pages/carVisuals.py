import pydeck as pdk
import streamlit as st
import json

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

def main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude,departureDate,returnDate):
    jsonFile = "testdata.json"
    tripData = None
    with open(jsonFile) as file:
        data = json.load(file)
        tripData = data[0]


    #set zoom level
    zoom_level = 7


    # Define the data for the ArcLayer
    arc_data = [
        {
            "sourcePosition": [sourceLatitude, sourceLongitude],  # Starting point (latitude, longitude)
            "targetPosition": [targetLatitude, targetLongitude],  # Ending point (latitude, longitude)
            "height": 0.25  # Height of the arc
        }
    ]

    # Calculate the radius of the circles to be drawn by checking the distance between the two points
    distance = ((sourceLatitude - targetLatitude)**2 + (sourceLongitude - targetLongitude)**2)**0.5
    radius = distance * 1500

    # Calculate the center of the source and target
    centerLatitude = (sourceLatitude + targetLatitude) / 2
    centerLongitude = (sourceLongitude + targetLongitude) / 2


    # Define the data for the TextLayer
    text_data = [
        {
            "position": [sourceLatitude, sourceLongitude],  # Source position
            "text": departureDate,
            "color": [0, 255, 0,245],  # Green color
        },
        {
            "position": [targetLatitude, targetLongitude],  # Target position
            "text": returnDate,
            "color": [255, 0, 0,245],  # Red color
        }
    ]

        # Define the data for the ScatterplotLayer
    scatter_data = [
        {
            "position": [sourceLatitude, sourceLongitude],  # Source position
            "color": [0, 255, 0, 70],  # Green color
            "radius": radius * 1.5  # Radius in meters
        },
        {
            "position": [targetLatitude, targetLongitude],  # Target position
            "color": [255, 0, 0, 150],  # Red color
            "radius": radius  # Radius in meters
        }
    ]

    # Create the pydeck chart with the ArcLayer, ScatterplotLayer, and TextLayer
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=centerLongitude,
                longitude=centerLatitude,
                zoom=zoom_level,  # Set the zoom level here
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "ArcLayer",
                    data=arc_data,
                    get_source_position="sourcePosition",
                    get_target_position="targetPosition",
                    get_source_color=[0, 255, 0, 5],  # Green color for the source
                    get_target_color=[255, 0, 0, 180],  # Red color for the target
                    get_width=5,
                    get_height="height",  # Set the height of the arc
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=scatter_data,
                    get_position="position",
                    get_fill_color="color",
                    get_radius="radius",
                ),
                pdk.Layer(
                    "TextLayer",
                    data=text_data,
                    get_position="position",
                    get_text="text",
                    get_color="color",
                    get_size=32,
                ),
            ],
        ),
        use_container_width=True
    )


    # Display the trip data
    st.write("Trip Data:")
    #transforming distance in coordinates to distance in kilometers:
    distance2 = distance * 111.32
    st.write("Approximate Distance between the two points:", distance2)
    st.write("Distance that is free to cover with the car:", tripData.get("FreeKilometers"))
    st.write("With the included kilometers you can approximately cover the following distance in the cities:", tripData.get("FreeKilometers") - distance2)
    st.write("Price for the trip:", tripData.get("Price"))

    #removing footer:
    st.markdown('<style>footer{visibility: hidden;}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    sourceLatitude = 11.5820
    sourceLongitude = 48.1351
    targetLatitude = 9.2109
    targetLongitude = 49.1427

    main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude, "2021-11-01", "2021-11-02")