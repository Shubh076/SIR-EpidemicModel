# SIR-EpidemicModel
Epidemiological SIR model built in python to simulate how a disease spreads through a population using differential equations

## What is the SIR Model
the SIR model divides a population into three groups:

- **Susceptible** - individuals who can be infected
- **Infected** - individuals who are currently infected and can spread it
- **Recovered** - individuals who have recovered and are now immune 

the model is governed by a system of three differential equations: 

```
dS/dt = -β * S * I / N
dI/dt = β * S * I / N - γ * I
dR/dt = γ * I
```

where:
- `N` = total population 
- `β` = infection rate
- `γ` = recovery rate
- `R₀ = β / γ` = basic reproduction number (average number of people one infected person will infect)

## Features 
- Solves the SIR differential equations using `scipy.integrate.odeinr`
- Calculates and prints basic reproduction number (R₀)
- Plots the Susceptible, Infected, and Recovered curves over time
- Identifies the peak day of infection

## Customization 

The following parameters can be changed to simulate different scenarios:

- Increase `β` to simulate more contagious disease
- Increase `γ` to simulate faster recovery
- Change `N` to simulate a larger or smaller population

## Example 

Running default parameters (`N=1000`, `β=0.3`, `γ=0.1`) produces : 

![image alt](https://github.com/Shubh076/SIR-EpidemicModel/blob/48009c8bc9961c6a55b1ac8dbbd995d7e7bdaa40/SIR_Result.png)

## Requirements 
All dependencies are listed in `requirements.txt`. Install them with:
```bash
pip install -r requiremnets.txt
```

##Usage 

```bash
python SIR MODEL.py
```
