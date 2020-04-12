
def merge_and_rename (input_featclass, output_shapefile):
    #importing required packages and modules
    import arcpy
    import os
    from arcpy import env
    
    #assigning variable to user-fed parameters
    env.workspace=input_featclass
    env.overwriteOutput=True
    output=output_shapefile

    #Listing all the featureclasses in user-fed gdb 
    fcs=arcpy.ListFeatureClasses()
    
    #iterating through all the featureclass, creating a field inside the attribute table called "Name",
    # and appending the name of the featureclass into the "Name" field
    for f in fcs:       
        # assigning variable for the name of shapefile without extension
        name=os.path.splitext(f)[0]

        #Adding field called Name and updating the name for each shapefile in that field
        arcpy.AddField_management(f, 'Name', 'TEXT')
        with arcpy.da.UpdateCursor(f, 'Name') as cur:
            for row in cur:
                row[0]=name
                cur.updateRow(row)

    #Merging all the edited featureclasses into a single shapefile.
    arcpy.Merge_management(fcs, output)
    print"Successfully merged and renamed the feature classes inside the attribute table"

#merge_and_rename(r"..\test.gdb", r"\test.shp")

