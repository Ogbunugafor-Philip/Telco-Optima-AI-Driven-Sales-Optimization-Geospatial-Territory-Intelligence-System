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


#### What this script just did:

•	Bounding Box Encoding: It restricted every resident to the specific latitude/longitude limits of Bauchi, Alkaleri, and Kirfi.

•	Density Simulation: It created a high-density urban cluster for Bauchi Metro (1.34M dots) and sparse rural clusters for Kirfi (322k dots).

•	GIS Foundation: It created the population_ground_truth.csv file. This is your "Denominator" that you will use later to find the Delta (White Spaces).

#### Step 2.2: Subscriber Data Generation (Telco Logs)
Phase 2.2 focuses on building the "Business Layer"; the existing customer base. This phase involves generating 525,000 synthetic subscriber records that simulate internal billing and usage logs. This dataset provides the behavioral "signals" required for the Predictive Lead Scoring engine, allowing the system to distinguish between basic users and high-propensity targets.
The generation process is governed by a Socio-Economic Weighted Logic to mirror the North-East regional market. We distribute the records strategically: 50% in Bauchi Metro, 35% in Alkaleri, and 15% in Kirfi. By integrating the Faker library with custom probability distributions, we encode specific attributes into each profile, such as ARPU (Average Revenue Per User), Data Usage, and Device Type.
This phase is critical for simulating Economic Disparities. In the system, urban subscribers are assigned higher spending limits and flagship devices, while rural records reflect lower spend and basic phones. This realistic distribution creates a high-fidelity "Training Ground" for the AI, enabling it to learn the patterns necessary to break through the ₦400M revenue plateau and identify the next ₦1B in growth.

•	Create a file named p2_2_subscriber_engine.py and paste the below;

[p2_2_subscriber_engine.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p2_2_subscriber_engine.py)

•	Run the script;
```
python p2_2_subscriber_engine.py
```
 <img width="975" height="415" alt="image" src="https://github.com/user-attachments/assets/22f9b22c-7d48-41e4-b544-fa3ffdb7ad4c" />



#### What This Script Does (The Logic Breakdown)
When you run this command, the "Subscriber Engine" performs four high-level operations to simulate a realistic telecommunications environment:

1.	Socio-Economic Segmentation: The script divides the 525,000 records into three groups based on your strategic LGAs. It assigns 50% to Bauchi Metro, 35% to Alkaleri, and 15% to Kirfi, mimicking the actual population density and market presence in these areas.

2.	Advanced ARPU Modeling (The "Rural Millionaire" Logic): Instead of using simple averages, it uses a Log-Normal Distribution. This ensures that while most rural users spend less, the script naturally generates "outliers" high-value customers in Kirfi or Alkaleri who spend as much as, or more than, urban users.

3.	Behavioral Enrichment: It assigns each subscriber a specific Device Type, Data Usage (GB), and Tenure.

o	In the City: Higher probability of 5G-enabled premium devices and heavy streaming usage.

o	In Rural Zones: Higher probability of feature phones and voice-centric usage, but with a 5% "Premium" flag to account for high-net-worth individuals in developing zones.

4.	Automated Data Logging: Finally, it compiles these half-a-million records into a single DataFrame and exports it directly into your data/ folder as NE_Sub_Billing_P2_2.csv. This file becomes the "Source of Truth" for your ML model to learn from in the next phase.

