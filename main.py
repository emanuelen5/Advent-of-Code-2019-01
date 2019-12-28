#!/usr/bin/env python3

def check(masses):
    try:
        return sum([check(m) for m in masses])
    except TypeError:
        return int(masses/3)-2

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle_input_file")
    ns = parser.parse_args()

    with open(ns.puzzle_input_file) as f:
        masses = [int(m) for m in f.readlines()]

    fuel = check(masses)
    print(f"Fuel: {fuel}")

if __name__=="__main__":
    main()
