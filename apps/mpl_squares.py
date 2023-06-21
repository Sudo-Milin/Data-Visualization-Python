import matplotlib.pyplot as plt

sqrs = [1,2,9,16,25,36,49,64,81,100]

# subplots() generate one or more plots in the same figure.
fig, ax = plt.subplots() # The variable fig represents the entire figure or collection of plots that are generated. 
                         # The variable ax represents a single plot in the figure.
ax.plot(sqrs)

plt.show()