#### Step 2.3: Database Architecture & ETL Injection (NEW):
Phase 2.3 transitions the project from local flat files to a professional Data Warehouse environment. In a high-scale Telecommunications setting, managing 525,000 subscriber records requires a structured Relational Database Management System (RDBMS). This phase focuses on designing a robust MySQL Schema named telco_optima_db and implementing a custom ETL (Extract, Transform, Load) pipeline to simulate how industrial data centers ingest and process massive daily traffic.
The architecture begins with the creation of the database schema, specialized for high-speed analytical queries. Unlike standard transactional databases, this schema is optimized for Prescriptive Analytics by defining tables with strict data types and strategic indexing. This ensures that the Machine Learning and Geospatial modules can query subscriber data with zero latency, providing the structural integrity needed to drive regional revenue from ₦400M to ₦1B.
The ETL Injection serves as the system's "circulatory system," using a Python-based engine to automate the movement of data. The process involves Extracting raw subscriber and population data from Phase 2.1 and 2.2, Transforming it for SQL compatibility, and loading it into the MySQL environment. To simulate a real-world data warehouse, records are injected in batches of 10,000, which prevents memory overload and mirrors the process of updating central repositories from regional sales logs.
By the end of this phase, Telco-Optima moves from a script-based tool to a permanent, database-backed platform. This transition is critical for scalability, ensuring that as the population and subscriber counts grow, the system remains a reliable single source of truth for identifying "White Spaces" and high-propensity leads.

•	Before running the code, ensure you have MySQL Server installed and running on your machine. Run;
```
pip install mysql-connector-python
```
<img width="975" height="179" alt="image" src="https://github.com/user-attachments/assets/7510101a-4d69-4eb3-8f9a-cfb48488a019" />


•	Create the ETL file named p2_3_db_injection.py and paste the below;

[p2_3_db_injection.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p2_3_db_injection.py)


•	Run the command;
```
python p2_3_db_injection.py
```
<img width="975" height="440" alt="image" src="https://github.com/user-attachments/assets/67c65537-6d28-465f-87b2-77c69c102f9d" />

 
#### What is happening in this implementation?

•	Schema Creation: It automatically creates the telco_optima_db. You don't need to do it manually in phpMyAdmin.

•	The "T" in ETL: The script ensures that data types are correct (e.g., ARPU is a FLOAT, Tenure is an INT) before they hit the database.

•	The "L" (Batch Loading): By using execute many with 10,000 records at a time, we ensure the injection is fast and doesn't time out the server. This is exactly how high-volume telco data is moved.

#### Step 2.4: Target Variable Creation
Phase 2.4 is the transition from raw data storage to AI Readiness. In Machine Learning, a model cannot learn unless it has a "target" or "label" to predict. Think of this step as creating the Answer Key for a test. We are going to programmatically evaluate our 525,000 subscribers and tag them with a Propensity_Score (0 or 1). A "1" represents a subscriber who has a high likelihood of upgrading or "converting" to a premium plan, while a "0" represents a standard user.
This process is known as Feature Engineering. Instead of using random labels, we apply business-driven logic based on the North-East regional market. For example, if a subscriber in Bauchi Metro has high data consumption but is on a low-value plan, they are a prime candidate for an upgrade. By creating this variable, we are teaching the AI exactly what a "High-Value Lead" looks like. Later, the model will analyze thousands of these examples to find hidden patterns that a human analyst would miss.
This step is the final "bridge" in your data pipeline. Once we have these labels, your dataset changes from a simple list of names and numbers into a Supervised Learning Dataset. This is the foundation required to build the predictive engine that will identify the specific customers needed to scale your revenue from ₦400M to ₦1B.

•	Create a new file called p2_4_target_engineering.py and paste the below script

[p2_4_target_engineering.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p2_4_target_engineering.py)

#### Why This Implementation Matters

Feature Engineering: We are not just storing data; we are creating new knowledge. The np.where logic acts as an "expert system" that pre-identifies high-value leads for the AI to study.

Binary Classification: Most machine learning models for propensity (likelihood to act) require a 1 (Success) or 0 (No Action) target.

Database Synchronization: By using an UPDATE command, we ensure your MySQL database stays in sync with your Python logic, making it a "Live" data warehouse for the next phases.

•	Run the command;
```
python p2_4_target_engineering.py
```
<img width="975" height="403" alt="image" src="https://github.com/user-attachments/assets/a014715e-7c72-4cc1-8026-fc11fd0fe2ba" />
 

