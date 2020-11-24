print("Helleo World")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver" :
    print(counties[1])

temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the window")
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else: 
    print("Arapahoe or El Paso are in the list of counties")
x = 0
while x <= 5:
    print(x)
    x = x+1
print('\n')
for county in counties:
    print(county)
print('\n')
for i in range(len(counties)):
    print(counties[i])
print('\n')
for county in counties_dict:
    print(county)
print('\n')
for county in counties_dict.keys():
    print(county)
print('\n')
for voters in counties_dict.values():
    print(voters)
print('\n')
for county in counties_dict:
    print(counties_dict[county])
print('\n')    
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print("%s county has %d registered voters." %(county,voters))
    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")
for i in range(len(voting_data)):
    print(voting_data[i])
print('\n') 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

  