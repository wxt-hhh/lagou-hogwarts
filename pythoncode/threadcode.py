import logging
from time import sleep, ctime
import _thread

logging.basicConfig(level=logging.INFO)

# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())


# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())


# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)  # _thread 主线程退出时，所有的子线程会被强行kill，所以需要等待6秒执行子线程
#     logging.info("end all at " + ctime())

loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info(f"start loop{nloop} at {ctime()}")
    sleep(nsec)
    logging.info(f"end loop{nloop} at {ctime()}")
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
