---
date: 2026-08-12
description: Como gerar 3D usando Aspose.3D – criar um cilindro com offset top em
  Java, adicionar child node, set offset top, gerar modelo 3D, exportar OBJ e avaliar
  com uma temporary license.
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: Como gerar 3D – criar cilindro com offset top (Java)
og_description: Como gerar 3D com Aspose.3D para Java. Aprenda a offset cylinder tops,
  add child nodes e exportar OBJ usando uma temporary license.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: Como gerar 3D – criar cilindro com offset top (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: Como gerar 3D – criar cilindro com offset top (Java)
url: /pt/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como gerar 3d – criar cilindro com topo deslocado (Java)

## Introdução

Se você está procurando **criar cilindro** objetos com um topo deslocado personalizado em uma cena 3D baseada em Java, o Aspose.3D torna o processo simples. Neste tutorial vamos percorrer cada passo — desde a configuração da cena até a exportação do modelo final como um arquivo OBJ — para que você possa integrar cilindros com topo deslocado em suas aplicações com confiança. Ao final do guia você também entenderá como uma **licença temporária Aspose** permite avaliar esses recursos sem a necessidade de compra completa.

## Respostas rápidas
- **Qual biblioteca é usada?** Aspose.3D for Java  
- **Posso deslocar o topo de um cilindro?** Sim, via `setOffsetTop`  
- **Como adiciono um nó filho em Java?** Chame `createChildNode` no nó raiz  
- **Para qual formato posso exportar?** Wavefront OBJ (`export obj file`)  
- **Preciso de uma licença para testes?** Uma **licença temporária Aspose** está disponível para avaliação  

## O que é licença temporária Aspose?

Uma **licença temporária Aspose** é uma chave de avaliação de curto prazo e gratuita que desbloqueia o conjunto completo de recursos do Aspose.3D for Java durante o desenvolvimento e testes. Ela remove as marcas d'água de avaliação e permite gerar arquivos de modelo 3D, como OBJ, STL ou FBX, exatamente como faria uma licença paga.

## Por que usar Aspose.3D para Java?

O Aspose.3D fornece uma API de alto nível e multiplataforma que simplifica a criação e exportação 3D. Inclui exportadores integrados para mais de 30 formatos, suporta hierarquias de grafos de cena e permite que você se concentre na geometria em vez de lidar com malhas de baixo nível.

- **API de alto nível:** Não é necessário gerenciar dados de malha de baixo nível.  
- **Multiplataforma:** Funciona em qualquer ambiente compatível com JVM.  
- **Exportadores integrados:** Salve diretamente em OBJ, STL, FBX e mais — o Aspose.3D suporta **30+** formatos de exportação.  
- **Extensível:** Adicione facilmente nós filhos, aplique transformações e integre com outras bibliotecas Java.  

## Pré-requisitos

- **Java Development Kit (JDK)** – uma versão compatível instalada.  
- **Biblioteca Aspose.3D for Java** – faça download do JAR mais recente no site oficial **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Uma IDE de sua escolha (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Importar pacotes

As importações a seguir trazem as classes essenciais do Aspose.3D necessárias para criar e exportar um cilindro.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Guia passo a passo

### Passo 1: Criar uma cena 3D Java

`Scene` é o contêiner de nível superior que contém todos os nós, malhas, luzes e câmeras em um ambiente 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Passo 2: Inicializar cilindro com topo deslocado

`Cylinder` representa uma malha cilíndrica e fornece propriedades como raio, altura e deslocamento.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Passo 3: Adicionar nó filho Java – anexar o primeiro cilindro

`Node` é um elemento no grafo da cena que pode conter geometria e transformações.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Passo 4: Inicializar um segundo cilindro (sem deslocamento)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Passo 5: Adicionar nó filho Java – anexar o segundo cilindro

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Passo 6: Exportar OBJ em Java – salvar a cena como OBJ

`FileFormat` enumera os formatos de exportação suportados, como OBJ, STL e FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Como gerar modelo 3d e exportar OBJ em Java

Para gerar um modelo 3D, carregue a cena, aplique as transformações necessárias e então chame `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)`. A **licença temporária Aspose** remove a marca d'água de avaliação, permitindo que você produza arquivos OBJ prontos para produção sem comprar uma licença completa.

## Casos de uso reais

- **Visualização arquitetônica:** Cilindros com topo deslocado modelam colunas que afinam em direção ao teto.  
- **Peças mecânicas:** Crie pistões ou carcaças de engrenagens onde a superfície superior é intencionalmente deslocada.  
- **Recursos de jogos:** Produza formas variadas de pilares em tempo real, reduzindo a necessidade de malhas feitas à mão.  

## Problemas comuns e soluções

| Problema | Razão | Solução |
|-------|--------|-----|
| **Arquivo OBJ está vazio** | Cena não salva corretamente ou caminho errado. | Verifique se o diretório de saída existe e se você tem permissão de escrita. |
| **Deslocamento não aplicado** | Uso de uma versão antiga do Aspose.3D. | Atualize para a biblioteca mais recente onde `setOffsetTop` é suportado. |
| **Nó filho não visível** | Transformação não aplicada. | Certifique‑se de chamar `getTransform().setTranslation` após criar o nó filho. |

## Perguntas frequentes

**Q: O Aspose.3D é compatível com diferentes IDEs Java?**  
A: Sim, funciona perfeitamente com Eclipse, IntelliJ IDEA, NetBeans e outras IDEs.

**Q: Posso aplicar texturas aos objetos 3D criados?**  
A: Absolutamente! Use a classe `Material` para atribuir texturas e propriedades de superfície.

**Q: Existem opções de licenciamento para o Aspose.3D?**  
A: Diversos modelos de licenciamento estão disponíveis; você pode explorá‑los **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Q: Como posso obter ajuda ou compartilhar experiências?**  
A: Participe do **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** para suporte e discussões.

**Q: Uma licença temporária está disponível para testes?**  
A: Sim, uma **licença temporária Aspose** pode ser obtida para avaliação **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

---

**Last updated:** 2026-08-12  
**Tested with:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

---

{{< blocks/products/products-backtop-button >}}

## Tutoriais Relacionados

- [Como criar modelos de cilindro com Aspose.3D para Java](/3d/java/cylinders/)
- [Como criar forma de ventilador cilíndrico usando Aspose.3D para Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Criar nós filhos e exportar FBX em Java com Aspose.3D](/3d/java/geometry/build-node-hierarchies/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}