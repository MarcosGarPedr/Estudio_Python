name = "Cris"
print(f"Hola, {name}, te gustaría aprender Python hoy?")

print(name.upper())
print(name.lower())

name = "marcos garcía"
print(name.title())


print('Antonio Escohotado una vez dijo "Una sociedad que anteponga la igualdad a la libertad terminara sin ambas"')

autor = "Antonio Escohotado"
cita = "Una sociedad que anteponga la igualdad a la libertad terminara sin ambas"
print(f'{autor} una vez dijo "{cita}"')


name = "\tBono\t"
print(f'"{name}"')
print(f'"{name.lstrip()}"')
print(f'"{name.rstrip()}"')
print(f'"{name.strip()}"')


filename = "python_notes.txt"
print(filename.removesuffix(".txt"))