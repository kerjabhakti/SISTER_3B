import multiprocessing

def start_game(game_name, player_name):
    print(f"{player_name} mulai bermain {game_name}...")
    print(f"{player_name} selesai bermain {game_name}!")

if __name__ == '__main__':
    game_players = {
        'God Of War': ['Dadang', 'Eni'],
        'The Last Of Us': ['Herman', 'Wili', 'Ilham'],
        'Resident Evil 4': ['Jaka', 'Kurniawan']
    }

    processes = []
    for game_name, players in game_players.items():
        for player in players:
            p = multiprocessing.Process(target=start_game, args=(game_name, player))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()