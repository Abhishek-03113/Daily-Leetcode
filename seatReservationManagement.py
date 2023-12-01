from sortedcontainers import SortedSet


class SeatManager:

    """APPROACH 1 Min Heap"""

    # def __init__(self, n: int):
    #     self.n = n
    #     self.available_seats = [i for i in range(1,n+1)]

    # def reserve(self) -> int:
    #     seat_number = heapq.heappop(self.available_seats)
    #     return seat_number

    # def unreserve(self, seatNumber: int) -> None:
    #     heapq.heappush(self.available_seats,seatNumber)

    """Approach 2 : Min Heap without PreInitializations"""

    # def __init__(self, n: int):
    #     self.n = n
    #     self.marker = 1

    #     self.availableSeats = []

    # def reserve(self) -> int:
    #     if self.availableSeats:
    #         seatNumber = heapq.heappop(self.availableSeats)
    #         return seatNumber
    #     seatNumber = self.marker
    #     self.marker += 1
    #     return seatNumber

    # def unreserve(self, seatNumber: int) -> None:
    #     heapq.heappush(self.availableSeats,seatNumber)

    """ Approach 3 : Ordered Set """

    def __init__(self, n: int):
        self.n = n
        self.marker = 1
        self.availableSeats = SortedSet()

    def reserve(self) -> int:
        if self.availableSeats:
            seatNumber = self.availableSeats.pop(0)

            return seatNumber
        seatNumber = self.marker
        self.marker += 1
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        self.availableSeats.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
