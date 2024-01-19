---
title: Transformando Nó por Matriz de Transformação em Cenas 3D
linktitle: Transformando Nó por Matriz de Transformação em Cenas 3D
second_title: API Aspose.3D .NET
description: Transforme nós sem esforço em cenas 3D usando Aspose.3D para .NET. Aprenda transformações de nós passo a passo com tutorial.
type: docs
weight: 21
url: /pt/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Introdução

No domínio dinâmico dos gráficos e visualizações 3D, a capacidade de manipular objetos dentro de uma cena é um aspecto crucial. Aspose.3D for .NET capacita os desenvolvedores a transformar nós perfeitamente usando matrizes de transformação, adicionando uma camada de criatividade e controle às cenas 3D. Este tutorial irá guiá-lo passo a passo pelo processo de transformação de um nó em uma cena 3D.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

1.  Biblioteca Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D instalada em seu projeto .NET. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).

2. Ambiente de desenvolvimento: configure um ambiente de desenvolvimento .NET funcional e, se ainda não o fez, crie um novo projeto onde implementará as transformações.

## Importar namespaces

Comece importando os namespaces necessários para o seu projeto .NET. Esses namespaces fornecem as classes e métodos essenciais para manipulação de cenas 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Agora que cobrimos o básico, vamos dividir o processo de transformação em um guia passo a passo.

## Etapa 1: inicializar cena e nó

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Inicializar objeto de cena
Scene scene = new Scene();

// Inicializar objeto de classe Node
Node cubeNode = new Node("cube");
```

Nesta etapa, criamos uma nova cena 3D e um nó denominado “cubo” dentro dessa cena.

## Passo 2: Criar Malha e Definir Geometria

```csharp
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Aponte o nó para a geometria da malha
cubeNode.Entity = mesh;
```

Aqui, geramos uma malha usando o método construtor de polígonos e a atribuímos ao nó, estabelecendo a geometria do nosso cubo.

## Etapa 3: definir matriz de tradução personalizada

```csharp
// Definir matriz de tradução personalizada
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Defina uma matriz de tradução personalizada para determinar a transformação específica aplicada ao nó. Ajuste os valores da matriz conforme necessário para a transformação desejada.

## Etapa 4: adicionar nó à cena

```csharp
// Adicione um cubo à cena
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Inclua o nó do cubo na cena, tornando-o parte do ambiente 3D geral.

## Etapa 5: salve a cena

```csharp
// O caminho para o diretório de documentos.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Salve cenas 3D nos formatos de arquivo suportados
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Especifique o diretório de saída e o nome do arquivo e salve a cena 3D no formato de arquivo desejado. Neste exemplo, salvamos no formato FBX7500ASCII.

## Conclusão

Parabéns! Você transformou com sucesso um nó usando uma matriz de transformação em uma cena 3D com Aspose.3D para .NET. Esse recurso abre portas para aplicações 3D diversas e visualmente cativantes.

## Perguntas frequentes

### Q1: O que é uma matriz de transformação em gráficos 3D?

A1: Uma matriz de transformação é uma representação matemática usada para aplicar várias transformações (translação, rotação, escala) a objetos no espaço 3D.

### P2: Posso aplicar múltiplas transformações a um único nó?

A2: Sim, você pode combinar múltiplas transformações multiplicando suas respectivas matrizes e aplicando o resultado ao nó.

### P3: Existem outros formatos de arquivo suportados para salvar cenas 3D?

 A3: Aspose.3D for .NET suporta vários formatos de arquivo, incluindo STL, GLTF, OBJ e muito mais. Consulte o[documentação](https://reference.aspose.com/3d/net/) para uma lista abrangente.

### Q4: Como posso obter uma licença temporária para Aspose.3D for .NET?

 A4: Visite o[página de licença temporária](https://purchase.aspose.com/temporary-license/) no site Aspose para obter uma licença temporária para fins de avaliação.

### Q5: Onde posso procurar assistência ou conectar-me com a comunidade Aspose.3D?

A5: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para fazer perguntas, compartilhar experiências e conectar-se com outros desenvolvedores usando Aspose.3D.