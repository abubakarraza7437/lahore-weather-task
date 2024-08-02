import os
import pandas as pd
from typing import List, Dict


class ReadData:
    def __init__(self, directory='csv2'):
        self.directory = directory
        self.files = [file for file in os.listdir(self.directory) if file.endswith(".txt")]
        self.data_dict = {}

    def path_finder(self):
        dataframes = {}
        for single_file in self.files:
            file_path = os.path.join(self.directory, single_file)
            df = pd.read_csv(file_path)
            dataframes[single_file] = df
        return dataframes


class Weather(ReadData):
    def __init__(self, directory: str = 'csv2'):
        super().__init__(directory)
        self.total_data = self.path_finder()

    def complete_data(self, weather_data_type: str) -> Dict[str, List]:
        for single_file, df in self.total_data.items():
            all_data = df[weather_data_type].to_list()
            self.data_dict[single_file] = all_data
        return self.data_dict

    def temp_specific_month(self, year: str, month: str) -> str | Dict:
        path = f"lahore_weather_{year}_{month}.txt"
        if path in self.data_dict:
            return self.data_dict[path]
        else:
            return f"No data available for {year} {month}"

    def max_min_total(self,weather_data_type: str) -> None:
        for single_file, df in self.total_data.items():
            all_max_value = df[weather_data_type]
            print(f"Month: '{single_file}'\nMaximum value is '{max(all_max_value)}' and "
                  f"Minimum value is '{min(all_max_value)}'.")

    def max_min_specific_month(self, year: str, month: str, weather_data_type: str):
        path = f"lahore_weather_{year}_{month}.txt"
        if path in self.total_data:
            data = self.total_data[path][weather_data_type]
            return (f"Data for Month '{month}' Year '{year}'\nMaximum value is '{max(data)}' and "
                    f"Minimum value is '{min(data)}'.")
        else:
            return f"No data available for {year} {month}"

    def specific_date(self, year:str, month_name: str, month_num: int, day: int, weather_data_type: str):
        date = f"{year}-{month_num}-{day}"
        df = self.total_data.get(f"lahore_weather_{year}_{month_name}.txt")
        if df.empty:
            return f"No file found for {year} {month_name}"
        if date in df["PKT"].values:
            value = df.loc[df["PKT"] == date, weather_data_type].values[0]
            return f"Value on {date} is {value}"
        else:
            return f"No data available for {date}"


# temperature = Weather()
#
# # Total temperatures for all files
# print(temperature.complete_data("Max TemperatureC"))
#
# # Maximum and minimum temperatures for all files
# temperature.max_min_temp_total()
#
# # Specific month temperatures
# year = input("Enter year (1997 to 2011): ")
# month = input("Enter month name (e.g., Jan, Apr): ").title()
# print(temperature.temp_specific_month(year, month))
#
# # Maximum and minimum temperatures for a specific month
# print(temperature.max_min_temp_specific_month(year, month))
#
# # Temperature of a specific date
# month_num = input("Enter month number (e.g., 1 for January): ")
# day = input("Enter day (e.g., 1 for the first day of the month): ")
# print(temperature.temp_of_specific_date(year, month, month_num, day))
