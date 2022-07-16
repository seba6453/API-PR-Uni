import pandas as pd
import numpy as np
import psycopg2 as pg
from io import StringIO


def crearDF(datos):
    TESTDATA = StringIO(datos)
    df_data = pd.read_csv(TESTDATA,sep=",")
    return df_data

def formatFecha(tupla):
    fecha = tupla["Fecha"]
    fecha = fecha.split("-")
    fecha = fecha[::-1]
    tupla["Fecha"] = str(fecha[0]) + "-" + str(fecha[1]) + "-" + str(fecha[2])
    return tupla

def ingresarMov(tupla,cuentaCliente):
    conn = pg.connect(database = "railway", user = "postgres", password = "hXQeCzfmkafLoQhKhjMy", host = "containers-us-west-69.railway.app", port = "5510")
    cur = conn.cursor()
    cur.execute("INSERT INTO public.movimientobancario (idcuenta,numerocartola,fechamovimiento,descripcion,cargo,abono) VALUES ({},{},'{}','{}',{},{});".format(cuentaCliente[0],1,tupla["Fecha"],tupla["Descripcion"],tupla["Giro"],tupla["Abono"]))
    conn.commit()
    conn.close()
    return tupla

def cargaScotiabank(rut,datos,nroCuenta):
    try:
        conn = pg.connect(database = "railway", user = "postgres", password = "hXQeCzfmkafLoQhKhjMy", host = "containers-us-west-69.railway.app", port = "5510")
        cur = conn.cursor()


        cur.execute("select * from cuenta as cu where cu.rutCliente = '%s' and cu.nombreBanco = 'Scotiabank' and cu.numeroCuenta = %i"%(rut,nroCuenta))
        cuentaCliente = cur.fetchall()

        conn.commit()
        conn.close()

        transacciones = crearDF(datos)

        transacciones = transacciones.replace(to_replace=np.nan, value=0)

        transacciones = transacciones.apply(formatFecha,axis=1)

        transacciones = transacciones.apply(ingresarMov,axis=1,args=(cuentaCliente))
        return True
    except:
        return False