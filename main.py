from rich.table import Table
from rich.console import Console
import pandas as pd

cuentas = {
        'year':[2014, 2015],
        'acreedores':[65.00, 50.00],
        'aportFuturos':[535.00, 545.00],
        'capitalSocial':[460.00, 460.00],
        'costoVentas':[2610.00, 2139.00],
        'cuentasCobrar':[629.00, 456.00],
        'cuentasPagar':[478.00, 338.00],
        'desprAcum':[2291.00, 2570.00],
        'docxPagar':[99.00, 124.00],
        'efectivo':[454.00, 393.00],
        'eqComputo':[123.00, 120.00],
        'eqTransportes':[344.00, 393.00],
        'gastosAdmin':[243.00, 234.00],
        'gastosVentas':[125.00, 135.00],
        'gastosFinancieros':[116.00, 114.00],
        'gastosDepre':[299.00, 279.00],
        'gastosPreop':[138.00, 138.00],
        'hipotecasPagarLP':[1279.00, 1209.00],
        'taxes':[134.00, 93.00],
        'inv':[361.00, 375.00],
        'invest':[85.00, 64.00],
        'maqEquipo':[1750.00, 2110.00],
        'mobAccesorios':[448.00, 395.00],
        'otrosGastos':[44.00, 44.00],
        'otrosProductos':[10.00, 45.00],
        'prodFinancieros':[5.00, 10.00],
        'reservaLegal':[30.00, 35.00],
        'terryEdificios':[2590.00, 2379.00],
        'utilyEjAnteriores':[1130.00, 1080.00],
        'ventas':[3843.00, 3209.00]
        }

cuentas = pd.DataFrame(cuentas)
cuentas.set_index('year', inplace=True)
#print(cuentas)

estado_resultados = {
            'year':[2013],
            'utilidadBruta':[100.00],
            'resultadoIntegral':[100.00],
            'totalGastosOp':[100.00],
            'utilidadOperativa':[100.00],
            'totalOtrosGastos':[100.00],
            'utilidadAntesTax':[100.00],
            'ISR':[100.00],
            'PTU':[100.00],
            'totalTaxesPagar':[100.00],
            'utilidadNetaEjercicio':[100.00]            
        }
estado_resultados = pd.DataFrame(estado_resultados)
estado_resultados.set_index('year', inplace=True)
#print(estado_resultados)

balance_general = {
            'year':[2013],
            'totalActivosCirculantes':[100.00],
            'totalActivosNOcirculantes':[100.00],
            'otrosActivos':[100.00],
            'totalActivos':[100.00],
            'Impuestos':[100.00],
            'totalPasivosCirculantes':[100.00],
            'totalPasivos':[100.00],
            'totalCapital':[100.00],
            'utilidadEjercicio':[100.00],
            'totalCapitalContable':[100.00] 
        }
balance_general = pd.DataFrame(balance_general)
balance_general.set_index('year', inplace=True)
#print(balance_general)

