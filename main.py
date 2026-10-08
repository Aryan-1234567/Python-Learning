
import gas

gas_level = int(input("Input gas level: "))
amount = int(input("Enter amount of gas used: "))

gas_display = gas.display_gas(gas_level)
gas_level = gas.use_gas(gas_level, amount)
gas.display_gas(gas_level)

