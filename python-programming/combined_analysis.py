import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ CREATE DATA (NumPy) ------------------
# Generate random marks for 10 students
marks = np.random.randint(50, 100, size=10)

# ------------------ CREATE DATAFRAME (Pandas) ------------------
df = pd.DataFrame({
    "Student": [f"S{i}" for i in range(1, 11)],
    "Marks": marks
})

print("Dataset:\n", df)

# ------------------ BASIC ANALYSIS ------------------
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# ------------------ VISUALIZATION (Matplotlib) ------------------
plt.figure()
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Student Marks (Line Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks (Bar Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()