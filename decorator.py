def greeting(name):
    def greeting_decorator(method_to_be_called):
        user_name = name

        def wrapper(*args, **kwargs):
            print("Hello {}!".format(user_name))
            method_to_be_called(*args, **kwargs)
            print("Good bye!")

        return wrapper

    return greeting_decorator


@greeting("User1")
def message(time):
    print("There is a meeting tomorrow at {}".format(time))


message("10 am")
