import pandas as pd
import sys

def get_all_characters():
    player_chars = {"Dalai": 13, "Tower": 10, "Eagle": 14, "Vatras": 8}
    npcs = {"zmob1": 13, "zmob2": 13, "zmob3": 13}

    combined_chars = {**player_chars, **npcs}
    combined_chars = pd.Series(combined_chars)
    combined_chars = combined_chars.reset_index()
    combined_chars.rename(columns={"index": "name", 0: "initiative"}, inplace=True)
    combined_chars.sort_values(by="initiative", inplace=True, ascending=False)
    combined_chars.reset_index(drop=True, inplace=True)
    combined_chars["name"] = combined_chars["name"].str.lower()
    return combined_chars

def get_next_char_name(combined_chars, current):
    index_current = combined_chars.loc[combined_chars["name"]==current].index.values[0]

    if index_current + 1 >= len(combined_chars):
        index_next = 0
    else:
        index_next = index_current + 1

    next_char = combined_chars.iloc[index_next, 0]
    return next_char

def display_turn_of_next_char():
    combined_chars = get_all_characters()
    names = list(combined_chars["name"])

    while True:
        current = input("\nType in current char or NPC name. Available are {}. \nType 'exit' if you want to end: ".format(names)).lower()

        if current == "exit":
            sys.exit("Exiting")
        elif current not in names:
            print("\n Your selection ***\t{}\t*** is not available. Please select a name that is available for selection.".format(current))
            continue

        character_list = "\nList of all characters: \n{}\n".format(combined_chars)
        print(character_list)

        next_char = get_next_char_name(combined_chars, current)
        result = "The character ***\t{}\t*** has the next turn".format(next_char.upper())
        print(result)


def main():
    display_turn_of_next_char()


if __name__ == "__main__":
    main()