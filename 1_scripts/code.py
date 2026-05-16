import pandas as pd
import numpy as np
import os
import sqlite3

#Directories

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "2_data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "3_outputs")

#Import the data file

df = pd.read_csv(os.path.join(DATA_DIR, "ncr_ride_bookings.csv"))

# Connect to SQLite database
conn = sqlite3.connect(os.path.join(OUTPUT_DIR, "python.db"))

# Import dataframe into SQLite
df.to_sql(
    name="uber",
    con=conn,
    if_exists="replace",
    index=False
)

print("Data imported successfully!")
#Close the connection
conn.close()