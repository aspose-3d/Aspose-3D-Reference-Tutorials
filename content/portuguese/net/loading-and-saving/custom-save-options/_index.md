---
title: Carregando e salvando - opções de salvamento personalizadas
linktitle: Carregando e salvando - opções de salvamento personalizadas
second_title: API Aspose.3D .NET
description: Explore o poder do Aspose.3D para .NET. Aprenda como personalizar seu salvamento de cena 3D com guias passo a passo nos formatos Collada, 3DS, FBX, OBJ, STL, U3D, glTF, DRC e RVM.
type: docs
weight: 21
url: /pt/net/loading-and-saving/custom-save-options/
---
## Introdução

Bem-vindo ao mundo do Aspose.3D para .NET! Se você deseja aprimorar seus recursos de desenvolvimento 3D, você está no lugar certo. Neste tutorial, nos aprofundaremos nas funcionalidades de Carregar e Salvar, focando especificamente nas Opções de Salvamento Personalizado. Aspose.3D for .NET é uma biblioteca poderosa que permite aos desenvolvedores manipular e salvar cenas 3D com eficiência.

## Pré-requisitos

Antes de começarmos a explorar os recursos interessantes do Aspose.3D, certifique-se de ter os seguintes pré-requisitos:

- Compreensão básica do desenvolvimento em C# e .NET.
-  Biblioteca Aspose.3D para .NET instalada. Você pode baixá-lo no[página de lançamento](https://releases.aspose.com/3d/net/).
- Um ambiente de desenvolvimento configurado com Visual Studio ou qualquer outro IDE C# preferido.

## Importar namespaces

Para começar, vamos importar os namespaces necessários:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Agora que definimos o cenário, vamos dividir o tutorial em várias etapas.

## Etapa 1: opção de salvar Collada

Vamos começar com Collada, um formato de arquivo 3D popular. Siga estas etapas para personalizar as opções de salvamento do Collada:

### 1. Configurar diretório:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inicialize as opções de salvamento do Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Configurar opções:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Etapa 2: opção de salvamento 3DS discreto

Agora, vamos explorar o Discreet 3DS e suas opções de personalização:

### 1. Configurar diretório:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inicialize as opções de salvamento do 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Configurar opções:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Opções adicionais de configuração...
   ```

Continue esta abordagem passo a passo para opções de salvamento FBX, OBJ, STL, U3D, glTF e DRC, personalizando cada uma de acordo com suas necessidades.

## Etapa 3: opções de salvamento do glTF

Agora vamos nos concentrar no glTF, um formato amplamente utilizado em aplicações web e móveis. Personalize suas opções de salvamento glTF com estas etapas:

### 1. Inicialize o objeto de cena:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Defina as opções de salvamento do glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Salve o arquivo glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Siga uma estrutura semelhante para outras opções de salvamento, como DRC e RVM.

## Conclusão

Parabéns! Você explorou com sucesso as opções de salvamento personalizadas no Aspose.3D for .NET. Esta poderosa biblioteca oferece uma infinidade de opções para personalizar seu processo de salvamento de cenas 3D.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras estruturas .NET?

A1: Sim, Aspose.3D é compatível com vários frameworks .NET, garantindo flexibilidade em seu ambiente de desenvolvimento.

### Q2: Há alguma opção de licenciamento disponível para Aspose.3D?

 A2: Sim, você pode explorar opções de licenciamento[aqui](https://purchase.aspose.com/buy).

### Q3: Onde posso encontrar suporte para consultas relacionadas ao Aspose.3D?

 A3: Você pode buscar suporte no[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Existe um teste gratuito disponível?

 A4: Sim, você pode acessar uma avaliação gratuita[aqui](https://releases.aspose.com/).

### Q5: Como posso obter uma licença temporária para Aspose.3D?

 A5: Obtenha uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).