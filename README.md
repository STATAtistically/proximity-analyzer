# OSRM Distance Calculator

This Python script calculates distances between pairs of locations using the OSRM (Open Source Routing Machine) API and saves the results to a CSV file.

## Features
- Supports multiple transport modes: driving, walking, cycling.
- Customizable input and output file paths.
- Error handling for API requests and data parsing.

## Requirements
- Python 3.x
- Pandas library
- Requests library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/osrm-distance-calculator.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with default settings:
```bash
python osrm_distance_calculator.py
```
Or specify input, output files, and mode:
```bash
python osrm_distance_calculator.py input.xlsx output.csv driving
```

## Example
Input file should contain columns:
- `School Latitude`, `School Longitude`
- `Closest School Latitude`, `Closest School Longitude`

## License
This project is licensed under the MIT License.
