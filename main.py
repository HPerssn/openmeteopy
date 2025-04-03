from openmeteopy import OpenMeteo
from openmeteopy.hourly import HourlyHistorical
from openmeteopy.options import HistoricalOptions

longitude = 62.390156
latitude = 17.22922

print("Longitude: ", longitude)
print("Latitude: ", latitude)

# Initialize HourlyHistorical with the desired parameters
hourly = HourlyHistorical()
hourly_params = hourly.surface_pressure()
# Create HistoricalOptions with the specified start and end dates
options = HistoricalOptions(latitude,
                            longitude, 
                            start_date="2005-01-01",
                            end_date="2023-12-31")

print("Options created:", options)

# Initialize OpenMeteo manager
mgr = OpenMeteo(options, hourly_params)

# Download data with error handling
try:
    print("Downloading data...")
    meteo = mgr.save_csv('/Users/henrikpersson/Documents/GitHub/openmeteopy/data.csv')
    print("Data saved to /Users/henrikpersson/Documents/GitHub/openmeteopy/data.csv")
    print("Downloaded data:", meteo)
except Exception as e:
    print(f"An error occurred: {e}")