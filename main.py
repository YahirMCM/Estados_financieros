from rich.table import Table
from rich.console import Console

print('¡Bienvenido/a al uso de este programa de estados financieros!\nFavor de ingresar los siguientes datos requeridos:\n\n')

y1 = input('Ingrese el año del cual se registrarán los datos: ')

while True:
    # Se solicitan los datos
    try:
        acreedores_y1 = float(input('\nAcreedores diversos: '))
        aportFuturos_y1 = float(input('Aportaciones para futuros aumentos de capital'))
        capitalSocial_y1 = float(input('Capital Social'))
        costoVentas_y1 = float(input('Costo de Ventas: '))
        cuentasCobrar_y1 = float(input('Cuentas por Cobrar: '))
        cuentasPagar_y1 = float(input('Cuentas por Pagar: '))
        desprAcum_y1 = float(input('Despreciación acumulada de Activos Fijo: '))
        docxPagar_y1 = float(input('Documentos por pagar: '))
        efectivo_y1 = float(input('Efectivo: '))
        eqComputo_y1 = float(input('Equipo de computo: '))
        eqTransportes_y1 = float(input('Equipo de Transportes: '))
        gastosAdmon_y1 = float(input('Gastos de administración: '))
        gastosVentas_y1 = float(input('Gastos de ventas: '))
        gastosFinancieros_y1 = float(input('Gastos Financieros: '))
        gastosDespr_y1 = float(input('Gastos por depreciación: '))
        gastosPreop_y1 = float(input('Gastos preoperativos: '))
        hipotecasPagarLP_y1 = float(input('Hipotecas por pagar largo plazo: '))
        taxes_y1 = float(input('Impuestos: '))
        inv_y1 = float(input('Inventarios: '))
        invest_y1 = float(input('Inversiones: '))
        maqEquipo_y1 = float(input('Maquinaria y equipo: '))
        mobAccesorios_y1 = float(input('Mobiliario y accesorios: '))
        otrosGastos_y1 = float(input('Otros Gastos: '))
        otrosProductos_y1 = float(input('Otros Productos: '))
        prodFinancieros_y1 = float(input('Productos Financieros: '))
        reservaLegal_y1 = float(input('Reserva Legal: '))
        terryEdificios_y1 = float(input('Terreno y edificios: '))
        utilyEjAnteriores_y1 = float(input('Utilidades ejercicios anteriores: '))
        ventas_y1 = float(input('Ventas: '))
    except:
        print('ERROR: INGRESE UN VALOR MONETARIO')
    else:
        break
# Se hacen los calculos de ER
utilyBruta_y1 = ventas_y1 -  costoVentas_y1
resIntegral_y1 = gastosFinancieros_y1 - prodFinancieros_y1
totalGastosOpe_y1 = gastosVentas_y1 + gastosAdmon_y1 + gastosDespr_y1 + resIntegral_y1
utilyOperativa_y1 = utilyBruta_y1 - totalGastosOpe_y1
totalOtrosGastos_y1 = otrosGastos_y1 - otrosProductos_y1
utilyAntesTax_y1 = utilyOperativa_y1 - totalOtrosGastos_y1
isr_y1 = utilyAntesTax_y1 * 0.30
ptu_y1 = utilyAntesTax_y1 * 0.10
totalTaxPagar_y1 = isr_y1 + ptu_y1
utilyNetaEj_y1 = utilyAntesTax_y1 - totalTaxPagar_y1

# Calculos Balance General
#   Activos             #
totalAC_y1 = efectivo_y1 + cuentasCobrar_y1 + invest_y1 + inv_y1
totalANC_y1 = (terryEdificios_y1 + maqEquipo_y1 + mobAccesorios_y1 + eqComputo_y1 + eqTransportes_y1) - desprAcum_y1
otrosActivos_y1 = gastosPreop_y1

totalActivos_y1 = totalAC_y1 +  totalANC_y1 + otrosActivos_y1
#   Pasivos             #
nwTaxes_y1 = (totalTaxPagar_y1 + taxes_y1)
totalPC_y1 = acreedores_y1 + cuentasPagar_y1 + docxPagar_y1 + nwTaxes_y1

