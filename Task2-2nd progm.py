def print_number_pyramid(rows):
	for i in range(1, rows + 1):
		# Print spaces
		for j in range(rows - i):
			print(" ", end="")
		# Print numbers
		for j in range(2 * i - 1):
			print(j + 1, end="")
		# Move to the next line after each row
		print()

# Example usage
num_rows = 10
print_number_pyramid(num_rows)
