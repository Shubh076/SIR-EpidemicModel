
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

"""1. BASE"""
N = 1000
I0 = 1
R0_p = 0
S0 = N - I0 - R0_p

"""2. PARAMETERS"""
beta = 0.3
gamma = 0.1
print(f"R0 (basic reproduction number) = {beta/gamma:.1f}")

"""3. DIFF EQUATIONS"""
def SIR_eq(y, t, N, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I / N
    dI_dt = beta * S * I / N - gamma * I
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt

""" 4 SIM SETUP"""
days = 160
t = np.linspace(0, days, days)
y0 = S0, I0, R0_p

result = odeint(SIR_eq,y0,t, args=(N, beta, gamma))
S, I, R = result.T

"""5. GRAPH"""
plt.figure(figsize=(9, 5))
plt.plot(t, S, label="Susceptible", color="blue")
plt.plot(t, I, label="Infected", color="red")
plt.plot(t, R, label="Recovered", color="green" )
plt.xlabel("Days")
plt.ylabel("population")
plt.title("SIR_Simulation")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("SIR_Result.png", dpi=150)
plt.show()
print("Graph saved! Peak infection day:", t[np.argmax(I)])

