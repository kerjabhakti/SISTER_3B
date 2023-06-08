import multiprocessing

class GameProcess(multiprocessing.Process):

    def __init__(self, player_id):
        super(GameProcess, self).__init__()
        self.player_id = player_id

    def run(self):
        print('Player %d telah memasuki game' % self.player_id)
        return
       
if __name__ == '__main__':
    for i in range(10):
        process = GameProcess(i)
        process.start()
        process.join()