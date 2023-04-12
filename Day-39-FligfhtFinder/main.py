from data_manager import DataManager
import os

# Data to sheety.com
USERNAME = os.environ['USERNAME_DAY39']
PASSWORD = os.environ['PASSWORD_DAY39']
sheet_endpoint = os.environ['SHEETY_DAY39']


# TODO 1: Connect with sheety, and get a data from it.
sheety = DataManager(USERNAME, PASSWORD, sheet_endpoint)
data = sheety.get_data()
print(data)

# TODO 2: Connect with Kiwi, and get a data from it.

# TODO 3: Connect with Tequila, and get a data from it.

# TODO 4: Connect with Twilio SMS and make a send sms function
