Campus Energy-Use Dashboard – Capstone Project
Course: Programming for Problem Solving using Python
Student: Shreya Verma

--> Project Overview
This project focuses on analyzing and visualizing electricity consumption across multiple buildings on campus.
The main objective is to design a complete energy dashboard pipeline — from reading raw meter data to producing insights that can help administrative teams identify energy-saving opportunities.

The assignment covers real-world tasks such as data ingestion, cleaning, aggregation, object-oriented modeling, visualization, and generating automated summary reports.

--> Objectives
1. Read and validate multiple CSV files containing building energy data.
2. Clean, combine, and process data using Pandas.
3. Apply aggregation logic to calculate daily, weekly, and building-wise energy usage.
4. Implement Object-Oriented Programming (OOP) to model buildings and meter readings.
5. Create a multi-chart dashboard using Matplotlib.
6. Export cleaned datasets and generate an executive summary.

-->Project Structure
campus-energy-dashboard/
│
├── data/
│      adminblock.csv
│      library.csv
|     hotel.csv
│
├── output/
│      dashboard.png
│      cleaned_energy_data.csv
│      building_summary.csv
│      summary.txt
│
├── main.py
└── README.md

-->Task Breakdown
✔ Task 1 — Data Ingestion & Validation
Automatically detected and read multiple CSV files from the /data/ folder.
Used exception handling for missing/corrupt files.
Combined all CSVs into one master DataFrame.
Converted timestamps into proper datetime format.

✔ Task 2 — Core Aggregation Logic
Using Pandas:
Daily electricity totals (resample('D'))
Weekly electricity totals (resample('W'))
Building-wise summary (mean, min, max, total)
Results stored as:
DataFrames for visualization
Summary tables for export

✔ Task 3 — Object-Oriented Modeling
Created OOP structure:
Classes Implemented:
MeterReading – stores timestamp and kWh
Building – stores readings and calculates total consumption
BuildingManager – manages multiple building objects
This ensures modularity, scalability, and clean organization.

✔ Task 4 — Visual Output (Dashboard)
Generated a multi-plot dashboard using Matplotlib containing:
Line chart – Daily consumption trend
Bar chart – Average weekly usage for each building
Scatter plot – Peak-hour load comparison
Dashboard saved as:
output/dashboard.png

✔ Task 5 — Persistence & Executive Summary
Exported:
Cleaned dataset → cleaned_energy_data.csv
Building summary → building_summary.csv
Text summary → summary.txt
Summary includes:
Total campus consumption
Highest-consuming building
Peak load
Daily/weekly usage insights

📊 Outputs Generated
File	Description
dashboard.png	Multi-chart visualization dashboard
cleaned_energy_data.csv	Combined & cleaned dataset
building_summary.csv	Building-wise statistics
summary.txt	Executive written summary

-->Technologies Used
Python
Pandas
Matplotlib
Object-Oriented Programming
OS / Pathlib for file handling

-->How to Run the Project
Clone or download the repository
Place CSV files in /data/

Run:
python main.py


Check /output/ folder for:
Dashboard image
Exported CSVs

-->Summary report
Insights
Energy usage varies significantly between buildings.
Weekly and daily trends help identify peak consumption periods.
Highest energy-consuming buildings can be prioritized for conservation measures.
A dashboard improves transparency for administrative teams.

-->Conclusion
This project demonstrates the complete workflow of data handling, modeling, visualization, and reporting using Python.
The end-to-end solution can be extended with automation, real-time monitoring, and predictive analytics in the future.
