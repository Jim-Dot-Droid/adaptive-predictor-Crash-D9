# MUST COME FIRST
import streamlit as st

# Check for Plotly with proper error handling
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError as e:
    PLOTLY_AVAILABLE = False
    st.error(f"Plotly import failed: {str(e)}. Using fallback display.")

# Rest of imports
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# Your existing app code continues here...
# [All your existing visualization code wrapped in PLOTLY_AVAILABLE checks]