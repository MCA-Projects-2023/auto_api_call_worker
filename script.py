import schedule
import time
import requests

# Array of websites to call
websites = [
    'https://annarestro-server.onrender.com',
    'https://baithak-video-conference-app.onrender.com',
    'https://vibe-backend-83cg.onrender.com',
    # Add more URLs as needed
]

# Function to call each website in the array
def call_websites():
    for website in websites:
        try:
            response = requests.get(website)
            print(f'Successfully called {website}: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error calling {website}: {e}')

# Schedule the function to run every 15 minutes
schedule.every(15).minutes.do(call_websites)

# Call the websites immediately on script start
call_websites()

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
