import tkinter as tk
from tkinter import messagebox

# ---- Ventana de introducción ----
def iniciar_encuesta():
    intro.destroy()  # Cierra la ventana de introducción
    crear_ventana_encuesta()

# ---- Ventana principal de encuesta ----
def crear_ventana_encuesta():
    global ventana, pregunta_label, seleccion, indice, respuestas

    respuestas = []
    indice = 0

    ventana = tk.Tk()
    ventana.title("Encuesta de Seguridad en Redes Sociales")
    ventana.geometry("700x400")
    ventana.configure(bg="#E8F0FE")  # Fondo azul claro

    # Título
    titulo = tk.Label(
        ventana,
        text="Encuesta de Seguridad en Redes Sociales",
        font=("Arial", 18, "bold"),
        bg="#E8F0FE",
        fg="#1A237E"
    )
    titulo.pack(pady=20)

    # Pregunta actual
    pregunta_label = tk.Label(
        ventana,
        text=preguntas[indice],
        font=("Arial", 13),
        wraplength=650,
        bg="#E8F0FE",
        fg="#000000"
    )
    pregunta_label.pack(pady=15)

    # Variable seleccionada
    seleccion = tk.StringVar(value="")

    # Opciones de respuesta
    opciones = ["Siempre", "Casi siempre", "A veces", "Pocas veces", "Nunca"]

    for op in opciones:
        tk.Radiobutton(
            ventana,
            text=op,
            variable=seleccion,
            value=op,
            font=("Arial", 12),
            bg="#E8F0FE",
            activebackground="#C5CAE9"
        ).pack(anchor="w", padx=40)

    # Botón siguiente
    boton_sig = tk.Button(
        ventana,
        text="Siguiente",
        command=siguiente,
        font=("Arial", 12, "bold"),
        bg="#3949AB",
        fg="white",
        activebackground="#1A237E",
        width=12
    )
    boton_sig.pack(pady=25)

    ventana.mainloop()


# ---- Botón SIGUIENTE ----
def siguiente():
    global indice

    opcion = seleccion.get()

    if opcion == "":
        messagebox.showwarning("Advertencia", "Debes seleccionar una respuesta.")
        return

    respuestas.append(valores[opcion])
    seleccion.set("")

    indice += 1

    if indice < len(preguntas):
        pregunta_label.config(text=preguntas[indice])
    else:
        calcular_resultado()


# ---- CALCULAR RESULTADO ----
def calcular_resultado():
    promedio = sum(respuestas) / len(respuestas)

    if promedio >= 4.5:
        nivel = "MUY ALTO"
    elif promedio >= 3.5:
        nivel = "ALTO"
    elif promedio >= 2.5:
        nivel = "MEDIO"
    elif promedio >= 1.5:
        nivel = "BAJO"
    else:
        nivel = "MUY BAJO"

    messagebox.showinfo(
        "Resultado Final",
        f"Tu nivel de seguridad es: {promedio:.2f}\n\nNivel de Seguridad: {nivel}"
    )

    ventana.destroy()


# ---- LISTA DE PREGUNTAS ----
preguntas = [
    "1. ¿Con qué frecuencia utilizas contraseñas fuertes y únicas?",
    "2. ¿Con qué frecuencia usas la Autenticación de Dos Factores (2FA)?",
    "3. ¿Con qué frecuencia cierras sesión en dispositivos compartidos?",
    "4. ¿Con qué frecuencia revisas la configuración de privacidad?",
    "5. ¿Con qué frecuencia revisas aplicaciones de terceros conectadas?",
    "6. ¿Con qué frecuencia revisas tu lista de amigos o seguidores?",
    "7. ¿Con qué frecuencia rechazas solicitudes sospechosas?",
    "8. ¿Con qué frecuencia evitas clics en concursos o regalos falsos?",
    "9. ¿Con qué frecuencia evitas publicar tu ubicación en tiempo real?",
    "10. ¿Con qué frecuencia evitas enviar información personal por DM?"
]

# ---- Valores asignados ----
valores = {
    "Siempre": 5,
    "Casi siempre": 4,
    "A veces": 3,
    "Pocas veces": 2,
    "Nunca": 1
}

# ---- Ventana de INTRODUCCIÓN ----
intro = tk.Tk()
intro.title("Bienvenido a la Encuesta")
intro.geometry("650x350")
intro.configure(bg="#E3F2FD")

titulo_intro = tk.Label(
    intro,
    text="Bienvenido a la Encuesta de Seguridad en Redes Sociales",
    font=("Arial", 18, "bold"),
    bg="#E3F2FD",
    fg="#0D47A1",
    wraplength=600
)
titulo_intro.pack(pady=20)

texto_intro = tk.Label(
    intro,
    text=(
        "Esta encuesta tiene como objetivo evaluar tus hábitos de seguridad al usar redes "
        "sociales. Tu participación es importante y tus respuestas se manejarán de manera confidencial.\n\n"
        "Cuando estés listo, haz clic en el botón 'Iniciar Encuesta'."
    ),
    font=("Arial", 13),
    bg="#E3F2FD",
    fg="#000000",
    wraplength=600
)
texto_intro.pack(pady=20)

boton_iniciar = tk.Button(
    intro,
    text="Iniciar Encuesta",
    command=iniciar_encuesta,
    font=("Arial", 14, "bold"),
    bg="#1565C0",
    fg="white",
    activebackground="#0D47A1",
    width=15
)
boton_iniciar.pack(pady=20)

intro.mainloop()

