from dataclasses import dataclass


@dataclass
class Lanternfish:
    internal_timer: int

    def perform_day(self) -> bool:
        """
        Perform any work for the day on the fish
        :return: 'True' if the timer reset, 'False' otherwise.
        """
        return self.tick_timer()

    def tick_timer(self) -> bool:
        """
        Tick the timer on the fish.
        :return: 'True' if the timer reset, 'False' otherwise.
        """
        self.internal_timer -= 1

        if self.internal_timer == -1:
            self.internal_timer = self.get_timer_reset_value()
            return True
        else:
            return False

    @staticmethod
    def get_timer_reset_value() -> int:
        return 6
