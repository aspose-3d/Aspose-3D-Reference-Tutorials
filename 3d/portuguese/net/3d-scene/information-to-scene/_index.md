---
title: Extraindo informações para ativos de cena
linktitle: Extraindo informações para ativos de cena
second_title: API Aspose.3D .NET
description: Aprimore suas cenas 3D sem esforço com Aspose.3D for .NET. Aprenda a adicionar informações valiosas sobre ativos passo a passo. Baixe agora para uma experiência 3D dinâmica.
weight: 10
url: /pt/net/3d-scene/information-to-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Extraindo informações para ativos de cena

## Introdução

Bem-vindo a este tutorial abrangente sobre como usar Aspose.3D for .NET para extrair informações valiosas e aprimorar suas cenas 3D. Aspose.3D é uma biblioteca poderosa que permite aos desenvolvedores manipular cenas 3D perfeitamente em aplicativos .NET. Neste tutorial, focaremos na tarefa crucial de adicionar informações de ativos a uma cena.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca instalada. Você pode baixá-lo no[Página Aspose.3D para .NET](https://releases.aspose.com/3d/net/).

## Importar namespaces

Em seu projeto .NET, certifique-se de incluir os namespaces necessários para acessar as funcionalidades do Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Etapa 1: inicializar uma cena 3D

```csharp
Scene scene = new Scene();
```

 Crie uma nova cena 3D usando o`Scene` aula.

## Etapa 2: definir informações do aplicativo e do fornecedor

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Defina os nomes dos aplicativos e fornecedores associados à sua cena 3D.

## Passo 3: Definir Unidades de Medida

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Especifique as unidades de medida usadas em sua cena. Neste exemplo, usamos unidades egípcias antigas chamadas “pólo”, com 1 pólo igual a 60 cm.

## Etapa 4: salve a cena

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Salve a cena com as informações de ativos adicionadas em um formato de arquivo compatível com 3D. Ajuste o diretório de saída conforme necessário.

## Etapa 5: exibir mensagem de sucesso

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Informe ao usuário que as informações do ativo foram adicionadas com êxito e que o arquivo foi salvo.

## Conclusão

Parabéns! Você aprendeu com sucesso como usar o Aspose.3D for .NET para extrair e adicionar informações essenciais de ativos às suas cenas 3D. Esse conhecimento abre infinitas possibilidades para a criação de conteúdo 3D mais informativo e envolvente.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D oferece suporte principalmente a linguagens .NET, mas você pode explorar opções de interoperabilidade para outras linguagens.

### Q2: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?

 A2: Sim, você pode acessar o teste gratuito[aqui](https://releases.aspose.com/).

### Q3: Como obtenho suporte para consultas relacionadas ao Aspose.3D?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para comunidade e apoio.

### Q4: Posso adquirir uma licença temporária do Aspose.3D for .NET?

 A4: Sim, você pode adquirir uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso encontrar documentação detalhada para Aspose.3D for .NET?

 A5: Consulte o[documentação](https://reference.aspose.com/3d/net/) para obter informações detalhadas.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
