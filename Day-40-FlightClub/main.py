from data_manager import DataManager
import os
from pprint import pprint

# Data to sheety.com
sheet_endpoint = os.environ['SHEETY_DAY39']


# TODO 1: Connect with sheety, and get a data from it.
sheety = DataManager(sheet_endpoint)
data = sheety.get_data()
pprint(data)

# TODO 2: Connect with Kiwi, and get a data from it.

# TODO 3: Connect with Twilio SMS and make a send sms function
