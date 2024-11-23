import streamlit as st
import json

#get all the possible trips from testdata.json
def main():
    jsonFile = "testdata.json"
    st.title("Chosen trip will be shown here:")


    with open(jsonFile) as file:
        data = json.load(file)

        #truncate the data to only first 20 entries
        data = data[:20]
        import pages.carVisuals
        sourceLatitude = 11.5820
        sourceLongitude = 48.1351
        targetLatitude = 9.2109
        targetLongitude = 49.1427
        #pages.carVisuals.main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude,data[0].get("StartTimestamp"),data[0].get("EndTimestamp")) 

        st.write("Select a trip from the list below:")
        for trip in data:
            st.write(trip)
            buttonString = "Select " + trip.get("OfferID")
            if st.button(buttonString):
                st.write("Selected trip:")
                #forwarding to carVisuals.py
                import pages.carVisuals
                sourceLatitude = 11.5820
                sourceLongitude = 48.1351
                targetLatitude = 9.2109
                targetLongitude = 49.1427
                pages.carVisuals.main(sourceLatitude, sourceLongitude, targetLatitude, targetLongitude,trip.get("StartTimestamp"),trip.get("EndTimestamp")) 
                    
                    
                distance = ((sourceLatitude - targetLatitude)**2 + (sourceLongitude - targetLongitude)**2)**0.5
                #transforming distance in coordinates to distance in kilometers:
                distance = distance * 111.32
                st.write("Approximate Distance between the two points:", distance)
                st.write("Distance that is free to cover with the car:", trip.get("FreeKilometers"))
                st.write("With the included kilometers you can approximately cover the following distance in the cities:", trip.get("FreeKilometers") - distance)
                st.write("Price for the trip:", trip.get("Price"))
                #get to the top of the page:

                st.markdown('[Go to Chosen Trip](#chosen-trip-will-be-shown-here)', unsafe_allow_html=True)

if __name__ == "__main__":
    main()