import typing


def chain_sum(number: int) -> typing.Callable:

    class Calculator:
        def __init__(self, init_value) -> None:
            self.init_value = init_value
        
        def __call__(self, value: int = 0) -> typing.Self:
            self.init_value += value
            if value == 0:
                print(self.init_value)
            return self
            
        

    return Calculator(number)


if __name__ == "__main__":
    chain_sum(5)()
    chain_sum(5)(10)(20)()