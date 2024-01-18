import streamlit as st
import pandas as pd
import plotly
import plotly.express as px

df = pd.read_csv("common_travels_data.csv",index_col=0)

# Affichage du dataframe shuffled
st.write("### Aperçu du dataframe")
st.dataframe(df.sample(frac=1, random_state=50).reset_index())

# Visualisation prix du trajet
st.write("### Comparaison du prix du trajet")
fig = px.box(df, x='travel', y='price', color='travel_mean',color_discrete_sequence=px.colors.qualitative.Prism)
fig.update_layout(title_text='Boîtes à moustache des prix (en euros) de chaque trajet pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Prix (en euros)')
fig.show()
st.plotly_chart(fig)

# Visualisation empreinte carbone
st.write("### Comparaison de l'empreinte carbone du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])['carbon_footprint'].max().reset_index(),
             x='travel', y='carbon_footprint', color='travel_mean',
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)
fig.update_layout(title_text='Empreinte carbone (en kg) des différents trajets pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Empreinte carbone (en kg)')
fig.show()
st.plotly_chart(fig)

# Visualisation durée du trajet
st.write("### Comparaison de la durée moyenne du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])['travel_duration'].mean().reset_index(),
             x='travel', y='travel_duration', color='travel_mean',
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)

fig.update_layout(title_text='Durée moyenne (en heures) des différents trajets pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Durée moyenne (en heures)')
fig.show()
st.plotly_chart(fig)