class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 1
        sort_cars = []
        for i in range(len(position)):
            sort_cars.append((position[i],speed[i]))
        sort_cars.sort(reverse=True)
        stack = []
        fleet_ahead = (target - sort_cars[0][0]) / sort_cars[0][1]

        for i in range(1,len(sort_cars)):
            time = (target - sort_cars[i][0]) / sort_cars[i][1]
            if time > fleet_ahead:
                fleet += 1
                fleet_ahead = time

        return fleet
            