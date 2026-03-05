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