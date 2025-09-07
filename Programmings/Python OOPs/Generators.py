def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Create a generator object
gen = infinite_sequence()

# Print the first 10 values
for _ in range(10):
    print(next(gen))
