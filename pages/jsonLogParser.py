import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide")
    st.title("JSON Log Parser")
    
    # Select file:
    uploaded_file = st.file_uploader("Choose a file", type=["log", "json", "txt"])

    if uploaded_file is not None:
        df = pd.read_json(uploaded_file, lines=True)
        df['log_str'] = df['log'].apply(lambda x: str(x))

        col1, col2, col3 = st.columns([2, 3,6 ])
        with col1:
            search = st.text_input("Search for requestType", "")
        with col2:
            searchInsideLog = st.text_input("Search inside log", "")
        with col3:
            selected_row = st.multiselect("Select a row", df.to_dict(orient='records'))

        if search:
            df = df[df['requestType'].str.contains(search, case=False)]
            st.write("Showing rows with requestType containing:'", search,"'")

        if searchInsideLog:
            df = df[df['log_str'].str.contains(searchInsideLog, case=False)]
            st.write("Showing rows with log containing:'", searchInsideLog,"'")

    

        st.dataframe(df.head(100), use_container_width=True)

        # Get the selected row
        col99, col100 = st.columns(2)

        i = 1 
        if selected_row:
            for row in selected_row:
                if i%2 == 1:
                    with col99:
                        st.write(f"## You selected row {i}")
                        i += 1
                        st.write(row)
                        st.write("requestType:", row['requestType'])
                        st.write("log:", row['log'])
                        st.write("timestamp:", row['timestamp'])
                        st.write("log_str:", row['log_str'])
                        st.write("message:", recursiveJsonParser(row['log'], 'message'))
                        st.write("requestType:", recursiveJsonParser(row['log'], 'requestType'))
                        st.write("timestamp:", recursiveJsonParser(row['log'], 'timestamp'))
                        st.write("log_str:", recursiveJsonParser(row['log'], 'log_str'))
                else:
                    with col100:
                        st.write(f"## You selected row {i}")
                        i += 1
                        st.write(row)
                        st.write("requestType:", row['requestType'])
                        st.write("log:", row['log'])
                        st.write("timestamp:", row['timestamp'])
                        st.write("log_str:", row['log_str'])
                        st.write("message:", recursiveJsonParser(row['log'], 'message'))
                        st.write("requestType:", recursiveJsonParser(row['log'], 'requestType'))
                        st.write("timestamp:", recursiveJsonParser(row['log'], 'timestamp'))
                        st.write("log_str:", recursiveJsonParser(row['log'], 'log_str'))
            



def recursiveJsonParser(jsonData, key):
    if isinstance(jsonData, dict):
        for k, v in jsonData.items():
            if k == key:
                return v
            else:
                return recursiveJsonParser(v, key)
    elif isinstance(jsonData, list):
        for item in jsonData:
            return recursiveJsonParser(item, key)
    else:
        return None

if __name__ == "__main__":
    main()