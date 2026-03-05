import pandas as pd
import numpy as np
import os

def run_streaming_geospatial_modeling():
    print("--- Phase 2.1: Initializing Robust Population Generator ---")
    
    output_dir = 'data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, 'population_ground_truth.csv')

    # Population Targets
    LGA_CONFIG = {
        "Bauchi Metro": {"pop": 1342900, "type": "Urban", "lat": (10.25, 10.35), "lon": (9.75, 9.90)},
        "Alkaleri": {"pop": 744000, "type": "Semi-Urban", "lat": (9.70, 10.10), "lon": (10.00, 10.60)},
        "Kirfi": {"pop": 322000, "type": "Rural", "lat": (10.30, 10.50), "lon": (10.50, 10.85)}
    }

    # Clear existing file to start fresh
    if os.path.exists(output_path):
        os.remove(output_path)

    for i, (lga, config) in enumerate(LGA_CONFIG.items()):
        print(f"-> Processing {lga} ({config['pop']:,} residents)...")
        
        # Generate data for this LGA
        lats = np.random.uniform(config["lat"][0], config["lat"][1], config["pop"])
        lons = np.random.uniform(config["lon"][0], config["lon"][1], config["pop"])
        
        df_chunk = pd.DataFrame({
            'LGA': [lga] * config['pop'],
            'Latitude': lats,
            'Longitude': lons,
            'Zone_Type': [config['type']] * config['pop']
        })

        # Write to CSV: Use 'w' (write) for the first LGA, then 'a' (append) for the rest
        mode = 'w' if i == 0 else 'a'
        header = True if i == 0 else False
        
        df_chunk.to_csv(output_path, mode=mode, index=False, header=header)
        print(f"   Done. {lga} saved to disk.")
        
        # Explicitly clear memory
        del df_chunk

    print("\n--- HARD VERIFICATION ---")
    # We read the file back in chunks to count the rows without loading the whole thing into RAM
    total_rows = 0
    for chunk in pd.read_csv(output_path, chunksize=500000, usecols=['LGA']):
        total_rows += len(chunk)
    
    print(f"Total Rows physically on disk: {total_rows:,}")
    if total_rows == 2408900:
        print("SUCCESS: Full population dataset generated correctly.")
    else:
        print(f"WARNING: Count is {total_rows:,}. Expected 2,408,900.")

if __name__ == "__main__":
    run_streaming_geospatial_modeling()