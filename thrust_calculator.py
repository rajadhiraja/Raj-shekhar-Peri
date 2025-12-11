# Rocket thrust equation in general#
m = float(input("Enter the mass flow rate in kg/s"))
A = float(input("Enter the Area of the exit))
Pe = float(input("Enter the Exit Pressure"))
P0 = float(input("Enter the Ambient pressure"))
V = float(input("Enter the Velocity at exit"))
F = (m*V)+(Pe-P0)*A
print(F)
