import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('krisis_bankAfrika.sav', 'rb'))

st.title('Prediksi Krisis Bank Di Negara Di Afrika')
c1, c2 = st.columns(2)

with c1:
    systemic_crisis = st.number_input('Gangguan sistem keuangan')
    domestic_debt_in_default = st.number_input('Utang dalam negeri')
    gdp_weighted_default = st.number_input('Total utang negara')
    independence = st.number_input('Kemerdekaan')
    inflation_crises = st.number_input('Krisis inflasi')

with c2:
    exch_usd = st.number_input('Nilai tukar uang dgn Dollar')
    sovereign_external_debt_default = st.number_input('Utang dengan negara lain')
    inflation_annual_cpi = st.number_input('Tingkat inflasi')
    currency_crises = st.number_input('Krisis mata uang')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[systemic_crisis, exch_usd, domestic_debt_in_default, sovereign_external_debt_default,
                               gdp_weighted_default, inflation_annual_cpi, independence, currency_crises,
                               inflation_crises]])

    if (prediksi [0] == 0):
        prediksi = ('Bank di negara tersebut mengalami krisis')
    else:
        prediksi = ('Bank di negara tersebut tidak mengalami krisis')
st.success(prediksi)