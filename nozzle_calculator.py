import tkinter as tk
import math
import matplotlib.pyplot as plt

def calculate():
    try:
        # Get the input values from the entry widgets
        Pc = float(entry_Pc.get())
        Tc = float(entry_Tc.get())
        Gc = float(entry_Gc.get())
        Cp = float(entry_Cp.get())
        me = float(entry_me.get())
        r = float(entry_r.get())
        pos = float(entry_pos.get())
        P = float(entry_P.get())
        l = float(entry_l.get())

        # Calculate the temperature, velocity, Mach number, area, density, nozzle pressure ratio, and mass flow per unit area
        T = (Tc) * ((P / Pc) ** (r - 1 / r))
        V = math.sqrt(2 * Cp * (Tc - T))
        M = V / math.sqrt(r * Gc * Tc)
        A = (me * Gc * Tc) / (Pc * V)
        ro = (me) / (A * V)
        NPR = (P / Pc)
        mass_flow_area = (me / A)

        # Update the result labels with the calculated values
        result_T_label.config(text=f"The Temperature at each station is: {T} K")
        result_V_label.config(text=f"The Velocity is: {V} m/s")
        result_M_label.config(text=f"The Mach Number is: {M}")
        result_A_label.config(text=f"The Area is: {A} m^2")
        result_NPR_label.config(text=f"The Nozzle Pressure Ratio is: {NPR}")
        result_mass_flow_area_label.config(text=f"The Mass flow per unit Area is: {mass_flow_area}")

        # Plot the Nozzle Pressure Ratio as a function of Area
        area_values = [i for i in range(1, int(A) + 1)]
        npr_values = [(P / Pc) for _ in area_values]

        plt.plot(area_values, npr_values)
        plt.xlabel('Area (m^2)')
        plt.ylabel('Nozzle Pressure Ratio')
        plt.title('Nozzle Pressure Ratio vs. Area')
        plt.show()

    except ValueError:
        result_T_label.config(text="Invalid input!")
        result_V_label.config(text="Invalid input!")
        result_M_label.config(text="Invalid input!")
        result_A_label.config(text="Invalid input!")
        result_NPR_label.config(text="Invalid input!")
        result_mass_flow_area_label.config(text="Invalid input!")

# Create the main window
window = tk.Tk()

# Create entry widgets to get the input values
entry_Pc = tk.Entry(window)
entry_Pc.pack()
entry_Pc_name = tk.Label(window, text="Chamber_pressure:")
entry_Pc_name.pack()

entry_Tc = tk.Entry(window)
entry_Tc.pack()
entry_Tc_name = tk.Label(window, text="Chamber_Temperature:")
entry_Tc_name.pack()

entry_Gc = tk.Entry(window)
entry_Gc.pack()
entry_Gc_name = tk.Label(window, text="Gas Constant:")
entry_Gc_name.pack()

entry_Cp = tk.Entry(window)
entry_Cp.pack()
entry_Cp_name = tk.Label(window, text="Value of Cp:")
entry_Cp_name.pack()

entry_me = tk.Entry(window)
entry_me.pack()
entry_me_name = tk.Label(window, text="Enter mass flow:")
entry_me_name.pack()

entry_r = tk.Entry(window)
entry_r.pack()
entry_r_name = tk.Label(window, text="Value of Gamma r:")
entry_r_name.pack()

entry_pos = tk.Entry(window)
entry_pos.pack()
entry_pos_name = tk.Label(window, text="Position at each station:")
entry_pos_name.pack()

entry_P = tk.Entry(window)
entry_P.pack()
entry_P_name = tk.Label(window, text="Pressure at each station:")
entry_P_name.pack()

entry_l = tk.Entry(window)
entry_l.pack()
entry_l_name = tk.Label(window, text="length of Nozzle:")
entry_l_name.pack()

# Create a button to calculate the results
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create labels to display the results
result_T_label = tk.Label(window, text="The Temperature at each station is: ")
result_T_label.pack()
result_V_label = tk.Label(window, text="The Velocity is: ")
result_V_label.pack()
result_M_label = tk.Label(window, text="The Mach Number is: ")
result_M_label.pack()
result_A_label = tk.Label(window, text="The Area is: ")
result_A_label.pack()
result_NPR_label = tk.Label(window, text="The Nozzle Pressure Ratio is: ")
result_NPR_label.pack()
result_mass_flow_area_label = tk.Label(window, text="The Mass flow per unit Area is: ")
result_mass_flow_area_label.pack()

# Start the main event loop
window.mainloop()
