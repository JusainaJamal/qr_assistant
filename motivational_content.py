import random
from datetime import datetime

class MotivationalContent:
    """Provide motivational quotes, success stories, and uplifting content"""
    
    def __init__(self):
        self.quotes = [
            "You are stronger than you think. This challenge is temporary, but your resilience is permanent. 💪",
            "Every day in quarantine is one day closer to freedom. You're doing amazing! 🌟",
            "Your patience and strength during this time are truly admirable. Keep going! 🌈",
            "This too shall pass. You're not alone in this journey. ❤️",
            "Healing is not linear, but you're making progress every single day. 🌱",
            "You're a warrior, not a worrier. You've got this! ⚡",
            "Your health and safety are worth the wait. Be proud of taking care of yourself! 🛡️",
            "Every small step forward is still progress. Celebrate your strength! 🎉",
            "You're writing a story of resilience right now. Make it a good one! 📖",
            "The sun will shine again, and you'll be there to feel its warmth. ☀️",
            "Your courage inspires others, even when you don't see it. 🦋",
            "Rest is not weakness. Taking care of yourself is strength. 🌸",
            "You've survived 100% of your worst days. Today will be no different! 💫",
            "This quarantine is a pause, not a stop. Better days are coming! 🚀",
            "Your mental health matters. Be kind to yourself today. 💚"
        ]
        
        self.success_stories = [
            {
                "title": "Sarah's Journey",
                "story": "Sarah felt lonely during her 14-day quarantine, but she discovered meditation and journaling. She says it transformed her mental health and she still practices these habits today!",
                "lesson": "Quarantine can be an opportunity for self-discovery."
            },
            {
                "title": "Michael's Recovery",
                "story": "Michael was anxious during quarantine, but he stayed connected with family through video calls every day. He learned that distance doesn't diminish love.",
                "lesson": "Stay connected - it makes all the difference."
            },
            {
                "title": "Priya's Transformation",
                "story": "Priya used her quarantine to learn cooking. She tried 20 new recipes and found a new passion. Now she shares her cooking on social media!",
                "lesson": "Use this time to explore new interests."
            },
            {
                "title": "James' Fitness Journey",
                "story": "James started with just 5 minutes of stretching during quarantine. By the end, he had a full exercise routine he still follows. Small starts lead to big changes!",
                "lesson": "Start small, dream big."
            },
            {
                "title": "Aisha's Gratitude Practice",
                "story": "Aisha wrote one thing she was grateful for each day. By day 14, she had a beautiful collection of positive memories that helped her appreciate life more.",
                "lesson": "Gratitude transforms perspective."
            }
        ]
        
        self.affirmations = [
            "I am strong and capable of handling this.",
            "I choose to focus on what I can control.",
            "My health and wellbeing are my top priorities.",
            "I am patient with myself and my healing process.",
            "I trust that better days are ahead.",
            "I am worthy of care, rest, and compassion.",
            "This challenge is making me stronger.",
            "I am doing the best I can, and that is enough.",
            "I choose hope over fear.",
            "I am not defined by this moment in time."
        ]
        
        self.calming_activities = [
            {
                "name": "Nature Sounds",
                "description": "Listen to rain, ocean waves, or forest sounds on YouTube or Spotify.",
                "benefit": "Natural sounds reduce stress and promote relaxation"
            },
            {
                "name": "Progressive Muscle Relaxation",
                "description": "Tense and relax each muscle group, starting from your toes to your head.",
                "benefit": "Releases physical tension and calms the nervous system"
            },
            {
                "name": "Visualization",
                "description": "Close your eyes and imagine your favorite peaceful place in vivid detail.",
                "benefit": "Mental escape that reduces anxiety"
            },
            {
                "name": "Aromatherapy",
                "description": "If you have essential oils or scented items, take a moment to breathe them in deeply.",
                "benefit": "Certain scents can promote calmness and wellbeing"
            },
            {
                "name": "Gentle Music",
                "description": "Put on classical, lo-fi, or acoustic music and just listen mindfully.",
                "benefit": "Music therapy reduces stress and elevates mood"
            }
        ]
    
    def get_daily_quote(self):
        """Get a random motivational quote"""
        # Use date to get consistent quote for the day
        today = datetime.now().date()
        random.seed(today.toordinal())
        quote = random.choice(self.quotes)
        random.seed()  # Reset seed
        return quote
    
    def get_random_quote(self):
        """Get a truly random quote"""
        return random.choice(self.quotes)
    
    def get_success_story(self):
        """Get a random success story"""
        return random.choice(self.success_stories)
    
    def get_affirmation(self):
        """Get a random positive affirmation"""
        return random.choice(self.affirmations)
    
    def get_calming_activity(self):
        """Get a calming activity suggestion"""
        return random.choice(self.calming_activities)
    
    def get_encouragement_package(self):
        """
        Get a complete package of encouragement
        
        Returns:
            dict: Quote, affirmation, and success story
        """
        return {
            "quote": self.get_random_quote(),
            "affirmation": self.get_affirmation(),
            "story": self.get_success_story()
        }
