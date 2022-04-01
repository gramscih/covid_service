from datetime import datetime
import random
import datetime
import optparse
import json

FILE_PATH = "src/%s"


def gender(): return random.choice(['Female', "Male"])
def age(): return random.choice(range(1, 100))
def covid_test(): return random.choice(['positive', 'negative'])
def confirm(): return random.choice(range(120, 10000))
def negative(): return random.choice(range(100, 10000))
def vaccines(): return random.choice(range(0, 5))


data_per_day = random.choice(range(100, 1000))


def generate_patient_per_day(date):
    result = []
    for _ in range(0, data_per_day):
        generated_data = {}
        generated_data["id"] = "{}{}".format(random.choice(
            range(0, 1000)), chr(random.choice(range(65, 70))))
        generated_data["date"] = date
        generated_data["gender"] = gender()
        generated_data["age"] = age()
        generated_data["test_result"] = covid_test()
        generated_data["vaccines"] = vaccines()
        generated_data["status"] = ""
        result.append(generated_data)
    return result


def generate_dummy_data(days=365):
    data = {}
    for index in range(0, days):
        date = (datetime.date.today() - datetime.timedelta(index)).isoformat()
        data["patients"] = data.get(
            "patients", []) + generate_patient_per_day(date)
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
