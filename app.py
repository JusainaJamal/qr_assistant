import streamlit as st
from chatbot import QuarantineChatbot
from emergency_handler import EmergencyHandler
from wellness_tracker import WellnessTracker
from activities import ActivitiesSuggester
from motivational_content import MotivationalContent
from config import Config
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Quarantine Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    load_css()
except FileNotFoundError:
    pass  # CSS file not found, use default styling

# Initialize session state
def initialize_session_state():
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = QuarantineChatbot()
    if 'emergency_handler' not in st.session_state:
        st.session_state.emergency_handler = EmergencyHandler()
    if 'wellness_tracker' not in st.session_state:
        st.session_state.wellness_tracker = WellnessTracker()
    if 'activities' not in st.session_state:
        st.session_state.activities = ActivitiesSuggester()
    if 'motivational' not in st.session_state:
        st.session_state.motivational = MotivationalContent()
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    if 'patient_name' not in st.session_state:
        st.session_state.patient_name = Config.PATIENT_NAME
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'show_emergency_modal' not in st.session_state:
        st.session_state.show_emergency_modal = False

initialize_session_state()

# Sidebar
with st.sidebar:
    st.title("🏥 Quarantine Assistant")
    
    # Patient name input
    if not st.session_state.initialized:
        st.session_state.patient_name = st.text_input(
            "What should I call you?", 
            value=Config.PATIENT_NAME,
            key="name_input"
        )
        if st.button("Start", type="primary"):
            st.session_state.initialized = True
            greeting = st.session_state.chatbot.get_greeting()
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": greeting
            })
            st.rerun()
    else:
        st.success(f"Welcome, {st.session_state.patient_name}! 👋")
        
        # Configuration status
        is_valid, msg = Config.validate()
        if is_valid:
            st.success("✅ System ready")
        else:
            st.warning(f"⚠️ {msg}")
        
        st.divider()
        
        # Quick stats
        st.subheader("Your Progress")
        mood_summary = st.session_state.wellness_tracker.get_mood_summary()
        st.metric("Mood Entries", mood_summary["total_entries"])
        st.metric("Current Trend", mood_summary["trend"])
        
        st.divider()
        
        # Daily quote
        st.subheader("💫 Daily Inspiration")
        daily_quote = st.session_state.motivational.get_daily_quote()
        st.info(daily_quote)

