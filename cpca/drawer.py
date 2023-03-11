# -*- coding: utf-8 -*-
from . import ad_2_addr_dict
from . import _fill_adcode
from collections import defaultdict
import itertools
import operator
import folium
from folium.plugins import HeatMap
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType


def ad2addr(part_adcode):
    return ad_2_addr_dict[_fill_adcode(part_adcode)]


def _base_input_check(locations):
    import pandas as pd
    from .exceptions import InputTypeNotSuportException
    if not isinstance(locations, pd.DataFrame):
        raise InputTypeNotSuportException(InputTypeNotSuportException.input_type)
    if "省" not in locations.columns or "市" not in locations.columns \
            or "区" not in locations.columns:
        raise InputTypeNotSuportException(InputTypeNotSuportException.input_type)


def _geo_update(geo, adcodes):
    coordinates = {}
    rest_adcodes = []
    for adcode in adcodes:
        if not ad2addr(adcode).longitude or not ad2addr(adcode).latitude:
            continue
        coordinates[adcode] = (float(ad2addr(adcode).longitude), float(ad2addr(adcode).latitude))
        rest_adcodes.append(adcode)
    geo._coordinates = coordinates
    return rest_adcodes


def folium_heatmap(adcodes, file_path, 
                   tiles= 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7', 
                   attr = 'amap'):
    """
    基于folium生成地域分布的热力图的html文件.
    :param adcodes: 地址集
    :param file_path: 生成的html文件的路径.
    """
    adcodes = filter(None, adcodes)

    # 注意判断key是否存在
    heatData = []
    for adcode in adcodes:
        attr_info = ad2addr(adcode)
        if not attr_info.latitude or not attr_info.longitude:
            continue
        heatData.append([float(attr_info.latitude), float(attr_info.longitude), 1])
    # 绘制Map，开始缩放程度是5倍
    map_osm = folium.Map(location=[35, 110], zoom_start=5, 
                         tiles = tiles, attr=attr)
    # 将热力图添加到前面建立的map里
    HeatMap(heatData).add_to(map_osm)
    # 保存为html文件
    map_osm.save(file_path)


def echarts_heatmap(adcodes, file_path, title="地域分布图"):
    """
    生成地域分布的echarts热力图的html文件.
    :param adcodes: 地址集
    :param file_path: 生成的html文件路径.
    :param title: 图表的标题
    """

    geo = Geo().add_schema(maptype="china")    
    
    coordinates = {}
    counter = defaultdict(int)
    for adcode in filter(None, adcodes):
        addr = ad2addr(adcode)
        if not addr.longitude or not addr.latitude:
            continue
        counter[adcode] = counter[adcode] + 1
        coordinates[adcode] = (float(addr.longitude), float(addr.latitude))
        geo.add_coordinate(adcode, float(addr.longitude), float(addr.latitude))
        
    geo.add(
        "geo",
        [list(z) for z in zip(counter.keys(), counter.values())],
        type_=ChartType.HEATMAP,
    ).set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title=title),
    ).render(file_path)