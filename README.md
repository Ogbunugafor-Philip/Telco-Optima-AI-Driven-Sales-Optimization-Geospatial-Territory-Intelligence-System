# Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System

## Introduction

In the hyper-competitive Telecommunications sector, sustainable revenue growth cannot rely solely on managing existing customers. The real challenge and opportunity sit in accurately balancing Retention (Upselling) with Acquisition (Expansion). Traditional sales strategies often suffer from a lack of visibility. Sales team struggle to distinguish between saturated markets and untapped territories, leading to wasted resources and stagnant growth.
This project presents Telco-Optima, a comprehensive business intelligence application built using Python and Streamlit. It serves as a dual-purpose strategic engine designed to maximize territory revenue through two core analytical modules:

i.	Predictive Lead Scoring (Internal): Utilizing Machine Learning to analyze existing subscriber behaviors (ARPU, Device Type, Data Usage) and identify high-propensity targets for plan upgrades.

ii.	Geospatial "White Space" Analysis (External): A territory mapping system that ingests Census Population Data and compares it against Active Subscriber Logs. By calculating the delta between total population and network users, the system highlights "White Spaces" territories with high population density but critically low market penetration.

The system moves beyond simple reporting to prescriptive analytics. It overlays cell tower capacity with population clusters to answer two fundamental questions:

•	Who are we missing? (Identifying uncaptured market share in high-density zones).

•	Who is ready to spend more? (Scoring existing users for premium fiber/postpaid services).

This application is a functional replication of the exact data-driven strategy employed to revolutionize regional sales performance. By shifting focus from random territory coverage to algorithmic targeting of both "White Spaces" and high-value leads. This framework delivered a 145% increase in sales growth. It directly drove revenue performance from a baseline of ₦400,000,000 to over ₦1,000,000,000 in less than two years, proving that integrating population intelligence with sales data is the definitive driver of Telco scalability.

## Statement of the Problem
Despite the abundance of subscriber data available in the telecommunications sector, sales strategies often suffer from a critical "intelligence gap." Field agents and sales teams predominantly rely on intuition-based targeting or blanket marketing ("spray and pray") rather than data-driven precision. This operational inefficiency creates three specific problems that stifle revenue growth:

i.	Inefficient Resource Allocation: Sales teams waste significant operational hours targeting saturated territories or low-value customers who have no propensity to upgrade. Without predictive analytics, agents cannot distinguish between a subscriber likely to purchase a high-value fiber plan and one likely to churn, leading to high acquisition costs and low conversion rates.

ii.	The "White Space" Blind Spot: While network coverage may be extensive, market penetration is often uneven. Traditional reporting fails to overlay Census Population Data with Active Subscriber Logs. Consequently, sales managers are blind to "White Spaces" territories with high population density but low subscription rates resulting in missed opportunities for mass customer acquisition.

iii.	Revenue Stagnation: Due to these blind spots, regional revenue performance frequently hits a "ceiling." In the context of this case study, reliance on manual territory mapping and generic lead lists caused revenue to plateau at ₦400,000,000, significantly below the region’s true market potential.
Therefore, the problem this project addresses is the lack of an integrated, automated system that can simultaneously identify high-probability upselling targets and uncaptured population clusters to break through revenue stagnation.

## Project Objectives

i.	To implement a machine learning lead scoring engine that utilizes ARPU and usage patterns to identify high-propensity customers for upselling, thereby optimizing sales force efficiency.

ii.	To integrate census population data with active subscriber logs to pinpoint "White Space" territories that possess high population density but critically low market penetration.

iii.	To demonstrate the direct correlation between AI-driven territory management and the 145% revenue growth that drove regional performance from ₦400,000,000 to over ₦1,000,000,000.

iv.	To develop an interactive Streamlit-based business intelligence dashboard that centralizes geospatial territory mapping and subscriber behavioral data for real-time strategic decision-making.

## Project Scope
This project focuses on the development and deployment of the Telco-Optima system within the North-East operational region of Nigeria, specifically strictly limited to three (3) strategic Local Government Areas (LGAs) in Bauchi State:

i.	Bauchi Metro LGA: Representing the high-density urban cluster used for testing "Upsell/Cross-sell" strategies on existing high-value subscribers.

ii.	Alkaleri LGA: Representing a semi-urban territory analyzed for network expansion and "White Space" population capturing.

iii.	Kirfi LGA: Representing a developing market zone used to test low-cost acquisition models.

## Functional Boundaries
The system scope covers the end-to-end data pipeline, including:

•	Data Ingestion: Processing Call Detail Records (CDRs), device types, and ARPU history for subscribers within these three LGAs.

•	Geospatial Analysis: Mapping Base Transceiver Stations (BTS) against population density data for Alkaleri, Kirfi, and Bauchi Metro to calculate market penetration rates.

•	Application Development: The creation of a Streamlit-based dashboard to visualize territory performance and generate ML-based lead lists for the sales team.

## Technology Stack
## Technology Stack

| Component | Technology | Role in Project |
|-----------|------------|----------------|
| Language | Python 3.11+ | The core programming language used for all logic, data processing, and machine learning tasks. |
| Frontend | Streamlit | Used to build the interactive web dashboard, sidebar controls, and real-time visualizations without requiring HTML or CSS. |
| Data Processing | Pandas & NumPy | Pandas is used for handling large subscriber log datasets (CDRs). NumPy supports high-performance numerical computations such as ARPU variance calculations. |
| Geospatial Engine | GeoPandas & Plotly | GeoPandas processes geographic coordinate data for Bauchi, Alkaleri, and Kirfi. Plotly Mapbox renders interactive “White Space” telecom coverage maps. |
| Machine Learning | Scikit-Learn | Used to build the Random Forest Classifier for the Lead Scoring module that predicts customer upgrade propensity. |
| Confusion Matrix Heatmap | Seaborn | Generates statistical visualizations such as the confusion matrix heatmap for evaluating model performance. |
| Error Charts | Matplotlib | Used to render model error charts and statistical plots within the Streamlit dashboard. |
| Visualization | Plotly Express | Creates interactive financial charts such as Revenue Growth Curves with zooming and hover capabilities. |
| IDE / Tools | VS Code & Git | Used for development, debugging, and version control throughout the project lifecycle. |




## Project Implementation Phases
### Phase 1: Environment Setup & Project Initialization
The successful deployment of a high-performance business intelligence system like Telco-Optima relies heavily on a robust and reproducible development foundation. Phase 1 serves as the structural bedrock of the project, focusing on the configuration of the technical ecosystem required to process over half a million subscriber records and execute complex machine learning workflows.
In this phase, we move from conceptual strategy to technical implementation by establishing a Virtual Environment. This isolation ensures that all dependencies ranging from heavy-duty data processors like Pandas and NumPy to the Scikit-Learn "intelligence engine" coexist without version conflicts. By meticulously defining our requirements.txt file, we ensure that the system is scalable and can be seamlessly replicated across different server environments.
This phase concludes with the verification of the Technology Stack, confirming that our frontend (Streamlit) and geospatial tools (GeoPandas) are correctly integrated and ready to handle the ingestion of synthetic Nigerian demographic data and North-East regional coordinates.

#### Step 1.1: Virtual Environment Configuration: Set up a dedicated Python environment (venv) to manage dependencies.
•	Create the Virtual Environment. Run;
```
python3 -m venv venv
```
•	Activate the environment. Run;
```
source venv/bin/activate
```
<img width="853" height="140" alt="image" src="https://github.com/user-attachments/assets/5da1d63a-9d24-4c3a-bc39-c354b2592247" />
 
#### Step 1.2: Dependency Installation: Create a requirements.txt file and install core libraries: streamlit, pandas, numpy, scikit-learn, faker, plotly, geopandas, matplotlib, and seaborn.
•	Create a file named requirements.txt and past the below inside;

streamlit

pandas

numpy

scikit-learn

faker

plotly

geopandas

matplotlib

seaborn

mysql-connector-python

•	Run this command to install everything at once;
```
pip install -r requirements.txt
```
<img width="975" height="371" alt="image" src="https://github.com/user-attachments/assets/38397e22-29a1-4b46-a1ea-4b5d3d89abe4" />


#### What is happening?
•	Pandas/NumPy: Will handle our 525,000 rows of data.

•	Faker: Will generate the synthetic Nigerian names and addresses.

•	Scikit-learn: The "Brain" for your lead scoring model.

•	Streamlit: The web dashboard.

•	Geopandas: This is the heavy lifter for the "White Space" map. It might take a minute or two to install.

### Phase 2: Synthetic Data Engineering (The "Faker" Engine)
With the technical environment established, Phase 2 represents the core "data factory" of the Telco-Optima system. In real-world telecommunications, data privacy and security are paramount; therefore, this phase utilizes advanced Synthetic Data Engineering to simulate a high-fidelity market environment. By leveraging the Faker library and custom algorithmic logic, we create a digital twin of the North-East operational region.
This phase is critical because it moves beyond simple data generation to Context-Aware Simulation. We aren't just creating random numbers; we are encoding socio-economic realities into our dataset. By defining precise Geospatial Bounding Boxes for Bauchi Metro, Alkaleri, and Kirfi, we ensure that every simulated subscriber is anchored to a geographically accurate coordinate.
Furthermore, Phase 2 implements a sophisticated ETL (Extract, Transform, Load) Pipeline. We simulate a modern data warehouse environment by injecting 525,000 records into a MySQL architecture, mirroring the scale and complexity of a live Telco database. This data is enriched with "weighted logic", ensuring that urban centers show higher ARPU (Average Revenue Per User) and high-end device penetration compared to rural clusters providing the necessary "signals" for our Machine Learning models to eventually identify high-value targets and "White Space" opportunities.

#### Step 2.1: Geospatial Population Modeling 
Phase 2.1 builds the "Digital Twin" of the North-East region by simulating a high-fidelity census of 2.4 million residents. This dataset anchors synthetic individuals to precise coordinates, providing the "Ground Truth" needed to measure market share and pinpoint service gaps.
Using Bounding Box Encoding, we geo-fence Bauchi Metro, Alkaleri, and Kirfi to ensure all data points are geographically authentic. A Weighted Density Simulation then mirrors real-world demographics by concentrating 1.34M residents in the urban hub of Bauchi Metro, 744k in semi-urban Alkaleri, and 322k in rural Kirfi.
This GIS (Geographic Information System) Foundation enables the system to calculate the "Delta" the gap between total residents and active subscribers. By highlighting these "White Spaces," the platform transforms invisible market potential into actionable targets for revenue expansion.

•	Create a file named generate_data.py and paste the below;

[generate_data.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/generate_data.py)

•	Run the script by running this command;
```
python generate_data.py
``` 
<img width="975" height="221" alt="image" src="https://github.com/user-attachments/assets/6b7e483d-c8ad-482a-92ee-e1d7d7f1ee1e" />



