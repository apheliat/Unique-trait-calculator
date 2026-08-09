import streamlit as st

# Set page layout & title
st.set_page_config(page_title="Unit Trait Calculator", page_icon="⚔️", layout="centered")

st.title("⚔️ Unit Trait Calculator")
st.write("Enter your base unit stats and select a trait to calculate the final values.")

st.divider()

# Input Section (Sidebar or main layout)
col_in1, col_in2 = st.columns(2)

with col_in1:
    hp = st.number_input("Base HP", min_value=0.0, value=100.0, step=10.0)
    speed = st.number_input("Base Speed", min_value=0.0, value=10.0, step=1.0)

with col_in2:
    dps = st.number_input("Base DPS", min_value=0.0, value=50.0, step=5.0)
    size = st.number_input("Base Size / Supply", min_value=0.0, value=5.0, step=1.0)

trait = st.selectbox(
    "Select Trait",
    ["None", "Gloom", "Awakened", "Ghostly", "Lightning"]
)

# Calculation Logic
final_hp = float(hp)
final_speed = float(speed)
final_dps = float(dps)
final_size = float(size)

if trait == "Gloom":
    final_speed *= 0.50
    final_hp *= 3.00
    final_size -= 2
elif trait == "Awakened":
    final_hp *= 2.50
    final_dps *= 2.50
elif trait == "Ghostly":
    final_hp *= 2.00
    final_dps *= 2.00
    final_speed *= 1.50
    final_size -= 1
elif trait == "Lightning":
    final_dps *= 3.00

final_size = max(0.0, final_size)

st.divider()
st.subheader("📊 Final Modified Stats")

# Display Output as Modern Visual Cards
col_out1, col_out2, col_out3, col_out4 = st.columns(4)

col_out1.metric("HP", f"{final_hp:.1f}", delta=f"{final_hp - hp:+.1f}" if trait != "None" else None)
col_out2.metric("Speed", f"{final_speed:.1f}", delta=f"{final_speed - speed:+.1f}" if trait != "None" else None)
col_out3.metric("DPS", f"{final_dps:.1f}", delta=f"{final_dps - dps:+.1f}" if trait != "None" else None)
col_out4.metric("Size / Supply", f"{final_size:.1f}", delta=f"{final_size - size:+.1f}" if trait != "None" else None)