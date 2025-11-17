def curry(func, arity):
    if not callable(func):
        raise TypeError("Expected callable function")

    if not isinstance(arity, int) or arity <= 0:
        raise ValueError("Arity must be a positive integer")

    def curried(*args, **kwargs):
        total_args = len(args) + len(kwargs)
        if total_args > arity:
            raise TypeError("Too many arguments")

        if total_args >= arity:
            return func(*args, **kwargs)

        def partial(*more_args, **more_kwargs):
            new_args = args + more_args
            new_kwargs = {**kwargs, **more_kwargs}
            return curried(*new_args, **new_kwargs)

        return partial

    return curried


def uncurry(curried_func, arity):
    if not callable(curried_func):
        raise TypeError("Expected callable function")

    if not isinstance(arity, int) or arity <= 0:
        raise ValueError("Arity must be a positive integer")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Expected {arity} arguments, got {len(args)}")

        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried


def sum3(x, y, z):
    return x + y + z


sum3_curry = curry(sum3, 3)
sum3_uncurry = uncurry(sum3_curry, 3)
print(sum3_curry(1)(2)(3))  # 6
print(sum3_uncurry(1, 2, 3))  # 6
