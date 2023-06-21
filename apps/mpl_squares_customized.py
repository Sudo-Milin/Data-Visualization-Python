import matplotlib.pyplot as plt

input_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
sqrs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fix, ax = plt.subplots()
ax.plot(input_vals, sqrs, linewidth=3)

# Set chart title and label axis
ax.set_title("Squared Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=12) # axis='both' shows tick marks on both the x- and y-axes and labelsize=14 set the font size of the tick mark labels to 14 
plt.show()