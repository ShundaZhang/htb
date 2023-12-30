import json

# File path to your JSON file
file_path = 'trading-firebase_bkup.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Initialize variables to store the highest profit percentage, related email, and associated profit
max_profit_percentage = float("-inf")
email_with_max_profit = None
max_profit = None

# Iterate through the data to find the entry with the highest profit_percentage
for key, value in json_data.items():
    profit_percentage = value["profit_percentage"]
    if profit_percentage > max_profit_percentage:
        max_profit_percentage = profit_percentage
        email_with_max_profit = value["email"]

# Print the email with the highest profit percentage and the profit_percentage
print(f"Email with the highest profit_percentage: {email_with_max_profit}")
print(f"Highest profit_percentage: {max_profit_percentage}")

#Precision missing, need to manually find the profit_percentage.