### Phase 3: Data Preprocessing & Exploratory Analysis (EDA)
With the data successfully "manufactured" and stored in our MySQL warehouse, Phase 3 represents the analytical bridge of the project. Raw data, even when structured, is rarely ready for Machine Learning. Before our Random Forest model can begin learning, we must transition from Data Engineering to Data Science.
Phase 3 is dedicated to refining our 525,000 subscriber records and 2.4 million census points into a clean, high-signal dataset. This phase serves three critical functions:

1.	Ensuring Data Integrity (Cleaning): We audit the synthetic logs to ensure no "impossible" values exist (e.g., negative data usage or missing coordinates) that could skew our results.

2.	Uncovering the "Why" (EDA): Through Exploratory Data Analysis, we will statistically prove the "Revenue Stagnation" problem. By visualizing current performance, we can see exactly where the ₦400M plateau occurs and validate the economic disparities between the urban hub of Bauchi Metro and the rural zones of Kirfi.

3.	Synthesizing New Intelligence (Feature Engineering): This is the most vital step for our Geospatial objective. We will programmatically calculate the Market Penetration Rate; the ratio of active subscribers to total population. This calculation is what finally reveals the "White Spaces": those high-density population clusters where our network footprint is large, but our subscriber count is low.

By the end of this phase, we will have moved from a collection of tables to a set of actionable insights. We will have a clear, visual map of our "intelligence gap," setting the stage for the AI to begin predicting exactly who our next high-value customers will be.

#### Step 3.1: Data Cleaning
In the lifecycle of a telecommunications data pipeline, the transition from raw ingestion to analytical readiness depends entirely on the integrity of the dataset. Phase 3.1 serves as the quality assurance gate where we perform a Structural Audit on our 525,000 subscriber records to eliminate "noise" that could degrade our AI's predictive accuracy. By identifying and handling null values, capping extreme ARPU outliers that could skew our revenue projections, and enforcing logical consistency across urban and rural device distributions, we transform raw logs into a high-fidelity "Gold Standard" dataset. This process ensures that the subsequent 145% revenue growth projections are based on stable, statistically sound data rather than simulation artifacts.

•	Create a new file named p3_1_data_cleaning.py and paste the below script;

[p3_1_data_cleaning.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p3_1_data_cleaning.py)
  

#### What this script does:

1.	Audits for Errors: Removes any empty or corrupted rows from the 525,000 records.

2.	Caps Outliers: Limits extreme high-spenders (top 1%) so they don't skew the AI's learning.

3.	Validates Voice-Only Users: Verifies that Feature Phone users have 0.00 GB data usage but still show revenue from call cards.

4.	Creates a Checkpoint: Saves the clean data as a .pkl file to preserve formatting for the mapping phase.

•	Run the following command;
```
python p3_1_data_cleaning.py
```
<img width="975" height="374" alt="image" src="https://github.com/user-attachments/assets/16f3b75e-b462-4c9e-836e-4745535b7756" />
 
#### Step 3.2: Feature Engineering:
Feature Engineering is the process of transforming raw data into meaningful indicators that drive business strategy. In this phase, we move beyond simple cleaning to create two critical intelligence layers: Market Penetration Rates and High-Value Flags. By calculating the ratio of subscribers to the total population for each LGA, we mathematically pinpoint the "White Space" opportunities where the market is most underserved. Simultaneously, we perform behavioral tagging at the subscriber level by identifying "High-Value" customers whose spending exceeds the regional average. These new features are the engine of our prescriptive analytics, allowing the system to determine exactly where to expand and who to target for premium services to break the ₦400M revenue ceiling.

•	Create a new file named p3_2_feature_engineering.py and paste the below script

[p3_2_feature_engineering.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p3_2_feature_engineering.py)

•	In your terminal, run: 
```
python p3_2_feature_engineering.py
```
 <img width="975" height="406" alt="image" src="https://github.com/user-attachments/assets/50e42045-2537-4151-9411-353724cb176d" />

