import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('lyfts_dropoff_campus.csv', low_memory=False)
df1 = pd.read_csv('lyfts_pickup_from_campus.csv', low_memory=False)

# Convert coordinates to floats and handle errors
df['dropoff_centroid_latitude'] = pd.to_numeric(df['dropoff_centroid_latitude'], errors='coerce')
df['dropoff_centroid_longitude'] = pd.to_numeric(df['dropoff_centroid_longitude'], errors='coerce')
df1['pickup_centroid_latitude'] = pd.to_numeric(df1['pickup_centroid_latitude'], errors='coerce')
df1['pickup_centroid_longitude'] = pd.to_numeric(df1['pickup_centroid_longitude'], errors='coerce')

# Drop rows with NaN values in coordinates
df.dropna(subset=['dropoff_centroid_latitude', 'dropoff_centroid_longitude'], inplace=True)
df1.dropna(subset=['pickup_centroid_latitude', 'pickup_centroid_longitude'], inplace=True)

# Combine datasets with a type label
df['type'] = 'Drop-off'
df1['type'] = 'Pick-up'
combined_df = pd.concat([df, df1], ignore_index=True)

# Ensure all latitude and longitude data are floats
combined_df['dropoff_centroid_latitude'] = combined_df['dropoff_centroid_latitude'].astype(float)
combined_df['dropoff_centroid_longitude'] = combined_df['dropoff_centroid_longitude'].astype(float)

# Check data types (debugging step)
print(combined_df.dtypes)

# Create the scatter map
fig = px.scatter_mapbox(combined_df, lat='dropoff_centroid_latitude', lon='dropoff_centroid_longitude',
                        color='type', size_max=15, zoom=10,
                        mapbox_style="open-street-map", title="Lyft Campus Rides")

# Display the map
fig.show()
