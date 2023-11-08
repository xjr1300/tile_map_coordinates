lint:
	poetry run black tile_map_coordinates
	poetry run isort tile_map_coordinates
	poetry run ruff tile_map_coordinates
fmt:
	poetry run black tile_map_coordinates
	poetry run isort tile_map_coordinates
	poetry run ruff tile_map_coordinates --fix
types:
	poetry run mypy tile_map_coordinates
