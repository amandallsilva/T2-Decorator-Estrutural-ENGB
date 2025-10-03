# Diagrama de Classes — Decorator

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