#### What happens in this step:

•	The Delta Calculation: It automatically compares your 2.4 million residents against your 525,000 subscribers to see where the market is "empty."

•	Acquisition Priority: It labels LGAs as High Priority if they have a low penetration rate but high population, telling the sales team exactly where to send field agents.

•	Behavioral Tagging: Every subscriber is now tagged with Is_High_Value. This allows the AI in Phase 4 to differentiate between a standard customer and a "Power User."

#### Step 3.3: EDA & Visualization
With our features engineered, Phase 3.3 shifts focus to Visual Evidence. In this phase, we use data visualization to transform abstract numbers into a compelling business case. We will generate specific charts to visually "prove" the two core pillars of this project: the historical Revenue Stagnation at the ₦400,000,000 plateau and the identification of "White Spaces" in territories like Alkaleri. By overlaying population density with current market penetration, we expose the "Intelligence Gap" that caused previous growth to stall. These visualizations serve as the diagnostic tool for regional managers, shifting the strategy from intuition-based coverage to data-driven precision.

•	Create a new file named p3_3_eda_visualization.py and paste the below script

[p3_3_eda_visualization.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p3_3_eda_visualization.py)

•	In your terminal, run; 
```
python p3_3_eda_visualization.py
``` 
<img width="975" height="273" alt="image" src="https://github.com/user-attachments/assets/f9a40ba0-b847-4183-9b0c-946c5617523c" />

#### What these charts prove

1.	The Stagnation Chart: Clearly shows the revenue ceiling that manual territory management hit and how AI-driven optimization targets a 145% increase.

2.	The White Space Chart: Highlights that Alkaleri and Kirfi have large uncaptured populations compared to the urban hub. Even if the population is lower than Metro, a low penetration rate indicates a "Greenfield" opportunity for mass acquisition.

3.	The Device Box Plot: Confirms that feature phone segments (Nokia/Feature Phone) show 0.00 GB usage, justifying why we need to target ARPU from calls rather than just data bundles in those zones.

### Phase 4: Machine Learning Model Development
Phase 4 represents the transition of Telco-Optima from a descriptive system to a predictive powerhouse. While the previous phases identified where the gaps are and what happened in the past, this phase builds the "Intelligence Engine" capable of forecasting future subscriber behavior. In a high-scale telecommunications environment, simply having data is insufficient; the competitive advantage lies in the ability to predict which customers are most likely to upgrade their services before a sales agent even makes a call.
In this phase, we implement a Random Forest Classifier, a robust ensemble learning algorithm chosen for its ability to handle the complex, non-linear relationships found in subscriber data (such as the interaction between tenure, device type, and spending habits). We move beyond simple accuracy to focus on high-precision metrics. In a business context, Precision is critical because it ensures sales teams do not waste operational hours on "False Positives" subscribers who have no actual intent to upgrade.
By the end of this phase, the system will be able to ingest raw subscriber logs and output a "Lead List" ranked by AI confidence. This predictive capability is the primary driver behind the transition from the ₦400,000,000 revenue plateau to the ₦1,000,000,000 target, as it allows for the surgical allocation of sales resources toward the highest-probability revenue opportunities.

#### Step 4.1: Data Splitting 
Data splitting is the foundational step of Supervised Machine Learning, where we establish a rigorous testing environment for our AI. By dividing our 525,000 records into a Training Set (80%) and a Testing Set (20%), we create a "blind test" for the model. The Random Forest algorithm will learn the complex behavioral patterns of upgrade propensity from the training data, while the testing data records, the AI has never encountered will serve as the ultimate validator of its accuracy. During this phase, we also implement Categorical Encoding, transforming text-based indicators like "LGA Location" and "Device Type" into mathematical vectors. This structural preparation ensures that the lead scoring engine is not just learning by rote, but is capable of generalizing its intelligence across different territories to drive the target ₦1,000,000,000 revenue outcome.

•	Create a new file named p4_1_data_splitting.py and paste the below script;

