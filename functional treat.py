print("\n=====welcome to the data analyzer and transformer program=====")

print("\n======main menu======")
while True:
 print("1.input data")
 print("2.display data summary (built-in functions)")
 print("3.calculate factorial (recursive function)")
 print("4.filter data by threshold (lambda function)")
 print("5.sort data")
 print("6.display dataset statistics (return multiple values)")
 print("7.exit program")

 choice = input("\nEnter your choice (1-7): ")

 if choice == '1':
     print("=====input data=====")
     data = input("Enter a data for a 1D array (separated by spaces): ")
     data_list = [float(x) for x in data.split()]
     print("Data has been stored successfully!")
    

 elif choice == '2':
     print("=====display data summary=====")
     def display_summary(data):
         total_elements = len(data)
         min_value = min(data)
         max_value = max(data)
         sum_values = sum(data)
         average_value = sum_values / total_elements if total_elements > 0 else 0
         return total_elements, min_value, max_value, sum_values, average_value
     if len(data_list) > 0:
         print("Data summary:")
         total, minimum, maximum, total_sum, average = display_summary(data_list)
         print("Total elements:", total)
         print("Minimum value:", minimum)
         print("Maximum value:", maximum)
         print("Sum of all values:", total_sum)
         print("Average value:", average)
     else:
         print("No data available. Please input data first.")

 elif choice == '3':
     print("=====calculate factorial=====")
     def factorial(n):
         print(factorial.__doc__)
         if n == 0 or n == 1:
             return 1
         else:
             return n * factorial(n - 1)

     num = int(input("Enter a non-negative integer to calculate its factorial: "))
     if num < 0:
         print("Factorial is not defined for negative numbers.")
     else:
         print(f"The factorial of {num} is: {factorial(num)}")

 elif choice == '4':
     print("=====filter data by threshold=====")
     if len(data_list) > 0:
         def total_sum(*numbers):
             return sum(numbers)
         threshold = float(input("Enter a threshold value to filter out values: "))
         filtered_data = list(filter(lambda x: x > threshold, data_list))
         print("Filtered data (values greater than threshold):", filtered_data)
     else:
         print("No data available. Please input data first.")

 elif choice == '5':
     print("=====sort data=====")
     print("1. Ascending")
     print("2. Descending")
     sort_choice = input("Enter your choice (1-2): ")
     if len(data_list) > 0:
         if sort_choice == '1':
             sorted_data = sorted(data_list)
         elif sort_choice == '2':
             sorted_data = sorted(data_list, reverse=True)
         else:
             print("Invalid choice. Data will be sorted in ascending order.")
             sorted_data = sorted(data_list)
         print("Sorted data:", sorted_data)
     else:
         print("No data available. Please input data first.")

 elif choice == '6':
     print("=====calculate dataset statistics=====")
     if len(data_list) > 0:
         def dataset_statistics(data):
             total_elements = len(data)
             min_value = min(data)
             max_value = max(data)
             sum_values = sum(data)
             average_value = sum_values / total_elements if total_elements > 0 else 0
             return total_elements, min_value, max_value, sum_values, average_value

         stats = dataset_statistics(data_list)
         print("Dataset statistics:")
         print("Total elements:", stats[0])
         print("Minimum value:", stats[1])
         print("Maximum value:", stats[2])
         print("Sum of all values:", stats[3])
         print("Average value:", stats[4])
     else:
         print("No data available. Please input data first.")

 elif choice == '7':
     print("=====exit program=====")
     print("*****thank you for using the data analyzer and transformer program. Goodbye!*****")
     break   
 else:
     print("Invalid choice. Please enter a number between 1 and 7.")

