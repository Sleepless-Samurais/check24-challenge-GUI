import pydeck as pdk
import streamlit as st
import json
import streamlit.components.v1 as components

#st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
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

def main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude,departureDate,returnDate):
    #removing footer:
    st.markdown('<style>footer{visibility: hidden;}</style>', unsafe_allow_html=True)

    st.markdown('<style>.mapboxgl-ctrl-bottom-right{display: none;}</style>', unsafe_allow_html=True)

    col1, col2, col3,col4 = st.columns([1, 10, 4,2])
    jsonFile = "testdata.json"
    tripData = None
    with open(jsonFile) as file:
        data = json.load(file)
        tripData = data[0]

    #check if state variables are set:




    if st.session_state["pickup_location"] is None:
        pickup_location = "Munich"
        return_location = "Heilbronn"
    else:
        sourceLatitude = st.session_state["pickupLongitude"]
        sourceLongitude = st.session_state["pickupLatitude"]
        targetLatitude = st.session_state["returnLongitude"]
        targetLongitude = st.session_state["returnLatitude"]
        pickup_location = st.session_state["pickup_location"]
        return_location = st.session_state["return_location"]


    # Calculate the radius of the circles to be drawn by checking the distance between the two points
    distance = ((sourceLatitude - targetLatitude)**2 + (sourceLongitude - targetLongitude)**2)**0.5
    radius = distance * 1500


    distance2 = distance * 111.32
    pickup_date = tripData.get("StartTimestamp")
    #remove last 10 characters from the string to get the date
    pickup_date = pickup_date[:-10]
    return_date = tripData.get("EndTimestamp")
    return_date = return_date[:-10]
    approxDistanceBetweenSourceAndTarget = distance2
    #remove unnecessary numbers after dots of float
        
    coveredDistance = tripData.get("FreeKilometers")
    leftDistance = coveredDistance - approxDistanceBetweenSourceAndTarget
    cost = tripData.get("Price")

    with col3:
        #this is the right side of screen.
        #transforming distance in coordinates to distance in kilometers:
        

        column3String = (
f"""
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 60%;
    }}

    .container {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      width: 60%;
      height: 60%;
      max-width: 600px;
      justify-items: center; /* Center items horizontally */
      align-items: center;  /* Center items vertically */
    }}

    .box {{
    position: relative;
    background-color: #efefef;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    text-align: center;
    padding: 2px;
    width: 100%;
    width: 220px;
    height: 110px; /* Set the maximum height for the box */
    overflow: hidden; /* Ensures content doesn't overflow the box */
    transition: 0.3s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
    scale: 1;
    }}

    .box .icon {{
      font-size: 30px;
      color: #007BFF;
      margin-bottom: 5px;
    }}

    .box .label {{
      font-size: 18px;
      font-weight: bold;
      color: #333;
    }}

    /* Hover effect */
    .box:hover {{
      
    }}

    .box:hover::after {{
      content: attr(data-hover-text);
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: rgba(0, 0, 0);
      color: #fff;
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      white-space: nowrap;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="box" data-hover-text="Change pickup location">
      <div class="icon">🚗</div>
      <div class="label">Pick car from {pickup_location}</div>
    </div>
    <div class="box" data-hover-text="Change return location">
      <div class="icon">📍</div>
      <div class="label">Return Car to {return_location}</div>
    </div>
    <div class="box" data-hover-text="Change your pickup date">
      <div class="icon">📅</div>
      <div class="label">Pick up car on: {pickup_date}</div>
    </div>
    <div class="box" data-hover-text="Change your return date">
      <div class="icon">🕒</div>
      <div class="label">Return car on: {return_date}</div>
    </div>
    <div class="box" data-hover-text="">
      <div class="icon">📏</div>
      <div class="label">Distance: {approxDistanceBetweenSourceAndTarget} km</div>
    </div>
    <div class="box" data-hover-text="">
      <div class="icon">📶</div>
      <div class="label">Free Kilometers: {coveredDistance} km</div>
    </div>
    <div class="box" data-hover-text="Distance left after the trip">
      <div class="icon">➖</div>
      <div class="label">Left Distance: {leftDistance} km</div>
    </div>
    <div class="box" data-hover-text="View trip cost details">
      <div class="icon">💰</div>
      <div class="label">Cost: {cost} EUR</div>
    </div>
  </div>
""")

        st.markdown(column3String, unsafe_allow_html=True)


    with col2:


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


        # Calculate the center of the source and target
        centerLatitude = (sourceLatitude + targetLatitude) / 2
        centerLongitude = (sourceLongitude + targetLongitude) / 2


        # Define the data for the TextLayer
        text_data = [
            {
                "position": [sourceLatitude, sourceLongitude],  # Source position
                "text": departureDate,
                "color": [40, 255, 140,245],  # Green color
            },
            {
                "position": [targetLatitude, targetLongitude],  # Target position
                "text": returnDate,
                "color": [255, 30, 30,245],  # Red color
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
                        get_source_color=[0, 255, 30, 100],  # Green color for the source
                        get_target_color=[255, 30, 30, 140],  # Red color for the target
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


    col10, col11,col12,col13 = st.columns([1,6,8,1])
    
    with col11:
        # auto play mkv file:
        #video_file = open('carSpinning.mp4', 'rb')
        #video_bytes = video_file.read()
        #st.video(video_bytes, start_time=0, loop=True, format='video/mp4')#www.cartrade.com
        #video_file.close()

        #open gif carSpinning.gif
        st.image("carSpinning.gif", use_column_width=True)

    with col12:
        st.write("Get suggestions with the extra kilometers you have included in your rental:")
        #center items in class="st-emotion-cache-1rsyhoq e1nzilvr5"
        #st.markdown('<style>.st-emotion-cache-1rsyhoq.e1nzilvr5 {display: flex;justify-content: center;align-items: center;}</style>', unsafe_allow_html=True)

        #adding buttons of cities to visit with distances:
        col14, col15, col16 = st.columns(3)
        #making divs with class="stColumn st-emotion-cache-1r6slb0 e1f1d6gn3" have centered elements
        st.markdown('<style>.stColumn.st-emotion-cache-1r6slb0.e1f1d6gn3 {display: flex;justify-content: center;align-items: center;}</style>', unsafe_allow_html=True)
        with col14:
            #location of Stuttgart: 48.7758° N, 9.1829° E
            distanceToSTG = ((sourceLatitude - 9.1829)**2 + (sourceLongitude - 48.7758)**2)**0.5
            distanceToSTG = distanceToSTG * 111.32
            st.write("Distance to Stuttgart:", distanceToSTG,"km")
            if True:
                with st.popover("Stuttgart"):
                    st.write("Stuttgart is the capital and largest city of the German state of Baden-Württemberg. It is located on the Neckar river in a fertile valley known as the Stuttgart Cauldron. It lies an hour from the Swabian Jura and the Black Forest. Its urban area has a population of 634,830, making it the sixth largest city in Germany.")
                    #open a popup with arc from source to Stuttgart

                    #Define the data for the ArcLayer
                    arc_data = [
                        {
                            "sourcePosition": [sourceLatitude, sourceLongitude],  # Starting point (latitude, longitude)
                            "targetPosition": [9.1829, 48.7758],  # Ending point (latitude, longitude)
                            "height": 0.25  # Height of the arc
                        },
                        {
                            "sourcePosition": [9.1829, 48.7758],  # Starting point (Stuttgart)
                            "targetPosition": [9.2219, 49.1427],  # Ending point (Heilbronn)
                            "height": 0.25  # Height of the arc
                        }
                    ]
                    # Create the pydeck chart with the ArcLayer
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
                                    get_source_color=[0, 255, 30, 100],  # Green color for the source
                                    get_target_color=[255, 30, 30, 140],  # Red color for the target
                                    get_width=5,
                                    get_height="height",  # Set the height of the arc
                                ),
                            ],
                        ),
                        use_container_width=True
                    )

        with col15:
            #location of Nuremberg: 49.4520° N, 11.0768° E
            distanceToNUE = ((sourceLatitude - 11.0768)**2 + (sourceLongitude - 49.4520)**2)**0.5
            distanceToNUE = distanceToNUE * 111.32
            st.write("Distance to Nuremberg:", distanceToNUE,"km")
            if True:
                with st.popover("Nuremberg"):
                    st.write("Nuremberg is the second-largest city of the German federal state of Bavaria after its capital Munich, and its 518,370 (2019) inhabitants make it the 14th largest city in Germany. On the Pegnitz River (from its confluence with the Rednitz in Fürth onwards: Regnitz, a tributary of the River Main), it lies in the Rhine-Main-Danube Region and is the largest city in Franconia.")
                    #open a popup with arc from source to Nuremberg

                    #Define the data for the ArcLayer
                    arc_data = [
                        {
                            "sourcePosition": [sourceLatitude, sourceLongitude],  # Starting point (latitude, longitude)
                            "targetPosition": [11.0768, 49.4520],  # Ending point (latitude, longitude)
                            "height": 0.25  # Height of the arc
                        },
                        {
                            "sourcePosition": [11.0768, 49.4520],  # Starting point (Nuremberg)
                            "targetPosition": [9.2219, 49.1427],  # Ending point (Heilbronn)
                            "height": 0.25  # Height of the arc
                        }
                    ]
                    # Create the pydeck chart with the ArcLayer
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
                                    get_source_color=[0, 255, 30, 100],  # Green color for the source
                                    get_target_color=[255, 30, 30, 140],  # Red color for the target
                                    get_width=5,
                                    get_height="height",  # Set the height of the arc
                                ),
                            ],
                        ),
                        use_container_width=True
                    )
        #now Ulm: 48.4011° N, 9.9876° E
        with col16:
            distanceToULM = ((sourceLatitude - 9.9876)**2 + (sourceLongitude - 48.4011)**2)**0.5
            distanceToULM = distanceToULM * 111.32
            st.write("Distance to Ulm:", distanceToULM,"km")
            if True:
                with st.popover("Ulm"):
                    st.write("Ulm is a city in the federal German state of Baden-Württemberg, situated on the River Danube. The city, whose population is estimated at 126,000 (2016), forms an urban district of its own (German: Stadtkreis) and is the administrative seat of the Alb-Donau district. Ulm, founded around 850, is rich in history and traditions as a former free imperial city (German: freie Reichsstadt).")
                    #open a popup with arc from source to Ulm

                    #Define the data for the ArcLayer
                    arc_data = [
                        {
                            "sourcePosition": [sourceLatitude, sourceLongitude],  # Starting point (latitude, longitude)
                            "targetPosition": [9.9876, 48.4011],  # Ending point (latitude, longitude)
                            "height": 0.25  # Height of the arc
                        },
                        {
                            "sourcePosition": [9.9876, 48.4011],  # Starting point (Ulm)
                            "targetPosition": [9.2219, 49.1427],  # Ending point (Heilbronn)
                            "height": 0.25  # Height of the arc
                        }
                    ]
                    # Create the pydeck chart with the ArcLayer
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
                                    get_source_color=[0, 255, 30, 100],  # Green color for the source
                                    get_target_color=[255, 30, 30, 140],  # Red color for the target
                                    get_width=5,
                                    get_height="height",  # Set the height of the arc
                                ),
                            ],
                        ),
                        use_container_width=True
                    )

                    

        


if __name__ == "__main__":
    sourceLatitude = 11.5820
    sourceLongitude = 48.1351
    targetLatitude = 9.2109
    targetLongitude = 49.1427

    main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude, "2021-11-01", "2021-11-02")