[p4_1_data_splitting.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p4_1_data_splitting.py)

•	In your terminal, execute: 
```
python p4_1_data_splitting.py
```
<img width="975" height="368" alt="image" src="https://github.com/user-attachments/assets/e3591880-4ba9-4231-99ee-a02d543772ed" />
 
#### Key Actions Performed:

•	One-Hot Encoding: Converts territory and device names into binary columns (0s and 1s) so the Random Forest math engine can calculate correlations.

•	Stratification: Guaranteed that the percentage of "High-Propensity" leads is identical in both the Training and Testing sets, preventing bias in the evaluation phase.

•	Serialization: Saves the split data as .pkl files to preserve the new column structure, ensuring that Step 4.2 starts with a perfectly formatted environment.

#### Step 4.2: Model Training (Random Forest)
With the data split into training and testing sets, we now initialize the "Intelligence Engine." For this project, we utilize the Random Forest Classifier, an ensemble learning method that builds multiple decision trees and merges them together to get a more accurate and stable prediction. In the Telco context, this algorithm is ideal because it handles "non-linear" relationships. For example, a user with a Feature Phone and High ARPU might have a very different upgrade path than a Smartphone user with Low Tenure. The model will analyze the 420,000 training records to discover these hidden patterns, creating a mathematical formula that can score any subscriber's likelihood to upgrade.

•	Create a new file named p4_2_model_training.py and paste the below script;

[p4_2_model_training.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p4_2_model_training.py)

•	In your terminal, run: 
```
python p4_2_model_training.py
```
<img width="975" height="235" alt="image" src="https://github.com/user-attachments/assets/5d9349a2-d051-4eda-999a-d9edea3d8458" />

#### What is happening in this step:

•	Ensemble Learning: The script creates 100 different decision trees. Each tree "votes" on whether a subscriber is a high-propensity lead. The majority vote becomes the final prediction.

•	Depth Control: We set max_depth=15 to prevent the model from "overfitting" (memorizing the data too perfectly), ensuring it works well on new subscribers it hasn't seen yet.

•	Joblib Serialization: This "freezes" the trained brain of the AI into a file. When we build the Streamlit dashboard later, we can simply load this file to get instant predictions.

#### Step 4.3: Model Evaluation 
In any Master's level research, the evaluation phase is the most critical; it proves that the system actually works. Now that our Random Forest model has been trained, we must subject it to a rigorous audit using the Testing Set (the 20% of data it has never seen). We don't just look at Accuracy, as high accuracy can be misleading in imbalanced datasets. Instead, we focus on Precision (ensuring we don't send sales agents to the wrong people) and Recall (ensuring we don't miss any "hidden gems"). This phase concludes with a Confusion Matrix, a visual diagnostic tool that breaks down exactly where the AI succeeded and where it failed, providing the statistical transparency required to justify the 145% revenue growth claim.

•	Create a new file named p4_3_model_evaluation.py and paste the below script;

[p4_3_model_evaluation.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p4_3_model_evaluation.py)

•	In your terminal, run: 
```
python p4_3_model_evaluation.py
```

#### What this output proves for your Master's defense:

1.	High Precision: If your precision is >90%, it proves that when the AI says "Target this person," it is almost always right. This justifies the ₦1B revenue goal by cutting down wasted sales labor.

2.	The Matrix breakdown: * True Positives: Your future ₦1B revenue.

o	False Positives: The 15% wasted effort you've eliminated from the old manual system.

3.	F1-Score: This single number proves the model is robust and not biased toward just predicting "non-leads."

#### Step 4.4: Model Evaluation & Performance Metrics
Step 4.4 is the "Moment of Truth" for our AI engine. In this phase, we subject the trained Random Forest model to a rigorous blind test using the 105,000 records (20%) it has never seen. This is where we validate the project's success. We don't just check for simple accuracy; we calculate Precision (ensuring sales teams don't waste time on the wrong people) and Recall (ensuring we don't miss high-value opportunities). The centerpiece of this evaluation is the Confusion Matrix, a visual breakdown of True Positives (the future ₦1B revenue) versus errors. This statistical proof is the cornerstone of a Master's level data project, providing the objective evidence needed to justify the 145% revenue growth claim.

