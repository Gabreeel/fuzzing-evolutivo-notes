# Planejamento de Leitura e Pesquisa (8 semanas)

> Arquivo: 00-meta/planejamento.md  
> Ideia: usar os checkboxes `[ ]` / `[x]` para marcar o que já foi feito.

---

## Visão geral

- [X] Criar/revisar estrutura do repositório de notas (pastas e arquivos principais).
- [ ] Definir linguagem-alvo inicial para o fuzzer (interpretador/compilador que você quer atacar).

---

## Semana 1 – Fundamentos básicos + visão geral do projeto do Rodrigo

**Objetivo:**  
Ter vocabulário mínimo de fuzzing e entender, em nível de “pitch”, o escopo do projeto de smart contracts do Rodrigo.

**Tarefas:**

- Leitura rápida do *The Fuzzing Book*:
  - [X] Ler introdução / overview.
  - [X] Ler a parte de fuzzing randômico (primeiro exemplo de fuzzer).
  - [X] Criar/atualizar `01-fundamentos-fuzzing/fuzzing-book-intro.md` com:
    - [X] Loop básico de um fuzzer.
    - [X] Conceitos principais (seed corpus, crash, input interessante, etc.).

- Projeto do Rodrigo:
  - [ ] Ler o artigo de smart contracts indicado por ele (leitura de sobrevôo).
  - [ ] Preencher `04-smart-contracts/projeto-rodrigo-visao-geral.md`:
    - [ ] Seções 1–4 (problema, PUT, estratégias, resultados).
    - [ ] Seções 5–6 (onde GA/GP encaixa + possíveis direções de colaboração).
    - [ ] Seção 7 com pelo menos 3 perguntas pra levar para conversa com Marcelo/Rodrigo.

- Organização:
  - [X] Criar a estrutura de pastas sugerida no repositório (ou adaptar):
    - `00-meta/`, `01-fundamentos-fuzzing/`, `04-smart-contracts/`, etc.
  - [X] Commit inicial no Git com essa estrutura.

---

## Semana 2 – Mutation-based fuzzing e cobertura

**Objetivo:**  
Entender melhor como funciona fuzzing guiado por cobertura e como isso pode virar função de fitness.

**Tarefas:**

- *The Fuzzing Book*:
  - [ ] Ler capítulos/trechos sobre mutation-based fuzzing.
  - [ ] Ler a parte de coverage-guided fuzzing.
  - [ ] Atualizar `01-fundamentos-fuzzing/fuzzing-book-coverage.md` com:
    - [ ] Tipos de cobertura (linhas, blocos básicos, edges).
    - [ ] Como o fuzzer decide quais inputs manter.

- Síntese:
  - [ ] Em `07-sintese/ideias-fitness.md`, criar:
    - [ ] Pelo menos 2 ideias de funções de fitness baseadas em cobertura (mesmo que simples).

---

## Semana 3 – Grammar-based fuzzing e ligação com Programação Genética

**Objetivo:**  
Entender geração estruturada/sintática e preparar o terreno pra representação de indivíduos em GA/GP.

**Tarefas:**

- *The Fuzzing Book*:
  - [ ] Ler capítulo/trechos sobre grammar-based fuzzing.
  - [ ] Anotar em `01-fundamentos-fuzzing/fuzzing-book-grammar.md`:
    - [ ] Como definem gramáticas.
    - [ ] Como garantem entradas sintaticamente válidas ou “quase válidas”.

- Síntese:
  - [ ] Criar `07-sintese/ideias-representacao.md` com:
    - [ ] 1–2 propostas de representação de indivíduo (AST/gramática) para seu fuzzer evolutivo.

---

## Semana 4 – Avaliação e benchmarks (Métricas e comparação de fuzzers)

**Objetivo:**  
Aprender a medir de forma científica, evitando armadilhas de avaliação fraca.

**Tarefas:**

- Leitura:
  - [ ] Ler um survey/trabalho sobre desafios na avaliação de fuzzers.
  - [ ] Ler o paper do benchmark **MAGMA** (ou equivalente).

- Notas:
  - [ ] `02-avaliacao-benchmarks/survey-fuzzing-metrics.md`:
    - [ ] Problemas clássicos na avaliação de fuzzers.
  - [ ] `02-avaliacao-benchmarks/magma-benchmark.md`:
    - [ ] Como definem ground truth.
    - [ ] Como medem “fuzzer X é melhor que Y”.

- Síntese:
  - [ ] Atualizar `07-sintese/ideias-benchmarks.md` com:
    - [ ] 2–3 métricas que você quer usar no seu projeto.
    - [ ] Uma ideia de mini-benchmark que você consiga montar.

---

## Semana 5 – Fuzzing de compiladores/interpretadores

**Objetivo:**  
Mergulhar no estado da arte do seu foco principal (interpreters/compilers).

**Tarefas:**

- Leitura:
  - [ ] Ler um survey de compiler fuzzing.
  - [ ] Ler 1–2 papers clássicos (ex.: Csmith / similares).

- Notas:
  - [ ] `03-compiladores-interpretadores/survey-compiler-fuzzing.md`.
  - [ ] `03-compiladores-interpretadores/csmith-paper.md`.
  - [ ] Opcional: `03-compiladores-interpretadores/zeller-outros.md` para mais 1–2 trabalhos.

- Síntese:
  - [ ] Em `07-sintese/ideias-fitness.md`, adicionar:
    - [ ] 1 ideia de fitness usando teste diferencial (divergência entre compilers/versões).
  - [ ] Em `07-sintese/ideias-benchmarks.md`, rascunhar:
    - [ ] Um cenário concreto de interpretador/compilador alvo.

---

## Semana 6 – Payer / HexHive (fuzzing + segurança de sistemas)

**Objetivo:**  
Conectar com a visão prática de segurança e benchmarks reais.

**Tarefas:**

- Leitura:
  - [ ] Escolher 1–2 papers do grupo do Mathias Payer (fuzzing/benchmarks).

- Notas:
  - [ ] `05-payer-hexhive/payer-magma-ou-outros.md` com:
    - [ ] Arquitetura do fuzzer.
    - [ ] Como eles desenham os experimentos.

- Síntese:
  - [ ] Atualizar `07-sintese/esboco-artigo.md` com:
    - [ ] Primeira versão da seção “Metodologia Experimental”.

---

## Semana 7 – Fuzzing diferencial e criptografia (Quarkslab + Cryptofuzz)

**Objetivo:**  
Aprender oráculos diferenciais e ganhar um segundo domínio de teste (cripto).

**Tarefas:**

- Leitura:
  - [ ] Artigo/post “Differential fuzzing for cryptography” (Quarkslab).
  - [ ] Explorar o repositório `cryptofuzz`.

- Notas:
  - [ ] `06-cripto-diff-fuzzing/quarkslab-diff-fuzzing-crypto.md`.
  - [ ] `06-crip
