# Decorator 🎭 — Padrão de Projeto (Estrutural)

![status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![categoria](https://img.shields.io/badge/categoria-estrutural-blue)
![uml](https://img.shields.io/badge/UML-mermaid-informational)

## 1) Contextualização
Sistemas crescem em variantes de comportamento (log, cache, compressão, criptografia…). Herança começa a explodir em subclasses. **Decorator** permite anexar responsabilidades **dinamicamente**, sem tocar no núcleo nem multiplicar classes.

## 2) Definição
> **Decorator** anexa responsabilidades adicionais a um objeto em **tempo de execução**, oferecendo uma alternativa flexível à herança para **estender funcionalidades** (OCP).

## 3) Problema que resolve
- Evitar explosão de subclasses.
- Ligar/desligar comportamentos em runtime.
- Compor funcionalidades em **pipeline** (ex.: validar → comprimir → criptografar).

## 4) Aplicação em um sistema real
**API/Web:** antes de enviar dados: validar, **comprimir**, **criptografar** e **logar**. Cada etapa é um *decorator* empilhado. A ordem pode mudar conforme a necessidade.

## 5) UML (links)

- ▶️ **Diagrama de Classes (Mermaid)** — [abrir](diagrams/class-diagram.md)

## 6) Código (links)

- 🗂 **Pasta do código em Python** — [abrir](src/)
- 🧩 Arquivos diretos:
  - [main.py](src/main.py)
  - [decorators.py](src/decorators.py)
  - [decorator.py](src/decorator.py)
  - [concrete_component.py](src/concrete_component.py)
  - [component.py](src/component.py)


