# Quarantine Assistant Robot 🏥

A compassionate AI-powered Streamlit application designed to support patients during quarantine with emotional support, emergency alerts, and wellness tracking.

## Features

### 💬 AI Chat Support
- Empathetic conversational AI powered by OpenAI GPT
- 24/7 emotional support and companionship
- Context-aware responses with conversation memory
- Crisis keyword detection

### 🚨 Emergency Alert System
- One-click emergency button
- Instant email notifications to medical staff
- Emergency message logging and history
- Configurable alert recipients

### 📊 Wellness Tracking
- Daily mood logging with emojis
- Interactive mood trend visualization
- Mood statistics and trend analysis
- Progress tracking over time

### 🎯 Activity Suggestions
- Categorized activities (meditation, physical, mental, creative, entertainment)
- Daily activity plan generator
- Detailed instructions and benefits for each activity
- Multiple options for different preferences

### 💪 Motivational Content
- Daily inspirational quotes
- Success stories from recovered patients
- Positive affirmations
- Calming activity suggestions

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Gmail account with app password (for emergency alerts)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd /home/ubuntu/ai_ml_luminar/qr_assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SMTP_USERNAME=your_email@gmail.com
   SMTP_PASSWORD=your_gmail_app_password
   ALERT_EMAIL=jusainajusu8086@gmail.com
   ```

4. **Get your OpenAI API Key**
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Add it to your `.env` file

5. **Setup Gmail App Password**
   - Go to your Google Account settings
   - Enable 2-factor authentication
   - Generate an app-specific password
   - Use this password in your `.env` file

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### First Time Setup

1. Enter your name when prompted
2. Click "Start" to begin
3. Explore the different tabs:
   - **Chat Support**: Talk to the AI companion
   - **Emergency**: Send urgent alerts
   - **Wellness Tracker**: Log your mood
   - **Activities**: Get activity suggestions
   - **Motivation**: Read inspirational content

### Using Emergency Alerts

1. Navigate to the "🚨 Emergency" tab
2. Describe your emergency in the text area
3. Click "🚨 SEND ALERT"
4. Medical staff will receive an email immediately

## Configuration

All configuration is managed through the `.env` file and `config.py`:

- **OPENAI_API_KEY**: Your OpenAI API key
- **OPENAI_MODEL**: AI model to use (default: gpt-3.5-turbo)
- **SMTP_SERVER**: Email server (default: smtp.gmail.com)
- **SMTP_PORT**: Email port (default: 587)
- **SMTP_USERNAME**: Your email address
- **SMTP_PASSWORD**: Your email app password
- **ALERT_EMAIL**: Email address to receive emergency alerts

## Project Structure

```
qr_assistant/
├── app.py                      # Main Streamlit application
├── chatbot.py                  # AI chatbot logic
├── emergency_handler.py        # Emergency alert system
├── wellness_tracker.py         # Mood and wellness tracking
├── activities.py               # Activity suggestions
├── motivational_content.py     # Quotes and inspiration
├── config.py                   # Configuration management
├── styles.css                  # Custom CSS styling
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## Troubleshooting

### OpenAI API Errors
- Ensure your API key is valid and has credits
- Check that you're using the correct model name
- Verify your internet connection

### Email Not Sending
- Confirm SMTP credentials are correct
- Make sure you're using an app password (not your regular password)
- Check that 2-factor authentication is enabled on Gmail
- Verify the recipient email address

### Module Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct directory

## Support

For issues or questions:
- Check the configuration in `.env`
- Review error messages in the Streamlit interface
- Ensure all required services (OpenAI, Gmail) are accessible

## Privacy & Security

- **API Keys**: Never commit your `.env` file to version control
- **Email**: Emergency messages are sent via secure SMTP
- **Data**: Mood and chat data are stored only in your session (not persisted)
- **AI**: Conversations are sent to OpenAI API (review their privacy policy)

## Future Enhancements

- Symptom tracking integration
- Medication reminders
- Family connection features
- Video call integration
- Multi-language support
- Mobile app version

---

**Built with ❤️ for quarantine support**

*Remember: You're stronger than you think, and you're not alone in this journey!*
