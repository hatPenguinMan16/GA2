import matplotlib.pyplot as plt
from main import in_nodes

plt.plot(in_nodes)

plt.title('Infiltration rate')
plt.xlabel('repeated')
plt.ylabel('dy/dx')
plt.grid(True)
plt.show()