import osmnx as ox
import geopandas as gpd

# 1. Extract the localized drivable road network for San Juan
place_name = "Puerto Rico"
G = ox.graph_from_place(place_name, network_type="drive")

# Convert the NetworkX graph into GeoDataFrames for spatial operations
nodes, edges = ox.graph_to_gdfs(G)

# 2. Extract the geographic bounding box of the node network
# The total_bounds attribute returns a tuple: (minx, miny, maxx, maxy)
# This corresponds to (min_longitude, min_latitude, max_longitude, max_latitude)
bounding_box = tuple(nodes.total_bounds)

# 3. Load strictly the population data that intersects with the bounding box
# The bbox parameter forces the geopandas engine to filter the file before loading it into RAM
# Ensure 'kontur_population.gpkg' is in your working directory
local_population = gpd.read_file(
    "kontur_population_20231101.gpkg", 
    bbox=bounding_box
)

# Verify the extraction
print(f"San Juan road nodes extracted: {len(nodes)}")
print(f"San Juan population hexagons extracted: {len(local_population)}")