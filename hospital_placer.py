import random
from math import sqrt


class Hospital:
    def __init__(self, width, height, cell_size, hospital_number, houses):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.hospital_number = hospital_number
        self.houses = houses

    def random_allotment(self):
        # Returning random co-ordinates for hospitals
        coordinate = (random.randint(0, self.width / self.cell_size),
                      random.randint(0, self.height / self.cell_size))
        return coordinate

    # Function to find neighbors of a particular cell
    def find_neighbors(self, cell, hospitals):
        neighbors = []
        (i, j) = cell
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if (i, j) != (k, l) and (k, l) not in hospitals \
                        and (k, l) not in self.houses and 0 <= k < self.width \
                        / self.cell_size and 0 <= l < self.height / \
                        self.cell_size:
                    neighbors.append((k, l))
        return neighbors

    def optimization(self, maximum):
        # Doing the optimization for maximum times with different initial
        # states
        best_formation = []
        best_score = 1000
        for i in range(maximum):
            hospitals = []
            # Adding hospital coordinates into the list
            while True:
                coordinate = self.random_allotment()
                if coordinate not in hospitals:
                    hospitals.append(coordinate)
                if len(hospitals) == self.hospital_number:
                    break

            # Finding the best formation for each initial state
            formation = self.hill_climb(hospitals)
            score = self.get_cost(formation)
            if score < best_score:
                best_formation = formation
                best_score = score
        return best_formation

    def hill_climb(self, hospitals):

        for i in range(len(hospitals)):
            # Taking each hospital
            best_score = 10000

            while True:
                # Finding the best move
                hospital = hospitals[i]
                best_move = hospital

                for move in self.find_neighbors(hospital, hospitals):
                    hospitals_copy = list(hospitals)
                    hospitals_copy[i] = move
                    cost = self.get_cost(hospitals_copy)
                    if cost < best_score:
                        best_score = cost
                        best_move = move

                # Checking if there is no efficient move
                if best_move == hospital:
                    break
                else:
                    hospitals[i] = best_move

        return hospitals

    def get_cost(self, hospitals):
        cost = 0
        for (h1, h2) in self.houses:
            minimum_displacement = 10000
            for (ho1, ho2) in hospitals:
                displacement = sqrt(pow(h1 - ho1, 2) + pow(h2 - ho2, 2))
                if displacement < minimum_displacement:
                    minimum_displacement = displacement
            cost += minimum_displacement
        return cost
