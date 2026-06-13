---
date: 2026-06-13
description: Aprenda um tutorial de gráficos 3D em Java sobre como controlar o centro
  na extrusão linear com Aspose.3D, incluindo como definir o raio de arredondamento
  e salvar o arquivo OBJ em Java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Controlando o Centro na Extrusão Linear com Aspose.3D para Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Criar Malha 3D Java – Centro na Extrusão Linear
url: /pt/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar Malha 3D Java – Centro na Extrusão Linear

## Introdução

Se você está criando visualizações 3‑D em Java, dominar técnicas de extrusão é essencial. Este **java 3d graphics tutorial** mostra como **create 3d mesh java** objetos controlando o centro de uma extrusão linear com Aspose.3D for Java. Ao final deste guia você entenderá por que a propriedade `center` é importante, como **set rounding radius**, e como **save obj file java**‑compatible output. Você também verá como **export 3d model obj** para uso em qualquer editor 3‑D importante.

## Respostas Rápidas
- **O que a propriedade center faz?** Ela determina se a extrusão é simétrica em torno da origem do perfil.  
- **Preciso de uma licença para executar o código?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Qual formato de arquivo é usado para o resultado?** A cena é salva como um arquivo Wavefront OBJ.  
- **Posso mudar o número de fatias?** Sim, use `setSlices(int)` no objeto `LinearExtrusion`.  
- **O Aspose.3D é compatível com Java 8+?** Absolutamente – ele suporta todas as versões modernas do Java.

## O que é um java 3d graphics tutorial?

Um **java 3d graphics tutorial** é um guia passo a passo que ensina como usar bibliotecas Java para criar, manipular e renderizar objetos tridimensionais. Neste tutorial você aprenderá a **create 3d mesh java** convertendo um perfil 2‑D em um modelo 3‑D completo, controlar seu alinhamento central, arredondar cantos da extrusão e, finalmente, exportar o resultado como um arquivo OBJ que qualquer programa 3‑D pode ler.

## Por que usar Aspose.3D para Java?

Aspose.3D for Java fornece uma API de alto nível que elimina a necessidade de cálculos manuais de malha, permitindo que você se concentre no design em vez da geometria de baixo nível. Ele suporta **50+ input and output formats** — incluindo OBJ, FBX, STL e GLTF — para que você possa **export 3d model obj** ou qualquer outro formato com uma única chamada de método. A biblioteca processa cenas com centenas de páginas sem carregar o arquivo inteiro na memória, oferecendo **até 3× melhor desempenho** comparado com pipelines OpenGL brutos em hardware de servidor típico.

## Pré-requisitos

1. **Ambiente de Desenvolvimento Java** – JDK 8 ou mais recente instalado.  
2. **Aspose.3D for Java** – Baixe a biblioteca e a documentação [aqui](https://reference.aspose.com/3d/java/).  
3. **Diretório de Documentos** – Crie uma pasta na sua máquina para armazenar os arquivos gerados; nos referiremos a ela como **“Your Document Directory.”**

## Importar Pacotes

No seu IDE Java, importe as classes Aspose.3D que você precisará. Isso fornece ao compilador acesso aos recursos de extrusão e construção de cena.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Guia Passo a Passo

### Passo 1: Configurar o Perfil Base

Primeiro, crie a forma 2‑D que será extrudida. Aqui usamos um retângulo e **set rounding radius** para 0.3, o que suaviza os cantos e demonstra como **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Passo 2: Criar uma Cena 3D

**Scene** é o contêiner de nível superior que contém todos os objetos 3‑D, luzes e câmeras.

```java
Scene scene = new Scene();
```

### Passo 3: Adicionar Nós Esquerdo e Direito

Um **Node** representa um objeto transformável no grafo da cena, permitindo posicionamento e hierarquia.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 4: Extrusão Linear – Sem Centro (Nó Esquerdo)

**LinearExtrusion** converte um perfil 2‑D em uma malha 3‑D varrendo-o ao longo de uma linha reta.  
**setCenter(boolean)** alterna se a extrusão está centrada em torno da origem do perfil.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Passo 5: Adicionar um Plano de Chão para Referência (Nó Esquerdo)

Uma caixa fina funciona como um piso visual, ajudando a ver a orientação da extrusão.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Passo 6: Extrusão Linear – Centralizada (Nó Direito)

Agora repita a extrusão, desta vez habilitando `center`. A geometria será simétrica em torno da origem do perfil, proporcionando um resultado **create 3d mesh java** perfeitamente equilibrado.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Passo 7: Adicionar um Plano de Chão para Referência (Nó Direito)

Mesmo plano de chão para o lado direito, tornando a comparação clara.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Passo 8: Salvar a Cena 3D

Finalmente, exporte a cena inteira para um arquivo Wavefront OBJ – um formato prontamente utilizável na maioria dos editores 3‑D. O método `save` converte automaticamente a malha para a especificação OBJ, permitindo que você **save obj file java** sem processamento adicional.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| **Extrusion appears offset** | `setCenter(false)` leaves the profile anchored at its corner. | Use `setCenter(true)` for symmetric results. |
| **OBJ file is empty** | Output directory path is incorrect or missing write permissions. | Verify `MyDir` points to an existing folder and the application has write access. |
| **Rounded corners look sharp** | Rounding radius is too small relative to rectangle size. | Increase the radius value (e.g., `setRoundingRadius(0.5)`). |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para Java em projetos comerciais?

A1: Sim, Aspose.3D para Java está disponível para uso comercial. Para detalhes de licenciamento, visite [aqui](https://purchase.aspose.com/buy).

### Q2: Existe uma versão de avaliação gratuita disponível?

A2: Sim, você pode explorar uma versão de avaliação gratuita do Aspose.3D para Java [aqui](https://releases.aspose.com/).

### Q3: Onde posso encontrar suporte para Aspose.3D para Java?

A3: O fórum da comunidade Aspose.3D é um ótimo lugar para buscar suporte e compartilhar suas experiências. Visite o fórum [aqui](https://forum.aspose.com/c/3d/18).

### Q4: Preciso de uma licença temporária para testes?

A4: Sim, se você precisar de uma licença temporária para fins de teste, pode obtê‑la [aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso encontrar a documentação?

A5: A documentação para Aspose.3D para Java está disponível [aqui](https://reference.aspose.com/3d/java/).

## Conclusão

Ao concluir este **java 3d graphics tutorial**, você agora sabe como **create 3d mesh java** objetos, controlar o centro de uma extrusão linear, ajustar o raio de arredondamento e **save obj file java** usando Aspose.3D. Essas técnicas dão a você controle detalhado sobre a simetria da malha, o que é vital para ativos de jogos, protótipos CAD e visualizações científicas. Sinta-se à vontade para experimentar diferentes perfis, contagens de fatias e formatos de exportação para expandir sua caixa de ferramentas 3‑D.

---

**Last Updated:** 2026-06-13  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Tutoriais Relacionados

- [Criar Extrusão 3D Java com Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Como Definir Direção na Extrusão Linear com Aspose.3D para Java](/3d/java/linear-extrusion/setting-direction/)
- [Criar Cena 3D com Torção na Extrusão Linear – Aspose.3D para Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}