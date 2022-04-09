from mpi4py import MPI
import numpy as np

world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank()


def is_prime(val):
    for n in range(2, int(val**0.5)+1):
        if val % n == 0:
            return False
    return True


def do_stuff(num_list):
    bool_arr = []
    for n in num_list:
        bool_arr.append(is_prime(n))
        # bool_arr.append(n)
    return bool_arr


if my_rank == 0:
    numbers = np.arange(0, world_size * 100, 1)
    numbers_chunks = np.array_split(numbers, world_size, axis=0)
else:
    numbers_chunks = None

numbers_chunks = world_comm.scatter(numbers_chunks, root=0)

# print('rank ', my_rank, ' has data ', numbers_chunks)

numbers_chunks = do_stuff(numbers_chunks)

newData = world_comm.gather(numbers_chunks, root=0)

if my_rank == 0:
    # print(newData)
    np.save('true-false.npy', newData)

