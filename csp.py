# Define the Map Coloring Constraint Satisfaction Problem
class CSP:
    def __init__(self, variables, domains):
        self.variables = variables  # List of variables (e.g., regions on the map)
        self.domains = domains      # Dictionary of domains (possible colors) for each variable
        self.constraints = {}       # Dictionary of constraints for each variable

    def add_constraint(self, variable, constraint):
        if variable not in self.constraints:
            self.constraints[variable] = []
        self.constraints[variable].append(constraint)

    def is_consistent(self, variable, assignment):
        # Check all constraints for a variable with the current assignment
        for constraint in self.constraints.get(variable, []):
            if not constraint(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        # If all variables are assigned, return the assignment
        if len(assignment) == len(self.variables):
            return assignment

        # Select an unassigned variable
        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]

        # Try each possible value in the domain for the selected variable
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value

            # Check if the current assignment is consistent with constraints
            if self.is_consistent(first, local_assignment):
                # Recur with the new assignment
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result

        return None


# Define constraints for adjacent regions
def different_values_constraint(assignment):
    for (var1, var2) in neighbors:
        if var1 in assignment and var2 in assignment and assignment[var1] == assignment[var2]:
            return False
    return True


# Define the variables, domains, and constraints
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]  # States in Australia
domains = {v: ["Red", "Green", "Blue"] for v in variables}

# Neighbors represented as tuples (adjacent states)
neighbors = [("WA", "NT"), ("WA", "SA"), ("NT", "Q"), ("NT", "SA"),
             ("SA", "Q"), ("SA", "NSW"), ("SA", "V"), ("Q", "NSW"), ("NSW", "V")]

# Initialize the CSP
csp = CSP(variables, domains)

# Add constraints that adjacent regions must have different colors
for variable in variables:
    csp.add_constraint(variable, different_values_constraint)

# Solve the CSP
solution = csp.backtracking_search()
print("Solution:", solution)
