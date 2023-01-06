from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")


print(table)
