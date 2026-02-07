import networkx as nx
import datetime


def get_traffic_multiplier():
	"""Simulates realistic traffic based on time of day"""
	hour = datetime.datetime.now().hour
	# Morning rush: 8-10 AM
	if 8 <= hour < 10:
		return 2.0  # Heavy traffic
	# Evening rush: 5-8 PM
	elif 17 <= hour < 20:
		return 2.5  # Very heavy traffic
	# Night: 10 PM - 6 AM
	elif hour >= 22 or hour < 6:
		return 0.5  # Light traffic
	# Afternoon: 2-4 PM
	elif 14 <= hour < 16:
		return 1.5  # Moderate traffic
	else:
		return 1.0  # Normal traffic


def rakshak_score(width, traffic, vehicle_type="Ambulance"):
	"""
	AI scoring system for emergency routing
	Lower score = better route for emergency vehicles
	"""
	# Base score: narrow roads and high traffic are penalized
	base_score = (5 - width) + traffic
	# Apply time-based traffic multiplier
	multiplier = get_traffic_multiplier()
	base_score = base_score * multiplier
	# Vehicle-specific adjustments
	if vehicle_type == "Fire Truck":
		# Fire trucks NEED wide roads - heavily penalize narrow ones
		if width < 3:
			base_score += 5  # Major penalty for narrow roads
	elif vehicle_type == "Police Vehicle":
		# Police vehicles prioritize speed over road width
		base_score = base_score * 0.9  # 10% bonus on all roads
	# Ambulance uses base calculation (default)
	return base_score


def apply_rakshak_weights(G, vehicle_type="Ambulance"):
	"""Apply AI scoring to all roads in the network"""
	for u, v, data in G.edges(data=True):
		data["rakshak_weight"] = rakshak_score(
			data["width"],
			data["traffic"],
			vehicle_type
		)
	return G


def shortest_route(G, start, end):
	"""Normal shortest path (by distance only)"""
	try:
		return nx.shortest_path(G, start, end, weight="weight")
	except nx.NetworkXNoPath:
		return None


def rakshak_route(G, start, end):
	"""Rakshak AI optimized path (by emergency delay)"""
	try:
		return nx.shortest_path(G, start, end, weight="rakshak_weight")
	except nx.NetworkXNoPath:
		return None


def calculate_route_time(G, route, weight_key="weight"):
	"""Calculate total time for a route"""
	if not route or len(route) < 2:
		return 0
	total = 0
	for i in range(len(route) - 1):
		total += G[route[i]][route[i+1]][weight_key]
	return total


def get_current_traffic_status():
	"""Returns human-readable traffic status"""
	hour = datetime.datetime.now().hour
	multiplier = get_traffic_multiplier()
	if multiplier >= 2.0:
		return "Heavy Traffic", multiplier
	elif multiplier >= 1.5:
		return "Moderate Traffic", multiplier
	elif multiplier >= 1.0:
		return "Normal Traffic", multiplier
	else:
		return "Light Traffic", multiplier