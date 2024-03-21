import streamlit as st
import math
from streamlit_gsheets import GSheetsConnection

# credit: https://docs.streamlit.io/knowledge-base/tutorials/databases/private-gsheet
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=20,
)

df = df.dropna(thresh=1)

# Print results.
for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")
