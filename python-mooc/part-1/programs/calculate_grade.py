def calulate_grade():
    try:
        num_assignments = int(input("Enter the number of assignments: "))
        if num_assignments <= 0:
            raise ValueError("Number of assignments should be greater than 0")

        assignment_weights = []
        total_assignment_weight = 0

        for i in range(num_assignments):
            weight = float(input(f"Enter the weight for assignment {i + 1} (as a decimal): "))
            if weight <= 0 or weight > 1:
                raise ValueError
