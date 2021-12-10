# coding=utf-8


import arcpy
import os, time

arcpy.env.overwriteOutput = True

# dirroot = r'E:\01_CityDiagnosis2021\01_Data'
# os.chdir(dirroot)

raw = r"C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis/"

poi_gdb = raw + r'02data\便民商业服务设施.gdb'
poi_buffer_gdb = raw + r'02data\便民商业服务设施buffer.gdb'
tempgdb = os.path.join(r'999_temp\index03.gdb')
tempgdb = raw + r'999_temp\index03.gdb'

arcpy.env.workspace = poi_buffer_gdb
citylist = arcpy.ListFeatureClasses()
len(citylist)

for city in citylist[5:]:
    print('--- Working with city: {} ---'.format(city))
    poi1 = poi_gdb + '/{}_bianlidian'.format(city) #便利店
    poi2 = poi_gdb + '/{}_chaoshi'.format(city) #超市
    poi3 = poi_gdb + '/{}_commu_service'.format(city) #社区服务中心
    poi4 = poi_gdb + '/{}_express'.format(city) #快递点
    poi5 = poi_gdb + '/{}_vege_market'.format(city) #菜市场
    poi6 = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\02data\Washroom.gdb\{}'.format(city) # 公厕
    poi7 = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\02data\Library.gdb\{}'.format(city)# 图书馆
    poi8 = unicode(r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\02data\消防站.gdb\{}'.format(city), 'utf-8')  #消防点

    for i in [poi1, poi2, poi3, poi4, poi5, poi6, poi7, poi8]:
        arcpy.DeleteField_management(i, ['typecode_x'])
    arcpy.Merge_management([poi1, poi2, poi3, poi4, poi5, poi6, poi7, poi8], tempgdb + '/' + city)



