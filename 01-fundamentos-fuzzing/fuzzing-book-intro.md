# Fuzzing Book - Introdução

## Referência
[The Fuzzing Book](https://www.fuzzingbook.org/)

## Notas
- A essência do Fuzzing é "Criar inputs aleatórios, e ver se eles quebram as coisas".
- Bart Miller deu o nome de "fuzz" as informações aleatórias e não-estruturadas geradas pelo fuzzer gerado por seus alunos, afinal, um programa que recebesse essa string como input provavelmente não seria capaz de rodar corretamente.
- O exercício proposto por Miller desencadeou muitos Buffer Overflows, já que muitos programas tem comprimentos máximos para inputs e elementos de inputs
### O que é Fuzzing?
Método de busca de falhas  e exceções em software, um Fuzzer é um software que por sua vez serve para automatizar o processo de "caça de bugs". Pelo The Fuzzing Book 
### Tipos de Fuzzing

### Quiz
1- Qual destas produz strings com números decimais arbitrariamente longos?

 a) fuzzer(100, 1, 100)
 b) fuzzer(100, 100, 0)
 c) fuzzer(100, 10, ord('0'))
 d) fuzzer(100, ord('0'), 10)

**Resposta correta: d) fuzzer(100, ord('0'), 10)**

Esta opção gera strings de até 100 caracteres no intervalo [48, 58), que corresponde aos dígitos '0' a '9' na tabela ASCII (ord('0') = 48).

**Por que as demais estão erradas:**

a) `fuzzer(100, 1, 100)` - Gera caracteres no intervalo [1, 101), incluindo caracteres de controle e diversos símbolos, não apenas dígitos.

b) `fuzzer(100, 100, 0)` - O `char_range = 0` faz com que `random.randrange(100, 100)` seja inválido (intervalo vazio), causando erro.

c) `fuzzer(100, 10, ord('0'))` - Gera caracteres no intervalo [10, 58), incluindo caracteres de controle, espaços e símbolos antes dos dígitos na tabela ASCII, não apenas números.

2- Apenas por diversão, imagine que você testaria um programa de remoção de arquivos - digamos rm -fr FILE, onde FILE é uma string produzida por fuzzer(). Qual é a chance de fuzzer() (com argumentos padrão) produzir um argumento FILE que resulte na exclusão de todos os seus arquivos?

a) Cerca de uma em um bilhão
b) Cerca de uma em um milhão
c) Cerca de uma em mil
d) Cerca de uma em dez

**Resposta correta: c) Cerca de uma em mil**

Para deletar todos os arquivos, o fuzzer precisa gerar a string `/` (raiz do sistema). Com os argumentos padrão (char_start=32, char_range=32), o caractere `/` (ASCII 47) está no intervalo possível [32, 64). 

# Fuzzing Book - Introdução (complementado)

