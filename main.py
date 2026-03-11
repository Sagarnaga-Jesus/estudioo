import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"
    page.scroll = "auto"
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20

    page.add(ft.Row(ft.Text("Registro de Participantes", size=30, weight=ft.FontWeight.BOLD), alignment=ft.MainAxisAlignment.CENTER))

    nombre = ft.TextField(label="Nombre Completo")
    correo = ft.TextField(label="Correo Electronico")

    taller = ft.Dropdown(
        label="Taller de interes",
        options=[
            ft.dropdown.Option("Python para principiantes"),
            ft.dropdown.Option("Python para intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )

    pago = ft.RadioGroup(
        value="Pago completo",
        content=ft.Column([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ])
    )

    requiere = ft.Checkbox(label="Requiere computadora portátil")

    nivel = ft.Slider(label="{value}",value=1, min=0, max=5, divisions=5, width=400., active_color="red")
    
    texto = ft.Text(size=16,color=ft.Colors.BLUE_900)
    
    def resume():
        requiere_text = "Sí" if requiere.value else "No"
        texto.value = f"--- FICHA DEL PARTICIPANTE ---\n Nombre: {nombre.value}\n Email: {correo.value}\n Taller: {taller.value}\n Modalidad de pago: {pago.value}\n Requiere Portatil: {requiere_text}\n Nivel: {int(nivel.value)}\n --- Gracias por su registro --- "
        nombre.value = ""
        correo.value = ""
        requiere.value = False
        page.update()

    boton = ft.ElevatedButton("Mostrar ficha del Participante", on_click=resume, bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE)

    texto.on_change= resume
    
    page.add(ft.Column([
            nombre, 
            correo, 
            taller, 
            ft.Text("Modalidad de pago"),
            pago, 
            requiere, 
            nivel,
            ft.Row(boton, alignment=ft.MainAxisAlignment.CENTER)]
            , spacing=15))
    
    page.add(texto)

ft.run(main)
