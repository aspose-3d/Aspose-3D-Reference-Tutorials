---
title: Transformando Nó por Quaternion
linktitle: Transformando Nó por Quaternion
second_title: API Aspose.3D .NET
description: Aprenda a transformar nós 3D com quaternions usando Aspose.3D for .NET. Guia passo a passo para iniciantes.
type: docs
weight: 20
url: /pt/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## Introdução

Bem-vindo a um guia passo a passo sobre como transformar um nó por quaternion em cenas 3D usando Aspose.3D para .NET. Neste tutorial, exploraremos os poderosos recursos do Aspose.3D para .NET e percorreremos o processo de adição de transformações a um nó 3D usando quaternions.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D instalada. Você pode baixá-lo no[página de lançamento](https://releases.aspose.com/3d/net/).

- Ambiente de desenvolvimento: Configure seu ambiente de desenvolvimento .NET com as ferramentas e configurações necessárias.

- Compreensão básica dos conceitos 3D: A familiaridade com gráficos e conceitos 3D será útil.

## Importar namespaces

Em seu projeto .NET, inclua os namespaces necessários para Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Etapa 1: inicializar o objeto de cena

```csharp
// ExStart: AddTransformationToNodeByQuaternion
// Inicializar objeto de cena
Scene scene = new Scene();
```

## Etapa 2: inicializar o objeto de classe do nó

```csharp
// Inicializar objeto de classe Node
Node cubeNode = new Node("cube");
```

## Etapa 3: Criar malha usando Polygon Builder

```csharp
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Etapa 4: apontar o nó para a geometria da malha

```csharp
// Aponte o nó para a geometria da malha
cubeNode.Entity = mesh;
```

## Etapa 5: definir rotação usando Quaternion

```csharp
// Definir rotação
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Etapa 6: definir a tradução

```csharp
// Definir tradução
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Passo 7: Adicionar Cubo à Cena

```csharp
// Adicione um cubo à cena
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Etapa 8: Salvar cena 3D

```csharp
// O caminho para o diretório de documentos.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Salve cenas 3D nos formatos de arquivo suportados
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd: AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Conclusão

 Parabéns! Você aprendeu com sucesso como transformar um nó por quaternion em cenas 3D usando Aspose.3D para .NET. Explore mais recursos e possibilidades consultando o[documentação](https://reference.aspose.com/3d/net/).

## Perguntas frequentes

### Q1: O que é um quaternion em gráficos 3D?

A1: Quaternions são entidades matemáticas usadas para representar rotações no espaço 3D.

### Q2: Como posso baixar o Aspose.3D para .NET?

 A2: Você pode baixar a biblioteca do[página de lançamento](https://releases.aspose.com/3d/net/).

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?

 A3: Sim, você pode obter uma avaliação gratuita em[aqui](https://releases.aspose.com/).

### Q4: Onde posso encontrar suporte para Aspose.3D para .NET?

 A4: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões.

### Q5: Como obtenho uma licença temporária para Aspose.3D?

 A5: Obtenha uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).
