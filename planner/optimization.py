import networkx as nx
import googlemaps
from decouple import config

gmaps = googlemaps.Client(key=config('GOOGLE_MAPS_API_KEY'))

def calculate_optimal_route(locations):
    """
    Calculate the optimal route using NetworkX's implementation of TSP
    Args:
        locations: List of Location objects
    Returns:
        List of locations in optimal order
    """
    if not locations:
        return []
    
    # Create a complete graph
    G = nx.complete_graph(len(locations))
    
    # Add distances as edge weights
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            origin = f"{locations[i].latitude},{locations[i].longitude}"
            destination = f"{locations[j].latitude},{locations[j].longitude}"
            
            # Get distance from Google Maps
            result = gmaps.distance_matrix(origin, destination, mode="driving")
            distance = result['rows'][0]['elements'][0]['distance']['value']
            
            # Add edge with weight
            G[i][j]['weight'] = distance
            G[j][i]['weight'] = distance
    
    # Calculate optimal route using TSP approximation
    tsp_route = nx.approximation.traveling_salesman_problem(G, cycle=True)
    
    # Return ordered locations
    return [locations[i] for i in tsp_route[:-1]]  # Exclude last node as it's same as first
