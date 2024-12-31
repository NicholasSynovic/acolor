from colorist.helper.generate import ansi_standard_color_sequence

COLORS: dict[str, int] = {
    "BLACK": 0,
    "RED": 1,
    "GREEN": 2,
    "YELLOW": 3,
    "BLUE": 4,
    "MAGENTA": 5,
    "CYAN": 6,
    "WHITE": 7,
}


def main(color: str) -> int:
    try:
        colorValue: int = COLORS[color.upper()]
    except KeyError:
        print(f"{color} is not a valid color: {COLORS.keys()}")
        return 1

    print(
        repr(
            ansi_standard_color_sequence(
                selector=3,
                value=colorValue,
            )
        )
    )
    return 0


if __name__ == "__main__":
    main("red")
