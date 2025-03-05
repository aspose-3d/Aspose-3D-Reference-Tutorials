---
title: Animando propriedades para documentos em cenas 3D
linktitle: Animando propriedades para documentos em cenas 3D
second_title: API Aspose.3D .NET
description: Aprenda a animar propriedades 3D com Aspose.3D para .NET. Guia passo a passo para criar cenas dinâmicas.
type: docs
weight: 10
url: /pt/net/animation/property-to-document/
---
## Introdução

Se você está mergulhando no reino da criação e animação de cenas 3D em .NET, Aspose.3D é o seu kit de ferramentas ideal. Neste guia passo a passo, exploraremos o processo de animação de propriedades em cenas 3D usando Aspose.3D para .NET. Ao final, você estará equipado com o conhecimento necessário para dar vida aos seus projetos 3D.

## Pré-requisitos

Antes de embarcarmos nesta jornada emocionante, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca instalada. Você pode baixá-lo no[Site Aspose.3D](https://releases.aspose.com/3d/net/).

- Conhecimento de C#: A familiaridade com a linguagem de programação C# é essencial para a compreensão e implementação dos exemplos.

- Ambiente de Desenvolvimento Integrado (IDE): Use seu IDE preferido, como Visual Studio, para codificação junto com os exemplos.

- Conceitos básicos de cena 3D: uma compreensão dos conceitos básicos de cena 3D tornará sua jornada de aprendizado mais tranquila.

## Importar namespaces

Em seu código C#, certifique-se de importar os namespaces necessários para Aspose.3D. Aqui está um exemplo:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Etapa 1: inicializar o objeto de cena

```csharp
Scene scene = new Scene();
```

## Etapa 2: criar malha usando o Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Etapa 3: criar nós de cubo

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Etapa 4: Encontre a propriedade de tradução

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Etapa 5: crie um ponto de vinculação

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Etapa 6: vincular curva de animação no componente X

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Etapa 7: vincular curva de animação ao componente Z

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Etapa 8: Salvar cena 3D

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Etapa 9: exibir mensagem de sucesso

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Conclusão

Parabéns! Você acabou de dominar a arte de animar propriedades em cenas 3D usando Aspose.3D for .NET. Agora, deixe sua criatividade fluir enquanto você dá vida às suas criações 3D.

## perguntas frequentes

### Q1: Onde posso encontrar a documentação do Aspose.3D?

 A1: A documentação está disponível[aqui](https://reference.aspose.com/3d/net/).

### Q2: Como faço o download do Aspose.3D para .NET?

 A2: Você pode baixá-lo do[página de lançamento](https://releases.aspose.com/3d/net/).

### Q3: Existe um teste gratuito disponível?

 A3: Sim, você pode obter uma avaliação gratuita[aqui](https://releases.aspose.com/).

### Q4: Onde posso obter suporte para Aspose.3D?

 A4: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte.

### Q5: Posso obter uma licença temporária?

 A5: Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).