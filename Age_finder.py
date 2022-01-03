def ageinxxxx():
    year_in = int(input("Enter the year: "))
    
    
    if ye:
        age = (year_in-age_or_year)
        age= int(age)
        if year_in<year_100:
            print(age)
        elif age>150:
            print(age)
             
        else:
            print(age)
            
    else:
        age = year_in-(2021-age_or_year)
        if age<0:
            print(age)
        elif age>150:
            print(age)
            
        else:
            print(age)



age_or_year = int(input("Enter your age or year: "))


if age_or_year<150:
    ag = True
    ye = False
    
    year_100 = (100-age_or_year)+2021
    print(year_100)
    
elif age_or_year>1000:
    ye = True
    ag = False
    year_100 = age_or_year+100
    print(year_100)
    
optional = input("\nHere is an optional function\n You can find your age whrn you will be in (year Entered by you)\n type 'yes' to continue else write 'no' to exit\n")
optional = optional.lower()
if optional == 'yes':
    ageinxxxx()
else:
    exit()
