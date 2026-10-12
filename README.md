# Simulação de Tomada de Decisão

Este projeto é um programa em Python que simula a análise de notas de um aluno e define sua situação escolar com base na média final.

## Funcionalidade

O programa solicita:

- Nome do aluno
- Primeira nota
- Segunda nota
- Confirmação se deseja gerar o relatório

Em seguida, calcula a média e classifica o aluno em uma das opções abaixo:

- Média >= 7: Aprovado
- Média >= 5: Recuperação
- Média < 5: Reprovado

## Como executar

1. Abra o terminal.
2. Acesse a pasta do projeto.
3. Execute o comando:

```bash
python app.py
```

## Exemplo de uso

```text
Digite o nome do aluno: Maria
Digite a primeira nota: 8
Digite a segunda nota: 6
Deseja gerar o relatório? (s/n): s
```

Saída esperada:

```text
Relatório de Notas
------------------
Aluno: Maria
Nota 1: 8.0
Nota 2: 6.0
Média: 7.0
Situação: Aprovado
```

## Observação

O programa é de console e usa entrada via teclado, com saída impressa no terminal.
