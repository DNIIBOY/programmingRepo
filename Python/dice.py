from __future__ import annotations
import time
import json


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


def group_combination_count(number_count, group_count, group_size) -> int:
    result = 1
    for i in range(number_count, group_count, -1):
        result *= i

    result = int(result)
    divider = 1
    for i in range(2, group_size + 1):
        divider *= i

    result /= divider**group_count
    return int(result)


def group_combinations(total_range, group_count, group_size):
    total_range = list(total_range)

    for i in range(group_combination_count(len(total_range), group_count, group_size)):
        yield total_range.copy()

        idx1 = (group_count - 1) * group_size - 1
        idx2 = len(total_range) - 1
        last1 = (group_count - 2) * group_size + 1

        while (idx2 > idx1 and total_range[idx2] > total_range[idx1]):
            idx2 -= 1

        if (idx2 + 1) < len(total_range):
            if total_range[idx2 + 1] > total_range[idx1]:
                total_range[idx1], total_range[idx2 + 1] = total_range[idx2 + 1], total_range[idx1]
        else:
            while idx1 > 0:
                tip_point = total_range[idx2]
                while (idx1 > last1 and tip_point < total_range[idx1]):
                    idx1 -= 1
                if tip_point > total_range[idx1]:
                    idx3 = idx1 + 1
                    total_range[idx3:] = sorted(total_range[idx3:])
                    xtr = last1 + group_size - idx3
                    while total_range[idx3] < total_range[idx1]:
                        idx3 += 1

                    total_range[idx3], total_range[idx1] = total_range[idx1], total_range[idx3]
                    total_range[(idx1 + 1):(idx3 + xtr)] = rotate(total_range[(idx1 + 1):(idx3 + xtr)], idx3 - idx1)

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


def find_success_dice(num_range, number_of_groups):
    success_dice: list[list[dice]] = []
    group_size = int(len(num_range) / number_of_groups)
    counter = 0
    current_percent = 0
    total_count = group_combination_count(len(num_range), number_of_groups, group_size)
    for a in group_combinations(num_range, number_of_groups, group_size):
        dice = []
        name_index = 0
        for i in range(0, len(a), group_size):
            dice.append(Dice(a[i:i + group_size], name=chr(65 + name_index)))
            name_index += 1

        if dice_are_success(dice):
            success_dice.append(dice)

        if counter/total_count * 100 > current_percent:
            current_percent += 1
            print(f"{current_percent}%")
            save_dice(success_dice)
            success_dice = []

        counter += 1

    return success_dice


def save_dice(success_dice):
    with open("success_dice.json", "r") as f:
        formatted_dice = json.load(f)
    for dice in success_dice:
        formatted_dice.append([list(die.values) for die in dice])
    with open("success_dice.json", "w") as f:
        json.dump(formatted_dice, f, indent=4)


def main(num_range, number_of_groups):
    with open("success_dice.json", "w") as f:
        json.dump([], f, indent=4)
    start = time.time()
    find_success_dice(num_range, number_of_groups)
    with open("success_dice.json", "r") as f:
        success_dice = json.load(f)
    print(f"Found {len(success_dice)} success dice in {time.time() - start} seconds")


if __name__ == "__main__":
    main(range(1, 19), 3)