print('¡Bienvenido/a al uso de este programa de estados financieros!\nFavor de ingresar los siguientes datos requeridos:\n\n')
# ELECCION DE SI QUIERE AñADIR DATOS O PREFIERE USAR LOS QUE YA TIENE
while True:
    print("Desea agregar datos?")
    print("1- SI")
    print("2- NO")
    agregar_datos = int(input("Seleccione el numero para la opcion: "))

    if agregar_datos == 1:
        # Se solicitan los datos
            try:
                año = int(input("Escribe el año de los datos a registrar:"))
                acreedores = float(input('\nAcreedores diversos: '))
                aportFuturos = float(input('Aportaciones para futuros aumentos de capital'))
                capitalSocial = float(input('Capital Social'))
                costoVentas = float(input('Costo de Ventas: '))
                cuentasCobrar = float(input('Cuentas por Cobrar: '))
                cuentasPagar = float(input('Cuentas por Pagar: '))           
                desprAcum = float(input('Despreciación acumulada de Activos Fijo: ')) 
                docxPagar = float(input('Documentos por pagar: '))
                efectivo = float(input('Efectivo: '))
                eqComputo = float(input('Equipo de computo: '))
                eqTransportes = float(input('Equipo de Transportes: '))
                gastosAdmon = float(input('Gastos de administración: '))
                gastosVentas = float(input('Gastos de ventas: '))
                gastosFinancieros = float(input('Gastos Financieros: '))
                gastosDespr = float(input('Gastos por depreciación: '))
                gastosPreop = float(input('Gastos preoperativos: '))
                hipotecasPagarLP = float(input('Hipotecas por pagar largo plazo: '))
                taxes = float(input('Impuestos: '))
                inv = float(input('Inventarios: '))
                invest = float(input('Inversiones: '))
                maqEquipo = float(input('Maquinaria y equipo: '))
                mobAccesorios = float(input('Mobiliario y accesorios: '))
                otrosGastos = float(input('Otros Gastos: '))
                otrosProductos = float(input('Otros Productos: '))
                prodFinancieros = float(input('Productos Financieros: '))
                reservaLegal = float(input('Reserva Legal: '))
                terryEdificios = float(input('Terreno y edificios: '))
                utilyEjAnteriores = float(input('Utilidades ejercicios anteriores: '))
                ventas = float(input('Ventas: '))
            except:
                print('ERROR: INGRESE UN VALOR MONETARIO')
    #-----------------------------------------------------------------------------------------------
            new_year = {
            'year':[año],
            'acreedores':[acreedores],
            'aportFuturos':[aportFuturos],            
            'capitalSocial':[capitalSocial],
            'costoVentas':[costoVentas],
            'cuentasCobrar':[cuentasCobrar],                        
            'cuentasPagar':[cuentasPagar],
            'desprAcum':[desprAcum],
            'docxPagar':[docxPagar],                        
            'efectivo':[efectivo],
            'eqComputo':[eqComputo],
            'eqTransportes':[eqTransportes],                        
            'gastosAdmin':[gastosAdmon],
            'gastosVentas':[gastosVentas],            
            'gastosFinancieros':[gastosFinancieros],            
            'gastosDepre':[gastosDespr],
            'gastosPreop':[gastosPreop],
            'hipotecasPagarLP':[hipotecasPagarLP],            
            'taxes':[taxes],            
            'inv':[inv],
            'invest':[invest],            
            'maqEquipo':[maqEquipo],
            'mobAccesorios':[mobAccesorios],
            'otrosGastos':[otrosGastos],            
            'otrosProductos':[otrosProductos],
            'prodFinancieros':[prodFinancieros],
            'reservaLegal':[reservaLegal],            
            'terryEdificios':[terryEdificios],
            'utilyEjAnteriores':[utilyEjAnteriores],
            'ventas':[ventas]
                }
            
            new_year_df = pd.DataFrame(new_year)
            cuentas = pd.concat([cuentas, new_year_df], ignore_index=True)
            print(cuentas)
# USANDO DATOS YA GUARDADOS
    elif agregar_datos == 2:
        console = Console()
        break
    #cuentas = {
    #    'acreedores':[65.00],
    #    'aportFuturos':[535.00],
    #    'capitalSocial':[460.00],
    #    'costoVentas':[2610.00],
    #    'cuentasCobrar':[629.00],
    #    'cuentasPagar':[478.00],
    #    'desprAcum':[2291.00],
    #    'docxPagar':[99.00],
    #    'efectivo':[454.00],
    #    'eqComputo':[123.00],
    #    'eqTransportes':[344.00],
    #    'gastosAdmin':[243.00],
    #    'gastosVentas':[125.00],
    #    'gastosFinancieros':[116.00],
    #    'gastosDepre':[299.00],
    #    'gastosPreop':[138.00],
    #    'hipotecasPagarLP':[1279.00],
    #    'taxes':[134.00],
    #    'inv':[361.00],
    #    'invest':[85.00],
    #    'maqEquipo':[1750.00],
    #    'mobAccesorios':[448.00],
    #    'otrosGastos':[44.00],
    #    'otrosProductos':[10.00],
    #    'prodFinancieros':[5.00],
    #    'reservaLegal':[30.00],
    #    'terryEdificios':[2590.00],
    #    'utilyEjAnteriores':[1130.00],
    #    'ventas':[3843.00]
    #}

