# LAB ASSIGNMENT 5 – CAPSTONE
# Campus Energy Consumption Dashboard


from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# TASK 1: DATA LOADING
def load_and_merge_data(data_folder="data"):
    data_path = Path(data_folder)
    all_files = list(data_path.glob("*.csv"))

    df_list = []
    error_log = []

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')

            if "timestamp" not in df.columns or "kwh" not in df.columns:
                error_log.append(f"Missing column in {file.name}")
                continue

            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            df["building"] = file.stem  

            df_list.append(df)

        except Exception as e:
            error_log.append(f"Error in {file.name} : {e}")

    if df_list:
        df_combined = pd.concat(df_list, ignore_index=True)
    else:
        df_combined = pd.DataFrame()

    return df_combined, error_log


df, errors = load_and_merge_data()

if not df.empty:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp").sort_index()

print("DATA LOADED. Rows:", len(df))
print("ERRORS:", errors)

# TASK 2: CALCULATIONS
def calculate_daily_totals(df):
    return df.groupby("building").resample("D")["kwh"].sum().reset_index()

def calculate_weekly_aggregates(df):
    return df.groupby("building").resample("W")["kwh"].sum().reset_index()

def building_wise_summary(df):
    return df.groupby("building")["kwh"].agg(
        total_kwh="sum",
        mean_kwh="mean",
        min_kwh="min",
        max_kwh="max",
    ).reset_index()


daily = calculate_daily_totals(df)
weekly = calculate_weekly_aggregates(df)
summary = building_wise_summary(df)

print("\nSUMMARY TABLE:")
print(summary)

# TASK 3: OOP MODEL
from dataclasses import dataclass

@dataclass
class MeterReading:
    timestamp: pd.Timestamp
    kwh: float

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, time, kwh):
        self.readings.append(MeterReading(time, kwh))

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return {
            "building": self.name,
            "total_kwh": total,
            "num_readings": len(self.readings)
        }

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def get_building(self, name):
        if name not in self.buildings:
            self.buildings[name] = Building(name)
        return self.buildings[name]

    def load_df(self, df):
        df_reset = df.reset_index()
        for _, row in df_reset.iterrows():
            b = self.get_building(row["building"])
            b.add_reading(row["timestamp"], row["kwh"])

    def generate_reports(self):
        return [b.generate_report() for b in self.buildings.values()]


manager = BuildingManager()
manager.load_df(df)
oop_report = manager.generate_reports()

print("\nOOP REPORT:")
print(oop_report)

# TASK 4: DASHBOARD VISUALS
daily_pivot = daily.pivot(index="timestamp", columns="building", values="kwh")
weekly_avg = weekly.groupby("building")["kwh"].mean().reset_index()

top_peaks = df.reset_index().nlargest(30, "kwh")

plt.figure(figsize=(10, 12))

# 1) Line Plot
plt.subplot(3, 1, 1)
plt.plot(daily_pivot.index, daily_pivot)
plt.title("Daily Energy Consumption")
plt.xlabel("Date")
plt.ylabel("kWh")
plt.legend(daily_pivot.columns)

# 2) Bar Chart
plt.subplot(3, 1, 2)
plt.bar(weekly_avg["building"], weekly_avg["kwh"])
plt.title("Average Weekly Usage")
plt.ylabel("kWh")

# 3) Scatter Plot
plt.subplot(3, 1, 3)
plt.scatter(top_peaks["timestamp"], top_peaks["kwh"])
plt.title("Peak Load Points")
plt.xlabel("Time")
plt.ylabel("kWh")

plt.tight_layout()
plt.savefig("output/dashboard.png")
plt.close()


# TASK 5: EXPORT FILES
df_output = df.reset_index()
df_output.to_csv("output/cleaned_energy_data.csv", index=False)
summary.to_csv("output/building_summary.csv", index=False)

total_consumption = df_output["kwh"].sum()
highest_building = summary.sort_values("total_kwh", ascending=False).iloc[0]

with open("output/summary.txt", "w") as f:
    f.write("CAMPUS ENERGY SUMMARY\n")
    f.write("---------------------------\n")
    f.write(f"Total consumption: {total_consumption:.2f} kWh\n")
    f.write(f"Highest consuming building: {highest_building['building']} ({highest_building['total_kwh']:.2f} kWh)\n")

print("\nFILES GENERATED IN /output FOLDER")
print("✔ cleaned_energy_data.csv")
print("✔ building_summary.csv")
print("✔ summary.txt")
print("✔ dashboard.png")
