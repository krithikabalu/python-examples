def greeting(name):
    user_name = name

    def greeting_decorator(method_to_be_called):
        def greeting_wrapper(time):
            print("Hello {}!".format(user_name))
            method_to_be_called(time)
            print("Good bye!")

        return greeting_wrapper

    return greeting_decorator


@greeting("User1")
def message(time):
    print("There is a meeting tomorrow at {}".format(time))


message("10 am")