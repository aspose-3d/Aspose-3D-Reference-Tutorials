---
title: Conversão de material não PBR em PBR
linktitle: Conversão de material não PBR em PBR
second_title: API Aspose.3D .NET
description: Explore Aspose.3D for .NET - Converta materiais não PBR em PBR sem esforço. Tutorial abrangente e API poderosa.
weight: 16
url: /pt/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Conversão de material não PBR em PBR

## Introdução

Bem-vindo a este guia passo a passo sobre como usar Aspose.3D para .NET para converter materiais não PBR (renderização com base física) em materiais PBR. Aspose.3D é uma API poderosa que permite aos desenvolvedores trabalhar perfeitamente com formatos de arquivo 3D em seus aplicativos .NET.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos:

-  Aspose.3D for .NET: Certifique-se de ter a biblioteca Aspose.3D for .NET instalada. Você pode encontrar o link para download[aqui](https://releases.aspose.com/3d/net/).

- Compreensão básica de C#: Este tutorial pressupõe que você tenha um conhecimento fundamental de programação C#.

- IDE (Ambiente de Desenvolvimento Integrado): Escolha seu IDE preferido para desenvolvimento .NET, como Visual Studio.

## Importar namespaces

No seu código C#, comece importando os namespaces necessários:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Etapa 1: inicializar uma nova cena 3D

Comece criando uma nova cena 3D usando o seguinte código:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// inicializar uma nova cena 3D
var scene = new Scene();
```

## Passo 2: Crie um objeto 3D

A seguir, crie um objeto 3D, por exemplo, uma caixa:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Etapa 3: configurar a conversão de materiais

Configure opções de conversão de material para conversão de não PBR em PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Etapa 4: Salvar no formato GLTF 2.0

Salve a cena convertida no formato GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Repita essas etapas conforme necessário para seu caso de uso específico, garantindo que cada detalhe esteja configurado corretamente.

## Conclusão

Parabéns! Você aprendeu com sucesso como converter materiais não PBR em PBR usando Aspose.3D para .NET. Esta ferramenta poderosa abre possibilidades infinitas para manipulação de gráficos 3D em seus aplicativos .NET.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com todos os formatos de arquivo 3D?

A1: Sim, Aspose.3D suporta uma ampla variedade de formatos de arquivo 3D, proporcionando flexibilidade em seus projetos.

### Q2: Posso usar o Aspose.3D para aplicações comerciais?

 A2: Com certeza! Aspose.3D é um produto comercial e você pode comprá-lo[aqui](https://purchase.aspose.com/buy).

### P3: Preciso de uma licença temporária para testes?

 A3: Sim, você pode obter uma licença temporária para fins de teste[aqui](https://purchase.aspose.com/temporary-license/).

### Q4: Onde posso encontrar suporte para Aspose.3D?

 A4: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.

### Q5: Existe um teste gratuito disponível?

 A5: Sim, você pode explorar uma versão de avaliação gratuita[aqui](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
