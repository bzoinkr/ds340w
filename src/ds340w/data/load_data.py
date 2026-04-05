from pyprojroot import here
import osmnx as ox
import geopandas as gpd

def load_san_juan_data(
    place_name: str = "San Juan, Puerto Rico", 
    filename: str = "kontur_population_PR_20231101.gpkg"
) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """
    Extracts drivable network and loads intersecting Kontur population data.
    """
    # Construct the absolute path to the raw data directory
    data_path = here() / "data" / "raw" / filename
    
    if not data_path.exists():
        raise FileNotFoundError(f"Expected data file at: {data_path}")

    # Extract road network
    G = ox.graph_from_place(place_name, network_type="drive")
    nodes, edges = ox.graph_to_gdfs(G)

    # Project to EPSG:3857 to match Kontur data projection before extracting bbox
    nodes_proj = nodes.to_crs("EPSG:3857")
    bounding_box = tuple(nodes_proj.total_bounds)

    # Load population data within the bounding box
    local_population = gpd.read_file(
        data_path,
        bbox=bounding_box
    )

    return nodes, edges, local_population

if __name__ == "__main__":
    # Test execution block
    nodes, edges, pop = load_san_juan_data()
    print(f"Nodes: {len(nodes)} | Edges: {len(edges)} | Hexagons: {len(pop)}")