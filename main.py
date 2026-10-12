# main.py - Interactive CLI for DataLens
from datalens import (
    reverse_array, count_element, find_maximum, 
    remove_duplicates_ordered, partition_array, 
    kth_smallest, time_tradeoff_demo
)

def main():
    print("=========================================")
    print("      Welcome to DataLens Engine         ")
    print("=========================================")
    
    # Sample default array
    sample_arr = [2, 5, 5, 9, 12, 18, 18, 25, 30]
    print(f"Default Working Array: {sample_arr}\n")
    
    while True:
        print("\n--- MENU ---")
        print("1. Reverse Array")
        print("2. Count Element Frequency")
        print("3. Find Maximum Number")
        print("4. Remove Duplicates from Ordered Array")
        print("5. Partition Array (by Pivot)")
        print("6. Find K-th Smallest Element")
        print("7. Run Time Tradeoff Demo (List vs Set)")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            print(f"Reversed: {reverse_array(sample_arr)}")
        elif choice == '2':
            val = int(input("Enter number to count: "))
            print(f"Count of {val}: {count_element(sample_arr, val)}")
        elif choice == '3':
            print(f"Maximum element: {find_maximum(sample_arr)}")
        elif choice == '4':
            print(f"Without duplicates: {remove_duplicates_ordered(sample_arr)}")
        elif choice == '5':
            pivot = int(input("Enter pivot value: "))
            res = partition_array(sample_arr, pivot)
            print(f"Partitions: {res}")
        elif choice == '6':
            k = int(input("Enter K (e.g., 1 for 1st smallest): "))
            print(f"The {k}-th smallest element is: {kth_smallest(sample_arr, k)}")
        elif choice == '7':
            print("Running Time Tradeoff Benchmark...")
            results = time_tradeoff_demo()
            for k, v in results.items():
                print(f"  - {k}: {v}")
        elif choice == '8':
            print("Exiting DataLens. Good luck with your B.Tech course!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
