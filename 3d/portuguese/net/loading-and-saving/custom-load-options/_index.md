---
title: Opções de carregamento personalizadas
linktitle: Opções de carregamento personalizadas
second_title: API Aspose.3D .NET
description: Explore o Aspose.3D for .NET, a solução definitiva para carregamento e salvamento contínuo de modelos 3D.
type: docs
weight: 15
url: /pt/net/loading-and-saving/custom-load-options/
---
## Introdução

Bem-vindo ao mundo do Aspose.3D for .NET – uma biblioteca poderosa que permite aos desenvolvedores trabalhar perfeitamente com arquivos 3D. Neste tutorial, nos aprofundaremos nas complexidades de carregar e salvar modelos 3D, com foco nas opções de carregamento personalizadas. Quer você seja um desenvolvedor experiente ou um novato, este guia irá guiá-lo passo a passo pelo processo, garantindo que você aproveite todo o potencial do Aspose.3D para .NET.

## Pré-requisitos

Antes de embarcarmos nesta jornada, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca instalada. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).

- Diretório de documentos: Crie um diretório para armazenar seus arquivos de modelo 3D.

Agora que você tem o essencial, vamos mergulhar no emocionante mundo da manipulação de modelos 3D!

## Importar namespaces

Primeiramente, vamos importar os namespaces necessários. Isso preparará o terreno para nossa jornada no reino Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Carregando e salvando - opções de carregamento personalizadas

### Etapa 1: Carregando arquivos Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Definir opções personalizadas
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carregar arquivo com as opções de carregamento
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Passo 2: Carregando Arquivos OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Definir opções personalizadas
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carregar arquivo com as opções de carregamento
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Etapa 3: Carregando arquivos STL

```csharp
private static void STLLoadOption()
{
    // O caminho para o diretório de documentos.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Definir opções personalizadas
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carregar arquivo com as opções de carregamento
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Etapa 4: Carregando arquivos U3D

```csharp
private static void U3DLoadOption()
{
    // O caminho para o diretório de documentos.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Definir opções personalizadas
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carregar arquivo com as opções de carregamento
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Etapa 5: Carregando arquivos glTF

```csharp
private static void glTFLoadOptions()
{
    // O caminho para o diretório de documentos.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Definir opções personalizadas
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Etapa 6: Carregando arquivos PLY

```csharp
private static void PlyLoadOptions()
{
    // O caminho para o diretório de documentos.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Definir opções personalizadas
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Etapa 7: Carregando arquivos FBX

```csharp
private static void FBXLoadOptions()
{
    // O caminho para o diretório de documentos.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Definir opções personalizadas
    scene.Open("test.FBX", opt);

    // Propriedades de saída definidas em GlobalSettings no arquivo FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusão

Parabéns! Você navegou com sucesso pelo intrincado mundo de carregar e salvar modelos 3D usando Aspose.3D for .NET. Este tutorial abordou vários formatos de arquivo e suas opções de carregamento personalizadas, permitindo manipular ativos 3D com facilidade.

## Perguntas frequentes

### Q1: O Aspose.3D for .NET é adequado para iniciantes?

A1: Com certeza! Aspose.3D for .NET fornece uma interface amigável, tornando-o acessível para desenvolvedores de todos os níveis.

### Q2: Posso usar Aspose.3D para projetos comerciais?

A2: Sim, o Aspose.3D for .NET vem com uma licença comercial, permitindo que você o utilize em seus projetos.

### Q3: Há alguma limitação nos formatos de arquivo suportados?

 A3: Aspose.3D for .NET suporta uma ampla variedade de formatos de arquivo 3D populares, incluindo OBJ, STL, FBX e muito mais. Consulte o[documentação](https://reference.aspose.com/3d/net/) para uma lista abrangente.

### Q4: Existe uma versão de teste disponível?

A4: Sim, você pode explorar os recursos do Aspose.3D for .NET baixando o[teste grátis](https://releases.aspose.com/).

### Q5: Onde posso buscar suporte para Aspose.3D for .NET?

 A5: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e assistência comunitária.