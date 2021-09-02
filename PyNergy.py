import pandas as pd
import geopandas as gpd

def get_geometry(df):

    shapes = gpd.read_file('data/shapes/regions-20170102.shp')

    # Adds geomatry from shapes
    # Drop regions not in dataset
    to_drop = ['La Réunion', 'Mayotte', 'Guyane', 'Guadeloupe', 'Martinique', 'Corse']
    shapes = shapes[~shapes.nom.isin(to_drop)]
    shapes.drop(columns=['wikipedia', 'wikidata', 'surf_ha', 'nom'], inplace=True)
    # Cast to int
    shapes.insee = shapes.insee.astype(int)
    # Merge
    gpd_df = pd.merge(left=df, left_on='code_insee_region', right=shapes, right_on='insee')
    gpd_df.drop(columns=['insee'], inplace=True) # Removes duplicates columns with insee code
    # Transform pd.DataFrame to gpd.GeoDataFrame
    # in order to save geometric type columns
    # something you cannot do with Pandas
    gdf = gpd.GeoDataFrame(gpd_df)

    return gdf