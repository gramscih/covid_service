from datetime import datetime
import random
import datetime

gender = ['Female', "Male"]
covid_tests = random.choice(range(200, 200000))
# confirm = random.choice(range())
# negative = random.choice(range())
# vaccines = random.choice(range())

for i in range(0, 365):
    # I need to add the auto generator here
    print((datetime.date.today() - datetime.timedelta(i)).isoformat())
