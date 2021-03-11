import streamlit as st
import pandas as pd 
import numpy as np 

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe','Chart')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Judul""")
elif option == 'Dataframe':
    st.write("""## Dataframe""")
    df = pd.DataFrame({
        'Column 1':[1,2,3,4],
        'Column 2':[10,12,14,16]
    })
    df
elif option == 'Chart':
    st.write("""## Draw Charts""")
    chart_data = pd.DataFrame(
        np.random.randn(20,2),
        columns=['a','b']
    )

    st.line_chart(chart_data)
elif option == 'Map':
    st.write("""## Plot a map""")
    map_data = pd.DataFrame(
        np.random.randn(100,2) / [20,20] + [37.76, -122.4],
        columns=['lat','lon']
    )