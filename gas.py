#function 1
def display_gas(gas_level):
    print(f"gas remaining: {gas_level}")
#function 2
def use_gas(gas_level, amount):
    gas_level -= amount
    return gas_level
