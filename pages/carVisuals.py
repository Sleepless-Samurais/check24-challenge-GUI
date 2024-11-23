import pydeck as pdk
import streamlit as st

def main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude):


    # Define the data for the ArcLayer
    arc_data = [
        {
            "sourcePosition": [ sourceLatitude, sourceLongitude ],  # Starting point (latitude, longitude)
            "targetPosition": [ targetLatitude, targetLongitude ],  # Ending point (latitude, longitude)
            "height": 0.25                          # Height of the arc
        }
    ]

    # Calculate the radius of the circles to be drawn by checking the distance between the two points
    distance = ((sourceLatitude - targetLatitude)**2 + (sourceLongitude - targetLongitude)**2)**0.5
    radius = distance * 1500

    # Define the data for the ScatterplotLayer
    scatter_data = [
        {
            "position": [ sourceLatitude, sourceLongitude ],  # Source position
            "color": [0, 255, 0,70],            # Green color
            "radius": radius*1.5                # Radius in meters
        },
        {
            "position": [ targetLatitude, targetLongitude ],  # Target position
            "color": [255, 0, 0,150],            # Red color
            "radius": radius                # Radius in meters
        }
    ]

    # Create the pydeck chart with the ArcLayer and ScatterplotLayer
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=48.1351,
                longitude=11.5820,
                zoom=6,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "ArcLayer",
                    data=arc_data,
                    get_source_position="sourcePosition",
                    get_target_position="targetPosition",
                    get_source_color=[0, 255, 0,5],  # Green color for the source
                    get_target_color=[255, 0, 0,180],  # Red color for the target
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
            ],
        )
    )

if __name__ == "__main__":
    sourceLatitude = 11.5820
    sourceLongitude = 48.1351
    targetLatitude = 9.2109
    targetLongitude = 49.1427

    main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude)