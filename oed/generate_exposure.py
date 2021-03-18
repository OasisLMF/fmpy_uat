
import pandas as pd
from numpy import random


base_loc_fields = ['PortNumber','AccNumber','LocNumber','CountryCode',
    'LocPerilsCovered','PostalCode','ConstructionCode','OccupancyCode',
    'LocCurrency','BuildingTIV','OtherTIV','ContentsTIV','BITIV']

bas_acc_fields = ['PortNumber','AccNumber','AccCurrency','PolNumber',
    'PolPerilsCovered']

# static values
PortNumber = 'BaseTest'
CountryCode = 'GB'
LocPerilsCovered = 'OSF'
LocCurrency = 'GBP'
AccCurrency = 'GBP'
PolPerilsCovered = 'OSF'

number_of_locations = 100000
locations_per_account = 1000

location_list=[]
account_list=[]

for l in range(1,number_of_locations+1):
    AccNumber=1
    LocNumber=l
    PostalCode=''
    ConstructionCode=0
    OccupancyCode=0
    BuildingTIV=round(random.rand()*1000000 + 100000,2)
    OtherTIV=round(random.rand()*10000,2)
    ContentsTIV=round(random.rand()*100000 + 1000,2)
    BITIV=round(random.rand()*100000 + 1000,2) if random.rand() < 0.1 else 0
    loc_row=[PortNumber,AccNumber,LocNumber,CountryCode,LocPerilsCovered,
        PostalCode,ConstructionCode,OccupancyCode,LocCurrency,BuildingTIV,
        OtherTIV,ContentsTIV,BITIV]

    location_list.append(loc_row)


df_location = pd.DataFrame(location_list,columns=base_loc_fields)

print(df_location)