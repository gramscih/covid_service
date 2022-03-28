from datetime import datetime
import random
import datetime
import optparse
import json

FILE_PATH = "src/%s"


def gender(): return random.choice(['Female', "Male"])
def age(): return random.choice(range(1, 100))
def covid_tests(): return random.choice(range(200, 200000))
def confirm(): return random.choice(range(120, 10000))
def negative(): return random.choice(range(100, 10000))
def vaccines(): return random.choice(range(100, 500))


def generate_dummy_data(days=365):
    data = []
    for index in range(0, days):
        generated_data = {}
        date = (datetime.date.today() - datetime.timedelta(index)).isoformat()
        generated_data["id"] = index
        generated_data["date"] = date
        generated_data["gender"] = gender()
        generated_data["age"] = age()
        generated_data["tests"] = covid_tests()
        generated_data["confirm"] = confirm()
        generated_data["negative"] = negative()
        generated_data["vaccines"] = vaccines()
        data.append(generated_data)
    return data


def save_dummy_data(file_name, dummy_data):
    file_name = "{}.json".format(
        file_name) if "json" not in file_name else file_name
    file = open(FILE_PATH % file_name, "a")
    json.dump(dummy_data, file, indent=4)
    file.close()


parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="file_name",
                  help="File that would be created with the dummy data")
parser.add_option("-d", "--days", dest="days",
                  help="Number of days for what would be generated the dummy data")

(options, arguments) = parser.parse_args()

try:
    days = int(options.days) if options.days else 365
except Exception as ex:
    print("Days parameter its invalid, please enter and valid integer")

data = generate_dummy_data(days)
save_dummy_data(options.file_name, data)
