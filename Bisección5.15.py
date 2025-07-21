
import math
import matplotlib.pyplot as plt

# Datos
g = 9.81  # Gravedad (m/s²)
L = 4.0   # Longitud del tubo (m)
t = 2.5   # Tiempo (s)
v_deseada = 5.0  # Velocidad deseada (m/s)

# calcular la velocidad
def velocidad(H):
    return math.sqrt(2*g*H) * math.tanh(math.sqrt(2*g*H)/(2*L)*t)

# cálculo de raíces (v - v_deseada = 0)
def f(H):
    return velocidad(H) - v_deseada

print("\n***  Solución gráfica ***")
H_valores = [x/100 for x in range(0, 201)]  
v_valores = [velocidad(H) for H in H_valores]

plt.plot(H_valores, v_valores, 'b-')
plt.axhline(y=v_deseada, color='r', linestyle='--')
plt.title('Velocidad vs Carga hidrostática')
plt.xlabel('Carga H (m)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.show()

# Método de bisección
print("\n***  Método de bisección ***")
xl = 0.0
xu = 2.0
error_deseado = 1.0  # 1%
iteracion = 0

print("Iter |   H   | Error (%) | f(H)")
print("-------------------------------")

while True:
    xr = (xl + xu) / 2
    error = 100 if iteracion == 0 else abs((xr - xr_anterior)/xr)*100
    
    print(f"{iteracion+1:3} | {xr:.5f} | {error:.4f}  | {f(xr):.5f}")
    
    if f(xl)*f(xr) < 0:
        xu = xr
    else:
        xl = xr
    
    xr_anterior = xr
    iteracion += 1
    
    if error < error_deseado or iteracion >= 20:
        break

print(f"\nResultado final: H = {xr:.5f} m")


#Método falsa posición 

print("\n*** Método de falsa posición ***")
xl = 0.0
xu = 2.0
iteracion = 0

print("Iter |   H   | Error (%) | f(H)")
print("-------------------------------")

while True:
    fl = f(xl)
    fu = f(xu)
    xr = xu - fu*(xu - xl)/(fu - fl)
    error = 100 if iteracion == 0 else abs((xr - xr_anterior)/xr)*100
    
    print(f"{iteracion+1:3} | {xr:.5f} | {error:.4f}  | {f(xr):.5f}")
    
    if f(xl)*f(xr) < 0:
        xu = xr
    else:
        xl = xr
    
    xr_anterior = xr
    iteracion += 1
    
    if error < error_deseado or iteracion >= 20:
        break

print(f"\nResultado final: H = {xr:.5f} m")

# Comprobación final
print("\n*** Comprobación ***")
print(f"Con H = {xr:.5f} m -> v = {velocidad(xr):.5f} m/s")