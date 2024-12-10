FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Open file, read in the memory a content to work with
    and return(create) the list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """" Write the to-do items list in the todo file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# if you use print(__name__) the result in another file is the name of the module (ex. function).
# The name inside the module (ex. function) itself is "__main__" as default.

if __name__ == "__main__":
    print("Hello")
    print(get_todos())