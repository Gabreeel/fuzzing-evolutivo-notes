# Título do trabalho
Autor(es), ano, onde foi publicado

## 1. Problema que o trabalho ataca
- O que eles querem resolver?
- Qual limitação de fuzzers / testes eles estão mirando?

## 2. Programa(s) sob teste (PUT)
- Tipo (compilador, interpretador, smart contract, lib cripto, etc.)
- Linguagem/plataforma
- Como executam os testes (ferramentas, ambiente)

## 3. Representação de entrada
- Como são os inputs? (bytes, AST, gramática, DSL...)
- Tem alguma restrição para evitar lixo total?

## 4. Feedback / Métrica (fitness "implícito")
- Usam cobertura? crashes? divergência? métricas específicas?
- Como decidem o que é um input “bom” ou “interessante”?

## 5. Estratégia de busca / Fuzzing
- Tipo de fuzzer (blackbox, greybox, whitebox)
- Heurísticas/estratégias principais
- Onde um GA/GP poderia encaixar aqui?

## 6. Benchmarks e protocolo experimental
- Que programas foram testados?
- Quantas execuções, por quanto tempo, que métricas comparam?

## 7. Resultados importantes
- Principais achados (em bullets)
- Comparações com outros métodos

## 8. Limitações apontadas pelos autores
- O que eles mesmos admitem que não funciona bem?
- Em que cenários o método falha / é fraco?

## 9. Ideias para o meu projeto
- Como isso inspira o meu fuzzer evolutivo?
- Ideias de:
  - representação de indivíduo
  - fitness
  - benchmarks
- Ganchos para colaboração (se for paper do Rodrigo/Payer/Diego)

## 10. Referência
- Citação BibTeX (pra colar depois no LaTeX)