from config import NAME_DATA_DIR
import pandas as pd

regiones ={
'norte': [19, 31, 25, 41, 42, 61, 76, 81, 104, 115 ],
'altos_norte' : [35, 53, 64, 72, 73, 91, 109,116],
'altos_sur' : [1, 8, 117, 46, 48, 60, 125, 74, 78, 93, 111, 118],
'cienega' : [13, 16, 33, 47, 18, 63, 66, 105, 123],
'sureste' : [30, 26, 50, 57, 59, 69, 56, 96, 107, 112],
'sur' : [79, 49, 65, 113, 85, 87, 99, 103, 108, 121, 122, 23],
'sierra' : [11,15,17,32,28,34,37,54,52,88,90,102,106,110],
'costa_sur': [21, 22, 27, 43, 100, 68],
'costa_sierra' : [12, 20, 38, 58, 62, 67, 80, 84],
'valles' : [3, 5, 6, 9, 36, 40, 55, 7, 75, 83, 94, 95],
'lagunas': [2, 4, 10, 14, 24, 77, 82, 86, 89, 92, 114, 119],
'centro' : [29, 70, 39, 44, 45, 51, 71, 98, 97, 101, 120, 124]
}



def idx_to_name(idx):
    df=pd.read_csv(NAME_DATA_DIR)

    return df[df['CVE_MUN']==idx].loc[:, 'NOM_MUN'].values[0]