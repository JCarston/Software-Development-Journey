def getPerson():
    name = "Leona"
    age = 35
    country = "UK"
    return name,age,country

name,age,country = getPerson()
print(name)
print(age + 1)
print(country)


test = '13'
update = test.replace("'","")
print(update)