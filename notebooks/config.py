import os 

MAIN_PATH=os.path.dirname(os.getcwd())
DATA_FOLDER=os.path.join(MAIN_PATH, 'datos')
IMAGES_FOLDER=os.path.join(MAIN_PATH, 'plots')

RAW_DATA_DIR=os.path.join(DATA_FOLDER, 'ce2019_jal.csv')
BASE_DATOS_DIR=os.path.join(DATA_FOLDER, 'base_datos.csv')
MATRICES_DIR=os.path.join(DATA_FOLDER, 'matrices_especializacion.csv')
NAME_DATA_DIR=os.path.join(DATA_FOLDER, 'nombres_municipios.csv')
REGIONES_DATA_FOLDER=os.path.join(DATA_FOLDER, 'regiones')

REGIONES_IMAGE_FOLDER=os.path.join(IMAGES_FOLDER, 'regiones')