•	Create a new file named p4_4_model_evaluation.py and paste the following scripts

[p4_4_model_evaluation.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p4_4_model_evaluation.py)

    

•	In your terminal, run:
```
python p4_4_model_evaluation.py
```
<img width="975" height="494" alt="image" src="https://github.com/user-attachments/assets/49732702-0b7f-4f65-90b7-4ee1aa3bd59b" />

### What these results prove:

•	True Positives: These are the subscribers who are ready to spend more. By targeting them precisely, we move from ₦400M toward ₦1B.

•	False Positives (Wasted Effort): If this number is low (High Precision), it proves the system is efficient. It means the sales team is not chasing people who won't buy.

•	Operational Efficiency: This model proves that AI-driven targeting is the definitive driver of Telco scalability, providing 145% more efficiency than "spray and pray" marketing.
 

#### Step 4.5: Model Serialization
Model Serialization is the process of translating a live, trained Machine Learning object into a static format—typically a .pkl or .joblib file—that can be stored on disk. This is a critical milestone for the Telco-Optima system, as it allows the Streamlit application to perform "Instant Lead Scoring" without needing to access the raw training data or re-execute the training logic. By centralizing the model and its metadata (such as feature names) alongside the performance reports, we create a self-contained "Production Artifact." This ensures that the intelligence which drove the 145% revenue growth is preserved, portable, and ready to be integrated into the real-time decision-making interface.

•	Create a new file named p4_5_serialization.py and paste the below script;

[p4_5_serialization.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p4_5_serialization.py)

•	In your terminal, run:
```
python p4_5_serialization.py
``` 
<img width="955" height="422" alt="image" src="https://github.com/user-attachments/assets/b17e6005-3836-4cf8-bd32-db9df9aaadf9" />

#### What this achieves:

•	Verification: It double-checks that your model (.pkl) and your visual proof of accuracy are physically on your disk.

•	Archiving: It gathers your "White Space" proofs into the /reports/ folder so you have everything ready for your Master's project documentation.

•	Deployment Readiness: Once this script gives you the [OK] for all items, you are officially ready to build the frontend dashboard.

### Phase 5: Geospatial "White Space" Analysis
Phase 5 represents the visual and geographic intelligence core of the Telco-Optima system. While the Machine Learning model in Phase 4 identified who is likely to spend more, Phase 5 answers the equally critical question: "Where are we not present?" In the Nigerian telecommunications landscape, revenue growth is often restricted not by a lack of interest, but by a lack of physical accessibility and network optimization in high-density areas.
This phase introduces Geospatial Analytics, where we move beyond flat tables and into multi-dimensional mapping. By utilizing GeoPandas and Plotly Mapbox, we overlay 2.4 million census records with over half a million active subscriber locations. This allows us to calculate the "Delta", the mathematical difference between human density and network penetration.
The primary objective here is to visualize "White Spaces" territories like Alkaleri or specific wards in Kirfi that possess massive population clusters but significantly low market share. By assigning an Opportunity 

Score, we transform raw coordinates into a strategic expansion roadmap. This module is the "Growth Compass" that provides the evidence needed to deploy new base stations and field agents, directly facilitating the leap from a ₦400M revenue baseline to the ₦1B target by capturing the uncaptured market.

#### Step 5.1: Geospatial Mapping
In Step 5.1, we move from purely statistical analysis into spatial intelligence. By plotting our two massive datasets, the 2.4 million census records and the 525,000 active subscribers on a geographic coordinate system. We can visually identify the physical boundaries of our market share. We use Plotly Mapbox because it allows for high-performance rendering of millions of data points with interactive zooming. This visualization provides the "Ground Truth" for regional managers, showing that while the urban hub of Bauchi Metro is densely packed with subscribers, large population clusters in Alkaleri remain "invisible" to our network, proving the existence of the untapped market.

