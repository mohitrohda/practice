street = "St.20"
city = "Bhilai"
country = "India"

address = '\n' + street  + '\n' + city + '\n' + country

print ("using + operator ",address)

print("using f string", f"{street}\n{city}\n{country}")

''' print(f"""
{street},
{city}'
{country}
""") '''