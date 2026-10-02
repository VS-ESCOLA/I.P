import secrets
import string

class GeradorSenhas:
    def __init__(self, tamanho, incluir_numeros, incluir_simbolos):
        self.tamanho = tamanho
        self.incluir_numeros = incluir_numeros
        self.incluir_simbolos = incluir_simbolos

        self.caracteres = string.ascii_letters

        if self.incluir_numeros:
            self.caracteres += string.digits
        if self.incluir_simbolos:
            self.caracteres += string.punctuation
        
    def gerar(self):
        senha = "".join(secrets.choice(self.caracteres) for _ in range(self.tamanho))
        return senha

print('=== GERADOR DE SENHAS ===')
tamanho_input= int(input('Qual o tamanho da senha que você deseja? '))
numeros_input = input('Deseja incluir números? (s/n): ').strip().lower() == 's'
simbolos_input = input('Deseja incluir símbolos? (s/n): ').strip().lower() == 's'

meu_gerador = GeradorSenhas(tamanho_input, numeros_input, simbolos_input)
senha_criada = meu_gerador.gerar()

print(f"\nSua nova senha é: {senha_criada}")    