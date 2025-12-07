import pulp

lp = pulp.LpProblem("ejercicio-09", pulp.LpMaximize)

# Variables:
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')

# Función objetivo:
lp += 0.3*x + 0.8*y, "Z"

# Restricciones
lp += 0.1*x <= 200
lp += 0.113398*y <= 800
lp += 2*x + 3*y <= 12000

# Resolvemos:
lp.solve()

# Imprimimos el status del problema:
print(pulp.LpStatus[lp.status])

# Imprimimos las variables en su valor óptimo:
for variable in lp.variables():
    print(f"{variable.name:s} = {variable.varValue:.2f}")

# Imprimimos el funcional óptimo:
print(pulp.value(lp.objective))