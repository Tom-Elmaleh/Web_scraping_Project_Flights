import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("common_travels_data.csv",index_col=0)

destinations = ['Venice-Naples', 'Venice-Bari', 'Milan-Bari', 'Milan-Naples','Milan-Pescara', 'Rome-Bari']
vals_train = [1,2,3.5,2.5,2,2]

df["carbon_footprint"] = 0

for i in range(len(destinations)):
    filt = (df['travel'] == destinations[i]) & (df['travel_mean']=='train')
    df.loc[filt, 'carbon_footprint'] = vals_train[i]
    
vals_avions = [191,202,233,233,186,166]

for i in range(len(destinations)):
    filt = (df['travel'] == destinations[i]) & (df['travel_mean']=='plane')
    df.loc[filt, 'carbon_footprint'] = vals_avions[i]


# Affichage du dataframe shuffled
st.dataframe(df.sample(frac=1, random_state=50).reset_index())

st.write("### Comparaison du prix du trajet")
fig = px.box(df, x='travel', y='price', color='travel_mean',color_discrete_sequence=px.colors.qualitative.Prism)
fig.update_layout(title_text='Boîtes à moustache des prix (en euros) de chaque trajet pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Prix (en euros)')
fig.show()
st.plotly_chart(fig)

st.write("### Comparaison de l'empreinte carbone du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])['carbon_footprint'].max().reset_index(),
             x='travel', y='carbon_footprint', color='travel_mean',
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)
fig.update_layout(title_text='Empreinte carbone (en kg) des différents trajets pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Empreinte carbone (en kg)')
fig.show()
st.plotly_chart(fig)

st.write("### Comparaison de la durée moyenne du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])['travel_duration'].mean().reset_index(),
             x='travel', y='travel_duration', color='travel_mean',
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)

fig.update_layout(title_text='Durée moyenne (en heures) des différents trajets pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Durée moyenne (en heures)')
fig.show()
st.plotly_chart(fig)