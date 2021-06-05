# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Forest Fires Data Set')
df = pd.DataFrame(pd.read_csv("forestfires.csv"))
if st.checkbox('Show Data'):
    st.subheader('Raw Data')
    st.write(df.head())


st.subheader('Spatial Coordinates')
sns.scatterplot(data=df, x="X", y="Y", hue="month")
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
st.pyplot()

link = '[Data_link](https://archive.ics.uci.edu/ml/datasets/Forest+Fires)'
st.sidebar.title("Data Set Information:")
st.sidebar.markdown("P. Cortez and A. Morais. A Data Mining Approach to Predict Forest"
                    " Fires using Meteorological Data. In J. Neves, M. F. Santos and J. Machado Eds., "
                    "New Trends in Artificial Intelligence, Proceedings of the 13th EPIA 2007 - Portuguese "
                    "Conference on Artificial Intelligence, December, Guimaraes, Portugal, pp. 512-523, 2007. "
                    "APPIA, ISBN-13 978-989-95618-0-9.")
st.sidebar.write(link)