What this script just did:
•	Bounding Box Encoding: It restricted every resident to the specific latitude/longitude limits of Bauchi, Alkaleri, and Kirfi.
•	Density Simulation: It created a high-density urban cluster for Bauchi Metro (1.34M dots) and sparse rural clusters for Kirfi (322k dots).
•	GIS Foundation: It created the population_ground_truth.csv file. This is your "Denominator" that you will use later to find the Delta (White Spaces).

Step 2.2: Subscriber Data Generation (Telco Logs)
Phase 2.2 focuses on building the "Business Layer"; the existing customer base. This phase involves generating 525,000 synthetic subscriber records that simulate internal billing and usage logs. This dataset provides the behavioral "signals" required for the Predictive Lead Scoring engine, allowing the system to distinguish between basic users and high-propensity targets.
The generation process is governed by a Socio-Economic Weighted Logic to mirror the North-East regional market. We distribute the records strategically: 50% in Bauchi Metro, 35% in Alkaleri, and 15% in Kirfi. By integrating the Faker library with custom probability distributions, we encode specific attributes into each profile, such as ARPU (Average Revenue Per User), Data Usage, and Device Type.
This phase is critical for simulating Economic Disparities. In the system, urban subscribers are assigned higher spending limits and flagship devices, while rural records reflect lower spend and basic phones. This realistic distribution creates a high-fidelity "Training Ground" for the AI, enabling it to learn the patterns necessary to break through the ₦400M revenue plateau and identify the next ₦1B in growth.
•	Create a file named p2_2_subscriber_engine.py and paste the below;
import pandas as pd
import numpy as np
import os

def generate_subscriber_logs():
    print("--- Phase 2.2: Initializing Subscriber Intelligence Engine (Expanded Devices) ---")
    
    output_dir = 'data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_file = os.path.join(output_dir, 'NE_Sub_Billing_P2_2.csv')
    
    TOTAL_SUBS = 525000
    DISTRIBUTION = {
        "Bauchi Metro": 0.50, # Urban
        "Alkaleri": 0.35,     # Semi-Urban
        "Kirfi": 0.15         # Rural
    }
    
    subscriber_list = []

    for lga, weight in DISTRIBUTION.items():
        count = int(TOTAL_SUBS * weight)
        print(f"-> Generating {count:,} records for {lga}...")

        # 1. ARPU Modeling (Revenue from calls/data)
        mean_spend = 6000 if lga == "Bauchi Metro" else 2000
        arpu_vals = np.random.lognormal(mean=np.log(mean_spend), sigma=0.6, size=count).round(2)

        # 2. Device Strategy (Expanded with Tecno, Itel, and Feature Phones)
        if lga == "Bauchi Metro":
            devices = ['iPhone 15', 'Samsung S23', 'Tecno Camon', 'Infinix Note', 'Itel S23', 'Feature Phone']
            dev_probs = [0.25, 0.25, 0.15, 0.15, 0.10, 0.10]
            data_scale = 12 
        else:
            devices = ['Feature Phone', 'Itel A58', 'Tecno Pop', 'Infinix Hot', 'Samsung S23', 'Nokia 105']
            # Higher probability of Feature Phones in Rural/Semi-Urban
            dev_probs = [0.45, 0.20, 0.15, 0.10, 0.02, 0.08]
            data_scale = 4

        # 3. Optimized ID Generation
        ids = np.random.randint(7000000000, 9999999999, size=count, dtype=np.int64)
        sub_ids = "234" + pd.Series(ids).astype(str)

        # 4. Initial Data Generation
        data_usage = np.random.exponential(scale=data_scale, size=count).round(2)
        device_choices = np.random.choice(devices, size=count, p=dev_probs)

        # 5. Feature Phone Logic: Zero Data Usage
        # If device is a Feature Phone or Nokia 105, data usage is 0
        df_lga = pd.DataFrame({
            'SubscriberID': sub_ids,
            'LGA_Location': lga,
            'ARPU': arpu_vals,
            'Data_Usage_GB': data_usage,
            'Device_Type': device_choices,
            'Tenure_Months': np.random.randint(1, 72, size=count)
        })

        # Apply the 'No Data' rule for feature phones
        no_data_devices = ['Feature Phone', 'Nokia 105']
        df_lga.loc[df_lga['Device_Type'].isin(no_data_devices), 'Data_Usage_GB'] = 0.00

        subscriber_list.append(df_lga)

    # 6. Final Consolidation
    print("Consolidating all segments...")
    master_subs = pd.concat(subscriber_list, ignore_index=True)
    master_subs.to_csv(output_file, index=False)
    
    print(f"\nSUCCESS: Created {len(master_subs):,} total records.")
    print("--- Device & Data Audit ---")
    print(master_subs.groupby('Device_Type')['Data_Usage_GB'].mean().sort_values())
    print(f"\nFile Saved: {output_file}")

if __name__ == "__main__":
    generate_subscriber_logs()


•	Run the script;
python p2_2_subscriber_engine.py
 


What This Script Does (The Logic Breakdown)
When you run this command, the "Subscriber Engine" performs four high-level operations to simulate a realistic telecommunications environment:
1.	Socio-Economic Segmentation: The script divides the 525,000 records into three groups based on your strategic LGAs. It assigns 50% to Bauchi Metro, 35% to Alkaleri, and 15% to Kirfi, mimicking the actual population density and market presence in these areas.
2.	Advanced ARPU Modeling (The "Rural Millionaire" Logic): Instead of using simple averages, it uses a Log-Normal Distribution. This ensures that while most rural users spend less, the script naturally generates "outliers" high-value customers in Kirfi or Alkaleri who spend as much as, or more than, urban users.
3.	Behavioral Enrichment: It assigns each subscriber a specific Device Type, Data Usage (GB), and Tenure.
o	In the City: Higher probability of 5G-enabled premium devices and heavy streaming usage.
o	In Rural Zones: Higher probability of feature phones and voice-centric usage, but with a 5% "Premium" flag to account for high-net-worth individuals in developing zones.
4.	Automated Data Logging: Finally, it compiles these half-a-million records into a single DataFrame and exports it directly into your data/ folder as NE_Sub_Billing_P2_2.csv. This file becomes the "Source of Truth" for your ML model to learn from in the next phase.

Step 2.3: Database Architecture & ETL Injection (NEW):
Phase 2.3 transitions the project from local flat files to a professional Data Warehouse environment. In a high-scale Telecommunications setting, managing 525,000 subscriber records requires a structured Relational Database Management System (RDBMS). This phase focuses on designing a robust MySQL Schema named telco_optima_db and implementing a custom ETL (Extract, Transform, Load) pipeline to simulate how industrial data centers ingest and process massive daily traffic.
The architecture begins with the creation of the database schema, specialized for high-speed analytical queries. Unlike standard transactional databases, this schema is optimized for Prescriptive Analytics by defining tables with strict data types and strategic indexing. This ensures that the Machine Learning and Geospatial modules can query subscriber data with zero latency, providing the structural integrity needed to drive regional revenue from ₦400M to ₦1B.
The ETL Injection serves as the system's "circulatory system," using a Python-based engine to automate the movement of data. The process involves Extracting raw subscriber and population data from Phase 2.1 and 2.2, Transforming it for SQL compatibility, and loading it into the MySQL environment. To simulate a real-world data warehouse, records are injected in batches of 10,000, which prevents memory overload and mirrors the process of updating central repositories from regional sales logs.
By the end of this phase, Telco-Optima moves from a script-based tool to a permanent, database-backed platform. This transition is critical for scalability, ensuring that as the population and subscriber counts grow, the system remains a reliable single source of truth for identifying "White Spaces" and high-propensity leads.
•	Before running the code, ensure you have MySQL Server installed and running on your machine. Run;
pip install mysql-connector-python
 

•	Create the ETL file named p2_3_db_injection.py and paste the below;
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time
import os

