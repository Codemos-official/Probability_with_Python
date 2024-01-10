import pdb 

class CombinationGenerator:
    def __init__(self, elements):
        self.elements = elements
        self.combinations = []

    def generate_combinations(self, r):
        print(f"Generating combinations of {r} elements from {self.elements}")
        pdb.set_trace() 
        self._generate_combinations_recursive([], 0, r)
        return self.combinations 

    def _generate_combinations_recursive(self, current_combination, start_index, r):
        pdb.set_trace() 
        print("value of r is " , r) 
        if r == 0:
            self.combinations.append(list(current_combination))
            print(f"Combination added: {current_combination}")
            return

        for i in range(start_index, len(self.elements) - r + 1):
            print(f"value of i is {i} and r is {r}")
            current_combination.append(self.elements[i])
            print(f"Appending {self.elements[i]} to current_combination: {current_combination}")
            pdb.set_trace() 
            self._generate_combinations_recursive(current_combination, i + 1, r - 1)
            current_combination.pop()
            print(f"Pop last element from current_combination: {current_combination}")


my_elements = ['A', 'B', 'C' ]
r = 2

combinations_generator = CombinationGenerator(my_elements)

combinations_result = combinations_generator.generate_combinations(r)

print(f"\nFinal Combinations of {r} elements from {my_elements}:")
print(combinations_result)
