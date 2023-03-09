# About

This is a forked version of the cpca project (https://github.com/DQinYuan/chinese_province_city_area_mapper). 

# Purpose

cpca has stopped maintenance since 2021. We encountered several problems during using cpca.  
Some of the problems are:  

1. Inaccessible map data.  
cpca uses the map patches from openstreetmap.org, which can not be accessed now. 

<img src='inaccessible_map_data.png'>

2. Fix some bugs due to incompatible versions. 

Issue: In `drawer.echarts_draw`, `ImportError: cannot import name 'environmentfunction' from 'jinja2'`  
Fix: `jinja2==3.0.0`

Issue: `cannot import name 'Geo' from 'pyecharts'`  
Fix: support the latest pyecharts version. `from pyecharts.charts import Geo`

3. Two few style configurations.   
cpca doesnot expose enough parameters to configure the map styles. e.g., `draw_locations()`, `echarts_draw()` and `echarts_cata_draw()` cannot set background and marker colors.

In this repo, we try to revise and fix the above issues. 

## Main Revisions

1. Use map tiles from AMap

```
def draw_locations(adcodes, file_path, 
                   tiles= 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7', 
                   attr = 'amap'):
    ...
    map_osm = folium.Map(location=[35, 110], zoom_start=5, 
                         tiles = tiles, attr=attr)
```

2. 

# Install

`pip install cpcax`

# Use

```


```