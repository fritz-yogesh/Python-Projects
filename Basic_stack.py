''' Basic Stack '''

stack = []  
size = 5

def main():

    while True:
        print("==== Stack Menu ====")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        print("====================")
        try:
            ch = int(input("Enter Option: "))
        except ValueError:
            print("Invail input")
        except:
            print("Error occured.")
        if ch == 1:
            push(stack)
        elif ch == 2:
            pop(stack)
        elif ch == 3:
            peek(stack)
        elif ch == 4:
            display(stack)
        elif ch == 5:
            print("Thank you Visit again!")
            break
        else:
            print("Invaild Input")

def push(stack):
    if len(stack) == 5:
        print("Error: Overflow")
    else:
        print("======= PUSH Menu =======")
        ele = input("Element: ")
        stack.append(ele)
        print("==========================")
        print("Element has been pushed.")


def pop(Stack):
    if len(stack) == 0:
        print("Error: Underflow")
    else:
        stack.pop()
        print("Elemnt has been popped")

def peek(Stack):
    if len(stack) == 0:
        print("Stack is Empty!")
    else:
        print("Top Element: ", stack[-1])

def display(Stack):
    if len(stack) == 0:
        print("Stack is Empty!")
    else:
        for i in range(-1,-len(stack)-1,-1):
            print(stack[i])

#main program
main()