totalPasivos_y1 = totalPC_y1 +  hipotecasPagarLP_y1
#   Capital Contable    #
totalCap_y1 = capitalSocial_y1 + reservaLegal_y1 + aportFuturos_y1
utilyEjercicio_y1 = utilyEjAnteriores_y1 + utilyNetaEj_y1
totalCC_y1 = totalCap_y1 + utilyEjercicio_y1

# Generación de tablas

t_er = Table(title= f"ESTADO DE RESULTADOS AÑO {y1}", show_lines=True)
t_er.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
t_er.add_column("1", justify="center", style="red", no_wrap=False)
t_er.add_column("2", justify="center", style="green", no_wrap=False)
t_er.add_column("3", justify="center", style="green", no_wrap=False)
t_er.add_column("4", justify="center", style="green", no_wrap=False)

t_er.add_row("Ventas", "", "", "", f"${ventas_y1}")
t_er.add_row("Costo de ventas", "", "", "", f"${costoVentas_y1}")
t_er.add_row("", "Utilidad Bruta", "", "", f"${utilyBruta_y1}")

t_er.add_row("Gastos de Venta", "", "", f"${gastosVentas_y1}", "")
t_er.add_row("Gastos de Administración", "", "", f"${gastosAdmon_y1}", "")
t_er.add_row("Gastos por Despreciación", "", "", f"${gastosDespr_y1}", "")
t_er.add_row("Gastos Financieros", "", f"${gastosFinancieros_y1}", "", "")
t_er.add_row("Productos Financieros", "", f"${prodFinancieros_y1}", "", "")
t_er.add_row("", "Resultado Integral de Financiamiento", "", f"${resIntegral_y1}", "")
t_er.add_row("", "Total de Gastos Operativos", "", "", f"${totalGastosOpe_y1}")
t_er.add_row("", "Utilidad Operativa", "", "", f"${utilyOperativa_y1}")

t_er.add_row("Otros Gastos", "", "", f"${otrosGastos_y1}", "")
t_er.add_row("Otros Productos", "", "", f"${otrosProductos_y1}", "")
t_er.add_row("", "Total de Otros Gastos y Productos", "", "", f"${totalOtrosGastos_y1}")
t_er.add_row("", "Utilidad antes de impuestos", "", "", f"${utilyAntesTax_y1}")

t_er.add_row("ISR", "30%", "", f"${isr_y1}", "")
t_er.add_row("PTU", "10%", "", f"${ptu_y1}", "")

t_er.add_row("", "Total de Impuestos por Pagar", "", "", f"${totalTaxPagar_y1}")
t_er.add_row("", "Utilidad NETA del ejercicio", "", "", f"${utilyNetaEj_y1}")

# Generación de Balance General
t_bg = Table(title=f'BALANCE GENERAL AL {y1}', show_lines=True)
t_bg.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
t_bg.add_column("1", justify="center", style="red", no_wrap=False)
t_bg.add_column("2", justify="center", style="green", no_wrap=False)
t_bg.add_column("3", justify="center", style="green", no_wrap=False)
t_bg.add_column("4", justify="center", style="green", no_wrap=False)

t_bg.add_row("Efectivo", "", f"${efectivo_y1}", "", "")
t_bg.add_row("Cuentas por cobrar", "", f"${cuentasCobrar_y1}", "", "")
t_bg.add_row("Inventarios", "", f"${inv_y1}", "", "")
t_bg.add_row("Inversiones", "", f"${invest_y1}", "", "")
t_bg.add_row("", "TOTAL ACTIVOS CIRCULANTES", "", f"${totalAC_y1}", "")

