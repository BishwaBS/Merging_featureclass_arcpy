# Merging_featureclass_arcpy

This repository contains a python function that merges featureclass (*.shp) within file geodatabase and appends the name of individual featureclass to merged shapefile

This package is oeirented towards ArcGIS users and to those who often play with shapefiles and geodatabases.

Why this package??
Suppose you have multiples shapefiles with name. When you merge those shapefiles to create a single shapefile in ArcGIS, your merged shapefile wouldn't carry the names of the shapefiles along with it. The merge shapefiles would have multiple rows correponding to featureclasses, but without their names. What if you have thousands of shapefiles in a merge file and want to select a specific shapefile with its name? This is where my package comes into handy.

What you need to do use this python file?
You would just need to pass in the path for the gdb file and the output shapefile. Note that the python file accepts only the gdb file. If you have shapefiles in a folder, you would have to lift a burdon of combining the individual shapefiles into a geodatabase.
