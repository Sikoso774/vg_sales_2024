import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg') 
x = np.linspace(-25, 25, 100) 

y = x**2

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='y = x²', color='#295921')

# Astuce visuelle : marquer le sommet
sommet_x = 0 # Formule -b/2a
sommet_y = sommet_x**2

plt.plot(sommet_x, sommet_y, 'bo', label='Sommet') # Point bleu

plt.title("Visualisation de la parabole entière")
plt.grid(True)
plt.legend()
plt.show()