t_bg.add_row("Terreno y Edificios", "", f"${terryEdificios_y1}", "", "")
t_bg.add_row("Maquinaria y Equipo", "", f"${maqEquipo_y1}", "", "")
t_bg.add_row("Mobiliario y Accesorios", "", f"${mobAccesorios_y1}", "", "")
t_bg.add_row("Equipo de Computo", "", f"${eqComputo_y1}", "", "")
t_bg.add_row("Equipo de Transportes", "", f"${eqTransportes_y1}", "", "")
t_bg.add_row("Despreciación acumulada de Activos Fijos", "", f"${desprAcum_y1}", "", "")
t_bg.add_row("", "TOTAL ACTIVOS NO CIRCULANTES", "", f"${totalANC_y1}", "")

t_bg.add_row("Gastos Preoperativos", "", f"${gastosPreop_y1}", "", "")

t_bg.add_row("", "TOTAL ACTIVOS", "", "", f"${totalActivos_y1}")

t_bg.add_row("Acreedores diversos", "", f"${acreedores_y1}", "", "")
t_bg.add_row("Cuentas por Pagar", "", f"${cuentasPagar_y1}", "", "")
t_bg.add_row("Documentos por Pagar", "", f"${docxPagar_y1}", "", "")
t_bg.add_row("Impuestos", "", f"${nwTaxes_y1}", "", "")
t_bg.add_row("", "TOTAL PASIVOS CORTO PLAZO", "", f"${totalPC_y1}", "")

t_bg.add_row("Hipotécas por pagar a largo plazo", "", f"${hipotecasPagarLP_y1}", "", "")

t_bg.add_row("", "TOTAL PASIVOS", "", "", f"{totalPasivos_y1}")

t_bg.add_row("Capital Social", "", f"${capitalSocial_y1}", "", "")
t_bg.add_row("Reserva Legal", "", f"${reservaLegal_y1}", "", "")
t_bg.add_row("Aportaciones para futuros aumentos de capital", "", f"${aportFuturos_y1}", "", "")

t_bg.add_row("", "TOTAL CAPITAL", "", f"{totalCap_y1}", "")

t_bg.add_row("Utilidades del ejercicio anteriores", "", f"${utilyEjAnteriores_y1}", "", "")
t_bg.add_row("Utilidad del ejercicio", "", f"${utilyNetaEj_y1}", "", "")

t_bg.add_row("", "TOTAL CAPITAL CONTABLE", "", "", f"${totalCC_y1}")
# Generación de Consola
console = Console()

# Menú
while True:
    main_menu = int(input('\n¿Qué desea ver?\n\t1. Estado de Resultados\n\t2. Balance General\n\t3. Salir'))
    
    if main_menu == 1:
        console.print(t_er)

        sub_op = input('\nEscribir "menú" para mostrar el menú nuevamente, presionar enter para salir del programa')

        if sub_op == "menú":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 2:
        console.print(t_bg)

        sub_op = input('\nEscribir "menú" para mostrar el menú nuevamente, presionar enter para salir del programa')

        if sub_op == "menú":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 3:
        break

#**CAPITAL DE TRABAJO**
#**(EDITAR DESPUES, ESTO ES UN BORRADOR DEL CODIGO FINAL, SIN USAR LA ESTRUCTURA DE TABLE Y ROWS)**

#print(f"Activo Circulante 2014: ${totalAC_y1}")
#print(f"Activo Circulante 2015: ${totalAC_y2}")
#print("")
#print(f"Pasivo Corto Plazo 2014: ${totalPC_y1}")
#print(f"Pasivo Corto Plazo 2015: ${totalPC_y2}")
#print("")
#capTN_y1 = (totalAC_y1 - totalPC_y1)
#capTN_y2 = (totalAC_y2 - totalPC_y2)
#print(f"Capital de Trabajo Neto 2014: {capTN_y1}")
#print(f"Capital de Trabajo Neto 2015: {capTN_y2}")
#print("")
#razonCirc_y1 = (totalAC_y1 / totalPC_y1)
#razonCirc_y2 = (totalAC_y2 / totalPC_y2)
#print("")
#print(f"Razon Circulante 2014: ${razonCirc_y1:.2f}")
#print(f"Razon Circulante 2015: ${razonCirc_y2:.2f}")
