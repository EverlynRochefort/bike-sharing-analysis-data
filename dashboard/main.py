import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Assign variable untuk membaca csv
combine_df = pd.read_csv("combine_df.csv")

# Memberikan title
st.title('Analysis Data: Bike Sharing')

# Penjelasan mengenai analisa dan dataset
st.markdown(
    '''
    Pada analisa ada dua pertanyaan bisnis, sebagai berikut:

    1. Bagaimana perbandingan antara rental pada holidays dengan non-holidays?
    2. Bagaimana perbandingan antara rental pada kondisi cuaca tertentu?
    '''
)

# Penjelasan tentang masalah
st.markdown(
    '''
    Assesment result:

    |              | Missing Value | Duplicate Value | Inaccurate Value |
    | ------------ | ------------- | --------------- | ---------------- |
    | Data Combine | -             | -               | -                |

    Menurut tabel diatas bahwa tidak ada masalah serius pada dataset. 
    Tetapi pada saat melakukan check info() terdapat data type yang salah
    dan juga penamaan yang kurang tepat. Yaitu dtype pada 'dteday' dan nama 
    mnth dan yr (dteday dari object ke datetime, mnth & yr terubah ke month & year).
    '''
)

# Mendisplay data info()
with st.expander("Info Dataframe"):
    st.write("Column Names:", list(combine_df.columns))

st.text("Visualisasi dan Konklusi Jawaban:")

# Visualisasi dari pertanyaan pertama
holiday_groups = combine_df.groupby('holiday_y')
rentals_by_holiday = holiday_groups['cnt_y'].sum()

fig, ax = plt.subplots()
rentals_by_holiday.plot(kind='bar', rot=0, color=['skyblue', 'lightgreen'], ax=ax)
ax.set_title('Bike Rentals: Holidays vs. Non-Holidays')
ax.set_xlabel('Holiday Status')
ax.set_ylabel('Total Rental Counts')
ax.set_xticks(range(len(rentals_by_holiday)))
ax.set_xticklabels(['Non-Holiday', 'Holiday'])

# Print visual
st.pyplot(fig)
st.caption('Gambar 1') # Berikan caption

# Visualisasi dari pertanyaan kedua
weather_groups = combine_df.groupby('weathersit_x')
rentals_by_weather = weather_groups['cnt_y'].sum()

labels = ['Clear', 'Mist', 'Light Snow', 'Heavy Rain']

fig, ax = plt.subplots()
rentals_by_weather.plot(kind='bar', rot=0, color=['lightgreen', 'lightblue', 'lightcoral', 'lightgrey'], ax=ax)
ax.set_title('Bike Rentals by Weather Condition')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Total Rental Counts')
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45)

# Print visual
st.pyplot(fig)
st.caption('Gambar 2') # Berikan caption

# Konklusi
st.markdown(
    '''
    Gambar pertama menggambarkan bahwa orang-orang lebih suka untuk merental
    sepeda pada non-holidays ketimbang holidays. Hasil analisis dapat membantu untuk persiapan stok sepeda dan strategi pemasaran.
    \n
    Gambar kedua menunjukan bahwa orang-orang lebih cenderung meminjam sepeda saat cuaca sedang 'clear'. Hasil analisis dapat membantu 
    memahami pola peminjaman sepeda pada sebuah kondisi cuaca tertentu.
    '''
)