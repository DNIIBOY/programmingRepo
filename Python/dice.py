from __future__ import annotations
import time
import json
import threading


class Dice:
    def __init__(self, values: set, name=""):
        self.name = name
        self.values = values

    def __repr__(self):
        return f"Dice {self.name}: {self.values}"

    def __eq__(self, other: Dice):
        counts = self._get_win_count(other)
        return counts["own_wins"] == counts["other_wins"]

    def __gt__(self, other: Dice):
        counts = self._get_win_count(other)
        return counts["own_wins"] > counts["other_wins"]

    def __lt__(self, other: Dice):
        counts = self._get_win_count(other)
        return counts["own_wins"] < counts["other_wins"]

    def __ge__(self, other: Dice):
        counts = self._get_win_count(other)
        return counts["own_wins"] >= counts["other_wins"]

    def __le__(self, other: Dice):
        counts = self._get_win_count(other)
        return counts["own_wins"] <= counts["other_wins"]

    def _get_win_count(self, other: Dice) -> dict:
        own_wins = 0
        other_wins = 0
        draws = 0
        for own_value in self.values:
            for other_value in other.values:
                if own_value > other_value:
                    own_wins += 1
                    continue
                if own_value < other_value:
                    other_wins += 1
                    continue
                draws += 1

        return {
            "own_wins": own_wins,
            "other_wins": other_wins,
            "draws": draws
        }

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values: set):
        if len(values) != 6:
            raise ValueError("Dice must have 6 values")

        if not all(isinstance(value, int) for value in values):
            raise ValueError("Dice values must be integers")

        self._values = values


def rotate(rotate_list: list, n: int) -> list:
    return rotate_list[n:] + rotate_list[:n]


def group_combination_count(n, number_of_groups, group_size) -> int:
    result = 1
    for i in range(n, number_of_groups, -1):
        result *= i

    result = int(result)
    divider = 1
    for i in range(2, group_size + 1):
        divider *= i

    result /= divider**number_of_groups
    return int(result)


def combination_groups(num_range, number_of_groups, group_size, offset=0, stop: int = None):
    if stop is None:
        stop = group_combination_count(len(num_range), number_of_groups, group_size)

    num_range = list(num_range)

    for i in range(offset, stop, group_size):
        yield num_range.copy()

        idx1 = (number_of_groups - 1) * group_size - 1
        idx2 = len(num_range) - 1
        last1 = (number_of_groups - 2) * group_size + 1

        while (idx2 > idx1 and num_range[idx2] > num_range[idx1]):
            idx2 -= 1

        if (idx2 + 1) < len(num_range):
            if num_range[idx2 + 1] > num_range[idx1]:
                num_range[idx1], num_range[idx2 + 1] = num_range[idx2 + 1], num_range[idx1]
        else:
            while idx1 > 0:
                tip_point = num_range[idx2]
                while (idx1 > last1 and tip_point < num_range[idx1]):
                    idx1 -= 1
                if tip_point > num_range[idx1]:
                    idx3 = idx1 + 1
                    num_range[idx3:] = sorted(num_range[idx3:])
                    xtr = last1 + group_size - idx3
                    while num_range[idx3] < num_range[idx1]:
                        idx3 += 1

                    num_range[idx3], num_range[idx1] = num_range[idx1], num_range[idx3]
                    num_range[(idx1 + 1):(idx3 + xtr)] = rotate(num_range[(idx1 + 1):(idx3 + xtr)], idx3 - idx1)

                    break
                else:
                    idx1 -= 2
                    idx2 -= group_size
                    last1 -= group_size


def dice_are_success(dice: list[Dice]):
    for i, die in enumerate(dice):
        if i == len(dice) - 1:
            return die > dice[0]
        if not die > dice[i + 1]:
            return False
    return False


def find_success_dice(num_range, number_of_groups, offset=0, stop: int = None):
    group_size = int(len(num_range) / number_of_groups)
    for a in combination_groups(num_range, number_of_groups, group_size, offset, stop):
        dice = []
        name_index = 0
        for i in range(0, len(a), group_size):
            dice.append(Dice(a[i:i + group_size], name=chr(65 + name_index)))
            name_index += 1

        if dice_are_success(dice):
            SUCCESS_DICE.append(dice)


THREAD_COUNT = 1
DICE_COUNT = 3
DICE_SIDES = 6
TOTAL_RANGE = range(1, DICE_COUNT * DICE_SIDES + 1)
SUCCESS_DICE: list[list[Dice]] = []


def main():
    combination_count = group_combination_count(len(TOTAL_RANGE), DICE_COUNT, DICE_SIDES)
    print(f"Inspecting {combination_count} combinations")

    checks_per_thread = int(combination_count / THREAD_COUNT)
    threads = []
    for i in range(THREAD_COUNT):
        offset = i * checks_per_thread
        stop = offset + checks_per_thread
        print(offset, stop)
        if i == THREAD_COUNT - 1:
            stop = None

        t = threading.Thread(target=find_success_dice, args=(TOTAL_RANGE, DICE_COUNT, offset, stop))
        t.start()
        threads.append(t)

    start = time.time()
    while any(t.is_alive() for t in threads):
        time.sleep(1)
        print(f"Found {len(SUCCESS_DICE)} success dice in {time.time() - start} seconds")

    print(f"Found {len(SUCCESS_DICE)} success dice in {time.time() - start} seconds")

    formatted_dice = []
    for dice in SUCCESS_DICE:
        formatted_dice.append([list(die.values) for die in dice])
    with open("success_dice.json", "w") as f:
        json.dump(formatted_dice, f, indent=4)


if __name__ == "__main__":
    main()
