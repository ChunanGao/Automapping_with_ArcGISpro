# coding=utf-8


path = r'C:\Users\chuna\Desktop\CityDNA\botelini_check.gdb\botelini_check.gdb'
arcpy.env.workspace = r'C:\Users\chuna\Desktop\CityDNA\2021.10.14\botelini_check.gdb\botelini_check.gdb'
fclist = arcpy.ListFeatureClasses()



#fclist2 = [i for i in fclist if i.endswith('_ratio')]




import arcpy, os, csv

path = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\01boundary\边界带指标02\town_clip.gdb'
arcpy.env.workspace = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\01boundary\边界带指标02\town_clip.gdb'
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    print(fc)
    arcpy.TableToTable_conversion(fc, r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\town_outcsv02', fc + '.csv')


import arcpy, os, csv

path = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\01boundary\边界带指标03\town_clip.gdb'
arcpy.env.workspace = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\01boundary\边界带指标03\town_clip.gdb'
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    print(fc)
    arcpy.TableToTable_conversion(fc, r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\town_outcsv03', fc + '.csv')


