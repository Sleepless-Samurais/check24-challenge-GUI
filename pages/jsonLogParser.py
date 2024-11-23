import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


def main():
    st.set_page_config(layout="wide")
    st.title("JSON Log Parser")
    
    #select file:
    uploaded_file = st.file_uploader("Choose a file",type="log")

    if uploaded_file is not None:

        col0, col1, col2 = st.columns([1,2, 8])
        with col1:
            search = st.text_input("Search for requestType", "")

        if search:
            df=pd.read_json(uploaded_file, lines=True)
            df = df[df['requestType'].str.contains(search, case=False)]
            st.write("Showing rows with requestType containing", search)
            st.dataframe(df.head(100), use_container_width=True)
        else:
            st.write("Showing all rows")


        #show only first 100 lines of json as a pandas dataframe
        df=pd.read_json(uploaded_file, lines=True)
        st.dataframe(df.head(100), use_container_width=True)

        


if __name__ == "__main__":
    main()