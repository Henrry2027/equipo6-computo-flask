from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("registro_equipo.html", errores=[], datos={}, registro=None)


@app.route("/registro-equipo", methods=["GET", "POST"])
def registro_equipo():
    errores = []
    datos = {}
    registro = None

    if request.method == "POST":
        codigo_inventario = request.form.get("codigo_inventario", "").strip()
        tipo_equipo = request.form.get("tipo_equipo", "").strip()
        marca_modelo = request.form.get("marca_modelo", "").strip()
        numero_serie = request.form.get("numero_serie", "").strip()
        area_asignada = request.form.get("area_asignada", "").strip()
        responsable = request.form.get("responsable", "").strip()
        estado = request.form.get("estado", "").strip()

        datos = {
            "codigo_inventario": codigo_inventario,
            "tipo_equipo": tipo_equipo,
            "marca_modelo": marca_modelo,
            "numero_serie": numero_serie,
            "area_asignada": area_asignada,
            "responsable": responsable,
            "estado": estado,
        }

        if not codigo_inventario or len(codigo_inventario) < 4:
            errores.append("El código de inventario es obligatorio y debe tener al menos 4 caracteres.")
        if not tipo_equipo:
            errores.append("Debes seleccionar el tipo de equipo.")
        if not marca_modelo:
            errores.append("La marca y el modelo son obligatorios.")
        if not numero_serie or len(numero_serie) < 5:
            errores.append("El número de serie es obligatorio y debe tener al menos 5 caracteres.")
        if not area_asignada:
            errores.append("El área o laboratorio asignado es obligatorio.")
        if not responsable:
            errores.append("El nombre del responsable es obligatorio.")
        if estado not in ["Activo", "En mantenimiento", "Resguardo"]:
            errores.append("Selecciona un estado válido para el equipo.")

        if not errores:
            registro = datos

    return render_template(
        "registro_equipo.html",
        errores=errores,
        datos=datos,
        registro=registro,
    )


@app.route("/reporte-falla", methods=["GET", "POST"])
def reporte_falla():
    errores = []
    datos = {}
    reporte = None

    if request.method == "POST":
        codigo_equipo = request.form.get("codigo_equipo", "").strip()
        reportado_por = request.form.get("reportado_por", "").strip()
        categoria_falla = request.form.get("categoria_falla", "").strip()
        prioridad = request.form.get("prioridad", "").strip()
        bloquea_trabajo = request.form.get("bloquea_trabajo", "no").strip()
        descripcion = request.form.get("descripcion", "").strip()

        datos = {
            "codigo_equipo": codigo_equipo,
            "reportado_por": reportado_por,
            "categoria_falla": categoria_falla,
            "prioridad": prioridad,
            "bloquea_trabajo": bloquea_trabajo,
            "descripcion": descripcion,
        }

        if not codigo_equipo:
            errores.append("El código o identificador del equipo es obligatorio.")
        if not reportado_por:
            errores.append("Indica quién reporta la falla.")
        if not categoria_falla:
            errores.append("Selecciona la categoría de la falla.")
        if prioridad not in ["Baja", "Media", "Alta", "Crítica"]:
            errores.append("Selecciona una prioridad válida.")
        if not descripcion or len(descripcion) < 10:
            errores.append("Describe la falla con al menos 10 caracteres.")

        if not errores:
            reporte = datos

    return render_template(
        "reporte_falla.html",
        errores=errores,
        datos=datos,
        reporte=reporte,
    )


if __name__ == "__main__":
    app.run(debug=True)