
from sorting_algorithm import *
from visualization import *


if __name__ == "__main__":
    main()
    

# random_num = [random.randint(1000, 2999) for _ in range(10)]
# print ("Unsorted List: ", random_num)
# bubble_sort(random_num)
# print("Bubble Sort: ", random_num)
#
# random_num = [random.randint(1000, 2999) for _ in range(10)]
# print ("Unsorted List: ", random_num)
# merge_sort(random_num)
# print("Merge Sort: ", random_num)
#
# random_num = [random.randint(1000, 2999) for _ in range(10)]
# print ("Unsorted List: ", random_num)
# quick_sort(random_num, 0, len(random_num) - 1)
# print("Quick Sort: ", random_num)
#
# random_num = [random.randint(1000, 2999) for _ in range(10)]
# print ("Unsorted List: ", random_num)
# radix_sort(random_num)
# print("Radix Sort: ", random_num)
#
# indices = linear_search(random_num, int(input("Enter the target value: ")))
# print("Linear Search: ", indices)

# random_num = [random.randint(1000, 2999) for _ in range(10000)]
# print(f"Bubble Sort Time Execution: {time_analysis_sort(bubble_sort, random_num)}")
#
# random_num = [random.randint(1000, 2999) for _ in range(10000)]
# print(f"Merge Sort Time Execution: {time_analysis_sort(merge_sort, random_num)}")
#
# random_num = [random.randint(1000, 2999) for _ in range(10000)]
# print(f"Quick Sort Time Execution: {time_analysis_quick_sort(quick_sort, random_num, 0, len(random_num) - 1)}")
#
# random_num = [random.randint(1000, 2999) for _ in range(10000)]
# print(f"Radix Sort Time Execution: {time_analysis_sort(radix_sort, random_num)}")
#
# target = random.randint(1000, 2999)
# print(f"Linear Search Time Execution: {time_analysis_search(linear_search, random_num, target)}")