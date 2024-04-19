import pandas as pd
import folium

# Read the CSV file
df = pd.read_csv('combined_csv.csv')

# Create a map centered on the mean latitude and longitude of the dropoff coordinates
map_center = [df['dropoff_centroid_latitude_y'].mean(), df['dropoff_centroid_longitude_y'].mean()]
heatmap = folium.Map(location=map_center, zoom_start=10)

# Add heatmap layers for dropoff and pickup coordinates
dropoff_data = [[row['dropoff_centroid_latitude_y'], row['dropoff_centroid_longitude_y']] for index, row in df.iterrows()]
pickup_data = [[row['pickup_centroid_latitude_y'], row['pickup_centroid_longitude_y']] for index, row in df.iterrows()]

folium.plugins.HeatMap(dropoff_data, name='Dropoff Heatmap').add_to(heatmap)
folium.plugins.HeatMap(pickup_data, name='Pickup Heatmap').add_to(heatmap)

# Add layer control to toggle between heatmaps
folium.LayerControl().add_to(heatmap)

# Save the map as an HTML file
heatmap.save('heatmap.html')