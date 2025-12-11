# Raj-shekhar-Peri
# Raj Shekhar Peri - Aerospace & Mechanical Engineering Portfolio

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

## About

This repository contains computational tools, simulations, and analysis codes developed for aerospace and mechanical engineering applications. The projects demonstrate practical implementations of fundamental rocket propulsion principles, thermodynamics, and flight dynamics.

## 🚀 Projects

### 1. Nozzle Flow Calculator
**Location:** `projects/nozzle-equations/`

Computational tool for analyzing compressible flow through rocket nozzles, including:
- Isentropic flow relations
- Thrust coefficient calculations
- Expansion ratio optimization
- Nozzle geometry parameters

**Key Features:**
- Real-time flow property calculations
- Support for both converging and converging-diverging nozzles
- Visualization of pressure and Mach number distributions

### 2. Rocket Flight Simulation
**Location:** `projects/rocket-simulation/`

Physics-based simulation of rocket trajectories accounting for:
- Variable mass (propellant consumption)
- Atmospheric drag
- Gravity effects
- Multi-stage separation (if applicable)

**Key Features:**
- 1D vertical flight simulation
- Time-series output of altitude, velocity, and acceleration
- Burnout and apogee calculations
- Graphical trajectory visualization

### 3. Thrust Equation Calculator
**Location:** `projects/thrust-equation/`

Implementation of fundamental rocket thrust equations:
- Momentum thrust component
- Pressure thrust component
- Specific impulse calculations
- Chamber pressure effects

**Key Features:**
- Parametric analysis capabilities
- Comparison of different propellant combinations
- Performance optimization tools

## 📋 Requirements

```bash
Python >= 3.8
numpy >= 1.20.0
matplotlib >= 3.3.0
scipy >= 1.6.0
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Momentumspace/Raj-shekhar-Peri.git
cd Raj-shekhar-Peri
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Navigate to any project folder and run the scripts:
```bash
cd projects/nozzle-equations/
python nozzle_calculator.py
```

## 📖 Usage

Each project folder contains its own README with detailed usage instructions, example inputs, and expected outputs. Start with any project that interests you:

```bash
# For nozzle calculations
cd projects/nozzle-equations/
python nozzle_calculator.py

# For rocket simulation
cd projects/rocket-simulation/
python rocket_simulation.py

# For thrust calculations
cd projects/thrust-equation/
python thrust_equation.py
```

## 🎓 Background

These tools were developed as part of aerospace engineering coursework and research, focusing on:
- Rocket propulsion systems
- Compressible flow analysis
- Flight dynamics and trajectory optimization
- Thermodynamics and heat transfer

## 📊 Example Outputs

Each project includes example calculations and visualizations. See individual project READMEs for:
- Sample input parameters
- Expected numerical results
- Graphical outputs and plots
- Validation against analytical solutions

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Momentumspace/Raj-shekhar-Peri/issues).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

**Raj Shekhar Peri**
- GitHub: [@Momentumspace](https://github.com/Momentumspace)
- ORCID: https://orcid.org/0000-0002-6103-5667
- Email: rajshekhar@orbitallocker.com
- LinkedIn: https://www.linkedin.com/in/raj-shekhar-peri-33558b163/

## 🙏 Acknowledgments

- Aerospace engineering principles based on standard textbooks and research papers
- Computational methods validated against industry-standard tools
- Community feedback and suggestions

## 📚 References

Key references and theoretical background:
1. Sutton, G. P., & Biblarz, O. (2016). *Rocket Propulsion Elements*
2. Anderson, J. D. (2003). *Modern Compressible Flow*
3. Hill, P. G., & Peterson, C. R. (1992). *Mechanics and Thermodynamics of Propulsion*

---

**Note:** This repository is actively maintained and updated with new projects and improvements. Star ⭐ the repository to stay updated!
