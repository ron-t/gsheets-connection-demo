import streamlit as st
import math
from streamlit_gsheets import GSheetsConnection

MAX_ROWS = 20
MAX_COLS = 5

with st.form("form"):
    num_rows = st.slider("How many rows?", 1, MAX_ROWS)
    num_cols = st.slider("How many columns?", 1, MAX_COLS)

    submitted = st.form_submit_button("Retrieve")       

# credit: https://docs.streamlit.io/knowledge-base/tutorials/databases/private-gsheet
# Create a connection object.
if submitted:
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(
        worksheet="Sheet1",
        ttl="5s",
        usecols=range(0,num_cols),
        nrows=num_rows,
    )

    st.write(f"First {num_rows} rows and {num_cols} columns from {conn.client._spreadsheet}")
    st.dataframe(df, hide_index=True)
