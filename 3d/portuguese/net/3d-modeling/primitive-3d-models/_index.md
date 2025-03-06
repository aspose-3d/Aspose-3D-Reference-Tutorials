---
title: Criação de modelos 3D primitivos
linktitle: Criação de modelos 3D primitivos
second_title: API Aspose.3D .NET
description: Explore o mundo da modelagem 3D com Aspose.3D for .NET. Crie modelos primitivos impressionantes sem esforço.
weight: 10
url: /pt/net/3d-modeling/primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criação de modelos 3D primitivos

## Introdução

Bem-vindo ao emocionante mundo da modelagem 3D com Aspose.3D for .NET! Neste tutorial abrangente, exploraremos passo a passo o processo de criação de modelos 3D primitivos usando Aspose.3D. Quer você seja um desenvolvedor experiente ou um iniciante curioso, este guia o ajudará a aproveitar o poder do Aspose.3D para criar elementos 3D visualmente impressionantes para seus projetos.

## Pré-requisitos

Antes de mergulharmos no fascinante reino da modelagem 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D for .NET: Baixe e instale a biblioteca Aspose.3D for .NET do[Link para Download](https://releases.aspose.com/3d/net/).

- Ambiente de Desenvolvimento: Configure um ambiente de desenvolvimento .NET, garantindo compatibilidade com Aspose.3D.

Agora que você tem o essencial, vamos embarcar em nossa jornada para criar modelos 3D primitivos passo a passo.

## Importar namespaces

Comece importando os namespaces necessários para acessar a funcionalidade fornecida pelo Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Com esses namespaces implementados, você está pronto para liberar o poder do Aspose.3D em seu aplicativo .NET.

## Etapa 1: inicializar um objeto de cena

```csharp
//Inicializar um objeto Scene
Scene scene = new Scene();
```

Crie um novo objeto de cena, que servirá como tela para sua obra-prima 3D.

## Etapa 2: crie um modelo de caixa

```csharp
// Crie um modelo de caixa
scene.RootNode.CreateChildNode("box", new Box());
```

Adicione um modelo de caixa à raiz da sua cena. Personalize as dimensões e propriedades da caixa de acordo com a sua visão criativa.

## Etapa 3: Crie um modelo de cilindro

```csharp
// Crie um modelo de cilindro
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Aprimore sua cena introduzindo um modelo de cilindro. Ajuste seus parâmetros para obter a forma e o tamanho desejados.

## Etapa 4: salvar o desenho no formato FBX

```csharp
// Salvar desenho no formato FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Salve sua obra-prima 3D no formato FBX. Escolha um diretório de saída e um nome de arquivo adequados para sua criação.

## Etapa 5: exibir mensagem de sucesso

```csharp
// Exibir mensagem de sucesso
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Comemore sua conquista! A cena é construída com sucesso a partir de modelos 3D primitivos e o arquivo é salvo.

## Conclusão

 Parabéns! Você criou com sucesso modelos 3D impressionantes usando Aspose.3D para .NET. Este guia cobriu o básico, mas as possibilidades são ilimitadas. Explore o[documentação](https://reference.aspose.com/3d/net/) para recursos e técnicas mais avançadas.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D suporta principalmente .NET, mas existem outras versões disponíveis para Java e outras plataformas.

### P2: Existe um teste gratuito disponível?

 A2: Sim, você pode explorar os recursos do Aspose.3D com um[teste grátis](https://releases.aspose.com/).

### Q3: Onde posso encontrar suporte para Aspose.3D para .NET?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.

### P4: Como posso obter uma licença temporária?

 A4: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Há algum exemplo de tutorial disponível?

 A5: Sim, explore mais tutoriais e exemplos no[documentação](https://reference.aspose.com/3d/net/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
