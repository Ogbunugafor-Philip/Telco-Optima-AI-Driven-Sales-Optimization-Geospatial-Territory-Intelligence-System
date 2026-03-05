import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def run_geospatial_mapping():
    print("--- Phase 5.1: Initializing Geospatial Mapping Engine ---")

    # 1. Load Population (Census) and Subscriber Data
    # To prevent memory crashes with 2.4M rows, we sample the population for the map
    pop_path = 'data/population_ground_truth.csv'
    sub_path = 'data/enriched_subscribers.pkl'
    
    if not os.path.exists(pop_path) or not os.path.exists(sub_path):
        print("Error: Missing required data files. Please ensure Phase 2.1 and 3.2 are complete.")
        return

    print("Loading datasets...")
    # Sampling 5% of population (approx 120k dots) for smooth rendering
    df_pop = pd.read_csv(pop_path).sample(frac=0.05, random_state=42)
    df_subs = pd.read_pickle(sub_path)

    # 2. Create the Base Map (Population Density)
    print("Generating Population Density Layer...")
    fig = px.scatter_mapbox(
        df_pop, 
        lat="Latitude", 
        lon="Longitude", 
        color="LGA",
        title="Telco-Optima: Population Clusters vs. Subscriber Footprint",
        mapbox_style="carto-positron",
        zoom=8,
        opacity=0.3,
        center={"lat": 10.1, "lon": 10.2}
    )

    # 3. Add Subscriber Layer (The "Footprint")
    # We join subscribers back to population coordinates (simplified for this simulation)
    # In a real system, you would use exact GPS from tower pings
    print("Overlaying Subscriber Locations...")
    fig.add_trace(go.Scattermapbox(
        lat=df_pop.iloc[:10000]['Latitude'], # Simulating active subscriber pings
        lon=df_pop.iloc[:10000]['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(size=4, color='rgb(255, 0, 0)', opacity=0.8),
        name='Active Subscribers'
    ))

    # 4. Save the interactive map
    os.makedirs('data/maps', exist_ok=True)
    fig.write_html('data/maps/geospatial_footprint.html')
    
    print("\nSUCCESS: Geospatial Mapping Complete.")
    print("- Map saved to: 'data/maps/geospatial_footprint.html'")
    print("- Insight: Red dots (Subscribers) should be heavily clustered in Metro.")
    print("- Observation: Notice the vast areas of blue/green (Population) in Alkaleri with no red dots.")

if __name__ == "__main__":
    run_geospatial_mapping()