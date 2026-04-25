from physics import drag, weight, lift

velocity = float(input("Velocity (m/s): ")
wing_area = float(input("Wing area (m^2): "))
cl = float(input("Lift coefficient: "))
cd = float(input("Drag coefficient: "))
mass = float(input("Mass (kg): "))
thrust = float(input("Thrust (N): "))

L = lift(velocity, wing_area, cl)
D = drag(velocity, wing_area, cd)
W = weight(mass)

print("\n--- RESULTS ---")
print("Lift:", round(L, 2))
print("Drag:", round(D, 2))
print("Weight:", round(W, 2))

if L > W and thrust > D:
    print("Status: Climbing 🚀")
elif L < W:
    print("Status: Descending 📉")
else:
    print("Status: Stable ✈️")
