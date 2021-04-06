
import pandas as pd
from numpy import random


base_loc_fields = ['PortNumber','AccNumber','LocNumber','CountryCode',
    'LocPerilsCovered','LocPeril','PostalCode','ConstructionCode',
    'OccupancyCode','LocCurrency','BuildingTIV','OtherTIV','ContentsTIV',
    'BITIV']

base_acc_fields = ['PortNumber','AccNumber','AccCurrency','PolNumber',
    'PolPerilsCovered', 'PolPeril]

fm_loc_fileds = ['LocLimit1Building', 'LocLimit2Other', 'LocLimit3Contents',
    'LocLimit4BI','LocDed1Building','LocDed2Other','LocDed3Contents',
    'LocDed4BI','LocLimit6All','LocDed6All','LocDedType1Building',
    'LocDedType2Other','LocDedType3Contents','LocDedType4BI','LocDedType6All',
    'LocLimitType1Building','LocLimitType2Other','LocLimitType3Contents',
    'LocLimitType4BI','LocLimitType6All']

fm_acc_fileds = []

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