#!/usr/bin/env python3
# Created By: Keiden
# Date: 2 / 2 / 2022
# This program takes a number as input and adds it with every lower number.


def main():
    print("Hi! insert a number, and this program will add it with every number"
          " lower then it, ending at zero.")

    highest_num = input(">")
    counter = 0
    final_num = 0
    print()

    try:
        highest_num_int = int(highest_num)
        while counter <= highest_num_int:
            final_num = final_num + counter
            counter = counter + 1

        print("Your final number is", str(final_num) + "!")

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()
