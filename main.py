from rich.table import Table
from rich.console import Console

print('¡Bienvenido/a al uso de este programa de estados financieros!\nFavor de ingresar los siguientes datos requeridos:')

y1 = input('Ingrese el año del cual se registrarán los datos: ')
# acreedores_y1 = float(input('Acreedores diversos: '))
# aportFuturos_y1 = float(input())
# capitalSocial_y1 = float(input())
costoVentas_y1 = float(input('Costo de Ventas: '))

ventas_y1 = float(input('Ventas: '))

utilyBruta_y1 = costoVentas_y1 - ventas_y1


# Generación de tablas

t_ER = Table(title= f"ESTADO DE RESULTADOS AÑO {y1}", show_lines=True)
t_ER.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
t_ER.add_column("1", justify="center", style="red", no_wrap=True)
t_ER.add_column("2", justify="center", style="white", no_wrap=False)
t_ER.add_column("3", justify="center", style="white", no_wrap=False)
t_ER.add_column("4", justify="center", style="green", no_wrap=False)

t_ER.add_row("Ventas", "", "", "", f"${ventas_y1}")
t_ER.add_row("Costo de ventas", "", "", "", f"${costoVentas_y1}")
t_ER.add_row("", "Utilidad Bruta", "", "", f"${utilyBruta_y1}")

# Impresión de Consola

console = Console()
console.print(t_ER)
