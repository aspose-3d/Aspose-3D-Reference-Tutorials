---
date: 2026-06-03
description: Aprenda como exportar a cena como FBX e criar cilindro 3D, caixa e outros
  modelos primitivos usando Aspose.3D para Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Construindo Modelos 3D Primitivos com Aspose.3D para Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exportar cena como FBX e construir cilindro com Aspose.3D Java
url: /pt/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportar cena como FBX e construir cilindro com Aspose.3D Java

## Introdução

Se você já precisou **criar um cilindro 3D** (ou qualquer outra forma básica) diretamente a partir de código Java, o Aspose.3D torna a tarefa indolor. Neste tutorial percorreremos todo o fluxo de trabalho — desde a configuração do ambiente até **exportar cena como FBX** — para que você possa começar a gerar geometria 3D programaticamente imediatamente. Você verá como a biblioteca lida com primitivos, como organizá‑los em um grafo de cena e como salvar o resultado em um formato que Unity, Blender ou qualquer outra ferramenta 3D possa ler.

## Respostas Rápidas
- **Qual biblioteca me permite criar um cilindro 3D em Java?** Aspose.3D for Java.  
- **Qual formato posso exportar a cena?** FBX (ASCII 7500) usando `FileFormat.FBX7500ASCII`.  
- **Preciso de licença para desenvolvimento?** Um teste gratuito funciona para testes; uma licença permanente é necessária para produção.  
- **Quais são os principais primitivos suportados?** Box, Cylinder, Sphere, Cone e mais de 10 formas adicionais.  
- **O código é compatível com Java 8 e posteriores?** Sim, o Aspose.3D tem como alvo JDK 8+.

## O que é um primitivo de cilindro 3D?

Um primitivo de cilindro é uma forma geométrica básica definida por um raio e altura. Em muitas pipelines 3D ele serve como bloco de construção para modelos mais complexos, como tubos, rodas ou colunas arquitetônicas. O Aspose.3D fornece uma classe `Cylinder` pronta‑para‑uso, de modo que você não precise calcular vértices manualmente.

## Por que usar Aspose.3D para Java?

O Aspose.3D para Java oferece um motor 3D abrangente, puro‑Java, que elimina a necessidade de bibliotecas nativas, tornando‑o ideal para desenvolvimento multiplataforma. Ele suporta uma ampla gama de formatos de importação e exportação, fornece um grafo de cena robusto para organização hierárquica e inclui primitivos incorporados que permitem criar geometria com código mínimo. Esses recursos juntos aceleram o desenvolvimento e reduzem a sobrecarga de manutenção.

- **Motor 3D completo** – suporta importação/exportação de **mais de 30** formatos populares (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **API Java pura** – sem dependências nativas, perfeito para projetos multiplataforma.  
- **Grafo de cena robusto** – permite organizar objetos hierarquicamente, facilitando o gerenciamento de cenas grandes.  
- **Licenciamento simples** – comece com um teste gratuito e, depois, atualize para uma licença permanente quando entrar em produção.

## Pré-requisitos

Antes de mergulhar no código, certifique‑se de que você tem:

1. **Java Development Kit (JDK)** – JDK 8 ou mais recente instalado na sua máquina.  
2. **Aspose.3D for Java library** – faça o download e instale a partir da [download page](https://releases.aspose.com/3d/java/).  

## Importar Pacotes

Comece importando o namespace principal do Aspose.3D. Isso lhe dá acesso a `Scene`, `Box`, `Cylinder` e constantes de formato de arquivo.

```java
import com.aspose.threed.*;
```

Agora que a biblioteca está referenciada, vamos criar uma cena e adicionar alguma geometria primitiva.

## Como exportar cena como FBX e criar primitivos 3D?

Carregue um novo objeto `Scene`, adicione nós primitivos (Box, Cylinder, etc.) e então chame `save` com o formato FBX7500ASCII. Em apenas algumas linhas você obtém um arquivo FBX totalmente funcional que pode ser aberto em qualquer editor 3D importante, permitindo integração perfeita com motores de jogo, pipelines de renderização ou aplicações AR/VR.

### Etapa 1: Inicializar um Objeto Scene

A classe `Scene` é o contêiner de nível superior do Aspose.3D que contém todos os nós, luzes, câmeras e materiais na memória.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Etapa 2: Construir um modelo de caixa 3D

A classe `Box` representa um prisma retangular e é útil para testar o sistema de coordenadas. Adicioná‑la como filho do nó raiz da cena a posiciona na origem.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Etapa 3: Criar um modelo de cilindro 3D

A classe `Cylinder` é o primitivo de cilindro incorporado do Aspose.3D. Ela vem com dimensões padrão (raio = 1, altura = 2), mas você pode customizá‑las via seu construtor.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Etapa 4: Salvar o desenho no formato FBX

Depois de montar a cena, exporte‑a para que outras ferramentas (por exemplo, Unity, Blender) possam lê‑la. Usamos o formato `FBX7500ASCII`, que é amplamente suportado e legível por humanos.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Solução |
|----------|------------------|---------|
| **Arquivo não encontrado** ao salvar | `myDir` aponta para uma pasta inexistente | Garanta que o diretório exista ou crie‑o com `new File(myDir).mkdirs();` |
| **Cena vazia** após exportação | Nenhum nó foi adicionado antes de chamar `save` | Verifique se as chamadas `createChildNode` foram executadas (depure com `scene.getRootNode().getChildCount()` ) |
| **Exceção de licença** | Executando sem uma licença válida em produção | Aplique uma licença temporária ou permanente usando `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Perguntas Frequentes

**Q: Posso usar Aspose.3D para Java com outras linguagens de programação?**  
A: O Aspose.3D suporta principalmente Java, mas também há versões disponíveis para .NET e C++.

**Q: O Aspose.3D é adequado para tarefas complexas de modelagem 3D?**  
A: Absolutamente. Ele oferece um conjunto abrangente de recursos — incluindo manipulação de malhas, atribuição de materiais e animação — tornando‑o adequado tanto para primitivos simples quanto para modelos intricados.

**Q: Onde posso encontrar ajuda e suporte adicionais?**  
A: Visite o [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) para suporte da comunidade e discussões.

**Q: Posso experimentar o Aspose.3D antes de comprar?**  
A: Sim, você pode explorar um [free trial](https://releases.aspose.com/) antes de tomar a decisão de compra.

**Q: Como obtenho uma licença temporária para o Aspose.3D?**  
A: Você pode obter uma [temporary license](https://purchase.aspose.com/temporary-license/) para o Aspose.3D através do site.

## Conclusão

Agora você aprendeu como **exportar cena como FBX** e como **criar cilindro 3D**, caixa e outros modelos primitivos usando Aspose.3D para Java. Sinta‑se à vontade para experimentar primitivos adicionais como Sphere, Cone ou Torus, e explorar atribuições de material para dar aos seus modelos uma aparência realista. Quando estiver confortável, você pode integrar os arquivos FBX gerados em motores de jogo, pipelines AR/VR ou qualquer fluxo de trabalho 3D subsequente.

---

**Last Updated:** 2026-06-03  
**Testado com:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose

## Tutoriais Relacionados

- [Como Exportar Cena para FBX e Recuperar Informações da Cena 3D em Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Como Exportar FBX e Construir Hierarquias de Nós em Java](/3d/java/geometry/build-node-hierarchies/)
- [Como Criar Modelos de Cilindro com Aspose.3D para Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}