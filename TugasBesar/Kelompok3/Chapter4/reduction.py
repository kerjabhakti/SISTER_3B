from mpi4py import MPI

def reduce_sales_data(sales_data):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Menghitung total penjualan di setiap node
    total_sales = sum(sales_data)

    # Mengurangi total penjualan dari semua node
    global_total_sales = comm.reduce(total_sales, op=MPI.SUM, root=0)

    if rank == 0:
        print("Total penjualan dari semua node:", global_total_sales)

if __name__ == '__main__':
    # Data penjualan dari masing-masing node
    sales_data = [100, 200, 150, 300]

    # Memanggil fungsi pengurangan data penjualan
    reduce_sales_data(sales_data)

    # Hasilnya :
    # Total penjualan dari semua node: 750