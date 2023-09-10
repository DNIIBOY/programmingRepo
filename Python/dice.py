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


def rotate(l, n):
    return l[n:] + l[:n]


def numGroupCombs(n, nGrps, group_size):
    result = 1
    for i in range(n, nGrps, -1):
        result *= i

    result = int(result)
    myDiv = 1
    for i in range(2, group_size + 1):
        myDiv *= i

    result /= myDiv**nGrps
    return int(result)


def ComboGroups(v, nGrps, group_size):
    if not isinstance(v, list):
        z = list(v)
    else:
        z = v.copy()

    for i in range(numGroupCombs(len(z), nGrps, group_size)):
        yield z.copy()

        idx1 = (nGrps - 1) * group_size - 1
        idx2 = len(z) - 1
        last1 = (nGrps - 2) * group_size + 1

        while (idx2 > idx1 and z[idx2] > z[idx1]):
            idx2 -= 1

        if (idx2 + 1) < len(z):
            if z[idx2 + 1] > z[idx1]:
                z[idx1], z[idx2 + 1] = z[idx2 + 1], z[idx1]
        else:
            while idx1 > 0:
                tipPnt = z[idx2]
                while (idx1 > last1 and tipPnt < z[idx1]):
                    idx1 -= 1
                if tipPnt > z[idx1]:
                    idx3 = idx1 + 1
                    z[idx3:] = sorted(z[idx3:])
                    xtr = last1 + group_size - idx3
                    while z[idx3] < z[idx1]:
                        idx3 += 1

                    z[idx3], z[idx1] = z[idx1], z[idx3]
                    z[(idx1 + 1):(idx3 + xtr)] = rotate(z[(idx1 + 1):(idx3 + xtr)], idx3 - idx1)

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
    for a in ComboGroups(num_range, number_of_groups, group_size):
        dice = []
        name_index = 0
        for i in range(0, len(a), group_size):
            dice.append(Dice(a[i:i + group_size], name=chr(65 + name_index)))
            name_index += 1

        if dice_are_success(dice):
            success_dice.append(dice)

        if counter % 1000000 == 0:
            print(f"Found: {len(success_dice)}, current: {counter}")
        counter += 1

    return success_dice


def main(num_range, number_of_groups):
    start = time.time()
    success_dice = find_success_dice(num_range, number_of_groups)
    print(f"Found {len(success_dice)} success dice in {time.time() - start} seconds")
    formatted_dice = []
    for dice in success_dice:
        formatted_dice.append([list(die.values) for die in dice])
    with open("success_dice.json", "w") as f:
        json.dump(formatted_dice, f, indent=4)


if __name__ == "__main__":
    main(range(1, 19), 3)