## Referência
[The Fuzzing Book](https://www.fuzzingbook.org/)

## Resumo e objetivo
Anotações complementares ao primeiro capítulo e slides de "Fuzzer". Aqui estão os pontos essenciais e recomendações práticas — especialmente pensadas como base para o projeto de fuzzing evolutivo.

## O que é fuzzing
- Fuzzing: gerar entradas (inputs) aleatórias ou semi-aleatórias e alimentar o programa sob teste (PUT — program under test) para encontrar falhas.
- Origem: Barton Miller e o experimento clássico que mostrou como inputs aleatórios encontravam muitos buffer overflows em programas reais.

## Conceitos-chave
- Fuzzer: a ferramenta que gera inputs.
- Fuzz (noun): o dado gerado aleatoriamente.
- Corpus / Seed corpus: conjunto inicial de inputs "semente" usados como ponto de partida.
- Oracle: o método que decide se um comportamento é anômalo (crash, exceção, divergência, violação de invariant).
- Minimização / redução: processo de reduzir um teste que provoca falha para uma forma mínima que ainda reproduz o bug (delta debugging, creduce).

## Tipos de fuzzing (visão rápida)
- Random / dumb fuzzing: entradas puramente aleatórias (útil como baseline).
- Mutation-based fuzzing: parte de um corpus existente e aplica mutações (bit-flips, inserções, deletions, splicing).
- Generation / grammar-based: gera inputs a partir de uma gramática ou especificação (melhor para formatos estruturados).
- Coverage-guided fuzzing: usa feedback de cobertura para priorizar inputs que exploram novo código.
- Differential fuzzing: compara múltiplas implementações com o mesmo input para detectar divergências.

## Loop básico de um fuzzer (pseudo-código)

```
initialize corpus with seeds
while time remains:
    t = select_from(corpus)
    t' = mutate(t)        # ou gerar novo input
    result = run(PUT, t')
    if result indicates crash or new_feedback:
        store t' in corpus (and save crash)
        minimize t' (optional)
```

Observações:
- `select_from` pode priorizar inputs antigos/promissoes (corpus scheduling).
- `new_feedback` é o critério: pode ser cobertura (novas arestas/blocos), divergência ou outro sinal que valha a pena.

## Exemplo de fuzzer simples (Python)

```python
import random

def fuzzer(max_length: int = 100, char_start: int = 32, char_range: int = 32) -> str:
    """Return a random string up to max_length using characters in the
       interval [char_start, char_start + char_range)."""
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

# Uso simples
print(fuzzer(100, ord('0'), 10))  # string de dígitos
```

## Como detectar falhas no PUT (oráculos práticos)
- Crash / non-zero exit status.
- Sinais de memória (segfault) detectados por OS.
- Sanitizers: AddressSanitizer (ASan), UndefinedBehaviorSanitizer (UBSan), LeakSanitizer.
- Valgrind (mais lento, útil para investigação).
- Asserções/checagens lógicas e invariantes.
- Oráculos diferenciais (comparar comportamento entre versões/implementações).

## Cobertura e feedback
- Cobertura como sinal de valor: inputs que aumentam cobertura (linhas, edges, basic blocks) são guardados.
- Instrumentação: compile-time (libFuzzer, clang), dynamic (QEMU, DynamoRIO), ou ferramentas externas (AFL's instrumentation).
- Edge coverage é frequentemente mais informativo que line coverage para fuzzers.

## Minimização e triagem
- Após salvar um caso que causa crash, reduzir o input para uma forma mínima que ainda reproduz o bug (delta debugging / creduce).
- Agrupar crashes por stack trace / assinatura para evitar ruído duplicado.

## Estratégias de mutação comuns
- Bit/byte flips, arithmetic mutations, insertion/deletion, dictionary-based replacements, splicing (crossover entre dois inputs).
- Gramáticas: produção guiada por regras sintáticas para manter inputs válidos.

## Ferramentas e implementações de referência
- AFL / AFL++: mutation-based, instrumentation (user-space) e corpus scheduling.
- libFuzzer: in-process coverage-guided fuzzer para bibliotecas (LLVM sanitizers integrados).
- honggfuzz, fairfuzz, honggfuzz, etc.
- The Fuzzing Book: notebooks e exemplos em Python para aprender e prototipar rapidamente.

## Pontos práticos para o projeto (fuzzing evolutivo)
- Definir o PUT/ domínio inicial (ex.: parser, interpreter, biblioteca de criptografia).
- Iniciar com mutation-based coverage-guided fuzzer (boa relação esforço/retorno).
- Usar sanitizers (ASan/UBSan) para detectar falhas sutis.
- Manter um corpus inicial com poucos casos sintáticos válidos (se houver formato).
- Implementar minimização automática ao detectar crash.

## Onde encaixar GA/GP (ideias concretas)
- Indivíduos = inputs (strings / ASTs) — aplicar operadores genéticos (crossover, mutação) para gerar novos inputs.
- Indivíduos = estratégias/parametrizações (por exemplo, quais mutators usar, quais pesos) — evoluir controladores/meta-fuzzer.
- Fitness multi-objetivo: combinação de cobertura alcançada, novidade (novas arestas), e custo de execução (tempo).
- Representação sintática (GP) para gerar inputs válidos a partir de gramáticas — útil para linguagens/formatos estruturados.

## Métricas que valem para o projeto
- Coverage (linhas, edges, branches)
- Bugs únicos encontrados (agrupados por assinatura)
- Time-to-first-bug
- Throughput (execs/sec)
- Novidade / diversidade do corpus

## Recomendações de implementação inicial (passo a passo)
1. Escolher um alvo simples (um pequeno parser ou programa com entrada textual).
2. Implementar um harness Python que execute o PUT com um input e detecte crashes/timeouts.
3. Instrumentar (se possível) para coletar cobertura; começar sem cobertura e depois adicionar feedback.
4. Implementar um loop de mutação simples + corpus; salvar inputs que causam crash ou aumentam cobertura.
5. Adicionar minimização automática e agrupamento de falhas.
6. Experimentar uma versão evolutiva: indivíduos como inputs, fitness = cobertura + novelty.

## Recursos úteis
- The Fuzzing Book: notebooks e exemplos (estudar os exemplos de fuzzers e harnesses).
- AFL/AFL++ e libFuzzer: estudar como fazem scheduling, mutations e minimization.
- Ferramentas de redução: `creduce`, `git bisect` (para regressões), delta-debugging.

## Próximos passos daqui
- Implemento um pequeno harness em Python para o alvo que você escolher — quer que eu crie um template de `harness.py` que roda um executável com timeout e captura a saída/return code? 

---
*Notas:* estas anotações expandem o capítulo inicial e os slides, priorizando o que é útil para começar um fuzzer evolutivo (decisões de fitness, representação de indivíduos e integração com sanitizers e coverage feedback).