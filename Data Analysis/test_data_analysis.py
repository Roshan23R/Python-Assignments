from data_analysis import *

datastr= input("enter the data with comma seperated:  ")

data = list(map(int,datastr.split(',')))
# print(data)
print("DO DATA ANALYSIS:")
print("1. Calculate Mean \n2. Calculate Median \n3. Calculate Variance \n4. Calculate Standard Deviation \n5. Cumulative Sum")
while True:
    choice = input("Enter your choce b/w 1 to 4: ")
    if choice == '1':
        print("Mean: ",calculate_mean(data))
    elif choice == '2':
        print("Median: ",calculate_median(data))
    elif choice == '3':
        print("Variance: ",calculate_variance(data))
    elif choice == '4':
        print("Standard Deviation: ",calculate_std(data))
    elif choice == '5':
        print("Cumulative Sum: ",cumulative_sum(data))
    else:
        break    
