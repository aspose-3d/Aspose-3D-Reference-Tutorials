---
title: Transformando o nó por ângulos de Euler
linktitle: Transformando o nó por ângulos de Euler
second_title: API Aspose.3D .NET
description: Aprenda a transformar nós 3D sem esforço com Aspose.3D for .NET. Siga nosso guia passo a passo para obter resultados impressionantes em seus projetos.
type: docs
weight: 19
url: /pt/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## Introdução

Bem-vindo a este tutorial abrangente sobre como transformar nós por ângulos de Euler em cenas 3D usando Aspose.3D para .NET. Neste guia, mergulharemos no emocionante mundo dos gráficos 3D e exploraremos o processo de adição de transformações a um nó usando ângulos de Euler. Aspose.3D for .NET fornece ferramentas poderosas para trabalhar com cenas e malhas 3D, tornando-o uma excelente escolha para desenvolvedores que buscam versatilidade e eficiência em seus projetos.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Biblioteca Aspose.3D for .NET: Certifique-se de ter a biblioteca Aspose.3D instalada. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).

- Ambiente de desenvolvimento: configure seu ambiente de desenvolvimento .NET preferido, como Visual Studio.

## Importar namespaces

Comece importando os namespaces necessários para acessar a funcionalidade fornecida pelo Aspose.3D for .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Agora, vamos dividir o exemplo em várias etapas para uma compreensão clara.

## Etapa 1: inicializar o objeto de cena

```csharp
// ExStart: AddTransformationToNodeByEulerAngles
// Inicializar objeto de cena
Scene scene = new Scene();
```

 Comece criando uma nova cena 3D usando o`Scene` aula.


## Etapa 2: Criar malha usando caixa primitiva

```csharp
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = (new Box()).ToMesh();
```

 Invoque um método (neste caso,`CreateMeshUsingPolygonBuilder` de um costume`Common`class) para gerar uma malha para o objeto 3D.

## Etapa 3: crie um nó de contêiner para a malha

```csharp
// Aponte o nó para a geometria da malha
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

 Crie um nó dentro da cena usando o`Node` aula. Este nó servirá como contêiner para nosso objeto 3D.

## Etapa 4: definir ângulos de Euler e tradução

```csharp
// Ângulos de Euler
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Definir tradução
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Defina os ângulos de Euler e a translação do nó para posicioná-lo no espaço 3D.

## Etapa 5: salve a cena 3D

```csharp
// O caminho para o diretório de documentos.
var output = "TransformationToNode.fbx";

// Salve cenas 3D nos formatos de arquivo suportados
scene.Save(output);
// ExEnd: AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Especifique o diretório de saída e salve a cena 3D, incluindo o nó transformado, no formato de arquivo desejado (FBX7500ASCII neste caso).

## Conclusão

Parabéns! Você aprendeu com sucesso como transformar um nó por ângulos de Euler em cenas 3D usando Aspose.3D para .NET. Esta poderosa biblioteca abre portas para infinitas possibilidades no desenvolvimento de gráficos 3D.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com outras ferramentas de modelagem 3D?

A1: Aspose.3D suporta vários formatos de arquivo 3D, melhorando a compatibilidade com ferramentas de modelagem populares.

### P2: Posso aplicar múltiplas transformações a um único nó?

A2: Sim, você pode combinar e aplicar múltiplas transformações para obter efeitos complexos.

### Q3: Onde posso encontrar documentação adicional do Aspose.3D?

 A3: Consulte o[documentação](https://reference.aspose.com/3d/net/) para obter informações detalhadas e exemplos.

### Q4: Preciso de uma licença para usar o Aspose.3D for .NET?

 A4: Sim, você pode obter uma licença[aqui](https://purchase.aspose.com/buy) ou explorar um[teste grátis](https://releases.aspose.com/).

### P5: Precisa de ajuda ou tem dúvidas específicas?

 A5: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio comunitário.