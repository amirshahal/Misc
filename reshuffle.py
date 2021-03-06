# Python Program to shuffle a given array
import random


# A function to generate a random permutation of arr[]
def randomize(arr):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    n = len(arr)
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)

        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
        print('Replacing {} and {},arr now is {}'.format(arr[i], arr[j], arr))

    return arr


def main():
    # Driver program to test above function.
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(randomize(arr))


if __name__ == '__main__':
    main()
