---
title: Carregando e salvando - Salvando cena 3D
linktitle: Carregando e salvando - Salvando cena 3D
second_title: API Aspose.3D .NET
description: Explore o poder do Aspose.3D para .NET. uma biblioteca versátil para manipulação perfeita de cenas 3D. Carregue, salve e compacte sem esforço.
type: docs
weight: 20
url: /pt/net/loading-and-saving/save-3d-scene/
---
## Introdução

Bem-vindo a uma emocionante jornada no reino da manipulação de cenas 3D usando Aspose.3D for .NET! Quer você seja um desenvolvedor experiente ou um entusiasta curioso, este tutorial irá guiá-lo através do processo de carregar, salvar e compactar cenas 3D sem esforço.

## Pré-requisitos

Antes de mergulhar no mundo cativante da manipulação de cenas 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Baixe e instale a biblioteca Aspose.3D do[Link para Download](https://releases.aspose.com/3d/net/).
-  Documentação: Familiarize-se com as funcionalidades da biblioteca através do abrangente[documentação](https://reference.aspose.com/3d/net/).
- Seu diretório de saída: Configure um diretório para armazenar os arquivos de saída gerados durante o tutorial.

## Importar namespaces

Vamos começar nossa exploração importando os namespaces necessários para nosso ambiente .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Carregando e salvando - Salvando cena 3D

### Etapa 1: carregar um documento 3D

```csharp
Scene scene = new Scene();
scene.Open(RunExamples.GetDataFilePath("document.fbx"));
```

 Nesta etapa, criamos um novo`Scene` objeto e carregar um documento 3D existente usando o`Open` método.

### Etapa 2: salvar cena em um stream

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

 Salve a cena 3D carregada em um fluxo de memória usando o`Save` método, especificando o formato de arquivo desejado (neste caso, FBX7500ASCII).

### Etapa 3: retroceder a posição do fluxo

```csharp
dstStream.Position = 0;
```

Redefina a posição do fluxo para prepará-lo para o próximo leitor, garantindo um processamento contínuo.

### Etapa 4: salvar a cena em um caminho local

```csharp
scene.Save("Your Output Directory" + "output_out.fbx", FileFormat.FBX7500ASCII);
```

Salve a cena 3D em um caminho local, fornecendo um diretório de saída e um nome de arquivo significativos.

## Compressão

Agora, vamos explorar as opções de compactação para cenas 3D.

### Etapa 1: carregar um documento 3D

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
```

 Semelhante ao exemplo anterior, carregue um documento 3D no`Scene` objeto.

### Etapa 2: desative a compactação e salve

```csharp
scene.Save("Your Output Directory" + "UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

Desative a compactação ao salvar a cena 3D, fornecendo um caminho de saída e nome de arquivo claros.

## Conclusão

Neste tutorial, nos aprofundamos nos aspectos fundamentais de carregar, salvar e compactar cenas 3D usando Aspose.3D para .NET. Armado com esse conhecimento, você está pronto para embarcar em sua própria jornada 3D e liberar as possibilidades criativas dentro do reino do Aspose.3D.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com vários formatos de arquivo 3D?

A1: Sim, Aspose.3D suporta uma ampla variedade de formatos de arquivo 3D, proporcionando flexibilidade em seus projetos.

### Q2: Posso integrar o Aspose.3D com outras bibliotecas .NET?

A2: Com certeza! Aspose.3D integra-se perfeitamente com outras bibliotecas .NET, aprimorando os recursos de seus aplicativos.

### Q3: Como posso obter licenciamento temporário para Aspose.3D?

 A3: Visite o[licença temporária](https://purchase.aspose.com/temporary-license/) página no site Aspose para obter uma licença temporária.

### P4: Onde posso procurar assistência ou estabelecer contacto com a comunidade?

 A4: Junte-se à vibrante comunidade Aspose.3D no[fórum](https://forum.aspose.com/c/3d/18) para buscar apoio, compartilhar experiências e colaborar com outros entusiastas.

### Q5: Existe uma avaliação gratuita disponível para Aspose.3D?

 A5: Sim, explore os recursos do Aspose.3D pegando seu[teste grátis](https://releases.aspose.com/) hoje!