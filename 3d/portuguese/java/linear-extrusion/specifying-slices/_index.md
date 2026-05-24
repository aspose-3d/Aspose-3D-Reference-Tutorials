---
date: 2026-05-24
description: Aprenda como criar extrusão 3D com fatias usando Aspose.3D for Java.
  Este guia passo a passo cobre extrusão linear, definição do raio de arredondamento
  e exportação para OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Criar Extrusão 3D com Fatias – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Criar Extrusão 3D com Fatias – Aspose.3D for Java
url: /pt/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar Extrusão 3D com Fatias – Aspose.3D para Java

## Introdução

Se você precisa **criar extrusão 3D** objetos que pareçam suaves e precisos, controlar o número de fatias é fundamental. Neste tutorial, vamos percorrer como especificar as fatias ao realizar uma extrusão linear com Aspose.3D para Java. Você verá por que a contagem de fatias importa, como definir um raio de arredondamento e como exportar o resultado como um arquivo OBJ que pode ser usado em qualquer pipeline 3‑D.

## Respostas Rápidas
- **O que “fatias” controla?** O número de seções transversais intermediárias usadas para aproximar a superfície da extrusão.  
- **Qual método define a contagem de fatias?** `LinearExtrusion.setSlices(int)`  
- **Posso alterar o raio de arredondamento do perfil?** Sim, via `RectangleShape.setRoundingRadius(double)`  
- **Qual formato de arquivo é usado neste exemplo?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Preciso de uma licença para executar o código?** Um teste gratuito funciona para avaliação; uma licença comercial é necessária para produção.

`LinearExtrusion.setSlices(int)` define quantas fatias intermediárias a extrusão gerará.  
`RectangleShape.setRoundingRadius(double)` define o raio de canto de um perfil retangular.

## Como criar extrusão 3D Java com fatias?

Carregue seu perfil 2‑D, escolha uma contagem de fatias, defina o raio de arredondamento e chame `save` – todo o fluxo de trabalho cabe em algumas linhas. Aspose.3D para Java lida com a criação da geometria, interpolação de fatias e exportação OBJ automaticamente, permitindo que você se concentre na qualidade visual em vez de cálculos de malha de baixo nível.

## O que é uma extrusão linear com fatias?

Uma extrusão linear com fatias transforma uma forma 2‑D plana em um sólido 3‑D ao varrê‑la ao longo de uma linha reta enquanto gera um número configurável de seções transversais intermediárias. A contagem de fatias influencia diretamente a suavidade das bordas curvas, como cantos arredondados, ao serem renderizadas.

## Por que usar Aspose.3D para Java para criar extrusão 3D?

Aspose.3D oferece **controle programático total** sobre cada parâmetro de extrusão, suporta **mais de 50 formatos de entrada e saída** (incluindo OBJ, FBX, STL e GLTF) e pode processar **modelos com centenas de páginas** sem carregar o arquivo inteiro na memória. Ele funciona em qualquer plataforma com suporte a Java, não requer DLLs nativas e garante resultados determinísticos em Windows, Linux e macOS.

## Pré‑requisitos

1. **Java Development Kit** – JDK 8 ou superior instalado.  
2. **Aspose.3D for Java** – Baixe a biblioteca no site oficial [aqui](https://releases.aspose.com/3d/java/).  
3. Uma IDE ou editor de texto de sua escolha.

## Importar Pacotes

Adicione o namespace Aspose.3D ao seu projeto para que você possa acessar as classes de modelagem 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guia Passo a Passo

### Passo 1: Configurar a cena e definir o perfil

`RectangleShape` é uma classe que define um perfil de retângulo 2‑D.  
Primeiro criamos um `RectangleShape` e lhe atribuímos um **raio de arredondamento** para que os cantos fiquem suaves.  
`Scene` é o contêiner raiz para todos os nós e geometria.  
Em seguida, inicializamos uma nova `Scene` que conterá toda a geometria.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Passo 2: Criar objetos de nó filho para cada extrusão

`Node` representa um elemento no grafo da cena que pode conter geometria e transformações.  
Cada peça de geometria reside sob um `Node`. Aqui geramos dois nós irmãos – um para uma extrusão com poucas fatias e outro para uma extrusão com muitas fatias – e movemos o nó da esquerda um pouco para o lado para que os resultados sejam fáceis de comparar.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 3: Executar extrusão linear e definir fatias

`LinearExtrusion` é a classe que cria um sólido ao varrer um perfil linearmente.  
`LinearExtrusion` é a classe da Aspose.3D que gera um sólido ao extrudar um perfil 2‑D ao longo de uma linha reta. Usando uma **classe interna anônima** chamamos `setSlices` para controlar a suavidade. O nó da esquerda recebe apenas 2 fatias (grosseiras), enquanto o nó da direita recebe 10 fatias (suave).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Passo 4: Exportar OBJ – salvar a cena

Finalmente gravamos a cena em um arquivo Wavefront OBJ, um formato amplamente suportado por editores 3‑D e motores de jogos. Isso demonstra a capacidade de **exportar OBJ Java** da Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| **Extrusão aparece plana** | Contagem de fatias definida como 1 ou 0 | Certifique‑se de que `setSlices` seja chamado com um valor ≥ 2. |
| **Cantos arredondados parecem serrilhados** | Raio de arredondamento muito pequeno em relação à contagem de fatias | Aumente o raio ou a contagem de fatias para curvas mais suaves. |
| **Arquivo não encontrado ao salvar** | `MyDir` aponta para uma pasta inexistente | Crie o diretório antes ou use um caminho absoluto. |

## Perguntas Frequentes

**Q: Como posso baixar Aspose.3D para Java?**  
A: Você pode baixar a biblioteca [aqui](https://releases.aspose.com/3d/java/).

**Q: Onde posso encontrar a documentação do Aspose.3D?**  
A: Consulte a documentação [aqui](https://reference.aspose.com/3d/java/).

**Q: Existe uma versão de avaliação gratuita disponível?**  
A: Sim, você pode experimentar uma avaliação gratuita [aqui](https://releases.aspose.com/).

**Q: Como posso obter suporte para Aspose.3D?**  
A: Visite o fórum de suporte [aqui](https://forum.aspose.com/c/3d/18).

**Q: Posso adquirir uma licença temporária?**  
A: Sim, uma licença temporária pode ser obtida [aqui](https://purchase.aspose.com/temporary-license/).

---

**Última atualização:** 2026-05-24  
**Testado com:** Aspose.3D for Java 24.11 (mais recente no momento da escrita)  
**Autor:** Aspose

## Tutoriais Relacionados

- [Criar Extrusão 3D Java com Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Como Definir Direção na Extrusão Linear com Aspose.3D para Java](/3d/java/linear-extrusion/setting-direction/)
- [Criar Cena 3D com Torção na Extrusão Linear – Aspose.3D para Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}