from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    ride_request = None
    if rank == 0:
        ride_request = "Pick up penumpang Ilman di GG Bongkaran"
    elif rank == 1:
        ride_request = "Pick up penumpang Daffa di Cianjur"
    elif rank == 2:
        ride_request = "Pick up penumpang Nawaf di Land of dawn"
    ride_request = comm.gather(ride_request, root=0)

    if rank == 0:
        print("GoRide request gathering sukses!")
        for i in range(1,size):
            ride = ride_request[i]
            print("Received ride request '%s' from process %s" % (ride , i))

    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row
        
    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print("Building a %d x %d GoRide topology:" % (grid_row, grid_column))

    cartesian_communicator = comm.Create_cart((grid_row, grid_column), periods=(True, True), reorder=True)
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    print("Process = %s \nrow = %s \ncolumn = %s \n----> \nneighbour_processes[UP] = %s \nneighbour_processes[DOWN] = %s \nneighbour_processes[LEFT] = %s \nneighbour_processes[RIGHT] = %s \n" % (rank, my_mpi_row, my_mpi_col, neighbour_processes[UP], neighbour_processes[DOWN], neighbour_processes[LEFT], neighbour_processes[RIGHT]))

    if rank == 0:
        ride_request = "Pick up penumpang Fadil di Cibogo"
        destination_process = 4
        comm.send(ride_request, dest=destination_process)
        print("Sending ride request '%s' to process %d" % (ride_request, destination_process))
    elif rank == 1:
        ride_request = "Pick up penumpang Bryan di Mekkah"
        destination_process = 8
        comm.send(ride_request, dest=destination_process)
        print("Sending ride request '%s' to process %d" % (ride_request, destination_process))
    elif rank == 4:
        ride_request = comm.recv(source=0)
        print("Ride request received is '%s'" % ride_request)
    elif rank == 8:
        ride_request = comm.recv(source=1)
        print("Ride request received is '%s'" % ride_request)
