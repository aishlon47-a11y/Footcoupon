import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.api import SportsAPI

st.header("📊 Statistiques Avancées")

if 'api_key' in st.session_state:
    api = SportsAPI(st.session_state.api_key)
    
    # Stats générales
    col1, col2, col3 = st.columns(3)
    col1.metric("⚽ Total Matchs", "250+")
    col2.metric("📈 Précision Moyenne", "78.2%")
    col3.metric("🏆 Marchés Actifs", "52")
    
    # Tableau stats équipes (mock pour démo)
    stats_data = {
        'Équipe': ['PSG', 'Real Madrid', 'Man City', 'Bayern', 'Liverpool'],
        'Forme': [85, 82, 88, 79, 84],
        'Buts/Match': [2.4, 2.1, 2.6, 2.3, 2.2],
        'Clean Sheets': [45, 52, 48, 41, 50]
    }
    
    df_stats = pd.DataFrame(stats_data)
    st.subheader("⭐ Top 5 Équipes en Forme")
    st.dataframe(df_stats, use_container_width=True)
    
    # Graphique forme
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_stats['Équipe'], y=df_stats['Forme'], 
                        marker_color=['#4ecdc4', '#ff6b6b', '#ffd93d', '#6c5ce7', '#a55eea']))
    fig.update_layout(title="Forme actuelle (%)", xaxis_title="Équipes")
    st.plotly_chart(fig, use_container_width=True)
    
else:
    st.info("🔑 Clé API requise pour les stats")