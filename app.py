import streamlit as st
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

st.title("Projet de Web Scraping")
st.write("## Sujet : Comparaison entre les voyages en train et en avion au sein de l'Italie")
df = pd.read_csv("common_travels_data.csv",index_col=0)

# Affichage du dataframe shuffled
st.subheader("Aperçu des données")
st.dataframe(df.sample(frac=1, random_state=50).reset_index().head(10))

st.subheader("Analyse comparative des voyages à travers la visualisation")

# Visualisation sur le prix du voyage
st.write("#### Comparaison du prix du voyage")
fig = px.box(df, x='travel', y='price', color='travel_mean', color_discrete_sequence=px.colors.qualitative.Prism)
fig.update_layout(title_text='Boîtes à moustache des prix (€) de chaque trajet pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Prix (€) / Empreinte carbone (kg)')

# Empreinte carbone moyenne chaque voyage/moyen de transport
avg_footprint = df.groupby(['travel', 'travel_mean'])['carbon_footprint'].mean().reset_index()

# Color map pour chaque moyen de transport
color_map = dict(zip(avg_footprint['travel_mean'].unique(), px.colors.qualitative.T10[::-1]))

# Scatter plot pour chaque (travel,travel_mean) 
fig.add_trace(go.Scatter(
    x=avg_footprint['travel'],
    y=avg_footprint['carbon_footprint'],
    mode='markers',
    name = 'carbon scatter',
    marker=dict(color=avg_footprint['travel_mean'].map(color_map)), 
))

# Légende pour indiquer le moyen de transport associé au scatter
for mean, color in color_map.items():
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(color=color),
        name=f"{mean} carbon footprint"
    ))
st.plotly_chart(fig)

# Visualisation sur l'empreinte carbone
st.write("#### Comparaison de l'empreinte carbone du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])[['carbon_footprint','price','travel_duration']].mean().reset_index(),
             x='travel', y='carbon_footprint', color='travel_mean',hover_data=['price','travel_duration'],
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)

fig.update_layout(title_text='Empreinte carbone (kg) des différents trajets pour chaque moyen de transport',
                  xaxis_title='Trajet', yaxis_title='Empreinte carbone (kg)')

fig.update_traces(hovertemplate='Empreinte carbone : %{y} kg<br>Prix moyen : %{customdata[0]:.2f} €<br>Durée moyenne : %{customdata[1]:.2f} heures')
st.plotly_chart(fig)

# Visualisation durée du trajet
st.write("#### Comparaison de la durée moyenne du trajet")
fig = px.bar(df.groupby(['travel', 'travel_mean'])[['travel_duration','carbon_footprint','price']].mean().reset_index(),
             x='travel', y='travel_duration', color='travel_mean',hover_data=['carbon_footprint','price'],
             barmode='group',color_discrete_sequence=px.colors.qualitative.Prism)

fig.update_layout(title_text="Durée moyenne (heures) des différents trajets pour chaque moyen de transport",
                  xaxis_title='Trajet', yaxis_title='Durée moyenne (heures)')

fig.update_traces(hovertemplate='Durée moyenne : %{y:.2f} heures <br>Empreinte carbone : %{customdata[0]} kg <br>Prix moyen : %{customdata[1]:.2f} €')
st.plotly_chart(fig)