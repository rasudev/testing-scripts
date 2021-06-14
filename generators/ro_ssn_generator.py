import random
import datetime
from stdnum import ro

# Methods adopted from faker library
# https://github.com/joke2k/faker/tree/master/faker/providers/ssn/ro_RO

def ssn_checksum(number):
    """
    Calculate the checksum for the romanian SSN (CNP).
    """
    weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(weights, number)) % 11
    return 1 if check == 10 else check

def ssn(sex, age):
            """
            Romanian Social Security Number.

            :sex: male, female as string
            :age: no more then 122 years as integer
            :return: a random Romanian SSN
            """
    
            if sex == "male" and age >= 22: 
                sex = 1
            elif sex == "female" and age >= 22:
                sex = 2
            elif age < 22:
                sex = random.choice([5, 6])

            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            birth_year = int(date.strftime("%Y")) - age
            birth_year = str(birth_year)[2:4]

            gender = sex
            year = int(birth_year)
            month = random.randrange(1, 12)
            day = random.randrange(1, 31)
            county = random.choice([
            1,2,3,4,5,6,7,8,9, 10, 11, 12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                43, 44, 45, 46, 51, 52,
            ])
            serial = random.randrange(1, 999)

            num = f'{gender:01d}{year:02d}{month:02d}{day:02d}{county:02d}{serial:03d}'
            

            check = ssn_checksum(num)
            num += str(check)

            valid = ro.cnp.is_valid(num)

            if valid == True:
                print(num)
                return num
            else:
               raise Exception(GeneratorExit("generated cnp is invalid"))

ssn("male", 35)
