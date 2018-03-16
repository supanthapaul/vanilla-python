
user_number= int(input("Enter a number::"))

list_range = range(1, user_number+1)

devisor_list = []

for i in list_range:
    if user_number % i == 0:
        devisor_list.append(i)

print("The devisors are:: " + str(devisor_list))