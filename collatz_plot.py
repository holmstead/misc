# collatz conjecture plotted

import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Test the function with a starting number
starting_number = int(input("Please enter an integer: "))
sequence = collatz(starting_number)

# Plotting the sequence
plt.plot(sequence, marker='o')
plt.title('Collatz Conjecture Sequence')
plt.xlabel('Step')
plt.ylabel('Value')
plt.grid(True)
plt.show()
