import random

class JogoMarte:
    def __init__(self):
        self.dia = 1
        self.max_dias = 15
        self.jogadores = [{"nome": "Astronauta 1", "vida": 3, "oxigenio": 3, "agua": 3, "comida": 3, "energia": 2}]
        self.eventos = [
            "Tempestade de poeira! Todos gastam +1 Energia.",
            "Falha no traje! Perde 1 Oxigênio.",
            "Descobriu gelo subterrâneo! Ganha +2 Água.",
            "Equipamento com defeito! Precisa gastar 1 Energia para reparar.",
            "Dia tranquilo em Marte."
        ]

    def mostrar_status(self):
        print(f"\n🌌 Dia {self.dia} em Marte")
        for j in self.jogadores:
            print(f"{j['nome']}: ❤️{j['vida']} | O₂ {j['oxigenio']} | 💧 {j['agua']} | 🍞 {j['comida']} | 🔋 {j['energia']}")

    def evento(self):
        evento = random.choice(self.eventos)
        print(f"\n📢 Evento: {evento}")
        for j in self.jogadores:
            if "Energia" in evento:
                j["energia"] -= 1
            if "Oxigênio" in evento:
                j["oxigenio"] -= 1
            if "Água" in evento:
                j["agua"] += 2

    def acoes(self, jogador):
        print("\nEscolha sua ação:")
        print("1 - Explorar (chance de ganhar recurso)")
        print("2 - Descansar (+1 Energia)")
        print("3 - Construir (gasta 1 de cada recurso, mas prepara resgate)")
        escolha = input("👉 Sua escolha: ")

        if escolha == "1":
            if random.randint(1,6) >= 4:
                recurso = random.choice(["oxigenio", "agua", "comida", "energia"])
                jogador[recurso] += 1
                print(f"✨ Você encontrou +1 {recurso.capitalize()}!")
            else:
                print("Nada encontrado na exploração...")
        elif escolha == "2":
            jogador["energia"] += 1
            print("Você descansou e ganhou +1 Energia.")
        elif escolha == "3":
            if jogador["oxigenio"] > 0 and jogador["agua"] > 0 and jogador["comida"] > 0 and jogador["energia"] > 0:
                jogador["oxigenio"] -= 1
                jogador["agua"] -= 1
                jogador["comida"] -= 1
                jogador["energia"] -= 1
                print("Você ajudou a montar a Antena de Resgate!")
            else:
                print("❌ Recursos insuficientes para construir!")

    def consumo(self, jogador):
        jogador["oxigenio"] -= 1
        jogador["agua"] -= 1
        jogador["comida"] -= 1

        if jogador["oxigenio"] < 0 or jogador["agua"] < 0 or jogador["comida"] < 0:
            jogador["vida"] -= 1
            print(f"⚠️ {jogador['nome']} perdeu 1 ponto de vida por falta de recursos!")

    def jogar(self):
        while self.dia <= self.max_dias and any(j["vida"] > 0 for j in self.jogadores):
            self.mostrar_status()
            self.evento()
            for j in self.jogadores:
                if j["vida"] > 0:
                    self.acoes(j)
                    self.consumo(j)
            self.dia += 1

        print("\n🏁 Fim do jogo!")
        if any(j["vida"] > 0 for j in self.jogadores):
            print("🎉 Você sobreviveu em Marte!")
        else:
            print("💀 Todos morreram...")

# Rodar o jogo
jogo = JogoMarte()
jogo.jogar()