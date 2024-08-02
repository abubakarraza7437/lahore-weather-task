import os


class Weather:

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def find_extreme_temperatures(self):
        max_temps = []
        min_temps = []
        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            max_temp, min_temp, _ = self.read_file(file_path)
            if max_temp is not None:
                max_temps.append(max_temp)
            if min_temp is not None:
                min_temps.append(min_temp)

        overall_max_temp = max(max_temps) if max_temps else None
        overall_min_temp = min(min_temps) if min_temps else None

        hottest_months = self.search_extreme_months(overall_max_temp, 'max') if overall_max_temp is not None else []
        coldest_months = self.search_extreme_months(overall_min_temp, 'min') if overall_min_temp is not None else []

        return overall_max_temp, hottest_months, overall_min_temp, coldest_months

    def search_extreme_months(self, extreme_temp, temp_type):
        extreme_months = []
        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            max_temp, min_temp, _ = self.read_file(file_path)
            if (temp_type == 'max' and max_temp == extreme_temp) or (temp_type == 'min' and min_temp == extreme_temp):
                extreme_months.append(filename)
        return extreme_months

    def read_file(self, file_path):
        max_temps = []
        min_temps = []

        with open(file_path, 'r') as file:
            lines = file.readlines()[2:]  # Skip the first two lines (header)
            for line in lines:
                if line.strip() and '<' not in line:
                    data = line.strip().split(',')
                    if data[1]:
                        max_temps.append(int(data[1]))
                    if data[3]:
                        min_temps.append(int(data[3]))

        max_temp = max(max_temps) if max_temps else None
        min_temp = min(min_temps) if min_temps else None

        return max_temp, min_temp, os.path.basename(file_path)

    def display_results(self):
        overall_max_temp, hottest_months, overall_min_temp, coldest_months = self.find_extreme_temperatures()

        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            max_temp, min_temp, _ = self.read_file(file_path)
            print(f"List of Temperatures for {filename}:")
            print(f"Highest Temperature: {max_temp if max_temp is not None else 'No data available'}")
            print(f"Lowest Temperature: {min_temp if min_temp is not None else 'No data available'}\n")

        if overall_max_temp is not None:
            print(f"The hottest temperature across all files is: {overall_max_temp} in months: {hottest_months}")
        else:
            print("No valid temperature data found.")

        if overall_min_temp is not None:
            print(f"The coldest temperature across all files is: {overall_min_temp} in months: {coldest_months}")
        else:
            print("No valid temperature data found.\n")


if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(root_directory, 'csv2')
    weather = Weather(data_directory)
    weather.display_results()


