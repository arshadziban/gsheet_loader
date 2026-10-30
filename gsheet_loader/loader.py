import re
import pandas as pd
import requests
from io import StringIO


def load_sheet(sheet_url: str) -> StringIO:
   
    # Extract sheet ID from URL
    match = re.search(r"/spreadsheets/d/([\w-]+)", sheet_url)
    
    if not match:
        raise ValueError(
            "Invalid Google Sheets URL. "
            "URL should be in format: https://docs.google.com/spreadsheets/d/SHEET_ID/..."
        )
    
    sheet_id = match.group(1)
    
    # Build CSV export URL
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    
    # Fetch and return as StringIO
    response = requests.get(csv_url)
    response.raise_for_status()
    
    return StringIO(response.text)


def load_df(sheet_url: str, **kwargs) -> pd.DataFrame:
    """Load a public Google Sheet directly into a pandas DataFrame.

    Extra keyword arguments are passed to ``pd.read_csv``.
    """
    return pd.read_csv(load_sheet(sheet_url), **kwargs)


def get_sheet_id(sheet_url: str) -> str:
 
    match = re.search(r"/spreadsheets/d/([\w-]+)", sheet_url)
    
    if not match:
        raise ValueError("Invalid Google Sheets URL")
    
    return match.group(1)
