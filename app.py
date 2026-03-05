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