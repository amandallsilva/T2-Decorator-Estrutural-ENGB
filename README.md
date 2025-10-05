# Decorator 🎭 — Padrão de Projeto (Estrutural)

---

## 📚 Sumário
- [1) Contextualização](#1-contextualização)
- [2) Definição](#2-definição)
- [3) Problema que resolve](#3-problema-que-resolve)
- [4) Aplicação em um sistema real](#4-aplicação-em-um-sistema-real)
- [5) UML (links)](#5-uml-links)
- [6) Código (links)](#6-código-links)
- [7) Referências](#7-referências)

---

## 1) Contextualização
No campo da Engenharia de Software, padrões de projeto surgiram como uma resposta à necessidade de documentar soluções recorrentes para problemas que se repetem em diferentes contextos de desenvolvimento. A ideia foi consolidada em **Design Patterns: Elements of Reusable Object-Oriented Software** (Gamma, Helm, Johnson e Vlissides, 1995) — a *Gang of Four* (GoF) — que estabeleceu uma linguagem comum para arquitetos e desenvolvedores.

Entre os padrões apresentados, o **Decorator** (categoria **Estrutural**) resolve um problema frequente: **estender funcionalidades sem criar explosões de subclasses ou recorrer à herança múltipla**. Enquanto a herança adiciona comportamento em nível de classe (estático), o Decorator possibilita a **composição dinâmica** de responsabilidades — **em tempo de execução** — respeitando o **Princípio Aberto-Fechado** (Bertrand Meyer, 1988): *aberto para extensão, fechado para modificação*.

Na prática, é útil onde há **alta extensibilidade** e **baixo acoplamento**: I/O streams, camadas visuais (UI), observabilidade (logs/métricas), e pipelines de dados (validação → compressão → criptografia). O Decorator não é apenas técnica; é estratégia de **modularidade e clareza arquitetural** em sistemas complexos.

---

## 2) Definição
O padrão de projeto estrutural Decorator é uma solução no desenvolvimento de software orientado a objetos, projetada para estender as funcionalidades de objetos de maneira dinâmica, modular e altamente flexível, sem alterar o código original da classe base. Este padrão destaca-se por sua abordagem baseada em composição, que permite encapsular objetos com camadas adicionais de comportamento, preservando a integridade da interface original e possibilitando combinações variadas de funcionalidades. Reconhecido por promover extensibilidade e reusabilidade, o Decorator alinha-se a princípios fundamentais de design, como o princípio aberto/fechado do SOLID, que estabelece que classes devem estar abertas para extensão, mas fechadas para modificação.
### Definição Fundamental
O padrão Decorator é um mecanismo que permite adicionar responsabilidades ou comportamentos a objetos individuais de forma dinâmica, encapsulando-os em objetos decoradores que implementam a mesma interface do objeto base. Diferentemente da herança, que exige a criação de subclasses para cada variação de comportamento, o Decorator utiliza composição, envolvendo o objeto original com camadas de funcionalidade suplementar. Essa abordagem assegura que o objeto decorado permaneça compatível com a interface original, permitindo que o cliente interaja com ele de maneira transparente, como se fosse o objeto base, enquanto se beneficia das funcionalidades adicionais introduzidas pelos decoradores.

O cerne do padrão reside em sua capacidade de construir uma cadeia de objetos, onde cada decorador agrega uma responsabilidade específica, delegando chamadas ao objeto encapsulado e, simultaneamente, enriquecendo ou modificando seu comportamento. Essa estrutura em camadas possibilita que múltiplos decoradores sejam aplicados em sequência, criando combinações complexas de funcionalidades sem a necessidade de alterar a implementação original do objeto.

### Estrutura Conceitual
A arquitetura do padrão Decorator é composta por elementos bem definidos, que trabalham em conjunto para garantir modularidade e flexibilidade:

- **Componente Abstrato:** Uma interface ou classe abstrata que estabelece a assinatura dos métodos que serão implementados tanto pelo objeto base quanto pelos decoradores. Essa interface assegura que todos os objetos, sejam eles concretos ou decorados, sejam tratados de maneira uniforme pelo código cliente.
- **Componente Concreto:** A classe que implementa o componente abstrato, fornecendo a funcionalidade básica ou primária do objeto. Este é o ponto de partida que será estendido pelos decoradores.
- **Decorator Abstrato:** Uma classe que implementa a interface do componente abstrato e contém uma referência ao objeto que está sendo decorado. Essa classe serve como base abstrata para os decoradores concretos, delegando chamadas ao objeto encapsulado e permitindo a adição de comportamentos.
- **Decoradores Concretos:** Classes que estendem o Decorator abstrato e implementam responsabilidades específicas, complementando ou modificando o comportamento do objeto encapsulado. Cada decorador concreto é responsável por uma funcionalidade distinta, que pode ser combinada com outras.

A relação entre esses elementos é fundamentada na composição, onde o Decorator encapsula o objeto base ou outro decorador, formando uma cadeia de responsabilidades. Essa estrutura permite que os decoradores sejam empilhados em qualquer ordem, oferecendo flexibilidade na configuração do comportamento final do objeto.

### Funcionamento
O funcionamento do padrão Decorator baseia-se em um processo de delegação encadeada. Quando um método é invocado em um objeto decorado, o decorador correspondente executa sua lógica adicional (se aplicável) e, em seguida, delega a chamada ao objeto que ele encapsula. Esse objeto pode ser o componente concreto ou outro decorador na cadeia. O processo continua até que a chamada alcance o objeto base, garantindo que todas as camadas de funcionalidade sejam aplicadas na sequência correta.

Por exemplo, considere um objeto base com um comportamento padrão. Um primeiro decorador pode adicionar uma funcionalidade suplementar, como modificar o resultado do método original. Um segundo decorador, aplicado sobre o primeiro, pode introduzir outra funcionalidade, formando uma cadeia de processamento. O cliente interage com o objeto final, que reflete todas as responsabilidades adicionadas, mas utiliza a mesma interface do objeto original, mantendo a transparência e a compatibilidade. Essa abordagem dinâmica permite a composição de funcionalidades em tempo de execução, possibilitando a criação de objetos com comportamentos altamente personalizados sem a necessidade de subclasses específicas para cada combinação possível.

### Características Distintivas
O padrão Decorator possui características que o diferenciam de outras abordagens de design:

- **Dinamismo:** As funcionalidades podem ser adicionadas ou removidas em tempo de execução, sem recompilar o código ou modificar as classes existentes.
- **Modularidade:** Cada decorador é um componente independente, responsável por uma única funcionalidade, promovendo a separação de preocupações.
- **Transparência:** O objeto decorado mantém a mesma interface do objeto base, garantindo que o cliente não precise ajustar seu código para interagir com as funcionalidades adicionais.
- **Flexibilidade Combinatória:** Os decoradores podem ser combinados em diferentes ordens e quantidades, permitindo uma ampla gama de configurações de comportamento.
- **Conformidade com Princípios de Design:** O padrão alinha-se ao princípio aberto/fechado, pois permite a extensão de funcionalidades sem alterar o código original, e ao princípio da responsabilidade única, já que cada decorador lida com uma funcionalidade específica.

### Relação com Outros Padrões
O Decorator interage de maneira complementar com outros padrões de projeto, destacando-se por sua abordagem única:

- **Comparado ao Adapter,** que converte uma interface para outra, o Decorator mantém a interface original enquanto adiciona funcionalidades. Além disso, o Decorator suporta composição recursiva, o que não é possível com o Adapter.
- **Diferentemente do Composite,** que gerencia estruturas hierárquicas de objetos, o Decorator foca em estender um único objeto. Um Decorator é semelhante a um Composite, mas possui apenas um componente filho, adicionando responsabilidades ao objeto envolto, enquanto o Composite "soma" os resultados de seus filhos.
- **Em relação ao Strategy,** que substitui comportamentos inteiros, o Decorator adiciona comportamentos incrementalmente, permitindo combinações mais granulares.
- **Em comparação com o Proxy,** ambos utilizam composição, mas o Proxy gerencia o ciclo de vida do objeto de serviço, enquanto a composição de decoradores é controlada pelo cliente.
- **Semelhante ao Chain of Responsibility,** ambos dependem de composição recursiva, mas os manipuladores do Chain of Responsibility podem executar operações arbitrárias e interromper a passagem da solicitação, enquanto os decoradores mantêm a consistência da interface base e não quebram o fluxo da solicitação.

---

## 3) Problema que resolve
- 🧩 Evitar **explosão de subclasses** ao combinar variações de comportamento.  
- 🔀 Permitir **liga/desliga** e **reordenação** de responsabilidades em *runtime*.  
- 🧪 Manter o núcleo **estável**, favorecendo testes e manutenção.

---

## 4) Aplicação em um sistema real
**API/Web:** antes de enviar/persistir dados, aplicar **validação**, depois **compressão** e **criptografia**, registrando **logs**. Cada etapa é um *decorator* que embrulha o objeto principal. A ordem pode mudar conforme a política de segurança/desempenho.

---

## 5) UML (links)
- ▶️ **Diagrama de Classes ** — [`diagrams/class-diagram.md`](diagrams/class-diagram.md)  


> Dica: manter os diagramas em arquivos separados deixa a leitura do README mais limpa.

---

## 6) Código (links)
- 🗂 **Pasta do código (Python)** — [`src/`](src/)  

---

## 7) Referências
- Freeman, E.; Robson, E. *Head First Design Patterns*.
- Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*.
- Geeksforgeeks. *Decorator Pattern in System Design*. Disponível em: https://www.geeksforgeeks.org/system-design/decorator-pattern. Acesso em: 3 out. 2025.
- Kukhar, A. *Use decorator design pattern in program design for the formation of curriculum*. Тези доповідей, p. 51, 2014.
- Meyer, B. *Object-Oriented Software Construction* (Princípio Aberto-Fechado).
- Refactoring Guru. *Decorator.* Disponível em: https://refactoring.guru/design-patterns/decorator. Acesso em: 3 out. 2025.
- Softplan. *Decorator Design Pattern*. Disponível em: https://www.softplan.com.br/en/tech-writers/padrao-de-projeto-decorator. Acesso em: 3 out. 2025.

