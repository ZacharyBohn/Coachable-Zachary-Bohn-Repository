class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        bestETA = -1
        cars = []
        for i in range(len(position)):
            pos = position[i]
            arrival = (target - pos) / speed[i]
            cars.append([pos, arrival])
        # sort on position
        cars.sort(key=lambda x: x[0])
        while cars:
            car = cars.pop()
            # if car arrives slower than the car
            # that started before it
            if car[1] > bestETA:
                bestETA = car[1]
                fleets += 1
        return fleets