# Main content
if not st.session_state.initialized:
    # Welcome screen
    st.title("🏥 Welcome to Your Quarantine Assistant")
    st.markdown("""
    ### Your Digital Companion During Quarantine
    
    I'm here to support you through your quarantine journey. Here's how I can help:
    
    - 💬 **Chat Support**: Talk to me anytime. I'm here to listen and provide emotional support
    - 🚨 **Emergency Alerts**: Quick access to medical staff when you need urgent help
    - 📊 **Wellness Tracking**: Monitor your mood and emotional wellbeing
    - 🎯 **Activity Suggestions**: Stay engaged with exercises, games, and creative activities
    - 💪 **Motivation**: Daily quotes and success stories to keep your spirits high
    
    **You're not alone in this. Let's get through it together!**
    
    👈 Please enter your name in the sidebar to begin.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 💪 Stay Strong")
        st.write("Your resilience will see you through this.")
    with col2:
        st.markdown("### 😊 Stay Positive")
        st.write("Every day is progress toward recovery.")
    with col3:
        st.markdown("### 🤝 Stay Connected")
        st.write("We're here with you every step of the way.")

else:
    # Chat input must be outside tabs in Streamlit 1.29.0
    # Store the active tab in session state
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "💬 Chat Support"
    
    # Main application tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "💬 Chat Support", 
        "🚨 Emergency", 
        "📊 Wellness Tracker", 
        "🎯 Activities", 
        "💪 Motivation"
    ])
    
    # Tab 1: Chat Support
    with tab1:
        st.header("💬 Talk to Your AI Companion")
        st.markdown("*I'm here to listen and support you. Share what's on your mind.*")
        
        # Display chat messages
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    # Tab 2: Emergency
    with tab2:
        st.header("🚨 Emergency Alert System")
        
        st.warning("**Use this only for urgent situations that require immediate medical attention.**")
        
        st.markdown("""
        ### When to use this:
        - Severe symptoms (difficulty breathing, chest pain, etc.)
        - Medical emergencies
        - Urgent mental health crisis
        - Any situation requiring immediate help
        
        Your message will be sent to medical staff at: **{}**
        """.format(Config.ALERT_EMAIL))
        
        emergency_message = st.text_area(
            "Describe your emergency:",
            placeholder="I need help with...",
            height=150
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🚨 SEND ALERT", type="primary", use_container_width=True):
                if emergency_message.strip():
                    with st.spinner("Sending emergency alert..."):
                        success, msg = st.session_state.emergency_handler.send_email_alert(
                            st.session_state.patient_name,
                            emergency_message
                        )
                        
                        if success:
                            st.success("✅ " + msg)
                            st.success("Medical staff has been notified. Help is on the way!")
                        else:
                            st.error("❌ " + msg)
                            st.error("Please try again or use alternative contact methods.")
                else:
                    st.error("Please describe your emergency before sending.")
        
        st.divider()
        
        # Emergency history
        if st.session_state.emergency_handler.get_emergency_count() > 0:
            st.subheader("Alert History")
            last_emergency = st.session_state.emergency_handler.get_last_emergency()
            if last_emergency:
                st.info(f"**Last Alert**: {last_emergency['timestamp']}")
                st.text(f"Message: {last_emergency['message']}")
    
    # Tab 3: Wellness Tracker
    with tab3:
        st.header("📊 Wellness & Mood Tracker")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("How are you feeling?")
            
            selected_mood = st.select_slider(
                "Rate your mood:",
                options=Config.MOODS,
                value=Config.MOODS[2]
            )
            
            mood_notes = st.text_area(
                "Any notes about how you're feeling?",
                placeholder="Optional: What's affecting your mood today?",
                height=100
            )
            
            if st.button("Log Mood", type="primary"):
                st.session_state.wellness_tracker.log_mood(selected_mood, mood_notes)
                st.success("Mood logged! 💚")
                st.rerun()
            
            st.divider()
            
            # Mood summary
            summary = st.session_state.wellness_tracker.get_mood_summary()
            st.metric("Total Entries", summary["total_entries"])
            st.metric("Average Mood", summary["average_mood"])
            st.metric("Trend", summary["trend"])
        
        with col2:
            st.subheader("Your Mood Journey")
            
            mood_chart = st.session_state.wellness_tracker.create_mood_chart()
            if mood_chart:
                st.plotly_chart(mood_chart, use_container_width=True)
            else:
                st.info("Start logging your mood to see trends here! 📈")
                st.markdown("""
                **Tips for Tracking Mood:**
                - Log at least once a day
                - Be honest with yourself
                - Notice patterns over time
                - Celebrate improvement!
                """)
    
    # Tab 4: Activities
    with tab4:
        st.header("🎯 Activity Suggestions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Daily Activity Plan")
            if st.button("Generate Today's Plan", type="primary"):
                plan = st.session_state.activities.get_daily_activity_plan()
                st.session_state.daily_plan = plan
            
            if 'daily_plan' in st.session_state:
                for item in st.session_state.daily_plan:
                    with st.expander(f"{item['time']} - {item['activity']['name']}"):
                        st.write(f"**Duration:** {item['activity']['duration']}")
                        st.write(f"**What to do:** {item['activity']['description']}")
                        st.write(f"**Benefits:** {item['activity']['benefits']}")
        
        with col2:
            st.subheader("Browse by Category")
            
            category = st.selectbox(
                "Choose activity type:",
                ["meditation", "physical", "mental", "entertainment", "creative"]
            )
            
            activities = st.session_state.activities.get_activities_by_category(category)
            
            for activity in activities:
                with st.expander(f"{activity['name']}"):
                    st.write(f"**Duration:** {activity['duration']}")
                    st.write(f"**Description:** {activity['description']}")
                    st.write(f"**Benefits:** {activity['benefits']}")
    
    # Tab 5: Motivation
    with tab5:
        st.header("💪 Motivation & Inspiration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌟 Inspirational Quote")
            if st.button("Get New Quote"):
                quote = st.session_state.motivational.get_random_quote()
                st.session_state.current_quote = quote
            
            if 'current_quote' in st.session_state:
                st.success(st.session_state.current_quote)
            else:
                st.success(st.session_state.motivational.get_daily_quote())
            
            st.divider()
            
            st.subheader("💭 Daily Affirmation")
            affirmation = st.session_state.motivational.get_affirmation()
            st.info(f"*{affirmation}*")
        
        with col2:
            st.subheader("📖 Success Story")
            story = st.session_state.motivational.get_success_story()
            
            st.markdown(f"### {story['title']}")
            st.write(story['story'])
            st.success(f"**Lesson:** {story['lesson']}")
            
            if st.button("Read Another Story"):
                st.rerun()
        
        st.divider()
        
        st.subheader("🧘 Calming Activities")
        calming = st.session_state.motivational.get_calming_activity()
        
        with st.expander(f"Try: {calming['name']}", expanded=True):
            st.write(calming['description'])
            st.info(f"**Benefit:** {calming['benefit']}")

# Chat input must be at the top level (outside all tabs, columns, sidebar, forms, expanders)
if st.session_state.initialized:
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Display user message
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Check for crisis keywords
        if st.session_state.chatbot.detect_crisis(user_input):
            crisis_response = "I notice you might be experiencing something serious. If this is a medical emergency, please click the 🚨 Emergency tab and send an alert to medical staff immediately. I'm here to support you, but medical professionals can provide the urgent care you may need."
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": crisis_response
            })
        
        # Get AI response
        response = st.session_state.chatbot.get_response(user_input)
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": response
        })
        
        st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>💚 Remember: You're doing great. One day at a time. 💚</p>
    <p style='font-size: 12px;'>Quarantine Assistant Robot - Here for you 24/7</p>
</div>
""", unsafe_allow_html=True)
