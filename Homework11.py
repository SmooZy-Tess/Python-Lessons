import pandas as pd

def chickenpox_by_sex():
    df = pd.read_csv('/lof/NISPUF17.csv')

    vacin=df[df['P_NUMVRC']>0] 
    males=vacin[vacin['SEX']==1]
    mnocpox=len(males[males['HAD_CPOX']==2])
    menratio=len(males[males['HAD_CPOX']==1])/mnocpox
 
    females=vacin[vacin['SEX']==2]
    wnocpox=len(females[females['HAD_CPOX']==2])  
    wratio=len(females[females['HAD_CPOX']==1])/wnocpox
    sootn={'male':menratio,'female':wratio}
    return sootn

print(chickenpox_by_sex())