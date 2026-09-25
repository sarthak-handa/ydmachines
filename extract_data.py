import pandas as pd
import json
import sys
import os

try:
    util_df = pd.read_excel('Machine_Utilization__AllSheds.xlsx', skiprows=5)
    logs_df = pd.read_excel('Machines_Report_AllUnits.xlsx', skiprows=5)
    
    print("\nUtil Data:")
    print(util_df.head(5).to_json(orient='records'))
    
    print("\nLogs Data:")
    print(logs_df.head(5).to_json(orient='records'))
    
except Exception as e:
    print(f"Error: {e}")
