"""
Gets a positive integer from a user.

Demonstrates main.
"""


def main():
    i = get_revenue()
    print(f"${r}")


def get_revenue():
    while True:
        n = int(input("Revenue: "))
        if n >= 0:
            return n


if __name__ == "__main__":
    main()
