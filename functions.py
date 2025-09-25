def function_name():
    print("hello, world!")


def greet():
    print("welcome to python function!")
greet()

def greet_user(names):
    print("hello,",names)
    greet_user("hello")

def add (a,b):
    print("sum is:",a+b)
    add(5,10)

    def introduce(name,age):
        print(f"my name is {name}and i am {age}years old")
        introduce (age=29,name="hero")


        def greet(name="guest"):
            print("hello",name)
            greet()
            greet("sai")
            

