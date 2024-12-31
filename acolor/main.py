import click
from colorist.constants.ansi import RESET_ALL
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


@click.command()
@click.option(
    "-c",
    "--color",
    "color",
    type=str,
    nargs=1,
    default=None,
    required=False,
    help="Color name to generate ANSI code",
)
@click.option(
    "-r",
    "--reset",
    "reset",
    is_flag=True,
    default=False,
    required=False,
    help="Print ANSI reset code",
)
def main(reset: bool, color: str | None = None) -> int:
    if reset:
        print(repr(RESET_ALL))
        return 0

    if color is None:
        return 0

    try:
        colorValue: int = COLORS[color.upper()]
    except KeyError:
        print(f"{color} is not a valid color: {COLORS.keys()}")
        return 1

    print(
        repr(
            ansi_standard_color_sequence(
                selector=3,  # Selects the foreground
                value=colorValue,
            )
        )
    )
    return 0


if __name__ == "__main__":
    main()
