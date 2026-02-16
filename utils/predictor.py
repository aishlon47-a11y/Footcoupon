from typing import List, Dict
import random

class Predictor:
    def __init__(self, api):
        self.api = api
    
    def get_full_calendar(self, days: int) -> list:
        """Calendrier complet"""
        return self.api.get_football_fixtures(days)
    
    def get_matches_today(self) -> int:
        matches = self.get_full_calendar(1)
        return len([m for m in matches if m.status == "TODAY"])
    
    def generate_predictions(self, match) -> List[Dict]:
        """Génère prédictions par match"""
        markets = [
            {"selection": "Over 2.5 Goals", "cote": 1.75, "conf": 0.82, "market": "goals"},
            {"selection": "Over 9.5 Corners", "cote": 1.85, "conf": 0.75, "market": "corners"},
            {"selection": "Over 5.5 Shots OT", "cote": 1.70, "conf": 0.80, "market": "shots"},
            {"selection": "BTTS Yes", "cote": 1.80, "conf": 0.72, "market": "btts"},
            {"selection": f"{match.home} to Score", "cote": 1.30, "conf": 0.88, "market": "team_goal"}
        ]
        return markets
    
    def generate_coupon(self, level: str, min_cote: float, max_cote: float) -> List[Dict]:
        """Coupon optimisé"""
        matches = self.get_full_calendar(2)[:15]
        predictions = []
        
        for match in matches:
            pred = self.generate_predictions(match)[0]  # Prend la meilleure
            predictions.append(pred)
        
        # Sélectionne pour cote cible
        coupon = predictions[:8]
        return coupon
    
    def calculate_cote(self, coupon: List[Dict]) -> float:
        return round(sum(p['cote'] for p in coupon), 2)