import streamlit as st
from utils.api import SportsAPI
import time

st.header("🔴 Scores en Direct")

if 'api_key' in st.session_state:
    api = SportsAPI(st.session_state.api_key)
    
    # Auto-refresh
    refresh_time = st.button("🔄 Actualiser Live (30s)")
    
    live_matches = api.get_live_matches()
    
    if live_matches:
        for match in live_matches:
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(f"**{match.home} vs {match.away}**")
            with col2:
                st.markdown(f"**{match.score}**")
            with col3:
                st.caption(f"{match.minute}'")
    else:
        st.info("⏳ Aucun match live actuellement")
        st.balloons()
else:
    st.warning("⚠️ Clé API requise")