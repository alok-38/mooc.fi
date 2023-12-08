def get_valid_age():
    while True:
        try:
            age = int(input("Enter the person's age (between 1 and 120): "))

            # Chained conditions to check if age is within the valid range
            if 1 <= age <= 120:
                return age
            else:
                raise ValueError("Age must be between 1 and 120.")

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please enter a valid integer age.")

if __name__ == "__main__":
    try:
        person_age = get_valid_age()
        print(f"The entered age is: {person_age}")
    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

