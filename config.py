import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Quarantine Assistant application"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 500
    TEMPERATURE = 0.7
    
    # Email Configuration
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    ALERT_EMAIL = os.getenv("ALERT_EMAIL", "jusainajusu8086@gmail.com")
    
    # Application Settings
    APP_TITLE = os.getenv("APP_TITLE", "🏥 Quarantine Assistant")
    PATIENT_NAME = os.getenv("PATIENT_NAME", "Friend")
    
    # System Prompts
    SYSTEM_PROMPT = f"""You are a compassionate and empathetic AI assistant designed to support patients in quarantine. 
Your role is to:
- Provide emotional support and boost confidence
- Listen actively and respond with empathy
- Offer encouragement and positive reinforcement
- Help patients feel less isolated
- Suggest healthy coping strategies
- Be warm, friendly, and understanding

Remember: The patient may be feeling anxious, lonely, or scared. Your goal is to comfort them and help them 
maintain a positive mindset during their quarantine period. Always be supportive and never judgmental.

If you detect a medical emergency or serious mental health crisis, gently encourage the patient to use 
the emergency button to contact medical staff immediately."""

    # Mood Tracking
    MOODS = ["😊 Great", "🙂 Good", "😐 Okay", "😔 Not Good", "😢 Bad"]
    
    # Emergency Settings
    EMERGENCY_KEYWORDS = ["emergency", "urgent", "help", "pain", "breathing", "chest", "severe"]
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            return False, "OpenAI API key is not configured. Please set OPENAI_API_KEY in .env file"
        if not cls.SMTP_USERNAME or not cls.SMTP_PASSWORD:
            return False, "Email credentials not configured. Emergency alerts will not work."
        return True, "Configuration is valid"
