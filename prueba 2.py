import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos (puedes cambiarlos según tu caso)
posiciones = np.array([0, 2, 4, 8])      # en metros
tiempos = np.array([0, 3, 6, 10])   # en segundos

# Ajustamos un polinomio t(s): tiempo en función de la posición
coef_ts = np.polyfit(posiciones, tiempos, deg=2)
poly_ts = np.poly1d(coef_ts)

# Generamos muchos valores de posición para evaluar t(s)
s_vals = np.linspace(min(posiciones), max(posiciones), 100)
t_vals = poly_ts(s_vals)

# Invertimos los datos (s, t) para hacer ajuste de s(t) (posición en función del tiempo)
# Para eso, simplemente usamos los mismos puntos pero invirtiendo los ejes
coef_st = np.polyfit(tiempos, posiciones, deg=2)
poly_st = np.poly1d(coef_st)

# Derivamos para obtener velocidad y aceleración
poly_vt = np.polyder(poly_st)      # v(t) = ds/dt
poly_at = np.polyder(poly_vt)      # a(t) = dv/dt

# Imprimimos las funciones encontradas
print("Función posición s(t):")
print(poly_st)
print("\nFunción velocidad v(t):")
print(poly_vt)
print("\nFunción aceleración a(t):")
print(poly_at)

# Para graficar usamos un rango continuo de tiempo
t_plot = np.linspace(min(tiempos), max(tiempos), 200)
s_plot = poly_st(t_plot)
v_plot = poly_vt(t_plot)
a_plot = poly_at(t_plot)

# Graficamos
plt.figure(figsize=(12, 8))

# Posición
plt.subplot(3,1,1)
plt.plot(t_plot, s_plot, label='Posición s(t)', color='blue')
plt.scatter(tiempos, posiciones, color='red', label='Datos reales')
plt.ylabel("Posición (m)")
plt.title("Posición vs Tiempo")
plt.legend()
plt.grid(True)

# Velocidad
plt.subplot(3,1,2)
plt.plot(t_plot, v_plot, label='Velocidad v(t)', color='green')
plt.ylabel("Velocidad (m/s)")
plt.title("Velocidad vs Tiempo")
plt.legend()
plt.grid(True)

# Aceleración
plt.subplot(3,1,3)
plt.plot(t_plot, a_plot, label='Aceleración a(t)', color='orange')
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s²)")
plt.title("Aceleración vs Tiempo")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
