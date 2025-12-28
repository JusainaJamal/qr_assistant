from openai import OpenAI
from config import Config
from datetime import datetime

class QuarantineChatbot:
    """AI-powered chatbot for providing emotional support to quarantine patients"""
    
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.conversation_history = []
        self.initialize_conversation()
    
    def initialize_conversation(self):
        """Initialize the conversation with the system prompt"""
        self.conversation_history = [
            {"role": "system", "content": Config.SYSTEM_PROMPT}
        ]
    
    def get_response(self, user_message):
        """
        Get a response from the AI chatbot
        
        Args:
            user_message (str): The message from the patient
            
        Returns:
            str: The AI's response
        """
        try:
            # Add user message to conversation history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=self.conversation_history,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            # Extract the assistant's reply
            assistant_message = response.choices[0].message.content
            
            # Add assistant's response to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Keep conversation history manageable (last 20 messages)
            if len(self.conversation_history) > 21:  # 1 system + 20 messages
                self.conversation_history = [self.conversation_history[0]] + self.conversation_history[-20:]
            
            return assistant_message
            
        except Exception as e:
            return f"I apologize, but I'm having trouble connecting right now. Please try again in a moment. If this is an emergency, please use the emergency button. Error: {str(e)}"
    
    def detect_crisis(self, message):
        """
        Detect if the message contains crisis keywords
        
        Args:
            message (str): The patient's message
            
        Returns:
            bool: True if crisis keywords are detected
        """
        message_lower = message.lower()
        for keyword in Config.EMERGENCY_KEYWORDS:
            if keyword in message_lower:
                return True
        return False
    
    def get_greeting(self):
        """Get a personalized greeting message"""
        current_hour = datetime.now().hour
        
        if current_hour < 12:
            time_greeting = "Good morning"
        elif current_hour < 17:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        return f"{time_greeting}! I'm here to keep you company and support you during your quarantine. How are you feeling today?"
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.initialize_conversation()
