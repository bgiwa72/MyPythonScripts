import datetime
get = datetime.datetime.now()
name = input("Your name:\n")
age = int(input("Your age:\n"))
numcopy = int(input("Number of result messages:\n"))
currYear = get.year
century = ((100-age)+currYear)
print(numcopy * ("""Hello %r. Your current age is %r and you will turn 100 in year %r\n"""
      %(name,age,century)))
