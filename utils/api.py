import requests
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List

@dataclass
class Match:
    date: str
    time: str
    home: str
    away: str
    league: str
    match_id: str
    status: str

class SportsAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "v3.football.api-sports.io"
        }
    
    def get_football_fixtures(self, days: int = 7) -> List[Match]:
        """Tous les matchs foot 7 jours"""
        matches = []
        leagues = [39, 140, 78, 135, 61, 71]  # Top championnats
        
        date_from = datetime.now().strftime("%Y-%m-%d")
        date_to = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        
        for league_id in leagues:
            try:
                url = "https://v3.football.api-sports.io/fixtures"
                params = {"league": league_id, "from": date_from, "to": date_to}
                
                response = requests.get(url, headers=self.headers, params=params)
                data = response.json()['response']
                
                for fixture in data:
                    match_date = datetime.strptime(fixture['fixture']['date'][:10], "%Y-%m-%d")
                    days_ahead = (match_date.date() - datetime.now().date()).days
                    
                    status = "TODAY" if days_ahead == 0 else "TOMORROW" if days_ahead == 1 else "SOON"
                    
                    matches.append(Match(
                        fixture['fixture']['date'][:10],
                        fixture['fixture']['date'][11:16],
                        fixture['teams']['home']['name'],
                        fixture['teams']['away']['name'],
                        fixture['league']['name'],
                        str(fixture['fixture']['id']),
                        status
                    ))
            except Exception as e:
                print(f"Erreur league {league_id}: {e}")
        
        return matches
    
    def get_live_matches(self) -> List[Match]:
        """Matchs live"""
        url = "https://v3.football.api-sports.io/fixtures"
        params = {"live": "all"}
        # Implémentation live...
        return []