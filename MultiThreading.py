import time
import threading


def add1(sleep_after_read):
    global steps, x
    y = x
    thread_name = threading.current_thread().getName()
    print('Thread: {}, before sleep {} x is {}'.format(thread_name, sleep_after_read, y))
    time.sleep(sleep_after_read)
    if thread_name not in steps:
        steps[thread_name] = 0
    steps[thread_name] += 1
    x = y + 1
    print('Thread: {}, thread_steps: {} ,after sleep {} ,x became {}\n'.format(thread_name, steps[thread_name],
                                                                               sleep_after_read, y + 1))


def sleep(seconds):
    print('Thread: {}, sleeps {} seconds'.format(threading.current_thread().getName(), seconds))
    time.sleep(seconds)


def thread_1():
    add1(5.1)  # reads 0, writes 1
    sleep(5.1)  # wait for other threads to do all their additions besides the last one
    for i in range(9):
        add1(0)


def thread_other_than_1():
    time.sleep(1.2)  # allow thread 1 to read 0
    for i in range(9):  # while thread 1 sleeps, do all additions besides the last one
        add1(0)
    sleep(5.2)  # allow thread 1 to do all its additions
    add1(4.2)  # reads 1, writes 2


def main():
    # Creating threads
    thread1 = threading.Thread(target=thread_1)
    thread2 = threading.Thread(target=thread_other_than_1)
    thread3 = threading.Thread(target=thread_other_than_1)
    thread4 = threading.Thread(target=thread_other_than_1)

    # Run the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


if __name__ == '__main__':
    x = 0
    steps = {}
    main()
