import networkx as nx
# Enhanced: 20 locations covering key Jaipur areas
locations = {
# Hospitals
    "SMS Hospital": [26.9124, 75.7873],
    "Fortis Escorts Hospital": [26.8500, 75.8050],
    "Narayana Hospital": [26.8467, 75.7947],
    "Eternal Heart Care": [26.8892, 75.7781],
# Major Roads & Intersections
    "MI Road": [26.9160, 75.8200],
    "Tonk Road": [26.8700, 75.8100],
    "Ajmer Road": [26.9000, 75.7800],
    "JLN Marg": [26.9200, 75.7900],
    "Amber Road": [26.9850, 75.8500],
# Residential Areas
    "Malviya Nagar": [26.8500, 75.8000],
    "Vaishali Nagar": [26.9000, 75.7200],
    "Mansarovar": [26.8850, 75.7350],
    "C Scheme": [26.9120, 75.7870],
# Landmarks & Emergency Zones
    "City Palace": [26.9250, 75.8230],
    "Hawa Mahal": [26.9239, 75.8267],
    "Railway Station": [26.9180, 75.7870],
    "Airport": [26.8242, 75.8122],
    "Jal Mahal": [26.9531, 75.8458],
    "Sanganeri Gate": [26.8900, 75.8000],
    "Bani Park": [26.9300, 75.7850]
}
def create_city_graph():
#Creates road network with realistic Jaipur connections
    G = nx.Graph()
# Hospital connections to major roads
    G.add_edge("SMS Hospital", "MI Road", weight=5, width=3, traffic=4)
    G.add_edge("SMS Hospital", "Railway Station", weight=3, width=4, traffic=3)
    G.add_edge("Fortis Escorts Hospital", "Tonk Road", weight=4, width=4, traffic=3)
    G.add_edge("Narayana Hospital", "Tonk Road", weight=2, width=3, traffic=2)
    G.add_edge("Eternal Heart Care", "Ajmer Road", weight=3, width=4, traffic=3)
# Major road network
    G.add_edge("MI Road", "City Palace", weight=4, width=2, traffic=5)
    G.add_edge("MI Road", "C Scheme", weight=3, width=3, traffic=4)
    G.add_edge("MI Road", "Bani Park", weight=4, width=3, traffic=4)
    G.add_edge("Tonk Road", "Malviya Nagar", weight=5, width=4, traffic=3)
    G.add_edge("Ajmer Road", "Vaishali Nagar", weight=6, width=4, traffic=2)
    G.add_edge("JLN Marg", "C Scheme", weight=3, width=4, traffic=3)
# Residential to landmarks
    G.add_edge("Malviya Nagar", "City Palace", weight=5, width=3, traffic=3)
    G.add_edge("Vaishali Nagar", "Mansarovar", weight=4, width=3, traffic=2)
    G.add_edge("Mansarovar", "Sanganeri Gate", weight=4, width=3, traffic=3)
    G.add_edge("C Scheme", "Hawa Mahal", weight=2, width=2, traffic=5)
# Emergency zones
    G.add_edge("City Palace", "Hawa Mahal", weight=2, width=2, traffic=5)
    G.add_edge("Railway Station", "Bani Park", weight=3, width=3, traffic=4)
    G.add_edge("Airport", "Tonk Road", weight=8, width=5, traffic=2)
    G.add_edge("Jal Mahal", "Amber Road", weight=5, width=3, traffic=2)
    G.add_edge("Amber Road", "Bani Park", weight=6, width=4, traffic=3)
# Additional connections for network completeness
    G.add_edge("Sanganeri Gate", "Tonk Road", weight=3, width=3, traffic=3)
    G.add_edge("Hawa Mahal", "Bani Park", weight=4, width=2, traffic=4)
    G.add_edge("Ajmer Road", "JLN Marg", weight=5, width=4, traffic=3)
    return G