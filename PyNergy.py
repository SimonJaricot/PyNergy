import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def get_geometry(df, left='code_insee_region', right='insee'):

    shapes = gpd.read_file('data/shapes/regions-20170102.shp')
    # Adds geometry from shapes
    # Cast to int
    shapes.insee = shapes.insee.astype(int)
    # Merge
    gpd_df = df.merge(left_on=left, right=shapes, right_on=right)
    # Transform pd.DataFrame to gpd.GeoDataFrame
    # in order to save geometric type columns
    # something you cannot do with Pandas
    gdf = gpd.GeoDataFrame(gpd_df)

    return gdf

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)