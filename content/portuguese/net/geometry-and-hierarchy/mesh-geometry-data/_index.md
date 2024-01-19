---
title: Trabalhando com dados de geometria de malha em cenas 3D
linktitle: Trabalhando com dados de geometria de malha em cenas 3D
second_title: API Aspose.3D .NET
description: Domine a arte da programação gráfica 3D com Aspose.3D para .NET. Crie, manipule e salve cenas 3D impressionantes sem esforço.
type: docs
weight: 15
url: /pt/net/geometry-and-hierarchy/mesh-geometry-data/
---
## Introdução

Bem-vindo ao emocionante mundo da programação gráfica 3D com Aspose.3D for .NET! Neste tutorial, nos aprofundaremos nas complexidades de trabalhar com dados de geometria de malha em cenas 3D usando Aspose.3D, uma biblioteca poderosa e versátil para desenvolvedores .NET. Quer você seja um programador experiente ou esteja apenas começando com gráficos 3D, este guia passo a passo o ajudará a dominar a arte de lidar com dados de geometria de malha sem esforço.

## Pré-requisitos

Antes de embarcarmos nesta jornada 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

- Conhecimento prático de programação C# e .NET.
- Visual Studio instalado em sua máquina.
-  Biblioteca Aspose.3D para .NET, que você pode baixar[aqui](https://releases.aspose.com/3d/net/).

Agora que está tudo pronto, vamos entrar no fascinante mundo da programação gráfica 3D!

## Importar namespaces

No seu projeto C#, comece importando os namespaces necessários:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

Esses namespaces fornecem acesso às classes e métodos essenciais necessários para trabalhar com cenas 3D e dados de geometria de malha.

## Etapa 1: inicializar a cena

```csharp
// Inicializar objeto de cena
Scene scene = new Scene();
```

Isso cria uma cena 3D em branco onde você pode construir e manipular seus modelos 3D.

## Etapa 2: definir vetores de cores

```csharp
// Definir vetores de cores
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

Especifique uma matriz de vetores de cores que serão aplicados a diferentes partes da sua cena 3D.

## Etapa 3: criar malha e definir cores

```csharp
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    // Inicializar objeto de nó de cubo
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    // Definir cor
    mat.DiffuseColor = color;
    
    // Definir material
    cube.Material = mat;
    
    // Definir tradução
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    // Adicionar nó de cubo
    scene.RootNode.ChildNodes.Add(cube);
}
```

Crie uma malha usando o método do construtor de polígonos e aplique cores a diferentes partes da cena.

## Passo 4: Salve a cena 3D

```csharp
// O caminho para o diretório de documentos.
var output = "Your Output Directory" + "MeshGeometryData.fbx";

//Salve cenas 3D nos formatos de arquivo suportados
scene.Save(output, FileFormat.FBX7400ASCII);
```

Especifique o diretório de saída e salve sua cena 3D no formato de arquivo FBX7400ASCII.

## Conclusão

Parabéns! Você aprendeu com sucesso como trabalhar com dados de geometria de malha em cenas 3D usando Aspose.3D for .NET. Este tutorial equipou você com as etapas essenciais para criar e manipular modelos 3D. Experimente, explore e eleve suas habilidades de programação gráfica 3D a novos patamares!

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: O Aspose.3D foi projetado principalmente para .NET, mas você pode explorar outros produtos Aspose que oferecem suporte a diferentes plataformas e idiomas.

### Q2: Existe uma avaliação gratuita disponível para Aspose.3D?

 A2: Sim, você pode acessar a avaliação gratuita[aqui](https://releases.aspose.com/).

### P3: Onde posso encontrar suporte e recursos adicionais?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.

### Q4: Como obtenho uma licença temporária para Aspose.3D?

 A4: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### P5: Quais formatos de arquivo são suportados para salvar cenas 3D?

 A5: Aspose.3D suporta vários formatos de arquivo, incluindo FBX, STL e muito mais. Consulte o[documentação](https://reference.aspose.com/3d/net/) para obter uma lista completa.