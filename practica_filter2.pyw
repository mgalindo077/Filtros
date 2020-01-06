class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan","Director",750000),
Empleado("Ana","Presidenta",850000),
Empleado("Mario","Administrativo",250000),
Empleado("Hugo","Secretario",270000),
Empleado("Mario","Receptor",210000),
]

salarios_altos=filter(lambda empleado:empleado.salario>50000,listaEmpleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)