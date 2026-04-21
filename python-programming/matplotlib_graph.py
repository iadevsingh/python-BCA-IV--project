import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# ------------------ LINE GRAPH ------------------
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ------------------ BAR GRAPH ------------------
plt.figure()
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()