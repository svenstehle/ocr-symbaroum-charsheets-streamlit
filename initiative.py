import sys

import pandas as pd
import streamlit as st

class Characters:
    def __init__(self):
        self.player_chars = {"Dalai": 13, "Tower": 10, "Eagle": 14, "Vatras": 8}
        self.npcs = {"zmob1": 13, "zmob2": 13, "zmob3": 13}

    def get_combined_chars(self):
        combined_chars = {**self.player_chars, **self.npcs}
        combined_chars = pd.Series(combined_chars)
        combined_chars = combined_chars.reset_index()
        combined_chars.rename(columns={"index": "name", 0: "initiative"}, inplace=True)
        combined_chars.sort_values(by="initiative", inplace=True, ascending=False)
        combined_chars.reset_index(drop=True, inplace=True)
        combined_chars["name"] = combined_chars["name"].str.lower()
        self.combined_characters = combined_chars
        return combined_chars

    def get_player_char_names(self):
        return pd.Series(self.player_chars.keys()).str.lower()

    def get_name_initiative_tuples(self):
        # all_names_inits = (self.combined_characters["name"] + ": " + str(self.combined_characters["initiative"])).values
        player_names_inits = [f"{k.lower()}: {v}" for k, v in self.player_chars.items()]
        # st.write(all_names_inits)
        # return all_names_inits, player_names_inits
        return player_names_inits, player_names_inits




def get_next_char_name(combined_chars, current):
    index_current = combined_chars.loc[combined_chars["name"]==current].index.values[0]

    if index_current + 1 >= len(combined_chars):
        index_next = 0
    else:
        index_next = index_current + 1

    next_char = combined_chars.iloc[index_next, 0]
    return next_char

def display_turn_of_next_char():
    all_chars = Characters()
    combined_chars = all_chars.get_combined_chars()
    names = list(combined_chars["name"])
    st.write("Try out streamlit for our initiative tracker")
    st.write("List of all characters:")

    st.write(combined_chars)
    st.write(f"player char names: {all_chars.get_player_char_names()}")
    st.write("test")

    all_available, players = all_chars.get_name_initiative_tuples()
    chars_to_consider = st.multiselect(
        'Select which characters are alive and in combat so we can consider their initiative',
        all_available,
        players,
    )
    names_of_chars = [x.split(":")[0].lower() for x in chars_to_consider]
    st.write('You want to track initiative for:')
    names_and_initiatives = combined_chars[combined_chars["name"].isin(names_of_chars)]
    st.write(names_and_initiatives)

    selected = st.sidebar.selectbox("Select character for current turn".upper(), names_and_initiatives)
    st.write(f"Current selected character is '_{selected}_'")

    next_char = get_next_char_name(combined_chars, selected)
    result = "The character \t**{}**\t has the next turn".format(next_char.upper())
    st.write(result)

def main():
    display_turn_of_next_char()


if __name__ == "__main__":
    main()
