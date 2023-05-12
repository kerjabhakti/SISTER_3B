import concurrent.futures
import time

food_menu = {
    'Burger': 10,
    'Pizza': 15,
    'Fried Chicken': 12,
    'Salad': 8,
    'Pasta': 13
}


def prepare_food(food_name):
    print(f'Preparing {food_name}...')
    time.sleep(food_menu[food_name])
    print(f'{food_name} is ready!')


def order_food(food_name):
    print(f'Ordering {food_name}...')
    prepare_food(food_name)
    print(f'{food_name} is served!')


if __name__ == '__main__':
    order_list = ['Burger', 'Pizza', 'Fried Chicken', 'Salad', 'Pasta']

    # Sequential Execution
    start_time = time.perf_counter()
    for food in order_list:
        order_food(food)
    print('Sequential Execution in %s seconds' %
          (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(order_food, order_list)
    print('Thread Pool Execution in %s seconds' %
          (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(order_food, order_list)
    print('Process Pool Execution in %s seconds' %
          (time.perf_counter() - start_time))
