import tkinter as tk

def calcular_imc():
    try:
        # entrada de dados do usuário
        nome = entry_nome.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # calcula IMC
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Você está abaixo do peso!"
        elif imc >= 18.5 and imc < 24.9:
            classificacao = "Seu peso está normal!"
        elif imc >= 25 and imc < 29.9:
            classificacao = "Você está acima do peso!"
        else:
            classificacao = "Você tem obesidade!"

        Label_resultado.config(text=f"{nome}, seu IMC é {imc:.2f}\n{classificacao}")

    except ValueError:
        Label_resultado.config(text="Erro: Digite números válidos!")

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x250")

tk.Label(janela, text="Digite seu nome: ").pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Peso (kg):").pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack()

tk.Label(janela, text="altura (m): ").pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack()

tk.Button(janela, text="Calcular", command=calcular_imc).pack(pady=10)

Label_resultado = tk.Label(janela, text="Resultado: ")
Label_resultado.pack(pady=10)

janela.mainloop()