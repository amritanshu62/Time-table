from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account .json key file
SERVICE_ACCOUNT_FILE = '/Users/amritanshurana/Desktop/Bot/whats-app-bot-439416-426d5a725eed.json'

# Define the scopes (Google Sheets)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Authenticate and build the service
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# The ID of your spreadsheet
SPREADSHEET_ID = '1tRsKB7hMItmtXaSA0ybOcfX-o-bGsKxlsA6KaVPTVD4'  # Replace with your actual Spreadsheet ID

# Date ranges based on your data
date_ranges = {
  
  
    'Tuesday, October 15, 2024': 'A5:A9',
    'Wednesday, October 16, 2024': 'A10:A14',
    'Thursday, October 17, 2024': 'A15:A20',
    'Friday, October 18, 2024': 'A21:A26',
    'Saturday, October 19, 2024': 'A27:A28',
    'Sunday, October 20, 2024': 'A29:A30',
    'Monday, October 21, 2024': 'A31:A36',
    'Tuesday, October 22, 2024': 'A37:A41',
    'Wednesday, October 23, 2024': 'A42:A46',
    'Thursday, October 24, 2024': 'A47:A51',
    'Friday, October 25, 2024': 'A52:A58',
    'Saturday, October 26, 2024': 'A59:A63',
    'Sunday, October 27, 2024': 'A64:A68',
    'Monday, October 28, 2024': 'A69:A74',
    'Tuesday, October 29, 2024': 'A75:A80',
    'Wednesday, October 30, 2024': 'A81:A86',
    'Thursday, October 31, 2024': 'A87:A89',
    'Friday, November 1, 2024': 'A90:A96',
    'Saturday, November 2, 2024': 'A97:A101',
    'Sunday, November 3, 2024': 'A102:A106',
    'Monday, November 4, 2024': 'A107:A112',
    'Tuesday, November 5, 2024': 'A113:A118',
    'Wednesday, November 6, 2024': 'A119:A124',
    'Thursday, November 7, 2024': 'A125:A131',
    'Friday, November 8, 2024': 'A132:A132',
    'Saturday, November 9, 2024': 'A133:A133',
    'Sunday, November 10, 2024': 'A134:A134',
    'Monday, November 11, 2024': 'A135:A141',
    'Tuesday, November 12, 2024': 'A142:A146',
    'Wednesday, November 13, 2024': 'A147:A151',
    'Thursday, November 14, 2024': 'A152:A156',
    'Friday, November 15, 2024': 'A157:A161',
    'Saturday, November 16, 2024': 'A162:A166',
    'Sunday, November 17, 2024': 'A167:A171',
    'Monday, November 18, 2024': 'A172:A177',
    'Tuesday, November 19, 2024': 'A178:A183',
    'Wednesday, November 20, 2024': 'A184:A188',
    'Thursday, November 21, 2024': 'A189:A195',
    'Friday, November 22, 2024': 'A196:A202',
    'Saturday, November 23, 2024': 'A203:A207',
    'Sunday, November 24, 2024': 'A208:A212',
    'Monday, November 25, 2024': 'A213:A218',
    'Tuesday, November 26, 2024': 'A219:A219',
    'Wednesday, November 27, 2024': 'A220:A220',
    'Thursday, November 28, 2024': 'A221:A221',
    'Friday, November 29, 2024': 'A222:A222',
    'Saturday, November 30, 2024': 'A223:A229',
    'Sunday, December 1, 2024': 'A230:A234',
    'Monday, December 2, 2024': 'A235:A240',
    'Tuesday, December 3, 2024': 'A241:A246',
    'Wednesday, December 4, 2024': 'A247:A251',
    'Thursday, December 5, 2024': 'A252:A256',
    'Friday, December 6, 2024': 'A257:A263',
    'Saturday, December 7, 2024': 'A264:A268',
    'Sunday, December 8, 2024': 'A269:A273',
    'Monday, December 9, 2024': 'A274:A279',
    'Tuesday, December 10, 2024': 'A280:A285',
    'Wednesday, December 11, 2024': 'A286:A290',
    'Thursday, December 12, 2024': 'A291:A295',
    'Friday, December 13, 2024': 'A296:A302',
    'Saturday, December 14, 2024': 'A303:A307',
    'Sunday, December 15, 2024': 'A308:A312',
    'Monday, December 16, 2024': 'A313:A318',
    'Tuesday, December 17, 2024': 'A319:A324',
    'Wednesday, December 18, 2024': 'A325:A329',
    'Thursday, December 19, 2024': 'A330:A334',
    'Friday, December 20, 2024': 'A335:A339',
    'Saturday, December 21, 2024': 'A340:A344',
    'Sunday, December 22, 2024': 'A345:A349',
    'Monday, December 23, 2024': 'A350:A355',
    'Tuesday, December 24, 2024': 'A356:A361',
    'Wednesday, December 25, 2024': 'A362:A364',
    'Thursday, December 26, 2024': 'A365:A369',
    'Friday, December 27, 2024': 'A370:A376',
    'Saturday, December 28, 2024': 'A377:A381',
    'Sunday, December 29, 2024': 'A382:A386',
    'Monday, December 30, 2024': 'A387:A392',
    'Tuesday, December 31, 2024': 'A393:A397',
    'Wednesday, January 1, 2025': 'A398:A402',
    'Thursday, January 2, 2025': 'A403:A407',
    'Friday, January 3, 2025': 'A408:A412',
    'Saturday, January 4, 2025': 'A413:A413',
    'Sunday, January 5, 2025': 'A414:A414',
    'Monday, January 6, 2025': 'A415:A415',
    'Tuesday, January 7, 2025': 'A416:A416',
    'Wednesday, January 8, 2025': 'A417:A417'

  
}

