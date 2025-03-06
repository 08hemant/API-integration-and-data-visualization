import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Key and Endpoint
api_key = 'YOUR_API_KEY'
city = 'Bhopal'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

# Fetch data from API
response = requests.get(url)
data = response.json()

# Parse data
weather_data = []
for entry in data['list']:
    weather_data.append({
        'date': entry['dt_txt'],
        'temperature': entry['main']['temp']
    })

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Plot data
plt.figure(filesize=(10, 5))
plt.plot(df['date'], df['temperature'], marker='o')
plt.title(f'Temperature Trend in {city}')
plt.label('Date')
plt.label('Temperature (°C)')
plt.ticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
