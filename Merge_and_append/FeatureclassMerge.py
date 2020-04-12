
#Code for iterating through list of feature classes, adding name of the featureclass in attribute, and merging all the featureclasses into one featureclass
def merge_and_rename (input_featclass, output_shapefile):

    import arcpy
    import os
    from arcpy import env
    env.workspace=input_featclass
    env.overwriteOutput=True
    output=output_shapefile

    #Listing all the featureclass in Practise.gdb
    fcs=arcpy.ListFeatureClasses()
    print fcs
    for f in fcs:
        print f

        # assigning variable for the name of shapefile without extension
        name=os.path.splitext(f)[0]

        #Adding field called Name and updating the name for each shapefile in that field
        arcpy.AddField_management(f, 'Name', 'TEXT')
        with arcpy.da.UpdateCursor(f, 'Name') as cur:
            for row in cur:
                row[0]=name
                cur.updateRow(row)

    #Merging into a different,seperate shapefile.

    arcpy.Merge_management(fcs, output)
    print"Successfully merged and renamed the feature classes inside the attribute table"

merge_and_rename(r"J:\Research\Coding_Works\GITHUB\Merge_and_rename\test.gdb", r"J:\Research\Coding_Works\GITHUB\Merge_and_rename\test.shp")

