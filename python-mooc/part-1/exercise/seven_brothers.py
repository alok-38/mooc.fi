# Initialize an empty list to store names
names = []

# Continue taking names until the user decides to stop
while True:
    # Get a name from the user
    name = input("Enter a name (or 'stop' to finish): ")

    # Check if the user wants to stop
    if name.lower() == 'stop':
        break

    # Add the name to the list
    names.append(name)

    # Sort the names alphabetically
    sorted_names = sorted(names)

# Print the final sorted names
print("Final Sorted Names:", sorted_names)

