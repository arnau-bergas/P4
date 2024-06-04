import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo de texto
data = np.loadtxt('/home/victhor/PAV/P4/plots/lp.txt')
data2 = np.loadtxt('/home/victhor/PAV/P4/plots/lpcc.txt')
data3 = np.loadtxt('/home/victhor/PAV/P4/plots/mfcc.txt')


# Separar los datos en dos arrays
x = data[:, 0]
y = data[:, 1]

x2 = data2[:, 0]
y2 = data2[:, 1]

x3 = data3[:, 0]
y3 = data3[:, 1]

# Crear la gráfica
plt.figure(figsize=(10, 5))

# Plot 1: LP
plt.subplot(1, 3, 1)
plt.scatter(x, y, label='LP', color='red', linestyle='dashed', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('LP Plot')
plt.legend()

# Plot 2: LPCC
plt.subplot(1, 3, 2)
plt.scatter(x2, y2, label='LPCC', color='green', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('LPCC Plot')
plt.legend()

# Plot 3: MFCC
plt.subplot(1, 3, 3)
plt.scatter(x3, y3, label='MFCC', color='blue', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('MFCC Plot')
plt.legend()

# Ajustar los subplots
plt.tight_layout()

# Mostrar la gráfica
plt.show()