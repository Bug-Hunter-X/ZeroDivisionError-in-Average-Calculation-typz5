def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0  # Or raise an exception, depending on your needs
    return sum(numbers) / len(numbers)