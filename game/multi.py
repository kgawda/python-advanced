from queue import Empty
from main import simulate
from multiprocessing import Process, Queue, Pool
from threading import Thread
import concurrent.futures


def f(queue):
    result = simulate()
    queue.put(result)

def f2(x):
    return simulate()

if __name__ == "__main__":
    # processes = []
    # threds = []
    # q = Queue()
    # for _ in range(5):
    #     # p = Process(target=f, args=(q,))
    #     # processes.append(p)
    #     # p.start()
    #     t = Thread(target=f, args=(q,))
    #     threds.append(t)
    #     t.start()
    
    # # for p in processes:
    # #     p.join()
    # for t in threds:
    #     t.join()

    # while True:
    #     try:
    #         print(q.get(block=False))
    #     except Empty:
    #         break

    # ====

    # with Pool(10) as pool:
    #     results = pool.map(f2, range(10))
    #     print(results)

    # ====

    with concurrent.futures.ThreadPoolExecutor(5) as executor:
        results = executor.map(f2, range(5))
        print(list(results))
