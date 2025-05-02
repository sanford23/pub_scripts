#!/usr/bin/env python3

import requests
from datetime import datetime
import os

def download_inmate_roster():
    """
    Downloads the inmate roster PDF from the specified URL, saves it with a date-prefixed filename 
    in the local folder, and returns the result of the operation.

    Returns:
        str: A message indicating success or failure of the download operation.
    """
    url = "https://www.steelecountymn.gov/Sheriff/Inmate_Roster.pdf"
    # Get current date in dd_mm_yyyy format
    date_str = datetime.now().strftime("%d_%m_%Y")
    # Create filename with date prefix
    filename = f"{date_str}_Inmate_Roster.pdf"
    # Define local folder to save
    local_folder = "/samba/wiki/test"
    # Full path
    filepath = os.path.join(local_folder, filename)
    
    # Ensure the local folder exists
    os.makedirs(local_folder, exist_ok=True)
    
    # Download the PDF
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.headers.get('Content-Type') == 'application/pdf':
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return f"File saved successfully as {filename}"
            else:
                return "Failed to save file: Content is not a PDF"
        else:
            return f"Failed to download file: HTTP {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred during the download: {e}"
# Run the function
print(download_inmate_roster())
# Run the function
result = download_inmate_roster()
print(result)
