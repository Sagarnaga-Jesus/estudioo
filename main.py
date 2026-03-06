import flet as ft

def main(page: ft.Page):

    page.add(ft.Text("Registro de Participantes", size=30))

    nombre = ft.TextField(label="Nombre Completo")
    correo = ft.TextField(label="Correo Electronico")

    taller = ft.Dropdown(
        options=[
            ft.dropdown.Option("Python para principiantes"),
            ft.dropdown.Option("Python para intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )

    pago = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Tarjeta", label="Tarjeta"),
            ft.Radio(value="Efectivo", label="Efectivo"),
        ])
    )

    requiere = ft.Checkbox(label="Requiere computadora portátil")

    nivel = ft.Slider(label="{value}", value=1, min=1, max=5, divisions=4, width=400)

    def resume(e):
        page.add(
            ft.Text(
                f"""--- FICHA DEL PARTICIPANTE ---
Nombre: {nombre.value}
Email: {correo.value}
Taller: {taller.value}
Pago: {pago.value}
Requiere Portatil: {requiere.value}
Nivel: {nivel.value}
--- Gracias por su registro ---
"""
            )
        )
        page.update()

    boton = ft.ElevatedButton("Registrar", on_click=resume)

    page.add(nombre, correo, taller, pago, requiere, nivel, boton)

ft.run(main)
