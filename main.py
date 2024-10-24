import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# FUNÇÃO QUE CALCULA O CUSTO COM FATOR EXTERNO 'A'
def custo(x, a=0):
    return 300 + 10 * x**2 + a * x

# FUNÇÃO QUE CALCULA A RECEITA
def receita(x):
    return 90 * x

# FUNÇÃO QUE CALCULA O LUCRO (RECEITA - CUSTO)
def lucro(x, a=0):
    return receita(x) - custo(x, a)

# INTEGRAL DA RECEITA (RECEITA ACUMULADA)
def receita_acumulada(x):
    return 45 * x**2

# INTEGRAL DO CUSTO (CUSTO ACUMULADO)
def custo_acumulado(x, a=0):
    return (10 * x**3) / 3 + 300 * x + (a * x**2) / 2

# CRIANDO VALORES DE UNIDADES PRODUZIDAS (DE 0 A 10)
x = np.linspace(0, 10, 100)

# FATOR EXTERNO 'A' (IMPOSTO/VARIAÇÃO)
a = 5

# CALCULANDO VALORES DE CUSTO, RECEITA, LUCRO, E SUAS VERSÕES ACUMULADAS
custo_values = custo(x, a)
receita_values = receita(x)
lucro_values = lucro(x, a)
receita_acum_values = receita_acumulada(x)
custo_acum_values = custo_acumulado(x, a)

# DEFININDO O ESTILO DO GRÁFICO
sns.set(style="whitegrid")

# CRIANDO O GRÁFICO
plt.figure(figsize=(10, 6))

# PLOTANDO CUSTO, RECEITA E LUCRO
plt.plot(x, custo_values, label="Custo", color="red")
plt.plot(x, receita_values, label="Receita", color="green")
plt.plot(x, lucro_values, label="Lucro", color="blue")

# PLOTANDO CUSTO ACUMULADO E RECEITA ACUMULADA (LINHAS TRACEJADAS)
plt.plot(x, receita_acum_values, label="Receita Acumulada", color="green", linestyle="--")
plt.plot(x, custo_acum_values, label="Custo Acumulado", color="red", linestyle="--")

# ADICIONANDO TÍTULO E RÓTULOS AO GRÁFICO
plt.title('Evolução do Custo, Receita e Lucro com Fatores Externos')
plt.xlabel('Unidades Produzidas (x)')
plt.ylabel('Valor')

# EXIBINDO A LEGENDA
plt.legend()

# EXIBINDO O GRÁFICO
plt.show()
