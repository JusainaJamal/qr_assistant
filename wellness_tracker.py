import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from config import Config

class WellnessTracker:
    """Track patient wellness and mood over time"""
    
    def __init__(self):
        self.mood_history = []
        self.check_ins = []
    
    def log_mood(self, mood, notes=""):
        """
        Log patient's current mood
        
        Args:
            mood (str): Selected mood from Config.MOODS
            notes (str): Optional notes about how they're feeling
        """
        entry = {
            "timestamp": datetime.now(),
            "mood": mood,
            "notes": notes
        }
        self.mood_history.append(entry)
    
    def get_mood_score(self, mood):
        """Convert mood emoji to numeric score for visualization"""
        mood_scores = {
            "😊 Great": 5,
            "🙂 Good": 4,
            "😐 Okay": 3,
            "😔 Not Good": 2,
            "😢  Bad" : 1
        }
        return mood_scores.get(mood, 3)
    
    def create_mood_chart(self):
        """
        Create a plotly chart showing mood trends
        
        Returns:
            plotly.graph_objects.Figure: Mood trend chart
        """
        if not self.mood_history:
            return None
        
        # Convert to DataFrame
        df = pd.DataFrame(self.mood_history)
        df['mood_score'] = df['mood'].apply(self.get_mood_score)
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')
        
        # Create line chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['mood_score'],
            mode='lines+markers',
            name='Mood',
            line=dict(color='#4CAF50', width=3),
            marker=dict(size=10, color='#66BB6A'),
            hovertemplate='<b>%{text}</b><br>Time: %{x}<extra></extra>',
            text=df['mood']
        ))
        
        fig.update_layout(
            title='Your Mood Journey',
            xaxis_title='Time',
            yaxis_title='Mood Level',
            yaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['😢 Bad', '😔 Not Good', '😐 Okay', '🙂 Good', '😊 Great']
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            hovermode='x unified'
        )
        
        return fig
    
    def get_mood_summary(self):
        """
        Get summary statistics of mood history
        
        Returns:
            dict: Summary statistics
        """
        if not self.mood_history:
            return {
                "total_entries": 0,
                "average_mood": "No data",
                "best_day": "No data",
                "trend": "No data"
            }
        
        df = pd.DataFrame(self.mood_history)
        df['mood_score'] = df['mood'].apply(self.get_mood_score)
        
        avg_score = df['mood_score'].mean()
        avg_mood_text = {
            (4.5, 5.1): "😊 Great",
            (3.5, 4.5): "🙂 Good",
            (2.5, 3.5): "😐 Okay",
            (1.5, 2.5): "😔 Not Good",
            (0, 1.5): "😢 Bad"
        }
        
        avg_mood = next((mood for (low, high), mood in avg_mood_text.items() if low <= avg_score < high), "😐 Okay")
        
        best_entry = df.loc[df['mood_score'].idxmax()]
        best_day = best_entry['timestamp'].strftime('%Y-%m-%d %H:%M')
        
        # Simple trend calculation
        if len(df) >= 2:
            recent_avg = df.tail(3)['mood_score'].mean()
            older_avg = df.head(max(3, len(df)-3))['mood_score'].mean()
            if recent_avg > older_avg + 0.5:
                trend = "📈 Improving"
            elif recent_avg < older_avg - 0.5:
                trend = "📉 Needs attention"
            else:
                trend = "➡️ Stable"
        else:
            trend = "➡️ Just started"
        
        return {
            "total_entries": len(self.mood_history),
            "average_mood": avg_mood,
            "best_day": best_day,
            "trend": trend
        }
    
    def log_check_in(self, symptoms, temperature=None, notes=""):
        """
        Log daily health check-in
        
        Args:
            symptoms (list): List of symptoms
            temperature (float): Body temperature if measured
            notes (str): Additional notes
        """
        entry = {
            "timestamp": datetime.now(),
            "symptoms": symptoms,
            "temperature": temperature,
            "notes": notes
        }
        self.check_ins.append(entry)
    
    def get_latest_check_in(self):
        """Get the most recent check-in"""
        if self.check_ins:
            return self.check_ins[-1]
        return None
