class Calculator:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if a == 0:
            raise ZeroDivisionError('Division by zero')
            return 0
        else:
            return a / b

        # if b == 0:
        #     raise ZeroDivisionError('Division by zero')
        #     return 0
        # else:
        #     return a / b

    def pov(self, a, b):
        return a ** b

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.div(s, len(nums))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

