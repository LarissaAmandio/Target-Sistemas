INDICE = 13
SOMA = 0
K = 0

# Enquanto K < INDICE
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

# Imprimir(SOMA)
print(SOMA)



----------------------------------------------------------------------------------



# Função para calcular a sequência de Fibonacci até um número máximo
def fibonacci(n):
    fib = [0, 1]  # A sequência começa com 0 e 1
    while fib[-1] < n:  # Enquanto o último número da sequência for menor que n
        fib.append(fib[-1] + fib[-2])  # Adiciona a soma dos dois últimos números
    return fib

# Entrada do usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Calcular a sequência de Fibonacci até o número informado
fib_sequence = fibonacci(numero)

# Verificar se o número pertence à sequência
if numero in fib_sequence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")




---------------------------------------------------------------------------------



import json

# Dados de faturamento diário (simulando como um JSON)
dados_faturamento_json = '''
{
  "faturamento": [67836.43, 0, 0, 34567.78, 40000.0, 0, 0, 0, 35678.9, 0, 43210.0, 0, 28765.5, 35678.9, 30000.0, 0, 0, 20000.0, 19999.0]
}
'''

# Carregar os dados do JSON
dados_faturamento = json.loads(dados_faturamento_json)

# Extrair o vetor de faturamento diário
faturamentos = dados_faturamento['faturamento']

# Filtrar os dias com faturamento (ignorando os dias com 0)
faturamentos_validos = [f for f in faturamentos if f > 0]

# 1. Menor valor de faturamento
menor_faturamento = min(faturamentos_validos)

# 2. Maior valor de faturamento
maior_faturamento = max(faturamentos_validos)

# 3. Cálculo da média mensal (ignorando os dias sem faturamento)
media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

# 4. Número de dias com faturamento superior à média
dias_acima_media = len([f for f in faturamentos_validos if f > media_mensal])

# Exibir os resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")





-------------------------------------------------------------------------------------------




# Dados de faturamento por estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento_estado.values())

# Cálculo do percentual de cada estado
for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")





------------------------------------------------------------------------------



# Entrada de string (pode ser inserida pelo usuário ou definida no código)
string = input("Informe uma string para inverter: ")

# Inversão da string (sem usar funções prontas)
string_invertida = ''
for char in string:
    string_invertida = char + string_invertida  # Coloca o caractere no início da nova string

# Exibir a string invertida
print("String invertida:", string_invertida)
