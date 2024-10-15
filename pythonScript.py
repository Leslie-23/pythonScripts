import matplotlib.pyplot as plt

# Function to take user inputs
def get_input_values():
    x_values = []
    y_values = []
    
    print("Enter 3 x values:")
    for i in range(3):
        x = float(input(f"Enter x{i+1}: "))
        x_values.append(x)
        
    print("Enter 3 y values:")
    for i in range(3):
        y = float(input(f"Enter y{i+1}: "))
        y_values.append(y)
    
    return x_values, y_values

# Plotting function
def plot_graph(x, y):
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data points')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Graph of User Inputs')
    plt.grid(True)
    plt.legend()
    plt.show()

# Main code
x_vals, y_vals = get_input_values()
plot_graph(x_vals, y_vals)
