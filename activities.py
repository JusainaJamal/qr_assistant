import random

class ActivitiesSuggester:
    """Suggest activities and exercises for quarantine patients"""
    
    def __init__(self):
        self.activities = {
            "meditation": [
                {
                    "name": "5-Minute Breathing Exercise",
                    "description": "Find a comfortable position. Breathe in slowly for 4 counts, hold for 4, exhale for 6. Repeat 10 times.",
                    "duration": "5 minutes",
                    "benefits": "Reduces anxiety, calms the mind"
                },
                {
                    "name": "Body Scan Meditation",
                    "description": "Lie down and mentally scan your body from toes to head, releasing tension in each area.",
                    "duration": "10 minutes",
                    "benefits": "Promotes relaxation, reduces stress"
                },
                {
                    "name": "Mindful Observation",
                    "description": "Choose an object and observe it for 5 minutes. Notice every detail - color, texture, shape.",
                    "duration": "5 minutes",
                    "benefits": "Improves focus, brings present moment awareness"
                }
            ],
            "physical": [
                {
                    "name": "Gentle Stretching",
                    "description": "Stretch your arms, legs, neck, and back. Hold each stretch for 15-30 seconds.",
                    "duration": "10 minutes",
                    "benefits": "Improves flexibility, reduces stiffness"
                },
                {
                    "name": "Chair Exercises",
                    "description": "Seated leg raises, arm circles, torso twists. 10 reps each.",
                    "duration": "15 minutes",
                    "benefits": "Maintains muscle tone, improves circulation"
                },
                {
                    "name": "Wall Push-ups",
                    "description": "Stand arm's length from wall, do push-ups against it. 3 sets of 10.",
                    "duration": "10 minutes",
                    "benefits": "Builds strength, energizes body"
                },
                {
                    "name": "Balance Practice",
                    "description": "Stand on one leg for 30 seconds, then switch. Use wall for support if needed.",
                    "duration": "5 minutes",
                    "benefits": "Improves balance, core strength"
                }
            ],
            "mental": [
                {
                    "name": "Gratitude Journaling",
                    "description": "Write down 3 things you're grateful for today, no matter how small.",
                    "duration": "10 minutes",
                    "benefits": "Improves mood, positive thinking"
                },
                {
                    "name": "Memory Game",
                    "description": "Look at items in your room for 1 minute, close eyes, try to recall all items.",
                    "duration": "10 minutes",
                    "benefits": "Enhances memory, mental sharpness"
                },
                {
                    "name": "Creative Writing",
                    "description": "Write a short story, poem, or letter to your future self.",
                    "duration": "20 minutes",
                    "benefits": "Self-expression, creativity boost"
                },
                {
                    "name": "Learn Something New",
                    "description": "Pick a topic you're curious about and read about it for 15 minutes.",
                    "duration": "15 minutes",
                    "benefits": "Mental stimulation, sense of accomplishment"
                }
            ],
            "entertainment": [
                {
                    "name": "Virtual Museum Tour",
                    "description": "Many museums offer free virtual tours online. Explore art and culture from your room!",
                    "duration": "30 minutes",
                    "benefits": "Cultural enrichment, mental escape"
                },
                {
                    "name": "Podcast Listening",
                    "description": "Find a podcast on a topic you love - comedy, science, stories, etc.",
                    "duration": "30-60 minutes",
                    "benefits": "Entertainment, learning, time passes enjoyably"
                },
                {
                    "name": "Music Therapy",
                    "description": "Create a playlist of uplifting songs and have a personal dance party!",
                    "duration": "20 minutes",
                    "benefits": "Mood boost, stress relief"
                },
                {
                    "name": "Online Games",
                    "description": "Play puzzle games, word games, or connect with friends for online gaming.",
                    "duration": "30 minutes",
                    "benefits": "Fun, social connection, mental engagement"
                }
            ],
            "creative": [
                {
                    "name": "Drawing or Doodling",
                    "description": "No artistic skills needed! Just draw whatever comes to mind.",
                    "duration": "20 minutes",
                    "benefits": "Stress relief, self-expression"
                },
                {
                    "name": "Origami",
                    "description": "Learn to fold paper into beautiful shapes using online tutorials.",
                    "duration": "30 minutes",
                    "benefits": "Focus, accomplishment, creates something beautiful"
                },
                {
                    "name": "Photography Project",
                    "description": "Take creative photos with your phone - shadows, reflections, colors.",
                    "duration": "20 minutes",
                    "benefits": "Creative expression, new perspectives"
                },
                {
                    "name": "Cooking Experiment",
                    "description": "Try making something new with available ingredients.",
                    "duration": "40 minutes",
                    "benefits": "Accomplishment, enjoyment, tasty reward"
                }
            ]
        }
    
    def get_random_activity(self, category=None):
        """
        Get a random activity suggestion
        
        Args:
            category (str): Optional category to filter by
            
        Returns:
            dict: Activity details
        """
        if category and category in self.activities:
            return random.choice(self.activities[category])
        
        # Random from all categories
        all_activities = []
        for activities_list in self.activities.values():
            all_activities.extend(activities_list)
        
        return random.choice(all_activities)
    
    def get_activities_by_category(self, category):
        """Get all activities for a specific category"""
        return self.activities.get(category, [])
    
    def get_all_categories(self):
        """Get list of all activity categories"""
        return list(self.activities.keys())
    
    def get_daily_activity_plan(self):
        """
        Generate a balanced daily activity plan
        
        Returns:
            list: Mix of different activities for the day
        """
        plan = []
        
        # Morning: Meditation/Mindfulness
        plan.append({
            "time": "Morning",
            "activity": random.choice(self.activities["meditation"])
        })
        
        # Mid-Morning: Physical
        plan.append({
            "time": "Mid-Morning",
            "activity": random.choice(self.activities["physical"])
        })
        
        # Afternoon: Mental/Creative
        afternoon_choice = random.choice(["mental", "creative"])
        plan.append({
            "time": "Afternoon",
            "activity": random.choice(self.activities[afternoon_choice])
        })
        
        # Evening: Entertainment
        plan.append({
            "time": "Evening",
            "activity": random.choice(self.activities["entertainment"])
        })
        
        return plan
