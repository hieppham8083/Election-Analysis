#1.Total number of votes cast
#2.A complete list of candidates who received votes
#3.Total number of votes each candidate received
#4.Percentage of votes each candidate won
#5.The winner of the election based on popular vote
# Import the datetime class from the datetime module.
import datetime as dt
import os
import csv
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
#Add the filename variable that references the path to
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
 # To do: perform analysis.
    print(election_data)
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
# Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")