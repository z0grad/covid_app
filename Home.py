# Main Streamlit page

import streamlit as st

st.title('Covid-19 Data Analysis')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(''' # ''')
        st.markdown(''' WHO Covid-19 Dashboard ''')
        
    with col2:
        # Image
        st.image('https://www.who.int/images/default-source/health-topics/coronavirus/covid-19-who-5-1-2020.jpg?sfvrsn=3b1b1b1c_2', width=100)


# Description
st.header('Description')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')