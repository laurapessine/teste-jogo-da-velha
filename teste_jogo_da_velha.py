class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
        self.rodada = 0
        self.alguem_ganhou = False

    def atualiza_casa(self, linha: int, coluna: int, jogador: str) -> bool:
        """Atualiza uma casa do tabuleiro se estiver disponível."""
        if 0 <= linha <= 2 and 0 <= coluna <= 2 and self.tabuleiro[linha][coluna] == '':
            self.tabuleiro[linha][coluna] = jogador
            return True
        return False

    def verifica_ganhador(self):
        """Verifica se há um vencedor ou se o jogo terminou em empate."""
        # Verifica linhas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '':
                return self.tabuleiro[i][0]
        # Verifica colunas
        for i in range(3):
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '':
                return self.tabuleiro[0][i]
        # Verifica diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return self.tabuleiro[0][2]
        # Verifica se o tabuleiro está cheio (empate)
        if all(cell != '' for row in self.tabuleiro for cell in row):
            return "EMPATE"
        return None

    def imprime_jogo(self):
        """Exibe o tabuleiro formatado."""
        print('   0   1   2')
        for i in range(3):
            linha = f'{i} '
            for j in range(3):
                linha += f'[{self.tabuleiro[i][j] if self.tabuleiro[i][j] != "" else " "}] '
            print(linha)
        print('-' * 23)

    def jogar(self, jogadas):
        """Executa o loop principal do jogo com jogadas predefinidas."""
        print('==== JOGO DA VELHA ====')
        self.imprime_jogo()
        for linha, coluna in jogadas:
            jogador_atual = 'X' if self.rodada % 2 == 0 else 'O'
            print(f'Vez de {jogador_atual}: ({linha}, {coluna})')
            if self.atualiza_casa(linha, coluna, jogador_atual):
                self.imprime_jogo()
                vencedor = self.verifica_ganhador()
                if vencedor:
                    print(f'RESULTADO: O jogador {vencedor} ganhou!')
                    self.alguem_ganhou = True
                    return vencedor
                self.rodada += 1
            else:
                print('Jogada inválida. Tente novamente.')
        if not self.alguem_ganhou:
            print('RESULTADO: O jogo terminou em empate!')
            return None


# Para rodar o jogo sem input
if __name__ == "__main__":
    jogadas = [(0, 0), (1, 1), (0, 1), (1, 2), (0, 2)]  # Exemplo de jogadas predefinidas
    jogo = JogoDaVelha()
    jogo.jogar(jogadas)


# Testes com pytest
def test_atualiza_casa():
    jogo = JogoDaVelha()
    assert jogo.atualiza_casa(0, 0, 'X') == True
    assert jogo.atualiza_casa(0, 0, 'O') == False
    assert jogo.atualiza_casa(3, 3, 'X') == False


def test_verifica_ganhador():
    jogo = JogoDaVelha()
    jogo.tabuleiro = [['X', 'X', 'X'], ['', '', ''], ['', '', '']]
    assert jogo.verifica_ganhador() == 'X'
    jogo.tabuleiro = [['O', '', ''], ['O', '', ''], ['O', '', '']]
    assert jogo.verifica_ganhador() == 'O'
    jogo.tabuleiro = [['X', '', 'O'], ['', 'X', ''], ['O', '', 'X']]
    assert jogo.verifica_ganhador() == 'X'


def test_empate():
    jogo = JogoDaVelha()
    jogo.tabuleiro = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert jogo.verifica_ganhador() == 'EMPATE'


def test_jogo_completo():
    jogo = JogoDaVelha()
    jogadas = [(0, 0), (1, 1), (0, 1), (1, 2), (0, 2)]
    assert jogo.jogar(jogadas) == 'X'
