with open("students.txt","w") as file:
    for i in range(5):
        name = input(f"enter name of student {i + 1}")
        file.write(name + "\n")

        import os 
        filename = input("enter the file name to check: ")
        if os.path.exists(filename):
            print(f"the file '{filename}'exists.")
        else:
            print("the file '{filename}' does not exists.")


with open("student.txt","w") as file:
    file.write("your name\n")


def sum_of_list(lst):
    return sum(lst)

numbers= [1,2,3,4,5]
print("sum",sum_of_list(numbers))

numbers = [10,20,30,,40]
total,avg = sum_and_average(numbers)
print("sum:")