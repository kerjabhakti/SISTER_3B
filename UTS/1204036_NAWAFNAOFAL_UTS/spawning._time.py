import multiprocessing
import time

def play_game(player_name, game_name):
    print(f"{player_name} mulai bermain {game_name} pada waktu {time.ctime()}")
    time.sleep(3)
    print(f"{player_name} selesai bermain {game_name} pada waktu {time.ctime()}")

if __name__ == '__main__':
    games = {
        'God Of War': ['Dadang', 'Eni'],
        'The Last Of Us': ['Herman', 'Wili', 'Ilham'],
        'Resident Evil 4': ['Jaka', 'Kurniawan']
    }
    
    processes = []
    for game_name, players in games.items():
        for player_name in players:
            p = multiprocessing.Process(target=play_game, args=(player_name, game_name))
            p.start()
            processes.append(p)
    
    for p in processes:
        p.join()
    
    print("Semua pemain telah selesai bermain game pada waktu", time.ctime())
