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

## 5) UML (Mermaid)
### Diagrama de Classes
```mermaid
classDiagram
    class Component {
      <<interface>>
      +operation(data) any
    }

    class ConcreteComponent {
      +operation(data) any
    }

    class Decorator {
      -wrappee: Component
      +operation(data) any
    }

    class LoggingDecorator {
      +operation(data) any
    }

    class CompressDecorator {
      +operation(data) any
    }

    class EncryptDecorator {
      +operation(data) any
    }

    Component <|.. ConcreteComponent
    Component <|.. Decorator
    Decorator <|-- LoggingDecorator
    Decorator <|-- CompressDecorator
    Decorator <|-- EncryptDecorator
    Decorator o--> Component

