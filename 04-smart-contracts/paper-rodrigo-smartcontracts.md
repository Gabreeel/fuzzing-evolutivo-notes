# Paper Rodrigo - Smart Contracts

## Referência
[Adicionar referência do paper]

## Notas

### Problema

### Abordagem

### Resultados

### Relevância para Fuzzing Evolutivo

### Ideias para Aplicar


# Paper Rodrigo - Smart Contracts

## Referência
- Título: DogeFuzz: A Simple Yet Efficient Grey-box Fuzzer for Ethereum Smart Contracts
- ArXiv: 2409.01788v1
- (Adicionar link/DOI e autores quando disponível)

## Notas
Resumo e avaliação breve do paper DogeFuzz, com foco no que é relevante para integrar técnicas evolutivas.

### Problema
- Segurança de contratos Ethereum continua crítica (ex.: DAO, Parity, Uniswap). Há muitas ferramentas sofisticadas (symbolic execution, ML), mas faltam estudos que comparem essas técnicas com fuzzers simples e bem-engineerizados.

### Abordagem
- Desenvolvimento de uma infraestrutura extensível chamada DogeFuzz, composta por três modos:
	- DogeFuzz-B (black-box): geração ABI-aware sem feedback interno.
	- DogeFuzz-G (grey-box coverage-guided): prioriza seeds que aumentam cobertura (CFG/branches).
	- DogeFuzz-DG (directed grey-box): usa distância em CFG até instruções críticas da EVM (CALL, DELEGATECALL, CALLCODE, SELFDESTRUCT) para direcionar fuzzing.
- Arquitetura: EVM customizado (Go-Ethereum), uso do Vandal para análise estática (call graph/CFG), coleta em tempo real de eventos/instruções e um power-schedule comum para ordenar seeds.
- Oráculos: detecção de eventos (Delegate, GaslessSend, SendOp, ExceptionDisorder, BlockNumber, Timestamp, Reentrancy, StorageChanged, EtherTransfer) e pattern-matching para mapear sequências de eventos a classes de vulnerabilidade.

### Resultados
- Benchmarks:
	- BENCH72: 72 contratos com 82 bugs rotulados (reentrancy, mishandled exception, block dependency).
	- BENCH500: 500 contratos populares (409 compiláveis) sem ground-truth rotulado.
- Principais achados:
	- DogeFuzz-G aumenta cobertura ~9.7% vs black-box; DG +2.2% vs black-box.
	- G/DG alcançam F1 > 0.76 em BENCH72, superando sFuzz e ILF (~0.6); Smartian ainda lidera (F1 ~0.92).
	- G/DG continuam encontrando bugs ao longo de 1h por contrato; sFuzz/ILF param de achar novos bugs após ~15 minutos.
	- Em BENCH500, mediana de cobertura G/DG ~48% vs black-box ~40%.
	- Notável que o black-box do DogeFuzz é competitivo em vários cenários, indicando impacto forte de engenharia (ABI-aware input generation, seeds).

### Relevância para Fuzzing Evolutivo
- DogeFuzz fornece sinais de feedback muito úteis (cobertura, distância a instruções críticas, eventos) que podem ser usados como componentes de função de fitness para GA/GP.
- Posições de integração:
	- Indivíduos = inputs (calldata/seq. de transações): fitness = combinação de aumento de cobertura, redução de distância a instruções críticas e novidade/diversidade.
	- Indivíduos = estratégias/parametrizações (meta-fuzzer): GA para selecionar mutators, pesos do power-schedule ou alternância entre modos (B/G/DG).
	- GP para gerar inputs estruturados (AST/gramática) quando a validade sintática for importante.

### Ideias para Aplicar (práticas e imediatas)
- Implementar um módulo evolutivo que consome sinais do DogeFuzz sem alterar o core: um processo externo lê cobertura/distância/eventos e evolui um corpus, retornando seeds ao fuzzer.
- Fitness multi-objetivo sugerido:
	- f1 = cobertura_nova (bônus por novas edges/blocks)
	- f2 = -distancia_para_instrucao_critica (quanto menor, melhor)
	- f3 = novelty/diversity (penalizar duplicatas)
	- combinar com pesos ou usar seleção multi-objetivo (NSGA-II) dependendo da escala.
- Experimento inicial proposto:
	1) Mini-BENCH (10 contratos do BENCH72) — comparar DogeFuzz-G vs DogeFuzz-G+GA (população de seeds, crossover, mutação simples) medindo F1, time-to-first-bug e cobertura ao longo do tempo.
	2) Testar DG+GA: incluir distância a instruções críticas como componente de fitness para guiar operadores genéticos.

<!-- mantenha abaixo um espaço para notas futuras ou links -->
