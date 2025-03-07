---
title: Criando um documento 3D vazio
linktitle: Criando um documento 3D vazio
second_title: API Aspose.3D .NET
description: Explore o mundo da criação de documentos 3D com Aspose.3D for .NET. Crie, edite e salve cenas 3D impressionantes sem esforço.
weight: 11
url: /pt/net/loading-and-saving/create-empty-3d-document/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criando um documento 3D vazio

## Introdução

Bem-vindo ao mundo da criação de documentos 3D usando Aspose.3D for .NET! Neste tutorial, exploraremos os fundamentos do carregamento e salvamento de documentos 3D. Aspose.3D for .NET fornece um conjunto poderoso de ferramentas para trabalhar com cenas 3D e orientaremos você em cada etapa para ajudá-lo a começar sem problemas.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/net/).

## Importar namespaces

Para começar, importe os namespaces necessários em seu projeto .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Carregar e Salvar - Criando um Documento 3D Vazio

### Etapa 1: configure seu diretório de saída

```csharp
// O caminho para o diretório de documentos.
var output = "Your Output Directory" + "document.fbx";
```

### Etapa 2: crie um documento 3D vazio

```csharp
// ExStart:CriarEmpty3DDocument

// Crie um objeto da classe Scene
Scene scene = new Scene();

// Salve o documento da cena 3D no formato FBX
scene.Save(output);

// ExEnd:CriarEmpty3DDocument
```

### Etapa 3: exibir o resultado

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

Parabéns! Você acabou de criar seu primeiro documento 3D vazio usando Aspose.3D for .NET. Sinta-se à vontade para explorar mais recursos e funcionalidades para liberar todo o potencial desta biblioteca.

## Conclusão

 Neste tutorial, cobrimos os fundamentos da criação de um documento 3D vazio usando Aspose.3D para .NET. À medida que você continua sua jornada com o desenvolvimento 3D, consulte o[documentação](https://reference.aspose.com/3d/net/) para obter insights detalhados e recursos avançados.

## Perguntas frequentes

### Q1: O Aspose.3D for .NET é adequado para iniciantes?

A1: Sim, o Aspose.3D for .NET fornece uma interface amigável, tornando-o acessível tanto para iniciantes quanto para desenvolvedores experientes.

### Q2: Posso experimentar o Aspose.3D for .NET antes de comprar?

 A2: Com certeza! Você pode acessar um teste gratuito[aqui](https://releases.aspose.com/).

### Q3: Como posso obter suporte para Aspose.3D for .NET?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para buscar assistência e se conectar com a comunidade.

### Q4: As licenças temporárias estão disponíveis para Aspose.3D for .NET?

 A4: Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso comprar o Aspose.3D para .NET?

 A5: Você pode comprar a biblioteca[aqui](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
