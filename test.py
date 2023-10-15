import numpy as np

# Given material properties
ma = np.array([0.000, 0.000, 0.000])
md = np.array([0.000, 0.500, 0.500])
ms = np.array([0.500, 0.500, 0.500])
me = np.array([0.000, 0.000, 0.000])

# Given light properties
la = np.array([0.000, 0.000, 0.000])
ld = np.array([0.500, 0.500, 0.000])
ls = np.array([0.500, 0.800, 0.500])
ga = np.array([0.000, 0.000, 0.000])
h = 0.25

# Position of the light
light_position = np.array([-5.000, 0.000, 0.000])

# Point P and its normal vector N
point_P = np.array([-5.000, 2.000, 0.000])
N = np.array([0.707, -0.707, 0.000])

# Calculate the vector L (light direction)
L = light_position - point_P
L = L / np.linalg.norm(L)

# Calculate the vector R (reflection)
R = 2 * (np.dot(N, L)) * N - L
R = R / np.linalg.norm(R)

# Calculate the vector V (view direction)
V = -point_P
V = V / np.linalg.norm(V)

# Calculate the diffuse component
diffuse = ld * md * np.dot(L, N)

# Calculate the specular component
specular = ls * ms * (max(0, np.dot(R, V)) ** h)

# Calculate the ambient component
ambient = la * ma + ga * ma

# Calculate the intensity using the lighting equation
i = me + ambient + diffuse + specular

# Print the results rounded to 3 decimal places
print("L =", np.round(L, 3))
print("R =", np.round(R, 3))
print("V =", np.round(V, 3))
print("Intensity (i) =", np.round(i, 3))