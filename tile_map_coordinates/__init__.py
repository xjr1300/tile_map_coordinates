import math

# 座標値(x, y)
Coordinate = tuple[float, float]
# 矩形範囲(west, south, east, north)
Extent = tuple[float, float, float, float]
# 範囲(min, max)
Range = tuple[float, float]


def deg2tile_xy(lon_deg: float, lat_deg: float, zoom: int) -> Coordinate:
    """緯度、経度及びズームレベルからタイル座標を計算する。

    Args:
        lon_deg (float): 経度
        lat_deg (float): 緯度
        zoom (int): 計算するタイル座標のズームレベル

    Returns:
        Coordinate: タイル座標のXとYを格納したタプル
    """
    lat_rad = math.radians(lat_deg)
    n = 1 << zoom
    x_tile = int((lon_deg + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return x_tile, y_tile


def tile2deg(x_tile: int, y_tile: int, zoom: int) -> Coordinate:
    """タイル座標から経度と緯度を計算する。

    Args:
        x_tile (int): タイル座標のX値
        y_tile (int): タイル座標のY値
        zoom (int): タイル座標のズームレベル

    Returns:
        Coordinate: タイル座標の左上の経度と緯度を格納したタプル
    """
    n = 1 << zoom
    lon_deg = x_tile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y_tile / n)))
    lat_deg = math.degrees(lat_rad)
    return lon_deg, lat_deg


def mercator_to_lat(mercator_y: float) -> float:
    """メルカトル座標系のY座標から緯度を計算する。

    Args:
        mercator_y (float): メルカトル座標系のY座標

    Returns:
        float: 緯度
    """
    return math.degrees(math.atan(math.sinh(mercator_y)))


def tile_lat_edges(y_tile: float, zoom: int) -> Range:
    """タイル座標の緯度の範囲を計算する。

    Args:
        y_tile (float): タイル座標のY値
        zoom (int): タイル座標のズームレベル

    Returns:
        Range: タイル座標の緯度の範囲(south, north)
    """
    n = 1 << zoom
    unit = 1 / n
    y1 = y_tile * unit
    yw = y1 + unit
    lat1 = mercator_to_lat(math.pi * (1 - 2 * y1))
    lat2 = mercator_to_lat(math.pi * (1 - 2 * yw))
    return lat2, lat1


def tile_lon_edges(tile_x: float, zoom: int) -> Range:
    """タイル座標の経度の範囲を計算する。

    Args:tile_x
        x_tile (float): タイル座標のX値
        zoom (int): タイル座標のズームレベル

    Returns:
        Range: タイル座標の経度の範囲(west, east)
    """
    n = 1 << zoom
    unit = 360.0 / n
    lon1 = -180.0 + tile_x * unit
    lon2 = lon1 + unit
    return lon1, lon2


def tile_edges(tile_x: float, tile_y: float, zoom: int) -> Extent:
    """タイル座標の範囲を計算する。

    Args:
        tile_x (float): タイル座標のX値
        tile_y (float): タイル座標のY値
        zoom (int): タイル座標のズームレベル

    Returns:
        Extent: タイル座標の緯度軽度の範囲を格納したタプル(w, s, e, n)
    """
    south, north = tile_lat_edges(tile_y, zoom)
    west, east = tile_lon_edges(tile_x, zoom)
    return west, south, east, north
