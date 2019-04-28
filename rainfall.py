import numpy as np
import json
from matplotlib import pyplot as plt
import time

def rf_json(csv_file_path):
    rainfalls =  np.genfromtxt(csv_file_path, skip_header = 1, delimiter=',', 
                            names=['year', 'day', 'mm_day'], 
                            dtype=[int, int, float])
    rf_dict = {}
    for index, item in enumerate(rainfalls):
        year = str(item[0])
        if year in rf_dict:
            rf_dict[year].append(item[2])
        else:
            rf_dict[year] = [item[2]]
    with open("rainfall.json", "w") as f:
        json.dump(rf_dict, f, indent = 4)

def plot_rainfall(file_name, year, line_color='b'):
    with open(file_name, "r") as f:
        mydata = json.load(f)
    # print(mydata)
    y = mydata[str(year)]
    plt.figure()
    plt.plot(y, color=line_color)
    plt.title('Daily rainfall in the year')
    plt.xlabel('day')
    plt.ylabel('rainfall')
    plt.savefig('treetimeseries of daily rainfall-1998.png')

def plot_mean_rainfall(file_name, start_year, end_year):
    with open(file_name, "r") as f:
        mydata = json.load(f)
    mean = []
    for i in range(start_year, end_year + 1):
        rainfall = mydata[str(i)]
        mean.append(np.mean(rainfall))

    plt.figure()
    plt.plot(mean)
    plt.savefig('1988-2000.png')


def func1(file_name, year):
    with open(file_name, "r") as f:
        mydata = json.load(f)
    rainfall = mydata[str(year)]
    start_time = time.time()
    for i in range(len(rainfall)):
        rainfall[i] = rainfall[i] * (1.2**(2**0.5))
    print("func1: ", time.time() - start_time)
    return rainfall

def func2(file_name, year):
    with open(file_name, "r") as f:
        mydata = json.load(f)
    rainfall = np.array(mydata[str(year)])
    start_time = time.time()
    rainfall = rainfall * (1.2**(2**0.5))
    print("func2: ", time.time() - start_time)

    return rainfall.tolist()

rf_json('python_language_1_data.csv')
plot_rainfall("rainfall.json", 1998, 'b')
plot_mean_rainfall("rainfall.json", 1988, 2000)

print(func1("rainfall.json", 1998))

print(func2("rainfall.json", 1998))

