# -*- coding: utf-8 -*-
from utils import *
import time
from os.path import join

def Process_Body(smooth_level: int = 30, extend_distance: int = 100, spike_keep: int = 500):
    """
    处理的主题函数
    """
    try:
        arcpy.CreateFileGDB_management(FILE_ROOT, DATABASE_NAME)
    except:
        print("gdb already exist")
    arcpy.env.workspace = join(FILE_ROOT, DATABASE_NAME)
    arcpy.env.outputMFlag = "DISABLE_M_VALUE"  # 禁用M值输出
    arcpy.env.overwriteOutput = True
    print(f"config workspace : {arcpy.env.workspace}")

    # 1. 裁剪 + 按属性筛选出所需要的道路
    osm_clip = Clip_Road(BOUNDARY_PATH, OSM_PATH)
    select_osm = Select_Road(osm_clip)
    raw_road = select_osm

    # 2. 缓冲区后获取中心线
    centerline = Convert_Centerline(select_osm, smooth_level)
    print(f"Convert_centerline Finish:{centerline}")

    # 3. 延伸中心线
    extendedlines = Extend_Road(centerline, extend_distance)
    print("Extend roads Finish")

    # 4. 检查拓扑
    err_point = Check_Topo(extendedlines)
    print("Check Topo Finish")

    # 5. 清除过短的悬挂线
    master_road = Clean_Spike(extendedlines, err_point, spike_keep, keep_spike=False)
    print("Clean Spike Finish")

    # 6. 把属性连接回来
    master_road = Join_Attributes(raw_road, master_road)
    road_result = Delete_Fields(master_road)

    # 7. 生成地块
    road_result = "road_results"
    parcel = Create_Parcel(road_result)
    return parcel

if __name__ == '__main__':
    print(f"😈😈😈😈😈            Begin process                     😈😈😈😈😈")
    start_time = time.time()
    output_path = Process_Body(smooth_level=10, extend_distance=100, spike_keep=500)
    print(f"🤭🤭🤭🤭🤭            processed                          🤭🤭🤭🤭🤭")
    print(f"🎉🎉🎉🎉🎉            time used: {time.time()- start_time}       🎉🎉🎉🎉🎉")
    print(f"🚀🚀🚀🚀🚀            result: {output_path}      🚀🚀🚀🚀🚀")