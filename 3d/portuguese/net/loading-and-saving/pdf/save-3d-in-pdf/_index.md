---
title: Salvando 3D em PDF
linktitle: Salvando 3D em PDF
second_title: API Aspose.3D .NET
description: Explore Aspose.3D para .NET. Sua biblioteca ideal para modelagem e renderização 3D perfeitas. Salve facilmente modelos 3D em PDF.
weight: 19
url: /pt/net/loading-and-saving/pdf/save-3d-in-pdf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Salvando 3D em PDF

## Introdução

Bem-vindo ao nosso guia completo sobre como usar o Aspose.3D para .NET! Neste tutorial, orientaremos você no processo de carregamento e salvamento de modelos 3D, com foco na tarefa específica de salvar um modelo 3D em formato PDF. Aspose.3D for .NET é uma biblioteca poderosa que fornece ferramentas eficientes para trabalhar com arquivos 3D, tornando-se um recurso essencial para desenvolvedores e entusiastas da área.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca instalada. Caso contrário, você pode baixá-lo no[Documentação do Aspose.3D para .NET](https://reference.aspose.com/3d/net/).

- Ambiente de desenvolvimento: configure seu ambiente de desenvolvimento .NET preferido.

- Compreensão básica dos conceitos 3D: Familiarize-se com os conceitos 3D fundamentais, pois este guia pressupõe um conhecimento básico de modelagem 3D.

## Importar namespaces

Em seu projeto .NET, certifique-se de importar os namespaces necessários para acessar as funcionalidades fornecidas pelo Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## Etapa 1: crie uma nova cena

Comece inicializando uma nova cena 3D usando a biblioteca Aspose.3D. Isso serve como base para o seu modelo 3D.

```csharp
Scene scene = new Scene();
```

## Etapa 2: adicionar um nó filho do cilindro

Para demonstrar o processo de salvamento, vamos criar um modelo 3D simples - um cilindro. Adicione um cilindro como nó filho à cena.

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## Etapa 3: definir o modo de renderização e o esquema de iluminação

Defina o modo de renderização e o esquema de iluminação para sua cena 3D. Esta etapa permite personalizar a aparência visual do seu modelo.

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## Passo 4: Salvar em formato PDF

Finalmente, execute o processo de salvamento especificando o diretório de saída e o nome do arquivo. Neste caso, estamos salvando o modelo 3D em formato PDF.

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

Certifique-se de substituir "Seu diretório de saída" pelo caminho desejado.

## Conclusão

 Parabéns! Você aprendeu com sucesso como usar Aspose.3D for .NET para criar um modelo 3D simples e salvá-lo em formato PDF. Este é apenas o começo do que você pode alcançar com esta poderosa biblioteca. Explore mais recursos e possibilidades no[Documentação Aspose.3D](https://reference.aspose.com/3d/net/).

## Perguntas frequentes

### Q1: O Aspose.3D for .NET é compatível com todos os formatos de arquivo 3D?

R1: Sim, o Aspose.3D for .NET suporta uma ampla variedade de formatos de arquivo 3D, garantindo compatibilidade com vários padrões da indústria.

### P2: Posso personalizar os aspectos visuais do meu modelo 3D durante o processo de salvamento?

A2: Com certeza! Conforme mostrado no tutorial, você pode ajustar modos de renderização, esquemas de iluminação e muito mais para obter o resultado visual desejado.

### Q3: Onde posso encontrar suporte para Aspose.3D para .NET?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte da comunidade e discussões relacionadas ao Aspose.3D for .NET.

### Q4: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?

 A4: Sim, você pode acessar o[teste grátis](https://releases.aspose.com/) para explorar os recursos do Aspose.3D for .NET antes de fazer uma compra.

### Q5: Como posso obter uma licença temporária do Aspose.3D for .NET?

 A5: Para obter uma licença temporária, visite[esse link](https://purchase.aspose.com/temporary-license/) e siga as instruções fornecidas.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
