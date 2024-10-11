import asyncio
import random

async def tarefa(nome):
    tempo_execucao = random.randint(1, 3) 
    print(f"Tarefa {nome} começando e vai levar {tempo_execucao} segundos.")
    await asyncio.sleep(tempo_execucao) 
    print(f"Tarefa {nome} concluída após {tempo_execucao} segundos.")

async def main():
    tarefas = [tarefa(f"Tarefa {i}") for i in range(1, 4)]

    await asyncio.gather(*tarefas)

asyncio.run(main())
