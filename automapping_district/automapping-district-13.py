# coding=utf-8

import arcpy
import os, time

arcpy.env.overwriteOutput = True

def mikfolder(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

def zoomToLyrs(layerList, lyt, edge_num, edge_pct=10):
    xmin = ymin = xmax = ymax = 0
    mf = lyt.listElements("mapframe_element")[0]

    i2 = 0
    for lyr in layerList:
        ext = mf.getLayerExtent(lyr)
        if i2 == 0:
            xmin = ext.XMin
            ymin = ext.YMin
            xmax = ext.XMax
            ymax = ext.YMax
        else:
            if ext.XMin < xmin:
                xmin = ext.XMin
            if ext.YMin < ymin:
                ymin = ext.YMin
            if ext.XMax > xmax:
                xmax = ext.XMax
            if ext.YMax > ymax:
                ymax = ext.YMax
        i2 += 1

    xmin = xmin - edge_num
    xmax = xmax + edge_num
    ymin = ymin - edge_num
    ymax = ymax + edge_num
    # xmin = xmin - int(xmin * edge_pct * 0.01)
    # xmax = xmax + int(xmax * edge_pct * 0.01)
    # ymin = ymin - int(ymin*edge_pct*0.01)
    # ymax = ymax + int(ymax*edge_pct*0.01)

    new_extent = arcpy.Extent(xmin, ymin, xmax, ymax)
    mf.camera.setExtent(new_extent)


# 设置文件夹路径
root_path = r"C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\05Maps\auto_mapping\output_district" ##raw路径
outmap_fd = os.path.join(root_path, "output_map_13PEfieldPP")  ##create outmap folder
outmxd_fd = os.path.join(root_path, "output_mxd_13PEfieldPP")  ##create outmxd folder
mikfolder(outmap_fd)
mikfolder(outmxd_fd)
indi_gdb_path = os.path.join(os.path.join(root_path, "13PEfieldPP_gdb"), "13PEfieldPP.gdb") #手动添加

# get ready for all the mxd realated variables
aprx = arcpy.mp.ArcGISProject('current')

lyt = aprx.listLayouts()[0]
m = aprx.listMaps()[0]


raw = r'C:\Users\chuna\Desktop\CityDNA\2021-11-24\01_59Cities_Diagnosis\01boundary/'
district_gdb = raw + r'边界带指标02\district_clip.gdb'  ##边界带指标
shixiaqu_gdb = raw + r'district0910.gdb' ##原始路径+市辖区边界

arcpy.env.workspace = district_gdb


def addtown(lyrname, file_path, shp_stat,name_element, zoomYN='no'):
    # 建成区边界
    builtup_lyr = m.listLayers(lyrname)[0]
    # 添加乡镇数据
    builtup_shp_path = os.path.join(file_path, shp_stat)
    builtup_fc_path = os.path.join(indi_gdb_path, "{}".format(name_element + lyrname))
    arcpy.CopyFeatures_management(builtup_shp_path, builtup_fc_path)
    builtup_fc_lyr = m.listLayers("{}".format(name_element + lyrname))[0]
    builtup_fc_lyr.visible = False
    # change its symbology
    builtup_lyr.updateConnectionProperties(builtup_lyr.connectionProperties, builtup_fc_lyr.connectionProperties)
    # zoom to layer
    if zoomYN == 'yes':
        builtup_lyr = m.listLayers(lyrname)[0]
        layerList = [builtup_lyr]
        zoomToLyrs(layerList, lyt, 1300)

shp_list = arcpy.ListFeatureClasses() ##所有城市list

time1 = time.time()
for shp_stat in shp_list[2:]:
    print(shp_stat)
    name_element = shp_stat

    # 添加变量图层
    addtown('市辖区边界', shixiaqu_gdb, shp_stat, name_element, zoomYN='no')
    addtown('建成区边界', district_gdb, shp_stat, name_element, zoomYN='yes')

 # save pic and aprx
    lyt = aprx.listLayouts()[0]
    pic_path = os.path.join(outmap_fd, name_element + "_map.jpg")
    lyt.exportToJPEG(pic_path, resolution=200)

    mxd_copy_path = os.path.join(outmxd_fd, name_element + ".aprx")
    aprx.saveACopy(mxd_copy_path)

 # finally remove three added route related layers
    m.removeLayer(m.listLayers("{}".format(name_element + '市辖区边界'))[0])
    m.removeLayer(m.listLayers("{}".format(name_element + '建成区边界'))[0])


print('总时间消耗：' + str(round((time.time() - time1)/60, 2)) + 'min')