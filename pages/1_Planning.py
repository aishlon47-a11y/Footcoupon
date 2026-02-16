import streamlit as st
from utils.predictor import Predictor

st.header("🎫 Coupons Optimisés 3 Niveaux")

if 'api_key' in st.session_state:
    predictor = Predictor(st.session_state.api_key)
    
    # 3 Colonnes pour 3 coupons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("💰 **FAIBLE (5-10)**")
        faible = predictor.generate_coupon("faible", 5, 10)
        cote_faible = predictor.calculate_cote(faible)
        st.metric("Cote Totale", f"{cote_faible:.1f}")
        
        for i, pred in enumerate(faible[:8], 1):
            conf_emoji = "🔥" if pred['conf'] > 0.85 else "✅"
            st.markdown(f"{i}. {conf_emoji} **{pred['selection']}** @{pred['cote']:.2f} ({pred['conf']*100:.0f}%)")
        
        st.caption(f"💵 Mise 1000fcfa → Gain: **{cote_faible*1000:.0f}fcfa**")
    
    with col2:
        st.subheader("💎 **MOYEN (10-50)**")
        moyen = predictor.generate_coupon("moyen", 10, 50)
        cote_moyen = predictor.calculate_cote(moyen)
        st.metric("Cote Totale", f"{cote_moyen:.1f}")
        
        for i, pred in enumerate(moyen[:8], 1):
            st.markdown(f"{i}. 🔥 **{pred['selection']}** @{pred['cote']:.2f}")
        
        st.caption(f"💰 Mise 1000fcfa → Gain: **{cote_moyen*1000:.0f}fcfa**")
    
    with col3:
        st.subheader("💥 **FORT (50-300)**")
        fort = predictor.generate_coupon("fort", 50, 300)
        cote_fort = predictor.calculate_cote(fort)
        st.metric("Cote Totale", f"{cote_fort:.1f}")
        
        for i, pred in enumerate(fort[:8], 1):
            st.markdown(f"{i}. 🚀 **{pred['selection']}** @{pred['cote']:.2f}")
        
        st.caption(f"🎰 Mise 1000fcfa → Gain: **{cote_fort*1000:.0f}fcfa**")
        
        # Bouton Copier
        st.button("📋 Copier tous les coupons", on_click=lambda: st.balloons())
else:
    st.warning("👆 Ajoute ta clé API dans la sidebar")
