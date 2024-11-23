import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def main():
    st.set_page_config(layout="wide")
    st.title("JSON Log Parser")
    
    # Select file:
    uploaded_file = st.file_uploader("Choose a file", type="log")

    if uploaded_file is not None:
        df = pd.read_json(uploaded_file, lines=True)
        df['log_str'] = df['log'].apply(lambda x: str(x))

        col0, col1, col2, col3 = st.columns([1, 2, 6,2])
        with col1:
            search = st.text_input("Search for requestType", "")
        with col2:
            searchInsideLog = st.text_input("Search inside log", "")

        if search:
            df = df[df['requestType'].str.contains(search, case=False)]
            st.write("Showing rows with requestType containing:'", search,"'")

        if searchInsideLog:
            df = df[df['log_str'].str.contains(searchInsideLog, case=False)]
            st.write("Showing rows with log containing:'", searchInsideLog,"'")

        
        # Configure the grid options
        gb = GridOptionsBuilder.from_dataframe(df.head(100))
        gb.configure_selection('single', use_checkbox=True)
        grid_options = gb.build()

        # Display the dataframe with AgGrid
        grid_response = AgGrid(
            df,
            gridOptions=grid_options,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            height=400,
            width='100%'
        )

        st.dataframe(df.head(100), use_container_width=True)

        # Get the selected row
        selected_row = grid_response['selected_rows']
        if selected_row:
            st.write("You selected:", selected_row)

if __name__ == "__main__":
    main()