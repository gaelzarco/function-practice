def hello():
    print("Hello World")

hello()

def pack(first, second, third):
    return [f"{first}", f"{second}", f"{third}"]

print(pack("hi", "hello", "hey"))

full_list = ["apple", "sandwich", "chocolate bar"]
empty_list = []

def eat_lunch(list):
    if len(list) > 0:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[i]}")
            else :
                print((f"Next I eat {list[i]}"))
    else:
        print("My lunchbox is empty!")

eat_lunch(full_list)
eat_lunch(empty_list)
