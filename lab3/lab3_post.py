#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 09:28:58 2025

@author: tarynreitsma
"""

import geopandas as gpd
import os
from sqlalchemy import create_engine
import pandas as pd

# paths from ArcGIS Pro downloads
dem_path = "/Users/tarynreitsma/Desktop/lab3/dem_pointaccuracy.shp"
weather_path = "/Users/tarynreitsma/Desktop/lab3/weather_pointaccuracy.shp"
weather_tpath = "/Users/tarynreitsma/Desktop/lab3/weather_exploratoryinterpolation.csv"
dem_tpath = "/Users/tarynreitsma/Desktop/lab3/dem_exploratoryinterpolation.csv"

# read into gdf and df
dem_gdf= gpd.read_file(dem_path)
weather_gdf = gpd.read_file(weather_path)
weather_df = pd.read_csv(weather_tpath)
dem_df = pd.read_csv(dem_tpath)

# create postgis engine using sqlalchemy
# CHANGE TO RUN
engine = create_engine("postgresql://myusername:mypassword@myhost:5432/mydatabase")  

# upload DEM points
dem_gdf.to_postgis("dem_pointaccuracy", engine)  

# upload weather points
weather_gdf.to_postgis("weather_pointaccuracy", engine)  

#Upload tables
weather_df.to_sql("weather_exploratoryinterpolation", engine)
dem_df.to_sql("dem_exploratoryinterpolation", engine)



