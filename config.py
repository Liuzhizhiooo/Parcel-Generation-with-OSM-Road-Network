# gbd文件根目录
FILE_ROOT = r'E:/Dataset/OSM/ParcelGenerationFromRoad/results'
DATABASE_NAME = 'ROAD_OPTIMIZE.gdb'

# OSM文件路径
OSM_PATH = r'E:/Dataset/OSM/ParcelGenerationFromRoad/data/hangzhou_road/osm_hangzhou.shp'

# 边界数据
BOUNDARY_PATH = r'E:/Dataset/OSM/ParcelGenerationFromRoad/data/border/hangzhou_roi.shp'

# 输出路径
OUTPUT_PATH = r'E:/Dataset/OSM/ParcelGenerationFromRoad/results'

# 按属性筛选的表达式
# 可以在Arcgis Pro软件里弄好, 点击生成python代码来生成
ROAD_SELECT_EXPRESSION = "highway IN ('motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'residential', 'unclassified') or railway IN ('rail')"

# 空间连接是需要保留的字段
FIELD_TO_KEEP = ['osm_id', 'name', 'highway', 'railway', 'z_order', 'other_tags']

# 投影的空间参考，不建议修改
PROJ_CRS = 3857

