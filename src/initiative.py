# License: APACHE LICENSE, VERSION 2.0

from typing import Dict

import pandas as pd
import streamlit as st


class Characters:
    def __init__(self):
        self.player_chars = {"Dalai": 13, "Tower": 10, "Eagle": 14, "Vatras": 8}
        self.npcs = {"zmob1": 13, "zmob2": 13, "zmob3": 13}
        self.combined_chars = {**self.player_chars, **self.npcs}
        self.combined_characters_tidy: Dict[str, str] = None

    def get_combined_chars(self):
        combined_chars = pd.Series(self.combined_chars)
        combined_chars = combined_chars.reset_index()
        combined_chars.rename(columns={"index": "name", 0: "initiative"}, inplace=True)
        combined_chars.sort_values(by="initiative", inplace=True, ascending=False)
        combined_chars.reset_index(drop=True, inplace=True)
        combined_chars["name"] = combined_chars["name"].str.lower()
        self.combined_characters_tidy = combined_chars
        return combined_chars

    def get_name_initiative_tuples(self):
        all_names_inits = [f"{k.lower()}: {v}" for k, v in self.combined_chars.items()]
        player_names_inits = [f"{k.lower()}: {v}" for k, v in self.player_chars.items()]
        return all_names_inits, player_names_inits


def get_next_char_name(combined_chars, current):
    index_current = combined_chars.loc[combined_chars["name"] == current].index.values[0]

    if index_current + 1 >= len(combined_chars):
        index_next = 0
    else:
        index_next = index_current + 1

    next_char = combined_chars.iloc[index_next, 0]
    return next_char


def display_turn_of_next_char():
    all_chars = Characters()
    combined_chars = all_chars.get_combined_chars()
    st.header("Initiative Tracker")
    st.write("List of all characters:")

    st.write(combined_chars)

    all_available, players = all_chars.get_name_initiative_tuples()
    chars_to_consider = st.multiselect(
        'Selected characters we want to track initiative for:',
        all_available,
        players,
    )
    names_of_chars = [x.split(":")[0].lower() for x in chars_to_consider]
    names_and_initiatives = combined_chars[combined_chars["name"].isin(names_of_chars)]

    selected = st.selectbox("Select character for current turn".upper(), names_and_initiatives)

    # TODO FIX INITIATIVE falsely showing up for non-present npcs (deselected in multiselect)
    next_char = get_next_char_name(combined_chars, selected)
    result = f"Next character's turn is **{next_char.upper()}**"
    st.info(result)


def main():
    display_turn_of_next_char()


if __name__ == "__main__":
    main()
