def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n.

  Args:
      n: An integer representing the number of terms in the sequence.

  Returns:
      A list containing the first n terms of the Fibonacci sequence.
  """
  if n <= 1:
    return [n]
  else:
    sequence = fibonacci(n-1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Get user input for the number of terms
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)
