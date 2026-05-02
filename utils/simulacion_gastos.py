import random as rm
from datetime import datetime, timedelta
from enum import Enum

def simular_gastos(num_gastos):
    gastos = []
    
    lista_descripciones = [
        "Compra de ingredientes para menú del día",
        "Pago de servicio de energía eléctrica local",
        "Reparación de tubería en área de cocina",
        "Compra de set de cuchillos profesionales",
        "Insumos de limpieza para mesas y pisos",
        "Pago de suscripción software de inventarios",
        "Reposición de vajilla de porcelana",
        "Mantenimiento preventivo de horno industrial",
        "Compra de uniformes para personal de servicio",
        "Publicidad en redes sociales para evento especial"
    ]
    fecha_inicial = datetime(2020,1,1)
    lista_imagenes = [
        "imagen_1",
        "imagen_2",
        "imagen_3",
        "imagen_4",
        "imagen_5"
    ]
    class Moneda(Enum):
        PESOS = "Pesos",
        USD = "USD",
        EURO = "Euro"
    class MetodoPago(Enum):
        EFECTIVO ="Efectivo",
        CUENTA = "Cuenta"
    lista_lugar = [
        "Restaurante El Sabor",
        "Estación de Servicio Central",
        "Supermercado La Despensa",
        "Papelería El Escribano",
        "Ferretería Maestra",
        "Tienda de Tecnología TechWorld",
        "Cafetería Granos de Oro",
        "Transportes Urbanos S.A.",
        "Limpieza y Aseo BrillaTodo",
        "Mantenimiento Industrial Expertos"
    ]
    class TipoGasto(Enum):
        ALIMENTACION = "Alimentación y Bebidas"
        TRANSPORTE = "Transporte y Movilidad"
        SUMINISTROS = "Suministros de Oficina"
        LIMPIEZA = "Servicios de Limpieza"
        MANTENIMIENTO = "Mantenimiento y Reparaciones"
        TECNOLOGIA = "Equipos y Software"
        PUBLICIDAD = "Marketing y Publicidad"
        OTROS = "Gastos Varios"
    lista_observaciones = [
        "Bien",
        "Mal"
    ]
    for _ in range(num_gastos):
        
        fecha_simulada = fecha_inicial + timedelta(days=rm.randint(0, 365))
        
        gasto = {
            "id": rm.randint(0, 5000),
            "descripcion": rm.choice(lista_descripciones),
            "fecha": fecha_simulada.strftime("%Y/%m/%d"),
            "monto": rm.random(),
            "imagen": rm.choice(lista_imagenes),
            "moneda": rm.choice(list(Moneda)),
            "metodo_pago": rm.choice(list(MetodoPago)),
            "lugar": rm.choice(lista_lugar),
            "es_recurrente": rm.choice([True, False]),
            "tipo_gasto": rm.choice(list(TipoGasto)),
            "impacto_financiero": rm.randint(0, 10),
            "activo": rm.choice([True, False]),
            "observaciones": rm.choice(lista_observaciones)
        }
        gastos.append(gasto)
        return gastos