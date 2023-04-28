import pandas as pd

from chart import load_data


def test_load_basin_mouths():
    data = load_data.load_basins()
    assert isinstance(data, pd.DataFrame)

def test_load_chla():
    data = load_data.load_ocean_chla()
    assert isinstance(data, pd.DataFrame)

def test_load_tsm():
    data = load_data.load_ocean_tsm()
    assert isinstance(data, pd.DataFrame)
