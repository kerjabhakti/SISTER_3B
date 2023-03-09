#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def hit(data):
    damage = data*data
    return damage

if __name__ == '__main__':
    damages = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(hit, damages)

    pool.close()
    pool.join()

    print('Damage yang diterima secara bertahap : ', pool_outputs)
    total_damage = sum(pool_outputs)
    print(f"Total damage yang diterima oleh monster adalah jumlah kuadrat dari bilangan 0 hingga 99, yaitu {total_damage}.")
