---
title: Centro em Extrusão Linear
linktitle: Centro em Extrusão Linear
second_title: API Aspose.3D .NET
description: Explore o mundo da modelagem 3D com Aspose.3D for .NET. Centralize técnicas de extrusão linear, crie designs impressionantes e libere sua criatividade.
weight: 10
url: /pt/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centro em Extrusão Linear

## Introdução

Bem-vindo a este guia completo sobre como dominar a extrusão linear usando Aspose.3D para .NET. Se você deseja aprimorar suas habilidades de modelagem 3D e criar extrusões impressionantes, você está no lugar certo. Neste tutorial, nos aprofundaremos na técnica de extrusão linear, focando especificamente no aspecto de centralização para levar seus designs a um nível totalmente novo.

## Pré-requisitos

Antes de embarcarmos nesta jornada emocionante, certifique-se de ter os seguintes pré-requisitos em vigor:

- Compreensão básica da linguagem de programação C#.
- Visual Studio instalado em sua máquina.
-  Biblioteca Aspose.3D para .NET, que você pode baixar do[Documentação Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Certifique-se de ter acesso ao[Documentação Aspose.3D .NET](https://reference.aspose.com/3d/net/) para referência ao longo do tutorial.

## Importar namespaces

Para começar, vamos importar os namespaces necessários. Eles estabelecerão a base para nossa obra-prima de modelagem 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Etapa 1: inicializar o perfil base

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passo 2: Crie uma cena 3D

```csharp
Scene scene = new Scene();
```

## Etapa 3: criar nós esquerdo e direito

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Etapa 4: Execute a extrusão linear no nó esquerdo

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Etapa 5: definir plano de solo para referência

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Etapa 6: Execute a extrusão linear no nó direito

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Etapa 7: definir plano de solo para referência (nó direito)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Etapa 8: Salvar cena 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusão

Parabéns! Você dominou com sucesso a arte da extrusão linear com centralização usando Aspose.3D para .NET. Sinta-se à vontade para experimentar diferentes parâmetros e explorar as vastas possibilidades que esta técnica oferece.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D oferece suporte principalmente a linguagens .NET, como C# e VB.NET.

### P2: Onde posso encontrar suporte para consultas relacionadas ao Aspose.3D?

 A2: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte e discussões dedicados.

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?

 A3: Sim, você pode acessar a avaliação gratuita[aqui](https://releases.aspose.com/).

### Q4: Como posso obter uma licença temporária para Aspose.3D for .NET?

 A4: Você pode adquirir uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### P5: Onde posso adquirir a licença Aspose.3D for .NET?

 A5: Compre sua licença[aqui](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
