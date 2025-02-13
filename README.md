# Jogo da Velha em Python

## Descrição

Este repositório contém a implementação do jogo da velha em Python. O jogo é jogado em um tabuleiro 3x3 e alterna entre dois jogadores, 'X' e 'O', até que haja um vencedor ou o jogo termine em empate.

## Funcionalidade da Aplicação
- O jogo é executado com jogadas predefinidas, sem a necessidade de interação do usuário.
- O tabuleiro é impresso no console a cada jogada.
- A verificação do vencedor é realizada após cada jogada.
- O jogo termina quando um jogador vence ou quando o tabuleiro está cheio (empate).

## Como Executar
1. Clone este repositório.
2. Instale o `pytest` se necessário:
   ```bash
   pip install pytest
   ```
3. Execute os testes:
   ```bash
   pytest
   ```

## Testes
A aplicação possui os seguintes testes automatizados utilizando o `pytest`:
- Teste de atualização de casas no tabuleiro.
- Teste de verificação de vencedor (linhas, colunas, diagonais).
- Teste de empate.
- Teste de execução completa do jogo com jogadas predefinidas.

## Dependências
- Python 3.x
- pytest (para rodar os testes)

## Como Contribuir
Se você quiser contribuir, faça um fork deste repositório, crie uma branch com sua melhoria ou correção e envie um pull request.

#### Instruções de execução com `pytest`:
Os testes devem ser executados com o comando:

```bash
pytest
```

Isso vai rodar os testes definidos no arquivo `test_jogo_da_velha.py` e exibir os resultados.
