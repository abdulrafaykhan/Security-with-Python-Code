import threading
import time


def calc_square(numbers):
    print("Calculate Square Numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n * n)

def calc_cube(numbers):
    print("Calculate Cube Numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n*n)




arr = [3, 4, 5, 6]
t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))
t3 = threading.Thread(target=is_even, args=(arr,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Done in ", time.time()-t)
print("Ha! I am all done!")

