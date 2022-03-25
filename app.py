import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_tags import st_tags
from utils import merge_data, clean_data
import joblib

model= joblib.load('model.joblib')

st.set_page_config(page_title="My Webpage",page_icon=":bar_chart:", layout="wide")

# ---- LOAD ASSETS ----


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


names = pd.read_csv("company_names.csv")


st.markdown(""" <style> .green { color:#47AB53 ;}
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .red { color:#EE0E0E  ;}
</style> """, unsafe_allow_html=True)




# ---- HEADER SECTION ----
with st.container():
    st.title("Stock market performance prediction")
    st.write(
        "Choose a ticker and predict the performance of a share in accordance with the market performance next year"
    )


#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# ---- PREDICTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
with left_column:
    with st.container():
        st.write("##")

        ticker=st.text_input('Choose a ticker to predict the performance of the share')


        button=st.button('Predict')
        keyError='quarterlyReports'

        if button:
            if ticker in list(names.Symbol):


                try:

                    df=merge_data(ticker)
                    ticker_to_predict=clean_data(df)
                    response=model.predict_proba(ticker_to_predict)





                    if response [0][1] > 0.5:
                        st.markdown(f" <h3 class='green'> There is {response[0][1]:.2%} of chance that the share performs better than the market next year </h3>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<h3 class='red'> There is {response[0][0]:.2%} of chance that the share doesn't perform better than the market next year</h3>", unsafe_allow_html=True)

                except:
                    st.write('### Try again later')
            else:
                st.write('### The ticker is not in our database')

    with st.container():

        st.write("##")

        st.write('Dont you know the ticker of the company you are looking for?')



        ticker= st_tags(
                            label='**Insert the name of the company and press ENTER to search:**',
                            text='Example: Apple',
                            value='',
                            suggestions=list(names['Name'].unique()),
                            maxtags=1,
                            key="asd")

        try:
            if ticker:
                company = names[names['Name'] == ticker[0]].iloc[0,0]

                st.markdown(f'###  The ticker is: {company}')

        except:

            st.write('error')
with right_column:


        lottie_image = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ymyikn6l.json")

        st_lottie(lottie_image)
