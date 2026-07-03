# Documentação: Jogo da Forca em Python

## 🎯 O que o programa faz
Este projeto é uma implementação em Python do clássico "Jogo da Forca", jogado via terminal. O sistema sorteia aleatoriamente uma palavra secreta e sua respectiva categoria a partir de um dicionário pré-definido. O jogador deve adivinhar a palavra inserindo uma letra por vez, tendo um limite de 6 erros representados graficamente por um boneco em ASCII. O jogo possui um sistema de múltiplas rodadas, onde a pontuação é acumulada progressivamente.

## ✅ Funcionalidades Obrigatórias Atendidas
1. Sorteio aleatório de uma palavra a partir de uma lista com 15 opções.
2. Ocultação das letras não descobertas utilizando underscores (`_`).
3. Captura e tratamento de entrada do usuário para receber os chutes (letras).
4. Substituição precisa do underscore pela letra revelada na posição correta, caso o chute seja um acerto.
5. Contagem progressiva de erros no caso de chutes incorretos.
6. Exibição em tempo real do histórico de letras já tentadas.
7. Encerramento automático da rodada ao atingir a vitória (todas as letras reveladas) ou a derrota (6 erros).
8. Exibição de mensagens finais personalizadas informando o resultado e a palavra correta.

## 🌟 Funcionalidades Bônus Implementadas
* **Arte em ASCII:** O boneco da forca é desenhado progressivamente no terminal a cada erro cometido.
* **Categorias Dinâmicas (Dicas):** As palavras estão organizadas em um dicionário de categorias (Frutas, Países, Animais). O sistema informa a categoria sorteada como dica no início da rodada.
* **Sistema de Pontuação (Placar Global):** Implementação de um placar contínuo. A pontuação é dinâmica: o jogador recebe pontos pelo tamanho da palavra (10 pontos por letra) e não perde pontos acumulados ao errar, valorizando o avanço no jogo.
* **Múltiplas Rodadas:** Possibilidade de jogar infinitas partidas sequenciais mantendo o placar acumulado.

## 🛠️ Dificuldades Enfrentadas e Soluções
1. **Gerenciamento de Memória nas Múltiplas Rodadas:** * *Dificuldade:* Inicialmente, o sistema de repetição chamava a função principal do jogo dentro dela mesma (recursão). Em uma longa sessão de jogo, isso poderia causar um estouro de pilha (*Stack Overflow*).
   * *Solução:* A lógica foi refatorada para utilizar um loop `while` no escopo global (`__main__`), executando a função do jogo de forma limpa e independente a cada rodada.

2. **Gerenciamento de Escopo da Pontuação:**
   * *Dificuldade:* Fazer a pontuação persistir entre as rodadas sem que ela fosse zerada toda vez que a função principal fosse invocada.
   * *Solução:* A variável de pontuação total foi isolada no escopo principal. Ela é passada como argumento para a função do jogo e, ao final da rodada, a função utiliza o `return` para devolver o placar atualizado.

3. **Penalização Injusta por Letras Repetidas:**
   * *Dificuldade:* O jogador poderia perder "vidas" acidentalmente ao digitar uma letra que já havia sido tentada em turnos anteriores.
   * *Solução:* Implementado um sistema de validação que verifica se o input está contido na lista `letras_tentadas`. Caso esteja, o comando `continue` é acionado, alertando o usuário e reiniciando o loop sem incrementar a contagem de erros. Utilizou-se também `isalpha()` e `len()` para evitar inputs numéricos ou múltiplos caracteres.