import importlib.resources

import pandas as pd

def load_basins() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'basin_mouth.csv'
    with resource.open('r') as fin:
        data = pd.read_csv(fin)
    return data

def load_ocean_chla() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'OceanColor_CHART_Chla.xlsx'
    with resource.open('rb') as fin:
        data = pd.read_excel(fin)
    return data

def load_ocean_tsm() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'OceanColor_CHART_TSM.xlsx'
    with resource.open('rb') as fin:
        data = pd.read_excel(fin)
    return data

def load_wbm_sed_rivermouths() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'SE-Asia_River-Mouth_HydroSTN30_SED_01min_mTS.csv'
    with resource.open('r') as fin:
        data = pd.read_csv(fin)
    return data

def load_wbm_water_rivermouths() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'SE-Asia_River-Mouth_HydroSTN30_01min_mTS.csv'
    with resource.open('r') as fin:
        data = pd.read_csv(fin)
    return data

def load_wbm_water_riverbasins() -> pd.DataFrame:
    resource = importlib.resources.files('chart.data')/'SE-Asia_River-Basin_HydroSTN30_01min_mTS.csv'
    with resource.open('r') as fin:
        data = pd.read_csv(fin)
    return data