•	Create a new file named p5_1_geospatial_mapping.py and paste the below script;

[p5_1_geospatial_mapping.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p5_1_geospatial_mapping.py)
    
•	In your terminal, run:
```
python p5_1_geospatial_mapping.py
``` 
<img width="975" height="295" alt="image" src="https://github.com/user-attachments/assets/586f42ec-b5b9-45f2-86cc-5f792f578be5" />

#### What this achieves:

•	The Visual "Delta": You can now open the HTML file in any browser and zoom into Alkaleri. You will see thousands of population "dots" (Blue/Green) representing residents, but very few red dots representing subscribers.

•	Density Verification: It confirms that Bauchi Metro is saturated (Red dots overlapping everything), proving that further revenue growth there must come from Upselling (Phase 4), while growth in Alkaleri must come from Acquisition.

#### Step 5.2: The "Delta" Calculation
In Step 5.2, we execute the mathematical core of our geospatial intelligence: the "Delta" Calculation. While traditional maps simply show where subscribers are, this algorithmic approach calculates the gap (the Delta) between the Total Human Population and our Active Network Users.
We programmatically isolate regions that meet two criteria: High Population Density and Critically Low Subscriber Count. These specific intersections are what we define as "White Spaces." Identifying these gaps is the definitive driver for our revenue expansion; it transforms a vague desire for "more sales" into a surgical strike on uncaptured market clusters. This is the logic that proves we are not just growing, but specifically targeting the 1.8 million people in the North-East who are not yet on our network.

•	Create a new file named p5_2_delta_calculation.py and paste the below script;

[p5_2_delta_calculation.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p5_2_delta_calculation.py)
   

•	In your terminal, run: 
```
python p5_2_delta_calculation.py
```
<img width="975" height="343" alt="image" src="https://github.com/user-attachments/assets/dd54191a-7ab6-47f5-8db3-87228003f080" />

 
#### Why this step is vital 

•	Precision Targeting: You are no longer saying "we need more customers in Bauchi." You are saying "Alkaleri has 560,250 uncaptured residents (75% of its population). This is a 'YES - Expansion Target'."

•	Strategic Proof: This script mathematically identifies why Alkaleri is the growth engine. Even though Bauchi Metro has more people, its "Delta" is smaller because we have already captured most of them.

•	The Revenue Driver: By capturing just 20% of the "Uncaptured_Market" identified here, the system mathematically projects the jump from ₦400M to ₦1B.

#### Step 5.3: Opportunity Scoring
In the final step of the Geospatial Analysis, we transform our raw "Delta" calculations into a weighted Priority Score (0-100). In a professional Telco environment, sales managers cannot attack every gap at once; they need a ranked list of where the Return on Investment (ROI) will be highest.
This script applies a weighted formula that balances three factors: Uncaptured Market Size, Current Market Penetration, and Socio-Economic Type. By assigning a higher score to areas with high population but extremely low presence (like Alkaleri), the system programmatically dictates the regional expansion strategy. This score is the "final verdict" that justifies deploying resources to break through the ₦400M revenue ceiling and reach the ₦1B milestone.

•	Create a new file named p5_3_opportunity_scoring.py and paste the below script in it;

[p5_3_opportunity_scoring.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/p5_3_opportunity_scoring.py)


•	In your terminal, run:
```
python p5_3_opportunity_scoring.py
```
<img width="975" height="335" alt="image" src="https://github.com/user-attachments/assets/356fd4d5-809b-46be-9bbb-8e0eaa43e1f2" />

 
#### Why this is the "Strategic Verdict":

•	Mathematical Weighting: You are proving that Alkaleri is more important than Bauchi Metro for expansion, because even though Metro has more people, Alkaleri has a bigger "Penetration Gap."

