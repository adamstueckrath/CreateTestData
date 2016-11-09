__author__ = 'adam.stueckrath'

import pandas
import random
from faker import Factory
import os

fake = Factory.create()

subjectNumber = raw_input("Please enter the number of subjects: ")
subjectNumber = int(subjectNumber)

mrn1 = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')
sec_addresslist = ['yes','','','','','']
racelist = ['White','Black','Hispanic','Asian','Other']
gender = ['Male','Female']

def fakerperson():
    return {'mrn': ''.join(random.sample(mrn1, 3)) + str(fake.numerify('#######')),  # random number eg:2355336
            'ssn': fake.ssn(),  # random ssn
            'last': fake.last_name(),
            'middle': random.choice(mrn1),
            'first': fake.first_name(),
            'address_1': str(fake.random_int(min=5, max=9999))+ " " + fake.street_name(),
            'address_2': fake.secondary_address() if random.choice(sec_addresslist) == "yes" else '',  #
            'city': fake.city(),
            'state': fake.state_abbr(),  # datetime between mar16-2015 to mar30-2015
            'zip': fake.zipcode(),
            'date_of_birth': fake.date_time_between(start_date="-100y", end_date="now").date(),
            'gender': random.choice(gender),
            'race': random.choice(racelist),
            'phone': fake.phone_number(),
            'Occupation': fake.job()
            }

demographic = pandas.DataFrame([fakerperson() for i in xrange(subjectNumber)])

demographic.to_csv(os.path.expanduser("~/Desktop/myfile.csv"),sep=',',index=False)