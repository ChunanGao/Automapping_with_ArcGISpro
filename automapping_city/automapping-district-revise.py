# coding=utf-8

import arcpy
import os, time

arcpy.env.overwriteOutput = True


# 列出建成区和市辖区数据所在路径

raw = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis/'

shixiaqu_gdb = raw + r'01boundary\district0910.gdb' ##原始路径+市辖区边界

arcpy.env.workspace = shixiaqu_gdb

district_list = arcpy.ListFeatureClasses() ##所有城市list
for city in district_list:
    #fc = shixiaqu_gdb  + '/' + city
    field_names = []
    fields = arcpy.ListFields(city)
    for field in fields:
        field_names.append(field.name)
    if "NAME" in field_names:
        print(str(city)+ "yes")
    else:
        print(str(city) + 'no')
        arcpy.AddField_management(city, "NAME", "TEXT")
        arcpy.CalculateField_management(city, "NAME", "!COUNTY!", "PYTHON_9.3")

district_list.index('anshun')

raw = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis/'

builtup_gdb = raw + r'01boundary\builtup0910_1.gdb'##原始路径+建成区边界
bncs_gdb = raw + r'02data\bncs.gdb'##原始路径+避难场所
hospital_gdb = raw + r'02data\hospital23stars.gdb' ##原始路径+医院
hospital_buffer_gdb = raw + r'02data\hospital23stars_buffer.gdb' ##原始路径+医院覆盖范围
firestation_gdb = raw + r'02data\消防站.gdb' ##原始路径+消防站点位
firestation_service_gdb = raw + r'02data\fireStation7km.gdb' ##原始路径+消防站服务范围Network

arcpy.env.workspace = hospital_buffer_gdb

bncs_list = arcpy.ListFeatureClasses() ##所有城市list
#builtup_list.index('taiyuan')

hos_list = arcpy.ListFeatureClasses()
len(hos_list)

arcpy.env.workspace = firestation_gdb
fire_list = arcpy.ListFeatureClassess()
len(fire_list)


builtup_list[0:35]
builtup_list[36:]

len(bncs_list)
#builtup_list.remove('nanning')