•	Actionable Labels: By adding "Aggressive Acquisition" or "Retention Focus," you are moving from Data Science into Business Leadership.

•	Project Completion: This concludes Phase 5. You now have the exact map and the exact ranking needed for your final dashboard.

### Phase 6: Streamlit Application Development
Phase 6 is the final synthesis of the Telco-Optima project. This phase transforms our back-end scripts, MySQL databases, and Random Forest models into a unified, interactive Strategic Dashboard. In a professional corporate environment, stakeholders rarely interact with raw Python code; they require a "Single Pane of Glass" that translates data into decision-making power.

Using Streamlit, we will build an application that serves three distinct organizational levels:

1.	Executive Level: Visualizing the financial journey from the ₦400M stagnation point to the ₦1B growth target.

2.	Managerial Level: Interacting with Geospatial "White Space" maps to direct field agents to uncaptured clusters in Alkaleri and Kirfi.

3.	Operational Level: Providing sales agents with an AI-driven tool to upload subscriber lists and receive real-time propensity scores.

By the end of this phase, we would have a single app.py file that acts as the "Command Center" for the North-East region, proving that integrating population intelligence with AI is the definitive driver of Telco scalability.

•	Create a file named app.py and paste the below code;

[app.py](https://github.com/Ogbunugafor-Philip/Telco-Optima-AI-Driven-Sales-Optimization-Geospatial-Territory-Intelligence-System/blob/main/app.py)

•	Run the command;
```
streamlit run app.py --server.port 8509
```
•	View the dashboard on this url;
```
http://localhost:8509
``` 
<img width="975" height="444" alt="image" src="https://github.com/user-attachments/assets/2f38a25d-bc8f-4bc2-80bf-4f3c79c79f0b" />

<img width="975" height="321" alt="image" src="https://github.com/user-attachments/assets/fd6b45bf-f1a2-4a3f-b592-02ea4075f728" />

 
### Conclusion
The development and deployment of Telco-Optima mark a definitive shift from traditional, intuition-based telecommunications management to a sophisticated, AI-driven strategic framework. By bridging the "intelligence gap" through the integration of geospatial population modeling and predictive machine learning, this project has successfully demonstrated that data is not merely a byproduct of operations but the primary engine for scalability and revenue breakthrough.

Key Achievements and Business Impact:

1.	Breaking the Revenue Ceiling: The system provided the analytical roadmap required to move regional performance from a stagnant baseline of ₦400,000,000 to a projected ₦1,025,000,000. This 145% increase proves that algorithmic targeting can unlock market potential that remains invisible to manual mapping strategies.

2.	Surgical Market Acquisition: Through Geospatial "White Space" Analysis, we successfully identified high-density population clusters in territories like Alkaleri and Kirfi that were underserved. By calculating the "Delta" between total residents and active subscribers, Telco-Optima allows for the precision deployment of field agents and infrastructure, reducing customer acquisition costs (CAC) and maximizing market penetration.

3.	Predictive Sales Efficiency: The Machine Learning Lead Scoring engine achieved a precision rate of 87.3%. By utilizing a Random Forest Classifier to analyze subscriber behaviors (ARPU, device mix, and usage patterns), the system eliminated "spray and pray" marketing. Sales teams can now focus exclusively on high-propensity targets, directly reducing operational waste and increasing the conversion rate for premium services.

4.	Prescriptive Decision Support: The interactive Streamlit Dashboard serves as a centralized "Command Center." It empowers stakeholders at all levels—from executives tracking ROI to field managers directing daily sales routes—with real-time, actionable insights.

In summary, Telco-Optima proves that the future of the telecommunications sector in competitive regions like North-East Nigeria lies in Geospatial Intelligence. By treating every coordinate as a data point and every subscriber as a behavioral signal, the system provides a repeatable, scalable model for telco growth. This framework ensures that the path to the next billion in revenue is not found through random expansion, but through the scientific identification of "Who is missing?" and "Who is ready to spend more?"



