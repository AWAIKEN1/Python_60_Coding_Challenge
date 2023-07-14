todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("You entered an unknown command")
    #This is just an example to show that it is possible if you want you can include a variable - in this case whatever to say that if a case isn't matched then it tell you this.

print("Bye!")