# Function to get timetable for a specific date and section
def get_timetable(selected_date, section_column):
    # Get the cell range for the selected date from date_ranges dictionary
    date_range = date_ranges.get(selected_date)
    
    if not date_range:
        return 'Invalid date or date not found in the timetable.'
    
    # Call the Sheets API with the correct range and section column
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'Sheet1!{section_column}{date_range}').execute()
        
        # Extract values from the response
        rows = result.get('values', [])
        
        # Return the formatted timetable or a message if no data found
        return rows if rows else 'No data found for the given date and section.'
    
    except Exception as e:
        return f'An error occurred: {e}'




# Function to format the timetable data for display
def format_timetable(rows):
    if not rows:
        return 'No classes found for the given date and section.'

    formatted_timetable = ''
    
    # Time slots corresponding to the row data
    time_slots = [
        "09.15 – 10.30",
        "10.45 – 12.00",
        "12.15 – 13.30",
        "13.30 – 14.30",  # LUNCH BREAK or No Class
        "14.30 – 15.45",
        "16.00 – 17.15",
        "17.30 – 18.45",
    ]

    # Debugging: Print the raw data received
    print(f"Raw data received from Google Sheets: {rows}")

    # Iterate over the rows and format them properly
    for index, row in enumerate(rows):
        # Ensure there's a matching time slot and row has at least 2 columns for class name
        if index < len(time_slots):
            time_slot = time_slots[index]
            # Check if the row has enough columns to get the class name, otherwise default to "No Class"
            class_name = row[0] if len(row) > 0 else "No Class"
            formatted_timetable += f"{time_slot} - {class_name}\n"
    
    return formatted_timetable


# Function to get timetable for a specific date and section
def get_timetable(selected_date, section_column):
    # Get the cell range for the selected date from date_ranges dictionary
    date_range = date_ranges.get(selected_date)
    
    if not date_range:
        return 'Invalid date or date not found in the timetable.'

    # Extract the numeric row range from the 'A5:A9' string (e.g., 'A5:A9' -> '5:9')
    row_range = date_range.replace('A', '')  # Remove 'A' but keep the row range intact

    # Create the correct range using section_column and row_range
    full_range = f'{section_column}{row_range}'  # Example: 'C5:C9' for Section A

    # Debugging statement to print the constructed range
    print(f"Fetching data for range: {full_range}")

    # Call the Sheets API with the correct range
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'Sheet1!{full_range}').execute()

        # Extract values from the response
        rows = result.get('values', [])

        # Return the formatted timetable or a message if no data found
        return format_timetable(rows)
    
    except Exception as e:
        return f'An error occurred: {e}'

# Example usage
selected_date = 'Wednesday, October 23, 2024'  # Change this to the desired date
section_column = 'D'  # Column for Section B

timetable = get_timetable(selected_date, section_column)
print(f'Timetable for {selected_date}, Section B: {timetable}')