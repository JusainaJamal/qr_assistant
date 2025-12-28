import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import Config

class EmergencyHandler:
    """Handle emergency alerts and notifications"""
    
    def __init__(self):
        self.emergency_log = []
    
    def send_email_alert(self, patient_name, emergency_message):
        """
        Send emergency alert via email
        
        Args:
            patient_name (str): Name of the patient
            emergency_message (str): The emergency message from the patient
            
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = Config.SMTP_USERNAME
            msg['To'] = Config.ALERT_EMAIL
            msg['Subject'] = f'🚨 EMERGENCY ALERT - Patient: {patient_name}'
            
            # Email body
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            body = f"""
EMERGENCY ALERT - IMMEDIATE ATTENTION REQUIRED

Patient Name: {patient_name}
Time: {timestamp}
Status: EMERGENCY BUTTON ACTIVATED

Patient's Message:
{emergency_message}

---
This is an automated alert from the Quarantine Assistant System.
Please respond to this emergency immediately.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
            server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            # Log the emergency
            self.log_emergency(patient_name, emergency_message, timestamp)
            
            return True, "Emergency alert sent successfully!"
            
        except smtplib.SMTPAuthenticationError:
            return False, "Email authentication failed. Please check SMTP credentials in .env file."
        except smtplib.SMTPException as e:
            return False, f"Failed to send email: {str(e)}"
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
    
    def log_emergency(self, patient_name, message, timestamp):
        """
        Log emergency for record keeping
        
        Args:
            patient_name (str): Name of the patient
            message (str): Emergency message
            timestamp (str): Timestamp of the emergency
        """
        self.emergency_log.append({
            "patient": patient_name,
            "message": message,
            "timestamp": timestamp
        })
    
    def get_emergency_count(self):
        """Get the total number of emergencies logged"""
        return len(self.emergency_log)
    
    def get_last_emergency(self):
        """Get the most recent emergency"""
        if self.emergency_log:
            return self.emergency_log[-1]
        return None
