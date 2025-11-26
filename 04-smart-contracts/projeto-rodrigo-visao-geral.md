# Projeto do Rodrigo – Fuzzing de Smart Contracts

> Arquivo: 04-smart-contracts/projeto-rodrigo-visao-geral.md

## 0. Referência básica

- Título do artigo/trabalho: <!-- preencher -->
- Autores: <!-- preencher -->
- Link: <!-- preencher -->
- Grupo / laboratório: <!-- preencher, se fizer sentido -->

---

## 1. Problema que o trabalho ataca

- Qual é a dor principal que o trabalho tenta resolver?
  - <!-- ex: encontrar vulnerabilidades em smart contracts de forma mais eficiente -->
- Contexto:
  - <!-- ex: EVM / Ethereum, DeFi, contratos complexos, etc. -->
- Por que fuzzing “simples” não é suficiente aqui?
  - <!-- preencher -->

---

## 2. Programa(s) sob teste (PUT)

- Plataforma / ambiente:
  - <!-- ex: Ethereum, EVM, linguagem Solidity, etc. -->
- O que exatamente é fuzzado?
  - <!-- ex: funções públicas, sequência de transações, chamadas específicas -->
- Há algum tipo de oráculo?
  - <!-- ex: invariantes, falhas específicas, exceções, divergências de comportamento -->

---

## 3. Estratégias de fuzzing / otimização usadas

### 3.1 Estratégia 1

- Descrição:
  - <!-- descrever em 2–3 bullets -->
- Que tipo de feedback ela usa?
  - <!-- cobertura, falhas, métricas de gas, etc. -->
- Pontos fortes:
  - <!-- preencher -->
- Limitações:
  - <!-- preencher -->

### 3.2 Estratégia 2

- Descrição:
  - <!-- descrever em 2–3 bullets -->
- Que tipo de feedback ela usa?
  - <!-- preencher -->
- Pontos fortes:
  - <!-- preencher -->
- Limitações:
  - <!-- preencher -->

### 3.3 Como as duas estratégias interagem

- Elas são usadas em paralelo, em fases, alternadas…?
  - <!-- preencher -->
- Existe alguma lógica de seleção de estratégia?
  - <!-- preencher -->

---

## 4. Resultados principais (bem resumidos)

- Métricas usadas no artigo:
  - <!-- ex: número de vulnerabilidades encontradas, tipo de vulnerabilidade, cobertura, etc. -->
- Comparação com outras ferramentas ou abordagens:
  - <!-- preencher -->
- Conclusões que os autores destacam:
  - <!-- preencher -->

---

## 5. Pontos onde algoritmos genéticos / Programação Genética poderiam entrar

> Aqui é a parte mais “sua opinião” – é a ponte com seu projeto.

- Ideias de uso de GA/GP como **gerador de inputs/transações**:
  - <!-- ex: evoluir sequências de chamadas para explorar estados complexos -->
- Ideias de GA/GP como **camada de seleção/composição de estratégias**:
  - <!-- ex: indivíduo representa qual estratégia usar em qual momento -->
- Ideias de GA/GP como **otimizador de parâmetros**:
  - <!-- ex: ajustar pesos/thresholds das heurísticas existentes -->

**Resumo (em 2–3 linhas):**  
<!-- "Vejo o GA/GP encaixando melhor em X, porque..." -->

---

## 6. Possíveis direções de colaboração para mim

- (A) Extender diretamente o fuzzer do artigo com um módulo evolutivo:
  - <!-- prós/contras -->
- (B) Estudo comparativo:
  - <!-- implementar uma variante evolutiva e comparar com as duas estratégias do artigo -->
- (C) Camada “meta-fuzzer”:
  - <!-- GA decidindo qual estratégia rodar em qual momento, com base no feedback -->

**Qual dessas parece mais promissora pra mim agora? Por quê?**  
<!-- escrever um mini-parágrafo com sua preferência atual -->

---

## 7. Dúvidas / perguntas para levar aos professores

- Pergunta 1:
  - <!-- ex: "Qual parte do pipeline atual vocês consideram mais carente de heurísticas inteligentes?" -->
- Pergunta 2:
  - <!-- ex: "Vocês imaginam GA/GP mais como gerador de inputs, ou como combinador de estratégias?" -->
- Pergunta 3:
  - <!-- ex: "Quais limitações práticas vocês encontraram quando tentaram usar GA no passado?" -->
- Outras dúvidas:
  - <!-- preencher conforme surgirem na leitura -->

---

## 8. Notas soltas / impressões rápidas

- <!-- espaço livre pra anotar coisa que não se encaixa nas seções acima, insights, frases importantes, etc. -->
