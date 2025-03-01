# OSRM Distance Calculator

import pandas as pd
import requests

# Function to get OSRM distance

def get_osrm_distance(lat1, lon1, lat2, lon2, mode="driving"):
    """
    Fetches the OSRM distance between two coordinates.
    Args:
        lat1, lon1: Latitude and Longitude of the first location.
        lat2, lon2: Latitude and Longitude of the second location.
        mode: Transport mode for OSRM API (driving, walking, cycling). Default is 'driving'.
    Returns:
        Distance in kilometers if successful, None otherwise.
    """
    url = f"http://router.project-osrm.org/route/v1/{mode}/{lon1},{lat1};{lon2},{lat2}?overview=false"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['routes'][0]['distance'] / 1000  # Convert meters to kilometers
        except (KeyError, IndexError, ValueError):
            print("Error parsing OSRM response.")
            return None
    else:
        print(f"OSRM request failed with status code {response.status_code}.")
        return None

# Main function

def main(input_file, output_file, mode="driving"):
    """
    Reads an Excel file, calculates OSRM distances, and saves results.
    Args:
        input_file: Path to the input Excel file.
        output_file: Path to save the output CSV file.
        mode: Transport mode for OSRM API (driving, walking, cycling). Default is 'driving'.
    """
    df = pd.read_excel(input_file)
    osrm_distances = []
    for _, row in df.iterrows():
        distance = get_osrm_distance(
            row["School Latitude"], row["School Longitude"],
            row["Closest School Latitude"], row["Closest School Longitude"],
            mode
        )
        osrm_distances.append(distance)
    df["Distance OSRM (km)"] = osrm_distances
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

# Example usage
if __name__ == "__main__":
    main("closest_schools.xlsx", "closest_schools_osrm.csv", mode="driving")
