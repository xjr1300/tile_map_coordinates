import unittest

from tile_map_coordinates import (
    deg2tile_xy,
    tile2deg,
    tile_lat_edges,
    tile_lon_edges,
    tile_edges,
)

# 富士山三角点
FUJI_LON = 138.0 + 43.0 / 60.0 + 39 / 3600.0
FUJI_LAT = 35.0 + 21.0 / 60 + 39.0 / 3600.0


class TestDeg2TileXy(unittest.TestCase):
    """deg2tile_xy関数のテスト"""

    def test(self) -> None:
        expected_list = (
            (1, (1, 0)),
            (2, (3, 1)),
            (3, (7, 3)),
            (4, (14, 6)),
            (5, (28, 12)),
            (6, (56, 25)),
            (7, (113, 50)),
            (8, (226, 101)),
            (9, (453, 202)),
            (10, (906, 404)),
            (11, (1813, 808)),
            (12, (3626, 1617)),
            (13, (7252, 3234)),
            (14, (14505, 6469)),
            (15, (29011, 12939)),
            (16, (58022, 25878)),
            (17, (116045, 51756)),
            (18, (232090, 103513)),
        )
        for expected in expected_list:
            x_tile, y_tile = deg2tile_xy(FUJI_LON, FUJI_LAT, expected[0])
            self.assertEqual(expected[1][0], x_tile, f"{expected}")
            self.assertEqual(expected[1][1], y_tile, f"{expected}")


class TestTile2Deg(unittest.TestCase):
    """tilt2deg関数のテスト"""

    def test(self) -> None:
        expected = (138.724365234375, 35.362176059146805)
        actual = tile2deg(29011, 12939, 15)
        self.assertAlmostEqual(expected[0], actual[0], places=6)
        self.assertAlmostEqual(expected[1], actual[1], places=6)


class TesTileLatEdges(unittest.TestCase):
    """tile_lat_edges関数のテスト"""

    def test(self) -> None:
        expected = (35.353216101238225, 35.362176059146805)
        actual = tile_lat_edges(12939, 15)
        self.assertAlmostEqual(expected[0], actual[0], places=6)
        self.assertAlmostEqual(expected[1], actual[1], places=6)


class TesTileLonEdges(unittest.TestCase):
    """tile_lon_edges関数のテスト"""

    def test(self) -> None:
        expected = (138.724365234375, 138.7353515625)
        actual = tile_lon_edges(29011, 15)
        self.assertAlmostEqual(expected[0], actual[0], places=6)
        self.assertAlmostEqual(expected[1], actual[1], places=6)


class TestTileEdges(unittest.TestCase):
    """tile_edges関数のテスト"""

    def test(self) -> None:
        expected = (
            138.724365234375,
            35.353216101238225,
            138.7353515625,
            35.362176059146805,
        )
        west, south, east, north = tile_edges(29011, 12939, 15)
        self.assertAlmostEqual(expected[0], west, places=6)
        self.assertAlmostEqual(expected[1], south, places=6)
        self.assertAlmostEqual(expected[2], east, places=6)
        self.assertAlmostEqual(expected[3], north, places=6)
