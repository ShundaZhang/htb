import datetime

timestamp = 1682506392  # Your timestamp here
# Convert the timestamp to a readable date
readable_date = datetime.datetime.utcfromtimestamp(timestamp)

# Print the readable date
print("Human-readable date:", readable_date)

timestamp = 1682506431
readable_date = datetime.datetime.utcfromtimestamp(timestamp)
print("Human-readable date:", readable_date)

#timestamp = 1682506471
#readable_date = datetime.datetime.utcfromtimestamp(timestamp)
#print("Human-readable date:", readable_date)
