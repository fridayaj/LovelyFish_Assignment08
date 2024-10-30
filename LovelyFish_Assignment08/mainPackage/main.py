class Hole:
    def __init__(self, par, distance):
        self.par = par                # Par for the hole
        self.total_distance = distance # Total distance of the hole
        self.remaining_distance = distance # Distance remaining

    def hit_ball(self, distance):
        """Reduce the remaining distance by the distance hit."""
        self.remaining_distance -= distance
        if self.remaining_distance < 0:
            self.remaining_distance = 0

    def __str__(self):
        return f"Hole(par={self.par}, remaining_distance={self.remaining_distance})"

    def __repr__(self):
        return f"Hole(par={self.par})"

