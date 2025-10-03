# Decorator 🎭 — Padrão de Projeto (Estrutural)

![status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![categoria](https://img.shields.io/badge/categoria-estrutural-blue)
![linguagem](https://img.shields.io/badge/lang-Python%203.10%2B-yellow)
![uml](https://img.shields.io/badge/UML-mermaid-informational)

> Repositório do Trabalho 2 — ENGB. Estruturado para leitura rápida, com links clicáveis para diagramas e código.

---

## 📚 Sumário
- [1) Contextualização](#1-contextualização)
- [2) Definição](#2-definição)
- [3) Problema que resolve](#3-problema-que-resolve)
- [4) Aplicação em um sistema real](#4-aplicação-em-um-sistema-real)
- [5) UML (links)](#5-uml-links)
- [6) Código (links)](#6-código-links)
- [7) Como executar](#7-como-executar)
- [8) Vantagens / Limitações](#8-vantagens--limitações)
- [9) Referências](#9-referências)
- [10) Estrutura do repositório](#10-estrutura-do-repositório)

---

## 1) Contextualização
No campo da Engenharia de Software, padrões de projeto surgiram como uma resposta à necessidade de documentar soluções recorrentes para problemas que se repetem em diferentes contextos de desenvolvimento. A ideia foi consolidada em **Design Patterns: Elements of Reusable Object-Oriented Software** (Gamma, Helm, Johnson e Vlissides, 1995) — a *Gang of Four* (GoF) — que estabeleceu uma linguagem comum para arquitetos e desenvolvedores.

Entre os padrões apresentados, o **Decorator** (categoria **Estrutural**) resolve um problema frequente: **estender funcionalidades sem criar explosões de subclasses ou recorrer à herança múltipla**. Enquanto a herança adiciona comportamento em nível de classe (estático), o Decorator possibilita a **composição dinâmica** de responsabilidades — **em tempo de execução** — respeitando o **Princípio Aberto-Fechado** (Bertrand Meyer, 1988): *aberto para extensão, fechado para modificação*.

Na prática, é útil onde há **alta extensibilidade** e **baixo acoplamento**: I/O streams, camadas visuais (UI), observabilidade (logs/métricas), e pipelines de dados (validação → compressão → criptografia). O Decorator não é apenas técnica; é estratégia de **modularidade e clareza arquitetural** em sistemas complexos.

---

## 2) Definição
> **Decorator adiciona responsabilidades a um objeto de forma dinâmica**, provendo uma alternativa flexível à herança para **estender funcionalidades** sem modificar o código-fonte do componente central.

---

## 3) Problema que resolve
- Evitar **explosão de subclasses** ao combinar variações de comportamento.  
- Permitir **liga/desliga** e **reordenação** de responsabilidades em *runtime*.  
- Manter o núcleo **estável**, favorecendo testes e manutenção.

---

## 4) Aplicação em um sistema real
**API/Web**: antes de enviar/persistir dados, aplicar **validação**, depois **compressão** e **criptografia**, registrando **logs**. Cada etapa é um *decorator* que embrulha o objeto principal. A ordem pode mudar conforme a política de segurança/desempenho.

---

## 5) UML (links)
- ▶️ **Diagrama de Classes (Mermaid)** — [`diagrams/class-diagram.md`](diagrams/class-diagram.md)  

---

## 6) Código (links)
- 🗂 **Pasta do código (Python)** — [`src/`](src/)  
---

