"""Console script for pipe_line_with_cookie_cutter."""
import argparse
import sys


def main():
    """Console script for pipe_line_with_cookie_cutter."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "pipe_line_with_cookie_cutter.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
