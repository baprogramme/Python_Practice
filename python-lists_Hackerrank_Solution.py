if __name__ == '__main__':
    N = int(input())  # Read the number of commands
    my_list = []      # Initialize an empty list

    for _ in range(N):
        command = input().split()  # Read each command and split it into parts
        operation = command[0]     # First word is the command name

        if operation == 'insert':
            index = int(command[1])
            value = int(command[2])
            my_list.insert(index, value)
        elif operation == 'print':
            print(my_list)
        elif operation == 'remove':
            value = int(command[1])
            my_list.remove(value)
        elif operation == 'append':
            value = int(command[1])
            my_list.append(value)
        elif operation == 'sort':
            my_list.sort()
        elif operation == 'pop':
            my_list.pop()
        elif operation == 'reverse':
            my_list.reverse()