# Menú
while True:
    main_menu = int(input('\n¿Qué desea ver?\n\t1. Estado de Resultados\n\t2. Balance General\n\t3. Liquidez\n\t4. Actividad\n\t5. Ciclo Conversión de efectivo\n\t6. Razones de Endeudamiento\n\t7. Razones de Rentabilidad\n\t8. Salir\n\tIngrese su opción: '))

    if main_menu == 1:
        year = int(input("Dame el año: \n"))

        # Se hacen los calculos de ER
        utilyBruta = cuentas.at[year,'ventas'] - cuentas.at[year,'costoVentas']
        resIntegral = cuentas.at[year,"gastosFinancieros"] - cuentas.at[year,'prodFinancieros']
        totalGastosOpe = cuentas.at[year,'gastosVentas'] + cuentas.at[year,'gastosAdmin'] + cuentas.at[year,'gastosDepre']
        totalGastosOpe = totalGastosOpe + resIntegral

        utilyOperativa = utilyBruta - totalGastosOpe
        totalOtrosGastos = cuentas.at[year,'otrosGastos'] - cuentas.at[year,'otrosProductos']
        utilyAntesTax = utilyOperativa - totalOtrosGastos
        ISR = utilyAntesTax * 0.30
        PTU = utilyAntesTax * 0.10
        totalTaxPagar = ISR + PTU
        utilyNetaEj = utilyAntesTax - totalTaxPagar

        # SE GUARDAN EN UN DATA FRAME
        new_estado_resultados = {
            'year':[year],
            'utilidadBruta':[utilyBruta],
            'resultadoIntegral':[resIntegral],
            'totalGastosOp':[totalGastosOpe],
            'utilidadOperativa':[utilyOperativa],
            'totalOtrosGastos':[totalOtrosGastos],
            'utilidadAntesTax':[utilyAntesTax],
            'ISR':[ISR],
            'PTU':[PTU],
            'totalTaxesPagar':[totalTaxPagar],
            'utilidadNetaEjercicio':[utilyNetaEj]            
        }

        nw_er_df = pd.DataFrame(new_estado_resultados)
        nw_er_df.set_index('year', inplace=True)
        estado_resultados = pd.concat([estado_resultados, nw_er_df], ignore_index=False)
        #print(estado_resultados)

        t_er = Table(title= f"ESTADO DE RESULTADOS AÑO {year}", show_lines=True)
        t_er.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
        t_er.add_column("1", justify="center", style="red", no_wrap=False)
        t_er.add_column("2", justify="center", style="green", no_wrap=False)
        t_er.add_column("3", justify="center", style="green", no_wrap=False)
        t_er.add_column("4", justify="center", style="green", no_wrap=False)

        t_er.add_row("Ventas", "", "", "", f"${cuentas.at[year,'ventas']}")
        t_er.add_row("Costo de ventas", "", "", "", f"${cuentas.at[year,'costoVentas']}")
        t_er.add_row("", "Utilidad Bruta", "", "", f"${utilyBruta}")

        t_er.add_row("Gastos de Venta", "", "", f"${cuentas.at[year,'gastosVentas']}", "")
        t_er.add_row("Gastos de Administración", "", "", f"${cuentas.at[year,'gastosAdmin']}", "")
        t_er.add_row("Gastos por Despreciación", "", "", f"${cuentas.at[year,'gastosDepre']}", "")
        t_er.add_row("Gastos Financieros", "", f"${cuentas.at[year,'gastosFinancieros']}", "", "")
        t_er.add_row("Productos Financieros", "", f"${cuentas.at[year,'prodFinancieros']}", "", "")
        t_er.add_row("", "Resultado Integral de Financiamiento", "", f"${resIntegral}", "")
        t_er.add_row("", "Total de Gastos Operativos", "", "", f"${totalGastosOpe}")
        t_er.add_row("", "Utilidad Operativa", "", "", f"${utilyOperativa}")

        t_er.add_row("Otros Gastos", "", "", f"${cuentas.at[year,'otrosGastos']}", "")
        t_er.add_row("Otros Productos", "", "", f"${cuentas.at[year,'otrosProductos']}", "")
        t_er.add_row("", "Total de Otros Gastos y Productos", "", "", f"${totalOtrosGastos}")
        t_er.add_row("", "Utilidad antes de impuestos", "", "", f"${utilyAntesTax}")

        t_er.add_row("ISR", "30%", "", f"${ISR}", "")
        t_er.add_row("PTU", "10%", "", f"${PTU}", "")

        t_er.add_row("", "Total de Impuestos por Pagar", "", "", f"${totalTaxPagar}")
        t_er.add_row("", "Utilidad NETA del ejercicio", "", "", f"${utilyNetaEj}")

        console.print(t_er)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 2:
        year = int(input("Dame el año: \n"))
        # Calculos Balance General
        #   Activos             #
        totalAC = cuentas.at[year,'efectivo'] + cuentas.at[year,'cuentasCobrar'] + cuentas.at[year,'invest'] + cuentas.at[year,'inv']
        totalANC = (cuentas.at[year,"terryEdificios"] + cuentas.at[year,'maqEquipo'] + cuentas.at[year,"mobAccesorios"] + cuentas.at[year,'eqComputo'] + cuentas.at[year,'eqTransportes']) - cuentas.at[year,'desprAcum']
        otrosActivos = cuentas.at[year,'gastosPreop']
        totalActivos = totalAC +  totalANC + otrosActivos

        #   Pasivos             #
        nwTaxes = (totalTaxPagar + cuentas.at[year,'taxes'])
        totalPC = cuentas.at[year,'acreedores'] + cuentas.at[year,'cuentasPagar'] + cuentas.at[year,'docxPagar'] + nwTaxes
        totalPasivos = totalPC +  cuentas.at[year,'hipotecasPagarLP']

        #   Capital Contable    #
        totalCap = cuentas.at[year,'capitalSocial'] + cuentas.at[year,'reservaLegal'] + cuentas.at[year,'aportFuturos']
        utilyEjercicio = cuentas.at[year,"utilyEjAnteriores"] + utilyNetaEj
        totalCC = totalCap + utilyEjercicio

        # SE GUARDAN EN UN DATA FRAME
        new_balance_general = {
            'year':[year],
            'totalActivosCirculantes':[totalAC],
            'totalActivosNOcirculantes':[totalANC],
            'otrosActivos':[otrosActivos],
            'totalActivos':[totalActivos],
            'Impuestos':[nwTaxes],
            'totalPasivosCirculantes':[totalPC],
            'totalPasivos':[totalPasivos],
            'totalCapital':[totalCap],
            'utilidadEjercicio':[utilyEjercicio],
            'totalCapitalContable':[totalCC] 
        }

        nw_bg_df = pd.DataFrame(new_balance_general)
        nw_bg_df.set_index('year', inplace=True)
        balance_general = pd.concat([balance_general, nw_bg_df], ignore_index=False)
        #print(balance_general)

        # Generación de Balance General
        t_bg = Table(title=f'BALANCE GENERAL AL {year}', show_lines=True)
        t_bg.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
        t_bg.add_column("1", justify="center", style="red", no_wrap=False)
        t_bg.add_column("2", justify="center", style="green", no_wrap=False)
        t_bg.add_column("3", justify="center", style="green", no_wrap=False)
        t_bg.add_column("4", justify="center", style="green", no_wrap=False)

        t_bg.add_row("Efectivo", "", f"${cuentas.at[year,'efectivo']}", "", "")
        t_bg.add_row("Cuentas por cobrar", "", f"${cuentas.at[year,'cuentasCobrar']}", "", "")
        t_bg.add_row("Inventarios", "", f"${cuentas.at[year,'inv']}", "", "")
        t_bg.add_row("Inversiones", "", f"${cuentas.at[year,'invest']}", "", "")
        t_bg.add_row("", "TOTAL ACTIVOS CIRCULANTES", "", f"${totalAC}", "")

        t_bg.add_row("Terreno y Edificios", "", f"${cuentas.at[year,'terryEdificios']}", "", "")
        t_bg.add_row("Maquinaria y Equipo", "", f"${cuentas.at[year,'maqEquipo']}", "", "")
        t_bg.add_row("Mobiliario y Accesorios", "", f"${cuentas.at[year,'mobAccesorios']}", "", "")
        t_bg.add_row("Equipo de Computo", "", f"${cuentas.at[year,'eqComputo']}", "", "")
        t_bg.add_row("Equipo de Transportes", "", f"${cuentas.at[year,'eqTransportes']}", "", "")
        t_bg.add_row("Despreciación acumulada de Activos Fijos", "", f"${cuentas.at[year,'desprAcum']}", "", "")
        t_bg.add_row("", "TOTAL ACTIVOS NO CIRCULANTES", "", f"${totalANC}", "")

        t_bg.add_row("Gastos Preoperativos", "", f"${cuentas.at[year,'gastosPreop']}", "", "")

        t_bg.add_row("", "TOTAL ACTIVOS", "", "", f"${totalActivos}")

        t_bg.add_row("Acreedores diversos", "", f"${cuentas.at[year,'acreedores']}", "", "")
        t_bg.add_row("Cuentas por Pagar", "", f"${cuentas.at[year,'cuentasPagar']}", "", "")
        t_bg.add_row("Documentos por Pagar", "", f"${cuentas.at[year,'docxPagar']}", "", "")
        t_bg.add_row("Impuestos", "", f"${nwTaxes}", "", "")
        t_bg.add_row("", "TOTAL PASIVOS CORTO PLAZO", "", f"${totalPC}", "")

        t_bg.add_row("Hipotécas por pagar a largo plazo", "", f"${cuentas.at[year,'hipotecasPagarLP']}", "", "")

        t_bg.add_row("", "TOTAL PASIVOS", "", "", f"{totalPasivos}")

        t_bg.add_row("Capital Social", "", f"${cuentas.at[year,'capitalSocial']}", "", "")
        t_bg.add_row("Reserva Legal", "", f"${cuentas.at[year,'reservaLegal']}", "", "")
        t_bg.add_row("Aportaciones para futuros aumentos de capital", "", f"${cuentas.at[year,'aportFuturos']}", "", "")

        t_bg.add_row("", "TOTAL CAPITAL", "", f"{totalCap}", "")

        t_bg.add_row("Utilidades del ejercicio anteriores", "", f"${cuentas.at[year,'utilyEjAnteriores']}", "", "")
        t_bg.add_row("Utilidad del ejercicio", "", f"${utilyNetaEj}", "", "")

        t_bg.add_row("", "TOTAL CAPITAL CONTABLE", "", "", f"${totalCC}")

        console.print(t_bg)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 3:
        year1 = int(input("Dame el primer año a comparar:\n"))
        year2 = int(input("Dame el segundo año a comparar:\n"))

        # LIQUIDEZ
        t_liquidez = Table(title= f"LIQUIDEZ", show_lines=True)
        t_liquidez.add_column("", justify="center", style="red", no_wrap=False)
        t_liquidez.add_column(f"{year1}", justify="center", style="green", no_wrap=False)
        t_liquidez.add_column(f"{year2}", justify="center", style="green", no_wrap=False)

        totalAC_1 = cuentas.at[year1,'efectivo'] + cuentas.at[year1,'cuentasCobrar'] + cuentas.at[year1,'invest'] + cuentas.at[year1,'inv']
        totalAC_2 = cuentas.at[year2,'efectivo'] + cuentas.at[year2,'cuentasCobrar'] + cuentas.at[year2,'invest'] + cuentas.at[year2,'inv']
        
        totalPC_1 = cuentas.at[year1,'acreedores'] + cuentas.at[year1,'cuentasPagar'] + cuentas.at[year1,'docxPagar'] + nwTaxes
        totalPC_2 = cuentas.at[year2,'acreedores'] + cuentas.at[year2,'cuentasPagar'] + cuentas.at[year2,'docxPagar'] + nwTaxes

        liquidez_1 = totalAC_1 / totalPC_1
        liquidez_2 = totalAC_2 / totalPC_2

        prueba_acida_1 = totalAC_1 - cuentas.at[year1, 'inv'] / totalPC_1
        prueba_acida_2 = totalAC_2 - cuentas.at[year2, 'inv'] / totalPC_2

        efectivo_1 = cuentas.at[year1, 'efectivo'] / totalPC_1
        efectivo_2 = cuentas.at[year2, 'efectivo'] / totalPC_2


        t_liquidez.add_row("Liquidez", f"${liquidez_1}", f"${liquidez_2}")
        t_liquidez.add_row("Prueba acida",f"${prueba_acida_1}",f"${prueba_acida_2}")
        t_liquidez.add_row("Efectivo", f"{efectivo_1}", f"${efectivo_2}")

        console.print(t_liquidez)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    
    elif main_menu == 4:
        year1 = int(input("Dame el primer año a comparar:\n"))
        year2 = int(input("Dame el segundo año a comparar:\n"))

        # OPERACIONES DE ACTIVIDAD
        rotacion_inv1 = cuentas.at[year1, 'costoVentas'] / cuentas.at[year1, 'inv']
        rotacion_inv2 = cuentas.at[year2, 'costoVentas'] / cuentas.at[year2, 'inv']

        rotacion_cartera1 = cuentas.at[year1, 'ventas'] / cuentas.at[year1, 'cuentasCobrar']
        rotacion_cartera2 = cuentas.at[year2, 'ventas'] / cuentas.at[year2, 'cuentasCobrar']

        rotacion_pago1 = cuentas.at[year1, 'costoVentas'] / cuentas.at[year1, 'cuentasPagar']
        rotacion_pago2 = cuentas.at[year2, 'costoVentas'] / cuentas.at[year2, 'cuentasPagar']

        totalANC1 = (cuentas.at[year1,"terryEdificios"] + cuentas.at[year1,'maqEquipo'] + cuentas.at[year1,"mobAccesorios"] + cuentas.at[year1,'eqComputo'] + cuentas.at[year1,'eqTransportes']) - cuentas.at[year1,'desprAcum']
        totalANC2 = (cuentas.at[year2,"terryEdificios"] + cuentas.at[year2,'maqEquipo'] + cuentas.at[year2,"mobAccesorios"] + cuentas.at[year2,'eqComputo'] + cuentas.at[year2,'eqTransportes']) - cuentas.at[year2,'desprAcum']

        rotacion_AF1 = cuentas.at[year1, 'ventas'] / totalANC1
        rotacion_AF2 = cuentas.at[year2, 'ventas'] / totalANC2

        totalActivos1 =  cuentas.at[year1,'efectivo'] + cuentas.at[year1,'cuentasCobrar'] + cuentas.at[year1,'invest'] + cuentas.at[year1,'inv']
        totalActivos2 =  cuentas.at[year2,'efectivo'] + cuentas.at[year2,'cuentasCobrar'] + cuentas.at[year2,'invest'] + cuentas.at[year2,'inv']
        
        rotacion_AT1 = cuentas.at[year1, 'ventas'] / totalActivos1
        rotacion_AT2 = cuentas.at[year2, 'ventas'] / totalActivos2

        # CREACION DE ACTIVIDAD
        t_actividad = Table(title= f"ACTIVIDAD", show_lines=True)
        t_actividad.add_column("", justify="center", style="red", no_wrap=False)
        t_actividad.add_column(f"{year1}", justify="center", style="green", no_wrap=False)
        t_actividad.add_column(f"{year2}", justify="center", style="green", no_wrap=False)

        t_actividad.add_row("Rotacion de inventarios", f"${rotacion_inv1}", f"${rotacion_inv2}")
        t_actividad.add_row("Rotacion de cartera", f"${rotacion_cartera1}", f"${rotacion_cartera2}")
        t_actividad.add_row("Rotacion de pago", f"${rotacion_pago1}", f"${rotacion_pago2}")
        t_actividad.add_row("Rotacion de activo fijo", f"${rotacion_AF1}", f"${rotacion_AF2}")
        t_actividad.add_row("Rotacion activos totales", f"${rotacion_AT1}", f"${rotacion_AT2}")

        console.print(t_actividad)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 5:
        year1 = int(input("Dame el primer año a comparar:\n"))
        year2 = int(input("Dame el segundo año a comparar:\n"))

        # CALCULO DE ER DE AMBOS AñOS
        utilyBruta1 = cuentas.at[year1,'ventas'] - cuentas.at[year1,'costoVentas']
        utilyBruta2 = cuentas.at[year2,'ventas'] - cuentas.at[year2,'costoVentas']

        resIntegral1 = cuentas.at[year1,"gastosFinancieros"] - cuentas.at[year1,'prodFinancieros']
        resIntegral2 = cuentas.at[year2,"gastosFinancieros"] - cuentas.at[year2,'prodFinancieros']

        totalGastosOpe1 = cuentas.at[year1,'gastosVentas'] + cuentas.at[year1,'gastosAdmin'] + cuentas.at[year1,'gastosDepre']
        totalGastosOpe2 = cuentas.at[year2,'gastosVentas'] + cuentas.at[year2,'gastosAdmin'] + cuentas.at[year2,'gastosDepre']

        totalGastosOpe1 = totalGastosOpe1 + resIntegral1
        totalGastosOpe2 = totalGastosOpe2 + resIntegral2

        utilyOperativa1 = utilyBruta1 - totalGastosOpe1
        utilyOperativa2 = utilyBruta2 - totalGastosOpe2

        totalOtrosGastos1 = cuentas.at[year1,'otrosGastos'] - cuentas.at[year1,'otrosProductos']
        totalOtrosGastos2 = cuentas.at[year2,'otrosGastos'] - cuentas.at[year2,'otrosProductos']

        utilyAntesTax1 = utilyOperativa1 - totalOtrosGastos1
        utilyAntesTax2 = utilyOperativa2 - totalOtrosGastos2

        ISR1 = utilyAntesTax1 * 0.30
        ISR2 = utilyAntesTax2 * 0.30
        PTU1 = utilyAntesTax1 * 0.10
        PTU2 = utilyAntesTax2 * 0.10

        totalTaxPagar1 = ISR1 + PTU1
        totalTaxPagar2 = ISR2 + PTU2

        utilyNetaEj1 = utilyAntesTax1 - totalTaxPagar1
        utilyNetaEj2 = utilyAntesTax2 - totalTaxPagar2

        # OPERACIONES DE BG DE AMBOS AñOS 
        totalAC = cuentas.at[year,'efectivo'] + cuentas.at[year,'cuentasCobrar'] + cuentas.at[year,'invest'] + cuentas.at[year,'inv']
        
        totalANC = (cuentas.at[year,"terryEdificios"] + cuentas.at[year,'maqEquipo'] + cuentas.at[year,"mobAccesorios"] + cuentas.at[year,'eqComputo'] + cuentas.at[year,'eqTransportes']) - cuentas.at[year,'desprAcum']
        otrosActivos = cuentas.at[year,'gastosPreop']
        totalActivos = totalAC +  totalANC + otrosActivos

        #   Pasivos             #
        nwTaxes = (totalTaxPagar + cuentas.at[year,'taxes'])
        totalPC = cuentas.at[year,'acreedores'] + cuentas.at[year,'cuentasPagar'] + cuentas.at[year,'docxPagar'] + nwTaxes
        totalPasivos = totalPC +  cuentas.at[year,'hipotecasPagarLP']

        #   Capital Contable    #
        totalCap = cuentas.at[year,'capitalSocial'] + cuentas.at[year,'reservaLegal'] + cuentas.at[year,'aportFuturos']
        utilyEjercicio = cuentas.at[year,"utilyEjAnteriores"] + utilyNetaEj
        totalCC = totalCap + utilyEjercicio

        # OPERACIONES DE CICLO DE CONVERSION DE EFECTIVO

        totalPC = cuentas.at[year,'acreedores'] + cuentas.at[year,'cuentasPagar'] + cuentas.at[year,'docxPagar'] + nwTaxes

        totalAC_1 = cuentas.at[year1,'efectivo'] + cuentas.at[year1,'cuentasCobrar'] + cuentas.at[year1,'invest'] + cuentas.at[year1,'inv']
        totalAC_2 = cuentas.at[year2,'efectivo'] + cuentas.at[year2,'cuentasCobrar'] + cuentas.at[year2,'invest'] + cuentas.at[year2,'inv']
        
        totalPC_1 = cuentas.at[year1,'acreedores'] + cuentas.at[year1,'cuentasPagar'] + cuentas.at[year1,'docxPagar'] + nwTaxes
        totalPC_2 = cuentas.at[year2,'acreedores'] + cuentas.at[year2,'cuentasPagar'] + cuentas.at[year2,'docxPagar'] + nwTaxes



    elif main_menu == 6:
        # RAZONES DE ENDEUDAMIENTO #
        year1 = int(input("Dame el primer año a comparar:\n"))
        year2 = int(input("Dame el segundo año a comparar:\n"))

        # CALCULOS #
        razon_endeudamiento1 = (balance_general.at[year1,'totalPasivos'] / balance_general.at[year1,'totalActivos']) * 100
        razon_capital1 = (balance_general.at[year1, 'totalCapitalContable'] / balance_general.at[year1, 'totalActivos']) * 100
        razon_endeu_capital1 = (cuentas.at[year1, 'hipotecasPagarLP'] / balance_general.at[year1, 'totalCapitalContable']) * 100
        cobertura_intereses1 = estado_resultados.at[year1, 'utilidadAntesTax'] / cuentas.at[year1, 'gastosFinancieros']

        razon_endeudamiento2 = (balance_general.at[year2, 'totalPasivos'] / balance_general.at[year2, 'totalActivos']) * 100
        razon_capital2 = (balance_general.at[year2, 'totalCapitalContable'] / balance_general.at[year2, 'totalActivos']) * 100
        razon_endeu_capital2 = (cuentas.at[year2, 'hipotecasPagarLP'] / balance_general.at[year2, 'totalCapitalContable']) * 100
        cobertura_intereses2 = estado_resultados.at[year2, 'utilidadAntesTax'] / cuentas.at[year2, 'gastosFinancieros']

        # CREACIÓN DE TABLA
        t_razEnd = Table(title= 'RAZONES DE ENDEUDAMIENTO', show_lines=True)
        t_razEnd.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
        t_razEnd.add_column(f"{year1}", justify="center", style="yellow", no_wrap=False)
        t_razEnd.add_column(f"{year2}", justify="center", style="yellow", no_wrap=False)

        t_razEnd.add_row("Razon de Endeudamiento", f"{razon_endeudamiento1:.2f}%", f"{razon_endeudamiento2:.2f}%")
        t_razEnd.add_row("Razon de capital", f"{razon_capital1:.2f}%", f"{razon_capital2:.2f}%")
        t_razEnd.add_row("Razon de endeudamiento sobre capital", f"{razon_endeu_capital1:.2f}%", f"{razon_endeu_capital2:.2f}%")
        t_razEnd.add_row("Cobertura de intereses", f"{cobertura_intereses1:.2f}", f"{cobertura_intereses2:.2f}")

        console.print(t_razEnd)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break
    elif main_menu == 7:
        # RAZONES DE RENTABILIDAD
        year1 = int(input("Dame el primer año a comparar:\n"))
        year2 = int(input("Dame el segundo año a comparar:\n"))

        # OPERACIONES DE RENTABILIDAD
        
        margenUtility_y1 = (estado_resultados.at[year1, 'utilyNetaEj'] / cuentas.at[year1, 'ventas']) * 100
        margenUtility_y2 = (estado_resultados.at[year2, 'utilyNetaEj'] / cuentas.at[year2, 'ventas']) * 100
        
        margenUtilityBruta_y1 = (estado_resultados.at[year1, 'utilyBruta'] / cuentas.at[year1, 'ventas']) * 100
        margenUtilityBruta_y2 = (estado_resultados.at[year2, 'utilyBruta'] / cuentas.at[year2, 'ventas']) * 100
        
        margenUtilityOp_y1 = (estado_resultados.at[year1, 'utilyOperativa'] / cuentas.at[year1, 'ventas']) * 100
        margenUtilityOp_y2 = (estado_resultados.at[year2, 'utilyOperativa'] / cuentas.at[year2, 'ventas']) * 100
        
        RAT_y1 = (estado_resultados.at[year1, 'utilyNetaEj'] / balance_general.at[year1, 'totalActivos']) * 100
        RAT_y2 = (estado_resultados.at[year2, 'utilyNetaEj'] / balance_general.at[year2, 'totalActivos']) * 100
        
        ROE_y1 = (estado_resultados.at[year1, 'utilyNetaEj'] / balance_general.at[year1, 'totalCap']) * 100
        ROE_y2 = (estado_resultados.at[year2, 'utilyNetaEj'] / balance_general.at[year2, 'totalCap']) * 100
        
        RCC_y1 = (estado_resultados.at[year1, 'utilyNetaEj'] / cuentas.at[year1, 'capitalSocial']) * 100
        RCC_y2 = (estado_resultados.at[year2, 'utilyNetaEj'] / cuentas.at[year2, 'capitalSocial']) * 100

        # CREACIÓN DE TABLA

        t_razRent = Table(title= 'RAZONES DE RENTABILIDAD', show_lines=True)
        t_razRent.add_column("CONCEPTO", justify="center", style="cyan", no_wrap=False)
        t_razRent.add_column(f"{year1}", justify="center", style="yellow", no_wrap=False)
        t_razRent.add_column(f"{year2}", justify="center", style="yellow", no_wrap=False)

        t_razRent.add_row("Margen de Utilidad", f"{margenUtility_y1:.2f}%", f"{margenUtility_y2:.2f}%")
        t_razRent.add_row("Margen de Utilidad Bruta", f"{margenUtilityBruta_y1:.2f}%", f"{margenUtilityBruta_y2:.2f}%")
        t_razRent.add_row("Margen de Utilidad Operativa", f"{margenUtilityOp_y1:.2f}%", f"{margenUtilityOp_y2:.2f}%")
        t_razRent.add_row("Rendimiento sobre los Activos Totales", f"{RAT_y1:.2f}", f"{RAT_y2:.2f}")
        t_razRent.add_row("Rendimiento sobre el Patrimonio", f"{ROE_y1:.2f}", f"{ROE_y2:.2f}")
        t_razRent.add_row("Rendimiento sobre el Capital Comun", f"{RCC_y1:.2f}", f"{RCC_y2:.2f}")

        console.print(t_razRent)

        sub_op = input('\nEscribir "m" para mostrar el menú nuevamente, presionar enter para salir del programa ').lower()

        if sub_op == "m":
            continue
        elif sub_op == "":
            print('\n\t\tSaliendo . . . . .')
            break

    elif main_menu == 8:
        break
    
