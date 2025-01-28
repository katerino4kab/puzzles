from gameplay.puzzle import play_puzzle_game
from gameplay.rebus import play_rebus_game
from gameplay.matching import play_matching_game

def start_game(selected_game):
    if selected_game == "puzzle":
        play_puzzle_game(screen)
    elif selected_game == "rebus":
        play_rebus_game(screen)
    elif selected_game == "matching":
        play_matching_game(screen)