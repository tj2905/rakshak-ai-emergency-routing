import streamlit as st
import folium
from streamlit_folium import st_folium
from roads import create_city_graph, locations
from utils import (
    shortest_route, rakshak_route, apply_rakshak_weights,
    calculate_route_time, get_current_traffic_status
)
import datetime

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="RAKSHAK AI",
    page_icon="🚑",
    layout="wide"
)

# -------------------------
# Session state init
# -------------------------
if "show_routes" not in st.session_state:
    st.session_state.show_routes = False

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("🚨 Rakshak AI Control Panel")
st.sidebar.write("Emergency Routing Simulator")
import pytz
ist = pytz.timezone("Asia/Kolkata")
now_ist = datetime.datetime.now(ist)

st.sidebar.write("⏱️ Current Time (IST):", now_ist.strftime("%H:%M"))
# -------------------------
# Title and intro
# -------------------------
st.title("🚑 RAKSHAK AI - Emergency Smart Routing System")
st.markdown("## AI-Powered Emergency Routing for Smart Cities")
st.markdown(
    "RAKSHAK AI helps emergency vehicles reach destinations faster by "
    "avoiding congested and narrow roads using intelligent route optimization."
)

# -------------------------
# Traffic Status
# -------------------------
traffic_status, multiplier = get_current_traffic_status()
st.markdown(f"### Current Traffic: {traffic_status} (Multiplier: {multiplier}x)")

st.markdown("---")

# -------------------------
# User Inputs
# -------------------------
st.markdown("### 🎯 Step 1: Configure Emergency Route")

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_type = st.selectbox(
        "🚗 Emergency Vehicle Type",
        ["Ambulance", "Fire Truck", "Police Vehicle"]
    )

with col2:
    hospitals = [loc for loc in locations.keys() if "Hospital" in loc]
    start = st.selectbox("🏥 Starting Hospital", hospitals)

with col3:
    destinations = [loc for loc in locations.keys() if "Hospital" not in loc]
    end = st.selectbox("📍 Emergency Location", destinations)

# -------------------------
# Buttons
# -------------------------
bcol1, bcol2 = st.columns(2)

with bcol1:
    if st.button("🚨 Activate Emergency Routing", type="primary"):
        st.session_state.show_routes = True

with bcol2:
    if st.button("Reset"):
        st.session_state.show_routes = False

# -------------------------
# ROUTE ENGINE (persistent)
# -------------------------
if st.session_state.show_routes:

    G = create_city_graph()
    G = apply_rakshak_weights(G, vehicle_type)

    normal = shortest_route(G, start, end)
    rakshak = rakshak_route(G, start, end)

    if normal and rakshak:

        st.markdown("---")
        st.markdown("### 📊 Route Comparison")

        normal_time = calculate_route_time(G, normal, "weight")
        rakshak_time = calculate_route_time(G, rakshak, "rakshak_weight")
        time_saved = normal_time - rakshak_time

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Normal Route Time", f"{normal_time:.1f} min")

        with c2:
            st.metric(
                "Rakshak AI Route Time",
                f"{rakshak_time:.1f} min",
                delta=f"-{time_saved:.1f} min"
            )

        with c3:
            st.metric("Stops (AI Route)", len(rakshak))

        st.markdown("#### 🗺️ Route Details")

        rc1, rc2 = st.columns(2)
        with rc1:
            st.markdown("**🔴 Normal Route:**")
            st.write(" > ".join(normal))

        with rc2:
            st.markdown("**🟢 Rakshak AI Route:**")
            st.write(" > ".join(rakshak))

        st.success(
            f"✅ Rakshak AI reduces estimated delay by {time_saved:.1f} minutes "
            f"for {vehicle_type}"
        )

        # -------------------------
        # Map
        # -------------------------
        st.markdown("---")
        st.markdown("### 🗺️ Visual Route Map")

        m = folium.Map(
            location=[26.9124, 75.7873],
            zoom_start=12
        )

        for place, coords in locations.items():
            color = "blue"
            if place == start:
                color = "green"
            elif place == end:
                color = "red"

            folium.Marker(
                coords,
                tooltip=place,
                icon=folium.Icon(color=color)
            ).add_to(m)

        folium.PolyLine(
            [locations[x] for x in normal],
            color="red",
            weight=6
        ).add_to(m)

        folium.PolyLine(
            [locations[x] for x in rakshak],
            color="green",
            weight=8
        ).add_to(m)

        st_folium(m, width=1100, height=600)

    else:
        st.error("❌ No route found between selected locations")

# -------------------------
# Info Sections
# -------------------------
st.markdown("---")
st.markdown("### 🇮🇳 Built for Indian Cities")
st.markdown(
    "**Rakshak AI aapki jaan bachane ke liye design kiya gaya hai.** "
    "(Rakshak AI is designed to save your life.)"
)
st.markdown("---")
st.markdown("### ❓ Why This Matters")
st.write(
    "In emergency situations, every minute of delay can increase the risk to a "
    "patient's life by up to 10%. Traffic congestion and narrow roads often slow "
    "down ambulances in Indian cities. In Jaipur specifically, ambulances face "
    "8-15 minute delays during peak hours. Rakshak AI is designed to reduce that "
    "delay using intelligent route optimization that considers real-world factors."
)
st.markdown("---")
st.markdown("### 🤖 How Rakshak AI Works")
st.write("Rakshak AI assigns a priority score to each road based on multiple factors:")
st.write("1. **Road Width** - Wider roads allow faster emergency vehicle passage")
st.write("2. **Traffic Congestion** - Real-time traffic density on each route")
st.write("3. **Time of Day** - Rush hour vs normal vs late night traffic patterns")
st.write("4. **Vehicle Type** - Fire trucks need wide roads, ambulances prioritize speed")
st.write(
    "The system then calculates the route that minimizes emergency response delay, "
    "not just distance. This can save critical minutes in life-threatening situations."
)
st.markdown("---")
st.markdown("### 🚀 Future Scope")
st.write("In the future, Rakshak AI can integrate with:")
st.write("- Live traffic feeds from Google Maps / Bing Maps APIs")
st.write("- Smart traffic signal systems for automatic green lights")
st.write("- City emergency control rooms (108 ambulance dispatch)")
st.write("- Real-time accident and roadblock data")
st.write("- Integration with all Indian cities beyond Jaipur")
st.write(
    "This can help build faster and more efficient emergency response systems "
    "for smart cities across India, potentially saving thousands of lives annually."
)
st.markdown("---")
st.markdown("### 📚 Research Background")
st.markdown("**Why Every Minute Matters:**")
st.write("- Studies show 1-minute delay in ambulance response increases mortality risk by 10%")
st.write("- Average ambulance delay in Indian cities: 8-15 minutes")
st.write("- Traffic congestion is the #1 cause of emergency vehicle delays")
st.write("- Jaipur handles 500+ emergency calls daily")
st.markdown("**Sources:** WHO Emergency Medical Services Report, 2023")

st.markdown("---")
st.markdown("Made with ❤️ for AMD Slingshot 2026 | AI for Smart cities")