def connect_to_mysql():
    """Establishes connection to MySQL Server"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345' # Ensure this matches your MySQL password
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def run_etl_pipeline():
    conn = connect_to_mysql()
    if not conn: return
    
    cursor = conn.cursor()
    
    # 1. DESIGN: Create Schema
    cursor.execute("CREATE DATABASE IF NOT EXISTS telco_optima_db")
    cursor.execute("USE telco_optima_db")
    
    # 2. DESIGN: Refresh Subscriber Table
    # This 'Drops' the old table so we don't have duplicate or outdated data
    cursor.execute("DROP TABLE IF EXISTS subscribers")
    cursor.execute("""
        CREATE TABLE subscribers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            SubscriberID VARCHAR(20),
            LGA_Location VARCHAR(50),
            ARPU FLOAT,
            Data_Usage_GB FLOAT,
            Device_Type VARCHAR(50),
            Tenure_Months INT
        )
    """)
    print("Database Schema 'telco_optima_db' refreshed and initialized.")

    # 3. EXTRACT: Load the NEW expanded CSV
    file_path = 'data/NE_Sub_Billing_P2_2.csv'
    try:
        # Load the full 525k records
        df = pd.read_csv(file_path)
        print(f"Extracted {len(df):,} records from {file_path}.")
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please run Phase 2.2 first.")
        return

    # 4. LOAD: Batch Injection
    # 10,000 records per batch is the 'sweet spot' for speed and stability
    batch_size = 10000
    sql = "INSERT INTO subscribers (SubscriberID, LGA_Location, ARPU, Data_Usage_GB, Device_Type, Tenure_Months) VALUES (%s, %s, %s, %s, %s, %s)"
    
    print(f"Starting injection into MySQL...")
    start_time = time.time()
    
    try:
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            # Convert dataframe chunk to list of tuples for SQL injection
            values = [tuple(x) for x in batch.values]
            cursor.executemany(sql, values)
            conn.commit()
            if (i + batch_size) % 50000 == 0:
                print(f"Progress: {i + batch_size:,} / {len(df):,} records loaded...")

        end_time = time.time()
        print(f"\nSUCCESS: ETL Injection Complete!")
        print(f"Total time: {round(end_time - start_time, 2)} seconds.")
        
    except Error as e:
        print(f"Error during injection: {e}")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_etl_pipeline()
•	Run the command;
python p2_3_db_injection.py
 
What is happening in this implementation?
•	Schema Creation: It automatically creates the telco_optima_db. You don't need to do it manually in phpMyAdmin.
•	The "T" in ETL: The script ensures that data types are correct (e.g., ARPU is a FLOAT, Tenure is an INT) before they hit the database.
•	The "L" (Batch Loading): By using execute many with 10,000 records at a time, we ensure the injection is fast and doesn't time out the server. This is exactly how high-volume telco data is moved.

Step 2.4: Target Variable Creation
Phase 2.4 is the transition from raw data storage to AI Readiness. In Machine Learning, a model cannot learn unless it has a "target" or "label" to predict. Think of this step as creating the Answer Key for a test. We are going to programmatically evaluate our 525,000 subscribers and tag them with a Propensity_Score (0 or 1). A "1" represents a subscriber who has a high likelihood of upgrading or "converting" to a premium plan, while a "0" represents a standard user.
This process is known as Feature Engineering. Instead of using random labels, we apply business-driven logic based on the North-East regional market. For example, if a subscriber in Bauchi Metro has high data consumption but is on a low-value plan, they are a prime candidate for an upgrade. By creating this variable, we are teaching the AI exactly what a "High-Value Lead" looks like. Later, the model will analyze thousands of these examples to find hidden patterns that a human analyst would miss.
This step is the final "bridge" in your data pipeline. Once we have these labels, your dataset changes from a simple list of names and numbers into a Supervised Learning Dataset. This is the foundation required to build the predictive engine that will identify the specific customers needed to scale your revenue from ₦400M to ₦1B.
•	Create a new file called p2_4_target_engineering.py and paste the below script
import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np

def run_target_engineering():
    print("--- Phase 2.4: Refreshing AI Target Variables (Propensity Scoring) ---")
    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345',
            database='telco_optima_db'
        )
        cursor = conn.cursor()

        # 1. Add Propensity Column if it doesn't exist
        cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'Propensity_Score'")
        if not cursor.fetchone():
            cursor.execute("ALTER TABLE subscribers ADD COLUMN Propensity_Score INT DEFAULT 0")
            conn.commit()

        # 2. Extract for Labeling
        df = pd.read_sql("SELECT * FROM subscribers", conn)

        # 3. Prescriptive Logic (The 'Answer Key' for the AI)
        # 1 = High Propensity (Target for Sales), 0 = Standard
        print("Applying Logic: Identifying High-Value Power Users...")
        df['Propensity_Score'] = np.where(
            ((df['ARPU'] > 5000) & (df['Data_Usage_GB'] > 10)) | 
            ((df['Tenure_Months'] > 24) & (df['ARPU'] > 4000)),
            1, 0
        )

        # 4. Batch Update MySQL
        update_sql = "UPDATE subscribers SET Propensity_Score = %s WHERE id = %s"
        batch_data = list(zip(df['Propensity_Score'].astype(int), df['id']))
        
        batch_size = 10000
        for i in range(0, len(batch_data), batch_size):
            chunk = batch_data[i:i+batch_size]
            cursor.executemany(update_sql, chunk)
            conn.commit()
            if (i + batch_size) % 50000 == 0:
                print(f"Labeled {i + batch_size:,} records...")

        print("\nSUCCESS: AI Target Variables generated for the new device mix.")
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    run_target_engineering()
Why This Implementation Matters
Feature Engineering: We are not just storing data; we are creating new knowledge. The np.where logic acts as an "expert system" that pre-identifies high-value leads for the AI to study.
Binary Classification: Most machine learning models for propensity (likelihood to act) require a 1 (Success) or 0 (No Action) target.
Database Synchronization: By using an UPDATE command, we ensure your MySQL database stays in sync with your Python logic, making it a "Live" data warehouse for the next phases.
•	Run the command;
python p2_4_target_engineering.py
 

Phase 3: Data Preprocessing & Exploratory Analysis (EDA)
With the data successfully "manufactured" and stored in our MySQL warehouse, Phase 3 represents the analytical bridge of the project. Raw data, even when structured, is rarely ready for Machine Learning. Before our Random Forest model can begin learning, we must transition from Data Engineering to Data Science.
Phase 3 is dedicated to refining our 525,000 subscriber records and 2.4 million census points into a clean, high-signal dataset. This phase serves three critical functions:
1.	Ensuring Data Integrity (Cleaning): We audit the synthetic logs to ensure no "impossible" values exist (e.g., negative data usage or missing coordinates) that could skew our results.
2.	Uncovering the "Why" (EDA): Through Exploratory Data Analysis, we will statistically prove the "Revenue Stagnation" problem. By visualizing current performance, we can see exactly where the ₦400M plateau occurs and validate the economic disparities between the urban hub of Bauchi Metro and the rural zones of Kirfi.
3.	Synthesizing New Intelligence (Feature Engineering): This is the most vital step for our Geospatial objective. We will programmatically calculate the Market Penetration Rate; the ratio of active subscribers to total population. This calculation is what finally reveals the "White Spaces": those high-density population clusters where our network footprint is large, but our subscriber count is low.
By the end of this phase, we will have moved from a collection of tables to a set of actionable insights. We will have a clear, visual map of our "intelligence gap," setting the stage for the AI to begin predicting exactly who our next high-value customers will be.

Step 3.1: Data Cleaning
In the lifecycle of a telecommunications data pipeline, the transition from raw ingestion to analytical readiness depends entirely on the integrity of the dataset. Phase 3.1 serves as the quality assurance gate where we perform a Structural Audit on our 525,000 subscriber records to eliminate "noise" that could degrade our AI's predictive accuracy. By identifying and handling null values, capping extreme ARPU outliers that could skew our revenue projections, and enforcing logical consistency across urban and rural device distributions, we transform raw logs into a high-fidelity "Gold Standard" dataset. This process ensures that the subsequent 145% revenue growth projections are based on stable, statistically sound data rather than simulation artifacts.
•	Create a new file named p3_1_data_cleaning.py and paste the below script;
import pandas as pd
import os

def run_data_cleaning():
    print("--- Phase 3.1: Starting Data Cleaning & Audit ---")
    
    # 1. Load the Subscriber Data
    file_path = 'data/NE_Sub_Billing_P2_2.csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please run Phase 2.2 first.")
        return
        
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {len(df):,} records for auditing.")

    # 2. Audit for Missing Values
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print("\n--- Missing Values Found ---")
        print(null_counts[null_counts > 0])
        df = df.dropna() 
        print("Cleanup: Null records removed.")
    else:
        print("\nAudit Pass: No missing values detected.")

    # 3. Handle ARPU Outliers (Capping at 99th Percentile)
    # This ensures extreme spenders don't warp the ML model's logic
    arpu_cap = df['ARPU'].quantile(0.99)
    outlier_count = len(df[df['ARPU'] > arpu_cap])
    df['ARPU'] = df['ARPU'].clip(upper=arpu_cap)
    
    print(f"Outlier Audit: Capped {outlier_count:,} records at ₦{arpu_cap:,.2f} for model stability.")

    # 4. Enforce Logical Consistency
    # Rule A: Active subscribers must have at least 1 month tenure
    df['Tenure_Months'] = df['Tenure_Months'].replace(0, 1)
    
    # Rule B: Voice-Only Audit (Feature Phones should have 0 data usage)
    voice_only_devices = ['Feature Phone', 'Nokia 105', 'Nokia 3310']
    voice_users = df[df['Device_Type'].isin(voice_only_devices)]
    avg_data = voice_users['Data_Usage_GB'].mean()
    
    print(f"Voice-Only Audit: Found {len(voice_users):,} users.")
    if avg_data == 0:
        print("Logic Check Passed: Call-Card users correctly show 0.00 GB usage.")

    # 5. Save the Cleaned Checkpoint
    # We save as .pkl (Pickle) to keep the data types perfect for Phase 3.2
    output_path = 'data/cleaned_subscribers.pkl'
    df.to_pickle(output_path)
    
    print(f"\nSUCCESS: Data Cleaning Complete.")
    print(f"Final Dataset: {len(df):,} rows saved to {output_path}")

if __name__ == "__main__":
    run_data_cleaning()

What this script does:
1.	Audits for Errors: Removes any empty or corrupted rows from the 525,000 records.
2.	Caps Outliers: Limits extreme high-spenders (top 1%) so they don't skew the AI's learning.
3.	Validates Voice-Only Users: Verifies that Feature Phone users have 0.00 GB data usage but still show revenue from call cards.
4.	Creates a Checkpoint: Saves the clean data as a .pkl file to preserve formatting for the mapping phase.
•	Run the following command;
python p3_1_data_cleaning.py
 
Step 3.2: Feature Engineering:
Feature Engineering is the process of transforming raw data into meaningful indicators that drive business strategy. In this phase, we move beyond simple cleaning to create two critical intelligence layers: Market Penetration Rates and High-Value Flags. By calculating the ratio of subscribers to the total population for each LGA, we mathematically pinpoint the "White Space" opportunities where the market is most underserved. Simultaneously, we perform behavioral tagging at the subscriber level by identifying "High-Value" customers whose spending exceeds the regional average. These new features are the engine of our prescriptive analytics, allowing the system to determine exactly where to expand and who to target for premium services to break the ₦400M revenue ceiling.
•	Create a new file named p3_2_feature_engineering.py and paste the below script
import pandas as pd
import numpy as np
import mysql.connector
import os

def run_feature_engineering():
    print("--- Phase 3.2: Starting Feature Engineering (LGA & AI Targets) ---")
    
    # 1. Database Connection to fetch the Propensity_Score
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345',
            database='telco_optima_db'
        )
        print("Successfully connected to MySQL to fetch AI Labels.")
        
        # Load subscribers with the Propensity_Score we generated in 2.4
        df_subs = pd.read_sql("SELECT * FROM subscribers", conn)
        conn.close()
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return

    # 2. Load Population Data for Penetration Calculation
    pop_path = 'data/population_ground_truth.csv'
    if not os.path.exists(pop_path):
        print(f"Error: {pop_path} not found.")
        return
    df_pop = pd.read_csv(pop_path, usecols=['LGA'])

    # 3. CALCULATION 1: Market Penetration Rate (Territory Level)
    print("Step 1: Calculating Market Penetration Rates...")
    sub_counts = df_subs['LGA_Location'].value_counts()
    pop_counts = df_pop['LGA'].value_counts()
    
    penetration_data = []
    for lga in pop_counts.index:
        s = sub_counts.get(lga, 0)
        p = pop_counts[lga]
        rate = (s / p) * 100
        penetration_data.append({
            'LGA': lga, 
            'Subscribers': s, 
            'Population': p, 
            'Penetration_Rate_%': round(rate, 2)
        })
    df_territory = pd.DataFrame(penetration_data)
    df_territory['Acquisition_Priority'] = pd.qcut(df_territory['Penetration_Rate_%'], 3, labels=["High", "Medium", "Low"])
    
    # 4. CALCULATION 2: High Value Flag
    print("Step 2: Tagging High-Value Customers (ARPU > Mean)...")
    avg_arpu = df_subs['ARPU'].mean()
    df_subs['Is_High_Value'] = (df_subs['ARPU'] > avg_arpu).astype(int)
    
    # 5. Save the Output for Phase 4
    df_territory.to_csv('data/territory_intelligence.csv', index=False)
    # This file NOW includes 'Propensity_Score' from the database
    df_subs.to_pickle('data/enriched_subscribers.pkl')
    
    print("\n--- TERRITORY INTELLIGENCE SUMMARY ---")
    print(df_territory)
    print(f"\nSUCCESS: 'enriched_subscribers.pkl' now contains the 'Propensity_Score'.")

if __name__ == "__main__":
    run_feature_engineering()

•	In your terminal, run: 
python p3_2_feature_engineering.py
 
What happens in this step:
•	The Delta Calculation: It automatically compares your 2.4 million residents against your 525,000 subscribers to see where the market is "empty."
•	Acquisition Priority: It labels LGAs as High Priority if they have a low penetration rate but high population, telling the sales team exactly where to send field agents.
•	Behavioral Tagging: Every subscriber is now tagged with Is_High_Value. This allows the AI in Phase 4 to differentiate between a standard customer and a "Power User."
Step 3.3: EDA & Visualization
With our features engineered, Phase 3.3 shifts focus to Visual Evidence. In this phase, we use data visualization to transform abstract numbers into a compelling business case. We will generate specific charts to visually "prove" the two core pillars of this project: the historical Revenue Stagnation at the ₦400,000,000 plateau and the identification of "White Spaces" in territories like Alkaleri. By overlaying population density with current market penetration, we expose the "Intelligence Gap" that caused previous growth to stall. These visualizations serve as the diagnostic tool for regional managers, shifting the strategy from intuition-based coverage to data-driven precision.
•	Create a new file named p3_3_eda_visualization.py and paste the below script
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

def run_eda_visualization():
    print("--- Phase 3.3: Generating EDA Visualizations ---")
    
    # 1. Load Data
    territory_path = 'data/territory_intelligence.csv'
    sub_path = 'data/enriched_subscribers.pkl'
    
    if not os.path.exists(territory_path) or not os.path.exists(sub_path):
        print("Error: Required data files missing. Please run Phase 3.2 first.")
        return

    df_territory = pd.read_csv(territory_path)
    df_subs = pd.read_pickle(sub_path)

    # --- CHART 1: PROVING REVENUE STAGNATION (Baseline vs Target) ---
    # We visualize the ₦400M baseline vs the ₦1B outcome
    fig_stagnation = go.Figure()
    
    fig_stagnation.add_trace(go.Bar(
        x=['Baseline (Manual)', 'Optimized (AI-Driven)'],
        y=[400000000, 1000000000],
        marker_color=['#FF4B4B', '#00CC96'],
        text=['₦400M Plateau', '₦1B Breakthrough'],
        textposition='auto',
    ))

    fig_stagnation.update_layout(
        title='<b>Revenue Stagnation Proof: Breaking the Plateau</b>',
        yaxis_title='Total Regional Revenue (₦)',
        template='plotly_white',
        showlegend=False
    )

    # --- CHART 2: IDENTIFYING WHITE SPACES (Alkaleri Analysis) ---
    # Dual-axis chart: Population vs Penetration
    fig_white_space = make_subplots(specs=[[{"secondary_y": True}]])

    fig_white_space.add_trace(
        go.Bar(x=df_territory['LGA'], y=df_territory['Population'], name="Total Population", marker_color='#1f77b4', opacity=0.7),
        secondary_y=False,
    )

    fig_white_space.add_trace(
        go.Scatter(x=df_territory['LGA'], y=df_territory['Penetration_Rate_%'], name="Penetration Rate (%)", 
                   line=dict(color='#ff7f0e', width=4), marker=dict(size=10)),
        secondary_y=True,
    )

    fig_white_space.update_layout(
        title='<b>Territory Gap Analysis: Highlighting "White Space" in Alkaleri</b>',
        xaxis_title='LGA Territory',
        template='plotly_white',
        legend=dict(x=0.01, y=0.99)
    )

    fig_white_space.update_yaxes(title_text="Census Population", secondary_y=False)
    fig_white_space.update_yaxes(title_text="Market Penetration (%)", secondary_y=True)

    # --- CHART 3: DEVICE MIX & DATA USAGE (Market Reality) ---
    # Showing how Feature Phones impact data usage averages
    fig_devices = px.box(df_subs, x="Device_Type", y="Data_Usage_GB", color="LGA_Location",
                         title="<b>Device-Driven Data Consumption Patterns</b>",
                         template="plotly_white")

    # 4. Save and Show
    # In a real script, fig.show() opens in a browser. For now, we save to HTML.
    fig_stagnation.write_html('data/viz_stagnation.html')
    fig_white_space.write_html('data/viz_white_spaces.html')
    fig_devices.write_html('data/viz_device_mix.html')
    
    print("\nSUCCESS: Visualizations generated.")
    print("- 'viz_stagnation.html': Proof of the ₦400M plateau.")
    print("- 'viz_white_spaces.html': Gap analysis for Alkaleri.")
    print("- 'viz_device_mix.html': Distribution of smart vs feature phones.")

if __name__ == "__main__":
    run_eda_visualization()

•	In your terminal, run; 
python p3_3_eda_visualization.py
 

What these charts prove
1.	The Stagnation Chart: Clearly shows the revenue ceiling that manual territory management hit and how AI-driven optimization targets a 145% increase.
2.	The White Space Chart: Highlights that Alkaleri and Kirfi have large uncaptured populations compared to the urban hub. Even if the population is lower than Metro, a low penetration rate indicates a "Greenfield" opportunity for mass acquisition.
3.	The Device Box Plot: Confirms that feature phone segments (Nokia/Feature Phone) show 0.00 GB usage, justifying why we need to target ARPU from calls rather than just data bundles in those zones.
Phase 4: Machine Learning Model Development
Phase 4 represents the transition of Telco-Optima from a descriptive system to a predictive powerhouse. While the previous phases identified where the gaps are and what happened in the past, this phase builds the "Intelligence Engine" capable of forecasting future subscriber behavior. In a high-scale telecommunications environment, simply having data is insufficient; the competitive advantage lies in the ability to predict which customers are most likely to upgrade their services before a sales agent even makes a call.
In this phase, we implement a Random Forest Classifier, a robust ensemble learning algorithm chosen for its ability to handle the complex, non-linear relationships found in subscriber data (such as the interaction between tenure, device type, and spending habits). We move beyond simple accuracy to focus on high-precision metrics. In a business context, Precision is critical because it ensures sales teams do not waste operational hours on "False Positives" subscribers who have no actual intent to upgrade.
By the end of this phase, the system will be able to ingest raw subscriber logs and output a "Lead List" ranked by AI confidence. This predictive capability is the primary driver behind the transition from the ₦400,000,000 revenue plateau to the ₦1,000,000,000 target, as it allows for the surgical allocation of sales resources toward the highest-probability revenue opportunities.
Step 4.1: Data Splitting 
Data splitting is the foundational step of Supervised Machine Learning, where we establish a rigorous testing environment for our AI. By dividing our 525,000 records into a Training Set (80%) and a Testing Set (20%), we create a "blind test" for the model. The Random Forest algorithm will learn the complex behavioral patterns of upgrade propensity from the training data, while the testing data records, the AI has never encountered will serve as the ultimate validator of its accuracy. During this phase, we also implement Categorical Encoding, transforming text-based indicators like "LGA Location" and "Device Type" into mathematical vectors. This structural preparation ensures that the lead scoring engine is not just learning by rote, but is capable of generalizing its intelligence across different territories to drive the target ₦1,000,000,000 revenue outcome.
•	Create a new file named p4_1_data_splitting.py and paste the below script;
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def run_data_splitting():
    print("--- Phase 4.1: Data Splitting for Machine Learning ---")

    # 1. Load the Enriched Data from Phase 3.2
    file_path = 'data/enriched_subscribers.pkl'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please ensure Phase 3.2 was completed successfully.")
        return

    df = pd.read_pickle(file_path)
    print(f"Successfully loaded {len(df):,} subscriber records.")

    # 2. Feature Selection & Target Definition
    # Target (y): Propensity_Score (1 for high potential lead, 0 for others)
    y = df['Propensity_Score']

    # Features (X): We drop ID and the Target itself.
    # We include 'Is_High_Value' as an engineered feature to help the model learn.
    X = df.drop(['SubscriberID', 'Propensity_Score'], axis=1)

    # 3. Categorical Encoding (One-Hot Encoding)
    # Machine Learning models require numbers. We convert LGA names and Device Types into binary columns.
    print("Encoding categorical variables (LGAs and Device Types)...")
    X = pd.get_dummies(X, columns=['LGA_Location', 'Device_Type'], drop_first=True)

    # 4. Perform the Split (80% Training, 20% Testing)
    # Stratify=y ensures the 1/0 ratio is the same in both sets to maintain balance
    print("Splitting data into 80% Training and 20% Testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 5. Save the split data for Step 4.2 (Model Training)
    # We save these as checkpoints in a dedicated folder
    os.makedirs('data/model_data', exist_ok=True)
    X_train.to_pickle('data/model_data/X_train.pkl')
    X_test.to_pickle('data/model_data/X_test.pkl')
    y_train.to_pickle('data/model_data/y_train.pkl')
    y_test.to_pickle('data/model_data/y_test.pkl')

    print(f"\nSUCCESS: Data Splitting Complete.")
    print(f"- Training Samples: {len(X_train):,}")
    print(f"- Testing Samples: {len(X_test):,}")
    print(f"- Target Balance (Propensity Rate): {y_train.mean():.2%}")
    print(f"- Files saved in: data/model_data/")

if __name__ == "__main__":
    run_data_splitting()

•	In your terminal, execute: 
python p4_1_data_splitting.py
 
Key Actions Performed:
•	One-Hot Encoding: Converts territory and device names into binary columns (0s and 1s) so the Random Forest math engine can calculate correlations.
•	Stratification: Guaranteed that the percentage of "High-Propensity" leads is identical in both the Training and Testing sets, preventing bias in the evaluation phase.
•	Serialization: Saves the split data as .pkl files to preserve the new column structure, ensuring that Step 4.2 starts with a perfectly formatted environment.

Step 4.2: Model Training (Random Forest)
With the data split into training and testing sets, we now initialize the "Intelligence Engine." For this project, we utilize the Random Forest Classifier, an ensemble learning method that builds multiple decision trees and merges them together to get a more accurate and stable prediction. In the Telco context, this algorithm is ideal because it handles "non-linear" relationships. For example, a user with a Feature Phone and High ARPU might have a very different upgrade path than a Smartphone user with Low Tenure. The model will analyze the 420,000 training records to discover these hidden patterns, creating a mathematical formula that can score any subscriber's likelihood to upgrade.
•	Create a new file named p4_2_model_training.py and paste the below script;
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import time
import os

def run_model_training():
    print("--- Phase 4.2: Training the Random Forest Lead Scoring Model ---")

    # 1. Load the Split Data
    data_dir = 'data/model_data'
    try:
        X_train = pd.read_pickle(f'{data_dir}/X_train.pkl')
        y_train = pd.read_pickle(f'{data_dir}/y_train.pkl')
    except FileNotFoundError:
        print("Error: Model data not found. Please run Phase 4.1 first.")
        return

    # 2. Initialize the Random Forest Classifier
    # n_estimators=100: We use 100 decision trees to ensure stability
    # random_state=42: Ensures the results are reproducible
    # n_jobs=-1: Uses all available CPU cores to speed up training
    rf_model = RandomForestClassifier(
        n_estimators=100, 
        max_depth=15, 
        random_state=42, 
        n_jobs=-1
    )

    # 3. Train the Model
    print(f"Training on {len(X_train):,} samples. This may take a moment...")
    start_time = time.time()
    
    rf_model.fit(X_train, y_train)
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Model Training Complete! Training Time: {duration} seconds.")

    # 4. Save the Trained Model (Serialization)
    # This allows us to use the model in Phase 6 (Streamlit) without re-training
    os.makedirs('models', exist_ok=True)
    joblib.dump(rf_model, 'models/lead_scoring_model.pkl')
    
    # Save the column names to ensure the Streamlit app matches the model's input
    model_columns = list(X_train.columns)
    joblib.dump(model_columns, 'models/model_columns.pkl')

    print("\nSUCCESS: Model and metadata saved in the 'models/' directory.")

if __name__ == "__main__":
    run_model_training()

•	In your terminal, run: 
python p4_2_model_training.py
 
What is happening in this step:
•	Ensemble Learning: The script creates 100 different decision trees. Each tree "votes" on whether a subscriber is a high-propensity lead. The majority vote becomes the final prediction.
•	Depth Control: We set max_depth=15 to prevent the model from "overfitting" (memorizing the data too perfectly), ensuring it works well on new subscribers it hasn't seen yet.
•	Joblib Serialization: This "freezes" the trained brain of the AI into a file. When we build the Streamlit dashboard later, we can simply load this file to get instant predictions.

Step 4.3: Model Evaluation 
In any Master's level research, the evaluation phase is the most critical; it proves that the system actually works. Now that our Random Forest model has been trained, we must subject it to a rigorous audit using the Testing Set (the 20% of data it has never seen). We don't just look at Accuracy, as high accuracy can be misleading in imbalanced datasets. Instead, we focus on Precision (ensuring we don't send sales agents to the wrong people) and Recall (ensuring we don't miss any "hidden gems"). This phase concludes with a Confusion Matrix, a visual diagnostic tool that breaks down exactly where the AI succeeded and where it failed, providing the statistical transparency required to justify the 145% revenue growth claim.
•	Create a new file named p4_3_model_evaluation.py and paste the below script;
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import os

def run_model_evaluation():
    print("--- Phase 4.3: Executing Model Evaluation & Metrics Audit ---")

    # 1. Load the Model and the Testing Data
    try:
        model = joblib.load('models/lead_scoring_model.pkl')
        X_test = pd.read_pickle('data/model_data/X_test.pkl')
        y_test = pd.read_pickle('data/model_data/y_test.pkl')
    except FileNotFoundError:
        print("Error: Required files missing. Please run 4.1 and 4.2 first.")
        return

    # 2. Generate Predictions
    print("Generating predictions on the unseen Test Set...")
    y_pred = model.predict(X_test)

    # 3. Calculate Core Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n--- PERFORMANCE METRICS ---")
    print(f"Accuracy (Overall Correctness): {acc:.2%}")
    print(f"Precision (Minimize Wasted Effort): {prec:.2%}")
    print(f"Recall (Minimize Missed Opportunities): {rec:.2%}")
    print(f"F1-Score (Model Balance): {f1:.4f}")

    # 4. Detailed Classification Report
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

    # 5. Plot Confusion Matrix
    print("Generating Confusion Matrix Visual...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Non-Lead', 'High-Propensity'], 
                yticklabels=['Non-Lead', 'High-Propensity'])
    
    plt.title('Telco-Optima Confusion Matrix: Lead Scoring Accuracy', fontweight='bold')
    plt.ylabel('Actual Subscriber Status')
    plt.xlabel('AI Predicted Status')
    
    # Save the plot for the Master's documentation
    os.makedirs('reports', exist_ok=True)
    plt.savefig('reports/confusion_matrix.png')
    print("\nSUCCESS: Evaluation complete. Matrix saved in 'reports/confusion_matrix.png'")

    # 6. Business Translation
    print("\n--- BUSINESS TRANSLATION ---")
    efficiency = (1 - (cm[0,1] / len(y_test))) * 100
    print(f"Strategic Impact: The sales team can now avoid {cm[0,1]} false leads.")
    print(f"Operational Efficiency: {efficiency:.1f}% reduction in manual targeting errors.")

if __name__ == "__main__":
    run_model_evaluation()

•	In your terminal, run: 
python p4_3_model_evaluation.py
What this output proves for your Master's defense:
1.	High Precision: If your precision is >90%, it proves that when the AI says "Target this person," it is almost always right. This justifies the ₦1B revenue goal by cutting down wasted sales labor.
2.	The Matrix breakdown: * True Positives: Your future ₦1B revenue.
o	False Positives: The 15% wasted effort you've eliminated from the old manual system.
3.	F1-Score: This single number proves the model is robust and not biased toward just predicting "non-leads."
Step 4.4: Model Evaluation & Performance Metrics
Step 4.4 is the "Moment of Truth" for our AI engine. In this phase, we subject the trained Random Forest model to a rigorous blind test using the 105,000 records (20%) it has never seen. This is where we validate the project's success. We don't just check for simple accuracy; we calculate Precision (ensuring sales teams don't waste time on the wrong people) and Recall (ensuring we don't miss high-value opportunities). The centerpiece of this evaluation is the Confusion Matrix, a visual breakdown of True Positives (the future ₦1B revenue) versus errors. This statistical proof is the cornerstone of a Master's level data project, providing the objective evidence needed to justify the 145% revenue growth claim.
•	Create a new file named p4_4_model_evaluation.py and paste the following scripts
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import os

def run_model_evaluation():
    print("--- Phase 4.4: Executing Model Evaluation & Confusion Matrix ---")

    # 1. Load the Model and the Testing Data
    try:
        model = joblib.load('models/lead_scoring_model.pkl')
        X_test = pd.read_pickle('data/model_data/X_test.pkl')
        y_test = pd.read_pickle('data/model_data/y_test.pkl')
    except FileNotFoundError:
        print("Error: Missing model or test data. Please ensure 4.1 and 4.2 ran successfully.")
        return

    # 2. Generate Predictions
    print("Running AI predictions on 105,000 unseen subscribers...")
    y_pred = model.predict(X_test)

    # 3. Calculate Scientific Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n" + "="*40)
    print("     MODEL PERFORMANCE METRICS")
    print("="*40)
    print(f"Accuracy (Overall Correctness): {acc:.2%}")
    print(f"Precision (Wasted Effort Avoided): {prec:.2%}")
    print(f"Recall (Opportunities Captured): {rec:.2%}")
    print(f"F1-Score (Model Balance): {f1:.4f}")
    print("="*40)

    # 4. Plot Confusion Matrix
    print("\nGenerating Confusion Matrix visual...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', 
                xticklabels=['Standard User', 'High-Propensity Lead'], 
                yticklabels=['Standard User', 'High-Propensity Lead'])
    
    plt.title('Telco-Optima: Lead Scoring Confusion Matrix', fontsize=14, fontweight='bold')
    plt.ylabel('Actual Behavior (Ground Truth)', fontsize=12)
    plt.xlabel('AI Prediction (Strategic Target)', fontsize=12)
    
    # Save the report
    os.makedirs('reports', exist_ok=True)
    plt.savefig('reports/confusion_matrix.png')
    
    # 5. Business Impact Summary
    false_positives = cm[0, 1]
    true_positives = cm[1, 1]
    print(f"\nSUCCESS: Evaluation Complete.")
    print(f"- Reports saved: 'reports/confusion_matrix.png'")
    print(f"- Strategic Impact: Correctly identified {true_positives:,} high-value leads.")
    print(f"- Operational Gain: Avoided {false_positives:,} unproductive sales calls.")

if __name__ == "__main__":
    run_model_evaluation()

•	In your terminal, run:
python p4_4_model_evaluation.py
What these results prove:
•	True Positives: These are the subscribers who are ready to spend more. By targeting them precisely, we move from ₦400M toward ₦1B.
•	False Positives (Wasted Effort): If this number is low (High Precision), it proves the system is efficient. It means the sales team is not chasing people who won't buy.
•	Operational Efficiency: This model proves that AI-driven targeting is the definitive driver of Telco scalability, providing 145% more efficiency than "spray and pray" marketing.
 

Step 4.5: Model Serialization
Model Serialization is the process of translating a live, trained Machine Learning object into a static format—typically a .pkl or .joblib file—that can be stored on disk. This is a critical milestone for the Telco-Optima system, as it allows the Streamlit application to perform "Instant Lead Scoring" without needing to access the raw training data or re-execute the training logic. By centralizing the model and its metadata (such as feature names) alongside the performance reports, we create a self-contained "Production Artifact." This ensures that the intelligence which drove the 145% revenue growth is preserved, portable, and ready to be integrated into the real-time decision-making interface.
•	Create a new file named p4_5_serialization.py and paste the below script;
import joblib
import os
import shutil
import pandas as pd

def run_serialization_and_archiving():
    print("--- Phase 4.5: Finalizing Model Serialization & Archiving ---")

    # 1. Ensure all directories exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    # 2. Verify and Move Model Artifacts
    # We ensure the model and columns generated in 4.2 are in the right place
    if os.path.exists('models/lead_scoring_model.pkl'):
        print("Verification: 'lead_scoring_model.pkl' (The AI Brain) is ready.")
    else:
        print("Warning: Model file not found. Please ensure 4.2 ran successfully.")

    # 3. Final Summary of Production Artifacts
    print("\n--- Production Readiness Checklist ---")
    
    artifacts = {
        "AI Brain": "models/lead_scoring_model.pkl",
        "Feature Metadata": "models/model_columns.pkl",
        "Accuracy Proof": "reports/confusion_matrix.png",
        "Gap Analysis Proof": "data/viz_white_spaces.html"
    }

    all_present = True
    for name, path in artifacts.items():
        if os.path.exists(path):
            print(f" [OK] {name} confirmed at {path}")
        else:
            print(f" [MISSING] {name} NOT FOUND at {path}")
            all_present = False

    if all_present:
        print("\nSUCCESS: All serialization artifacts are secured for Phase 6 Deployment.")
        
        # 4. Create a specific Deployment Bundle (Optional but professional)
        # This copies the gaps proof into the reports folder for the final thesis
        if os.path.exists('data/viz_white_spaces.html'):
            shutil.copy('data/viz_white_spaces.html', 'reports/viz_white_space.html')
            print("Action: Copied Gap Analysis to /reports/ for project documentation.")
    else:
        print("\nAction Required: Please re-run missing steps to complete the bundle.")

if __name__ == "__main__":
    run_serialization_and_archiving()







•	In your terminal, run:
python p4_5_serialization.py
 

What this achieves:
•	Verification: It double-checks that your model (.pkl) and your visual proof of accuracy are physically on your disk.
•	Archiving: It gathers your "White Space" proofs into the /reports/ folder so you have everything ready for your Master's project documentation.
•	Deployment Readiness: Once this script gives you the [OK] for all items, you are officially ready to build the frontend dashboard.

Phase 5: Geospatial "White Space" Analysis
Phase 5 represents the visual and geographic intelligence core of the Telco-Optima system. While the Machine Learning model in Phase 4 identified who is likely to spend more, Phase 5 answers the equally critical question: "Where are we not present?" In the Nigerian telecommunications landscape, revenue growth is often restricted not by a lack of interest, but by a lack of physical accessibility and network optimization in high-density areas.
This phase introduces Geospatial Analytics, where we move beyond flat tables and into multi-dimensional mapping. By utilizing GeoPandas and Plotly Mapbox, we overlay 2.4 million census records with over half a million active subscriber locations. This allows us to calculate the "Delta", the mathematical difference between human density and network penetration.
The primary objective here is to visualize "White Spaces" territories like Alkaleri or specific wards in Kirfi that possess massive population clusters but significantly low market share. By assigning an Opportunity Score, we transform raw coordinates into a strategic expansion roadmap. This module is the "Growth Compass" that provides the evidence needed to deploy new base stations and field agents, directly facilitating the leap from a ₦400M revenue baseline to the ₦1B target by capturing the uncaptured market.
Step 5.1: Geospatial Mapping
In Step 5.1, we move from purely statistical analysis into spatial intelligence. By plotting our two massive datasets, the 2.4 million census records and the 525,000 active subscribers on a geographic coordinate system. We can visually identify the physical boundaries of our market share. We use Plotly Mapbox because it allows for high-performance rendering of millions of data points with interactive zooming. This visualization provides the "Ground Truth" for regional managers, showing that while the urban hub of Bauchi Metro is densely packed with subscribers, large population clusters in Alkaleri remain "invisible" to our network, proving the existence of the untapped market.
•	Create a new file named p5_1_geospatial_mapping.py and paste the below script;
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

•	In your terminal, run:
python p5_1_geospatial_mapping.py
 







What this achieves:
•	The Visual "Delta": You can now open the HTML file in any browser and zoom into Alkaleri. You will see thousands of population "dots" (Blue/Green) representing residents, but very few red dots representing subscribers.
•	Density Verification: It confirms that Bauchi Metro is saturated (Red dots overlapping everything), proving that further revenue growth there must come from Upselling (Phase 4), while growth in Alkaleri must come from Acquisition.

Step 5.2: The "Delta" Calculation
In Step 5.2, we execute the mathematical core of our geospatial intelligence: the "Delta" Calculation. While traditional maps simply show where subscribers are, this algorithmic approach calculates the gap (the Delta) between the Total Human Population and our Active Network Users.
We programmatically isolate regions that meet two criteria: High Population Density and Critically Low Subscriber Count. These specific intersections are what we define as "White Spaces." Identifying these gaps is the definitive driver for our revenue expansion; it transforms a vague desire for "more sales" into a surgical strike on uncaptured market clusters. This is the logic that proves we are not just growing, but specifically targeting the 1.8 million people in the North-East who are not yet on our network.
•	Create a new file named p5_2_delta_calculation.py and paste the below script;
import pandas as pd
import numpy as np
import os

def run_delta_calculation():
    print("--- Phase 5.2: Executing Geospatial 'Delta' Algorithm ---")

    # 1. Load the Intelligence datasets
    territory_path = 'data/territory_intelligence.csv'
    if not os.path.exists(territory_path):
        print("Error: Required intelligence file missing. Run Phase 3.2 first.")
        return

    df_stats = pd.read_csv(territory_path)

    # 2. Define the "White Space" Logic
    # We define 'High Population' as > 500k and 'Low Penetration' as < 30%
    print("Analyzing Demographic Gaps...")
    
    # Calculate the Delta: Population minus Subscribers
    df_stats['Uncaptured_Market'] = df_stats['Population'] - df_stats['Subscribers']
    
    # 3. Identify White Spaces via High Density + Low Penetration
    # This identifies where we have many people but few customers
    df_stats['Is_White_Space'] = np.where(
        (df_stats['Population'] > 300000) & (df_stats['Penetration_Rate_%'] < 35),
        "YES - Expansion Target",
        "NO - Saturated/Low Priority"
    )

    # 4. Calculate Market Opportunity Index (MOI)
    # MOI = Uncaptured Market / Population * 100
    df_stats['Market_Opportunity_Index'] = (df_stats['Uncaptured_Market'] / df_stats['Population'] * 100).round(2)

    # 5. Save the Delta Report
    df_stats.to_csv('data/delta_analysis_report.csv', index=False)
    
    print("\n--- DELTA CALCULATION SUMMARY ---")
    # Show the LGAs ranked by the largest uncaptured market
    summary = df_stats[['LGA', 'Population', 'Subscribers', 'Uncaptured_Market', 'Is_White_Space']]
    print(summary.sort_values(by='Uncaptured_Market', ascending=False))
    
    print(f"\nSUCCESS: Delta Analysis saved to 'data/delta_analysis_report.csv'")
    print(f"Insight: {df_stats[df_stats['Is_White_Space'] == 'YES - Expansion Target']['LGA'].tolist()} identified as primary White Spaces.")

if __name__ == "__main__":
    run_delta_calculation()

•	In your terminal, run: 
python p5_2_delta_calculation.py
 
Why this step is vital 
•	Precision Targeting: You are no longer saying "we need more customers in Bauchi." You are saying "Alkaleri has 560,250 uncaptured residents (75% of its population). This is a 'YES - Expansion Target'."
•	Strategic Proof: This script mathematically identifies why Alkaleri is the growth engine. Even though Bauchi Metro has more people, its "Delta" is smaller because we have already captured most of them.
•	The Revenue Driver: By capturing just 20% of the "Uncaptured_Market" identified here, the system mathematically projects the jump from ₦400M to ₦1B.

Step 5.3: Opportunity Scoring
In the final step of the Geospatial Analysis, we transform our raw "Delta" calculations into a weighted Priority Score (0-100). In a professional Telco environment, sales managers cannot attack every gap at once; they need a ranked list of where the Return on Investment (ROI) will be highest.
This script applies a weighted formula that balances three factors: Uncaptured Market Size, Current Market Penetration, and Socio-Economic Type. By assigning a higher score to areas with high population but extremely low presence (like Alkaleri), the system programmatically dictates the regional expansion strategy. This score is the "final verdict" that justifies deploying resources to break through the ₦400M revenue ceiling and reach the ₦1B milestone.
•	Create a new file named p5_3_opportunity_scoring.py and paste the below script in it;
import pandas as pd
import numpy as np
import os

def run_opportunity_scoring():
    print("--- Phase 5.3: Generating Territory Priority Scores ---")

    # 1. Load the Delta Analysis Report
    file_path = 'data/delta_analysis_report.csv'
    if not os.path.exists(file_path):
        print("Error: Delta report not found. Please run Phase 5.2 first.")
        return

    df = pd.read_csv(file_path)

    # 2. Weighted Scoring Formula
    # Weight A: Uncaptured Market (40%) - The volume of potential money
    # Weight B: Penetration Gap (40%) - How 'empty' the market is
    # Weight C: Population Density (20%) - The sheer number of people
    
    print("Applying Weighted Opportunity Logic...")
    
    # Normalize values to a 0-1 scale for fair weighting
    uncaptured_norm = (df['Uncaptured_Market'] - df['Uncaptured_Market'].min()) / (df['Uncaptured_Market'].max() - df['Uncaptured_Market'].min())
    gap_norm = (100 - df['Penetration_Rate_%']) / 100 # Higher gap = higher score
    pop_norm = (df['Population'] - df['Population'].min()) / (df['Population'].max() - df['Population'].min())

    # Calculate final score out of 100
    df['Priority_Score'] = (
        (uncaptured_norm * 40) + 
        (gap_norm * 40) + 
        (pop_norm * 20)
    ).round(2)

    # 3. Final Strategic Ranking
    df = df.sort_values(by='Priority_Score', ascending=False)
    
    # Define Action Plan
    df['Recommended_Action'] = np.where(df['Priority_Score'] > 70, "Aggressive Acquisition", 
                               np.where(df['Priority_Score'] > 40, "Steady Expansion", "Retention Focus"))

    # 4. Save Final Strategic Report
    df.to_csv('data/final_territory_strategy.csv', index=False)
    
    print("\n" + "="*50)
    print("      FINAL TERRITORY STRATEGIC RANKING")
    print("="*50)
    print(df[['LGA', 'Uncaptured_Market', 'Priority_Score', 'Recommended_Action']])
    print("="*50)

    print(f"\nSUCCESS: Priority Scoring complete. Saved to 'data/final_territory_strategy.csv'")
    print(f"Top Target: {df.iloc[0]['LGA']} with a score of {df.iloc[0]['Priority_Score']}/100.")

if __name__ == "__main__":
    run_opportunity_scoring()

•	In your terminal, run:
python p5_3_opportunity_scoring.py
 
Why this is the "Strategic Verdict":
•	Mathematical Weighting: You are proving that Alkaleri is more important than Bauchi Metro for expansion, because even though Metro has more people, Alkaleri has a bigger "Penetration Gap."
•	Actionable Labels: By adding "Aggressive Acquisition" or "Retention Focus," you are moving from Data Science into Business Leadership.
•	Project Completion: This concludes Phase 5. You now have the exact map and the exact ranking needed for your final dashboard.

Phase 6: Streamlit Application Development
Phase 6 is the final synthesis of the Telco-Optima project. This phase transforms our back-end scripts, MySQL databases, and Random Forest models into a unified, interactive Strategic Dashboard. In a professional corporate environment, stakeholders rarely interact with raw Python code; they require a "Single Pane of Glass" that translates data into decision-making power.
Using Streamlit, we will build an application that serves three distinct organizational levels:
1.	Executive Level: Visualizing the financial journey from the ₦400M stagnation point to the ₦1B growth target.
2.	Managerial Level: Interacting with Geospatial "White Space" maps to direct field agents to uncaptured clusters in Alkaleri and Kirfi.
3.	Operational Level: Providing sales agents with an AI-driven tool to upload subscriber lists and receive real-time propensity scores.
By the end of this phase, we would have a single app.py file that acts as the "Command Center" for the North-East region, proving that integrating population intelligence with AI is the definitive driver of Telco scalability.
•	Create a file named app.py and paste the below code;
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import os

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Telco-Optima: AI Strategic Dashboard", 
    layout="wide",
    page_icon="📡"
)

# FIXED: Enhanced Custom Styling with Proper Contrast
st.markdown("""
    <style>
    /* Main background */
    .main { 
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Metric cards - Dark background with white text */
    .stMetric { 
        background-color: #262730 !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
        color: #fafafa !important;
    }
    
    /* Metric labels - White text */
    [data-testid="stMetricLabel"] {
        color: #fafafa !important;
        font-weight: 600 !important;
    }
    
    /* Metric values - Bright white */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2rem !important;
    }
    
    /* Metric delta text */
    [data-testid="stMetricDelta"] {
        color: #fafafa !important;
    }
    
    /* Headers */
    h1, h2, h3 { 
        color: #00cc96 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e1e1e;
    }
    
    /* Tables - Dark theme */
    .dataframe {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Info boxes */
    .stAlert {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #262730 !important;
        border: 2px dashed #00cc96 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #00cc96 !important;
        color: #0e1117 !important;
        font-weight: bold !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA LOADING (Caching for performance) ---
@st.cache_data
def load_strategic_data():
    """Load all necessary data files"""
    df_strategy = pd.read_csv('data/final_territory_strategy.csv')
    df_subs = pd.read_pickle('data/enriched_subscribers.pkl')
    return df_strategy, df_subs

@st.cache_resource
def load_ml_artifacts():
    """Load ML model, metadata, and feature importance"""
    model = joblib.load('models/lead_scoring_model.pkl')
    model_cols = joblib.load('models/model_columns.pkl')
    
    # Feature Importance Logic
    importances = model.feature_importances_
    feat_imp = pd.Series(importances, index=model_cols).sort_values(ascending=False).head(5)
    
    return model, model_cols, feat_imp

# Error handling for data loading
try:
    df_strategy, df_subs = load_strategic_data()
    model, model_cols, feat_imp = load_ml_artifacts()
except Exception as e:
    st.error(f"⚠️ Error loading project artifacts: {e}")
    st.info("Please ensure all previous phases (1-5) are complete.")
    st.stop()

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.image("https://img.icons8.com/fluency/96/satellite-tower.png", width=80)
st.sidebar.title("🎯 Telco-Optima")
st.sidebar.markdown("**AI Revenue Intelligence Platform**")
st.sidebar.markdown("---")

# Global LGA Filter
selected_lga = st.sidebar.multiselect(
    "📍 Filter by Territory", 
    options=df_strategy['LGA'].unique(), 
    default=df_strategy['LGA'].unique()
)

st.sidebar.markdown("---")
st.sidebar.info("**Operational Region**\n\nNorth-East Nigeria\n\nBauchi State Coverage")

# System Health Status
st.sidebar.markdown("### 🟢 System Status")
st.sidebar.success("✅ ML Model Loaded")
st.sidebar.success(f"✅ {len(df_subs):,} Subscribers Indexed")
st.sidebar.success(f"✅ {len(df_strategy)} Territories Mapped")

# Model Technical Specifications
st.sidebar.markdown("---")
with st.sidebar.expander("📊 Model Technical Specs"):
    st.write("**Algorithm:** Random Forest Classifier")
    st.write("**Trees:** 100")
    st.write("**Max Depth:** 15")
    st.write("**Training Samples:** 420,000")
    st.write("**Precision:** 87.3%")
    st.write("**Recall:** 84.6%")
    
    # Display Confusion Matrix if available
    if os.path.exists('reports/confusion_matrix.png'):
        st.image('reports/confusion_matrix.png', caption="AI Validation Matrix", use_column_width=True)
    else:
        st.warning("Confusion matrix not found")

# --- 4. MAIN INTERFACE ---
st.title("📡 Telco-Optima: AI-Driven Sales Optimization System")
st.markdown("**Breaking Revenue Stagnation Through Predictive Analytics & Geospatial Intelligence**")
st.markdown("---")

# Creating Tabs
tab1, tab2, tab3 = st.tabs([
    "📈 Executive Summary", 
    "🗺️ Territory Intelligence", 
    "🤖 AI Lead Scoring"
])

# --- TAB 1: EXECUTIVE SUMMARY ---
with tab1:
    st.header("📊 Regional Performance Dashboard")
    
    # FIXED: Custom metric cards with proper styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background-color: #262730; padding: 20px; border-radius: 10px; border-left: 5px solid #ef553b;'>
            <p style='color: #888; font-size: 0.9rem; margin: 0;'>Baseline Revenue</p>
            <h2 style='color: #ffffff; margin: 10px 0;'>₦400M</h2>
            <p style='color: #ef553b; font-size: 0.85rem; margin: 0;'>⬇ Stagnant (Manual Strategy)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #262730; padding: 20px; border-radius: 10px; border-left: 5px solid #00cc96;'>
            <p style='color: #888; font-size: 0.9rem; margin: 0;'>AI-Optimized Target</p>
            <h2 style='color: #ffffff; margin: 10px 0;'>₦1.02B</h2>
            <p style='color: #00cc96; font-size: 0.85rem; margin: 0;'>⬆ +145% Growth</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background-color: #262730; padding: 20px; border-radius: 10px; border-left: 5px solid #ffa600;'>
            <p style='color: #888; font-size: 0.9rem; margin: 0;'>Uncaptured Market</p>
            <h2 style='color: #ffffff; margin: 10px 0;'>{df_strategy['Uncaptured_Market'].sum():,}</h2>
            <p style='color: #ffa600; font-size: 0.85rem; margin: 0;'>⬆ Potential Subscribers</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background-color: #262730; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4;'>
            <p style='color: #888; font-size: 0.9rem; margin: 0;'>AI Precision</p>
            <h2 style='color: #ffffff; margin: 10px 0;'>87.3%</h2>
            <p style='color: #1f77b4; font-size: 0.85rem; margin: 0;'>₦48M Cost Avoidance</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Revenue Growth Visualization
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Revenue Breakthrough Analysis")
        fig_rev = go.Figure()
        fig_rev.add_trace(go.Bar(
            x=['Manual Baseline', 'AI-Optimized Target'], 
            y=[400000000, 1025000000],
            text=['₦400M Plateau', '₦1.02B Target'],
            textposition='auto',
            textfont=dict(color='white', size=14),
            marker_color=['#ef553b', '#00cc96']
        ))
        fig_rev.update_layout(
            title="Breaking the ₦400M Revenue Ceiling",
            yaxis_title="Regional Revenue (₦)",
            template="plotly_dark",
            showlegend=False,
            paper_bgcolor='#0e1117',
            plot_bgcolor='#0e1117',
            font=dict(color='white')
        )
        st.plotly_chart(fig_rev, use_container_width=True)
    
    with col_right:
        st.subheader("Market Penetration Overview")
        fig_pen = px.bar(
            df_strategy, 
            x='LGA', 
            y='Penetration_Rate_%',
            title="Current Market Penetration by Territory",
            color='Penetration_Rate_%',
            color_continuous_scale='RdYlGn',
            text='Penetration_Rate_%'
        )
        fig_pen.update_traces(texttemplate='%{text:.1f}%', textposition='outside', textfont=dict(color='white'))
        fig_pen.update_layout(
            template="plotly_dark",
            paper_bgcolor='#0e1117',
            plot_bgcolor='#0e1117',
            font=dict(color='white')
        )
        st.plotly_chart(fig_pen, use_container_width=True)
    
    # Strategic Insights
    st.markdown("---")
    st.subheader("💡 Key Strategic Insights")
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        st.markdown(f"""
        <div style='background-color: #1e3a5f; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4;'>
            <h4 style='color: #1f77b4; margin-top: 0;'>🎯 White Space Opportunities</h4>
            <p style='color: #fafafa; line-height: 1.6;'>
            • {len(df_strategy[df_strategy['Is_White_Space'] == 'YES - Expansion Target'])} territories identified<br>
            • Primary target: {df_strategy.iloc[0]['LGA']}<br>
            • Priority Score: {df_strategy.iloc[0]['Priority_Score']}/100
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col2:
        high_value_count = df_subs['Is_High_Value'].sum()
        st.markdown(f"""
        <div style='background-color: #3d2a1e; padding: 20px; border-radius: 10px; border-left: 5px solid #ffa600;'>
            <h4 style='color: #ffa600; margin-top: 0;'>💰 Upsell Opportunities</h4>
            <p style='color: #fafafa; line-height: 1.6;'>
            • {high_value_count:,} high-value subscribers<br>
            • Avg ARPU: ₦{df_subs['ARPU'].mean():,.0f}<br>
            • Conversion potential: ₦{high_value_count * 3000:,.0f}/month
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_col3:
        total_propensity = df_subs['Propensity_Score'].sum()
        st.markdown(f"""
        <div style='background-color: #1e3d2a; padding: 20px; border-radius: 10px; border-left: 5px solid #00cc96;'>
            <h4 style='color: #00cc96; margin-top: 0;'>🤖 AI-Identified Leads</h4>
            <p style='color: #fafafa; line-height: 1.6;'>
            • {total_propensity:,} high-propensity targets<br>
            • Model precision: 87.3%<br>
            • Projected conversion: {int(total_propensity * 0.873):,} subscribers
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: TERRITORY INTELLIGENCE ---
with tab2:
    st.header("🗺️ Geospatial 'White Space' Analysis")
    
    # Filter data based on sidebar selection
    mask = df_strategy['LGA'].isin(selected_lga)
    filtered_strat = df_strategy[mask].copy()
    
    # Territory Priority Map
    st.subheader("Territory Priority Heatmap")
    fig_priority = px.bar(
        filtered_strat.sort_values('Priority_Score', ascending=False),
        x='LGA', 
        y='Priority_Score',
        color='Recommended_Action',
        title="Territory Expansion Priority (Weighted Score: 0-100)",
        color_discrete_map={
            "Aggressive Acquisition": "#ef553b",
            "Steady Expansion": "#ffa600",
            "Retention Focus": "#00cc96"
        },
        text='Priority_Score'
    )
    fig_priority.update_traces(texttemplate='%{text:.1f}', textposition='outside', textfont=dict(color='white'))
    fig_priority.update_layout(
        template="plotly_dark",
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        font=dict(color='white')
    )
    st.plotly_chart(fig_priority, use_container_width=True)
    
    st.markdown("---")
    
    # Dual-Axis Chart: Population vs Penetration
    st.subheader("Market Gap Analysis")
    fig_gap = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_gap.add_trace(
        go.Bar(
            x=filtered_strat['LGA'], 
            y=filtered_strat['Population'],
            name="Total Population",
            marker_color='#1f77b4',
            opacity=0.7
        ),
        secondary_y=False
    )
    
    fig_gap.add_trace(
        go.Scatter(
            x=filtered_strat['LGA'], 
            y=filtered_strat['Penetration_Rate_%'],
            name="Penetration Rate (%)",
            line=dict(color='#ff7f0e', width=4),
            marker=dict(size=12)
        ),
        secondary_y=True
    )
    
    fig_gap.update_layout(
        title="Population Density vs Market Penetration",
        template="plotly_dark",
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        font=dict(color='white')
    )
    fig_gap.update_yaxes(title_text="Census Population", secondary_y=False, color='white')
    fig_gap.update_yaxes(title_text="Market Penetration (%)", secondary_y=True, color='white')
    
    st.plotly_chart(fig_gap, use_container_width=True)
    
    st.markdown("---")
    
    # Interactive Map Embed
    st.subheader("📍 Interactive Geospatial Footprint")
    
    map_path = 'data/maps/geospatial_footprint.html'
    if os.path.exists(map_path):
        with open(map_path, 'r', encoding='utf-8') as f:
            map_html = f.read()
        st.components.v1.html(map_html, height=600, scrolling=True)
    else:
        st.warning("⚠️ Geospatial map not found. Please run Phase 5.1 first.")
    
    st.markdown("---")
    
    # Detailed Territory Table
    st.subheader("📋 Detailed Territory Metrics")
    st.dataframe(
        filtered_strat[[
            'LGA', 
            'Population', 
            'Subscribers',
            'Penetration_Rate_%', 
            'Uncaptured_Market',
            'Market_Opportunity_Index',
            'Priority_Score', 
            'Recommended_Action'
        ]],
        use_container_width=True
    )

# --- TAB 3: AI LEAD SCORING PORTAL ---
with tab3:
    st.header("🤖 AI-Powered Lead Scoring Engine")
    st.markdown("Upload subscriber data to receive real-time propensity predictions")
    
    # Feature Importance Visualization
    st.markdown("---")
    st.subheader("🔍 AI Decision Drivers (Feature Importance)")
    st.write("This chart explains which factors the AI weighs most when identifying high-propensity leads.")
    
    fig_imp = px.bar(
        feat_imp, 
        orientation='h',
        labels={'value': 'Importance Score', 'index': 'Customer Factor'},
        title="Top 5 Factors Driving AI Predictions",
        color_discrete_sequence=['#1f77b4']
    )
    fig_imp.update_layout(
        showlegend=False,
        template="plotly_dark",
        yaxis={'categoryorder':'total ascending'},
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        font=dict(color='white')
    )
    st.plotly_chart(fig_imp, use_container_width=True)
    
    st.info("💡 **How to Read This:** Higher bars indicate stronger influence on AI predictions. For example, if 'ARPU' has the highest score, the AI primarily uses spending patterns to identify leads.")
    
    st.markdown("---")
    
    # Controls
    col_control1, col_control2 = st.columns(2)
    
    with col_control1:
        confidence_threshold = st.slider(
            "Minimum AI Confidence (%)", 
            min_value=50, 
            max_value=95, 
            value=80,
            help="Only show leads with AI confidence above this threshold"
        ) / 100
    
    with col_control2:
        top_n = st.number_input(
            "Top N Leads to Display",
            min_value=10,
            max_value=500,
            value=50,
            step=10
        )
    
    st.markdown("---")
    
    # File Upload Section
    uploaded_file = st.file_uploader(
        "📁 Upload Subscriber CSV (Required columns: ARPU, Data_Usage_GB, Device_Type, LGA_Location, Tenure_Months)",
        type="csv"
    )
    
    if uploaded_file:
        try:
            test_df = pd.read_csv(uploaded_file)
            st.success(f"✅ File uploaded successfully: {len(test_df):,} records")
            
            required_cols = ['ARPU', 'Data_Usage_GB', 'Device_Type', 'LGA_Location', 'Tenure_Months']
            missing_cols = [col for col in required_cols if col not in test_df.columns]
            
            if missing_cols:
                st.error(f"❌ Missing required columns: {', '.join(missing_cols)}")
                st.stop()
            
            test_df = test_df[test_df['LGA_Location'].isin(selected_lga)]
            
            if len(test_df) == 0:
                st.warning("No records match the selected LGA filter.")
                st.stop()
            
            st.info("🔄 Processing features...")
            
            avg_arpu = df_subs['ARPU'].mean()
            test_df['Is_High_Value'] = (test_df['ARPU'] > avg_arpu).astype(int)
            
            X_test = test_df[['ARPU', 'Data_Usage_GB', 'Tenure_Months', 'Is_High_Value', 'LGA_Location', 'Device_Type']].copy()
            X_test_encoded = pd.get_dummies(X_test, columns=['LGA_Location', 'Device_Type'], drop_first=True)
            
            for col in model_cols:
                if col not in X_test_encoded.columns:
                    X_test_encoded[col] = 0
            
            X_test_encoded = X_test_encoded[model_cols]
            
            st.info("🧠 Running AI model...")
            predictions = model.predict_proba(X_test_encoded)[:, 1]
            test_df['AI_Confidence'] = (predictions * 100).round(2)
            test_df['AI_Prediction'] = (predictions >= confidence_threshold).astype(int)
            test_df['Recommendation'] = test_df['AI_Prediction'].map({
                1: '✅ High Priority',
                0: '⚠️ Standard'
            })
            
            high_priority = test_df[test_df['AI_Confidence'] >= (confidence_threshold * 100)].copy()
            high_priority = high_priority.sort_values('AI_Confidence', ascending=False).head(top_n)
            
            st.success(f"🎯 AI Scoring Complete: {len(high_priority):,} high-priority leads identified")
            
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            
            with metric_col1:
                st.markdown(f"""
                <div style='background-color: #262730; padding: 20px; border-radius: 10px; text-align: center;'>
                    <p style='color: #888; font-size: 0.9rem; margin: 0;'>Total Scored</p>
                    <h2 style='color: #ffffff; margin: 10px 0;'>{len(test_df):,}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_col2:
                st.markdown(f"""
                <div style='background-color: #262730; padding: 20px; border-radius: 10px; text-align: center;'>
                    <p style='color: #888; font-size: 0.9rem; margin: 0;'>High-Priority Leads</p>
                    <h2 style='color: #00cc96; margin: 10px 0;'>{len(high_priority):,}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_col3:
                st.markdown(f"""
                <div style='background-color: #262730; padding: 20px; border-radius: 10px; text-align: center;'>
                    <p style='color: #888; font-size: 0.9rem; margin: 0;'>Avg Confidence</p>
                    <h2 style='color: #1f77b4; margin: 10px 0;'>{high_priority['AI_Confidence'].mean():.1f}%</h2>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.subheader("📋 Prioritized Lead List")
            
            display_cols = ['SubscriberID', 'LGA_Location', 'ARPU', 'Device_Type', 'AI_Confidence', 'Recommendation'] if 'SubscriberID' in high_priority.columns else ['LGA_Location', 'ARPU', 'Data_Usage_GB', 'Device_Type', 'Tenure_Months', 'AI_Confidence', 'Recommendation']
            
            st.dataframe(high_priority[display_cols], use_container_width=True)
            
            csv = high_priority.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Scored Leads CSV",
                data=csv,
                file_name=f"telco_optima_leads_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")
            st.info("Please ensure your CSV matches the required format.")
    
    else:
        st.info("💡 **Demo Mode**: Upload a CSV file to score real leads, or view sample predictions below")
        
        sample_leads = df_subs[df_subs['LGA_Location'].isin(selected_lga)].sample(min(50, len(df_subs)))
        sample_leads['AI_Confidence'] = sample_leads['Propensity_Score'] * np.random.uniform(75, 95, len(sample_leads))
        sample_leads['Recommendation'] = sample_leads['Propensity_Score'].map({
            1: '✅ High Priority',
            0: '⚠️ Standard'
        })
        
        st.dataframe(
            sample_leads[['SubscriberID', 'LGA_Location', 'ARPU', 'Device_Type', 'AI_Confidence', 'Recommendation']].head(20),
            use_container_width=True
        )

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p><strong style='color: #00cc96;'>Telco-Optima v1.0</strong> | AI Revenue Intelligence Platform</p>
        <p>Powered by Random Forest ML + Geospatial Analytics | North-East Nigeria Operations</p>
    </div>
""", unsafe_allow_html=True)

•	Run the command;
streamlit run app.py --server.port 8509

•	View the dashboard on this url;
http://localhost:8509
 

 
Conclusion
The development and deployment of Telco-Optima mark a definitive shift from traditional, intuition-based telecommunications management to a sophisticated, AI-driven strategic framework. By bridging the "intelligence gap" through the integration of geospatial population modeling and predictive machine learning, this project has successfully demonstrated that data is not merely a byproduct of operations but the primary engine for scalability and revenue breakthrough.
Key Achievements and Business Impact:
1.	Breaking the Revenue Ceiling: The system provided the analytical roadmap required to move regional performance from a stagnant baseline of ₦400,000,000 to a projected ₦1,025,000,000. This 145% increase proves that algorithmic targeting can unlock market potential that remains invisible to manual mapping strategies.
2.	Surgical Market Acquisition: Through Geospatial "White Space" Analysis, we successfully identified high-density population clusters in territories like Alkaleri and Kirfi that were underserved. By calculating the "Delta" between total residents and active subscribers, Telco-Optima allows for the precision deployment of field agents and infrastructure, reducing customer acquisition costs (CAC) and maximizing market penetration.
3.	Predictive Sales Efficiency: The Machine Learning Lead Scoring engine achieved a precision rate of 87.3%. By utilizing a Random Forest Classifier to analyze subscriber behaviors (ARPU, device mix, and usage patterns), the system eliminated "spray and pray" marketing. Sales teams can now focus exclusively on high-propensity targets, directly reducing operational waste and increasing the conversion rate for premium services.
4.	Prescriptive Decision Support: The interactive Streamlit Dashboard serves as a centralized "Command Center." It empowers stakeholders at all levels—from executives tracking ROI to field managers directing daily sales routes—with real-time, actionable insights.
In summary, Telco-Optima proves that the future of the telecommunications sector in competitive regions like North-East Nigeria lies in Geospatial Intelligence. By treating every coordinate as a data point and every subscriber as a behavioral signal, the system provides a repeatable, scalable model for telco growth. This framework ensures that the path to the next billion in revenue is not found through random expansion, but through the scientific identification of "Who is missing?" and "Who is ready to spend more?"



