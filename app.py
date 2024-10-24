from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import BOT  # Import your timetable code
from datetime import datetime, timedelta

app = Flask(__name__)

# Dictionary to hold user states
user_states = {}

# Section column mapping
section_column_map = {
    'A': 'C',  # Section A is in Column C
    'B': 'D',  # Section B is in Column D
    'C': 'E',
    'D': 'F',
    'E': 'G',
    'F': 'H',
    'G': 'I',
    'H': 'J'
}

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()  # Get user's WhatsApp message
    user_number = request.values.get('From')  # Get the user's phone number (unique identifier)
    response = MessagingResponse()  # Create a response object
    msg = response.message()

    # Initialize user state if it's the first time they're interacting
    if user_number not in user_states:
        user_states[user_number] = {'step': 'start'}

    # Get current user state
    user_state = user_states[user_number]['step']

    # Start of the conversation (any message will trigger the bot)
    if user_state == 'start':
        msg.body("Please enter your section (e.g., A, B, C):")
        user_states[user_number]['step'] = 'awaiting_section'
        return str(response)

    # Waiting for the section input
    elif user_state == 'awaiting_section':
        section = incoming_msg.upper()  # Convert any input to uppercase (e.g., 'a' becomes 'A')
        if section in section_column_map:
            user_states[user_number]['section'] = section
            user_states[user_number]['section_column'] = section_column_map[section]  # Save the correct column

            msg.body(f"Got it! You are in Section {section}. \nWhen would you like the timetable for?\nPress 1 for today.\nPress 2 for tomorrow.\nPress 3 for day after tomorrow.")
            user_states[user_number]['step'] = 'awaiting_date_choice'
            return str(response)
        else:
            msg.body("Invalid section. Please enter a valid section (A, B, C, D, etc.).")
            return str(response)

    # Waiting for date input (today, tomorrow, or day after tomorrow)
    elif user_state == 'awaiting_date_choice':
        if incoming_msg in ['1', '2', '3']:
            section = user_states[user_number]['section']
            section_column = user_states[user_number]['section_column']  # Use the correct column from the saved state

            # Calculate the date based on the choice
            if incoming_msg == '1':
                date_choice = datetime.now().strftime('%A, %B %d, %Y')
            elif incoming_msg == '2':
                date_choice = (datetime.now() + timedelta(days=1)).strftime('%A, %B %d, %Y')
            else:  # 3 for day after tomorrow
                date_choice = (datetime.now() + timedelta(days=2)).strftime('%A, %B %d, %Y')

            # Fetch the timetable from BOT.py based on section and date
            timetable = BOT.get_timetable(date_choice, section_column)  # Pass the correct column dynamically
            msg.body(f"Timetable for {date_choice}, Section {section}: \n{timetable}")
            msg.body("\nAre you satisfied? (Y/N)")
            user_states[user_number]['step'] = 'satisfaction_check'
            return str(response)
        else:
            msg.body("Please press 1 for today, 2 for tomorrow, or 3 for day after tomorrow.")
        return str(response)

    # Checking user satisfaction
    elif user_state == 'satisfaction_check':
        if incoming_msg == 'y':
            msg.body("Thank you! If you need the timetable again, just message me!")
            user_states[user_number]['step'] = 'start'
        elif incoming_msg == 'n':
            msg.body("Press 1 to see the timetable for a different day for the same section.\nPress 2 to choose a different section.")
            user_states[user_number]['step'] = 'choose_next_action'
        else:
            msg.body("Please reply with Y for yes or N for no.")
        return str(response)

    # Choosing whether to stay in the same section or select a new one
    elif user_state == 'choose_next_action':
        if incoming_msg == '1':
            msg.body(f"When would you like the timetable for?\nPress 1 for today.\nPress 2 for tomorrow.\nPress 3 for day after tomorrow.")
            user_states[user_number]['step'] = 'awaiting_date_choice'
        elif incoming_msg == '2':
            msg.body("Please enter your section (e.g., A, B, C):")
            user_states[user_number]['step'] = 'awaiting_section'
        else:
            msg.body("Please press 1 for a different day in the same section, or 2 for a different section.")
        return str(response)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)