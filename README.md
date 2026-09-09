# Modeling-of-Photovoltaic-Cells-with-Simulation-Diagnostics-and-Monitoring
This is a personal project that aims to eventually build a homemade photovoltaic monitoring and diagnostics systems for personal use. Inspired by my classes in photovoltaics and optoelectronics, I am currently exploring options to have a centralized photovoltaic system for my domicile, reducing my carbon footprint with my own hands

## 1. Main File

Currently the main file supports the creation of PV cells, there are two models:

**Environmental model** Temperature and irradiation conditions
**Cell model** Based on the environmental model, create a Si PV Cell

## 2. Physics model

To make our PV cells as accurate as possible, the single-diode model is used, where the **I-V** and **V-P** characteristics are described by the following equation:

$I=I_{ph}-I_{0}*(e^{q*(V+I_{Rs})/nkT})-(V+IR_{s})/R_{sh}.

The cells are modeled individually and a given number of them can be used to form a complete PV Module. Some stochastic variation is added in the environmental conditions to account for natural variations of temperature and irradiation in the surface of the cell; this variation follows a normal distribution but it can be tuned to account for different effects in the cells
