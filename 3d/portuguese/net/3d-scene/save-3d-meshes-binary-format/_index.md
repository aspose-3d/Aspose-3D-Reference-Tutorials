---
title: Salvando malhas 3D em formato binário personalizado
linktitle: Salvando malhas 3D em formato binário personalizado
second_title: API Aspose.3D .NET
description: Explore o mundo do 3D com Aspose.3D para .NET. Aprenda a salvar malhas em formato binário personalizado.
type: docs
weight: 13
url: /pt/net/3d-scene/save-3d-meshes-binary-format/
---
## Introdução

Bem-vindo ao mundo do Aspose.3D for .NET, uma biblioteca poderosa que permite aos desenvolvedores trabalhar com arquivos 3D sem esforço. Neste tutorial, nos aprofundaremos no processo de salvar malhas 3D em um formato binário personalizado usando Aspose.3D para .NET. Este guia pressupõe que você tenha um conhecimento básico de C# e esteja familiarizado com a biblioteca Aspose.3D.

## Pré-requisitos

Antes de prosseguirmos para o tutorial, certifique-se de ter o seguinte em vigor:

-  Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/net/).

- Ambiente de desenvolvimento: configure seu ambiente de desenvolvimento C# preferido, como Visual Studio.

- Arquivo 3D de entrada: Tenha um arquivo 3D (por exemplo, test.fbx) que deseja converter em um formato binário personalizado.

## Importar namespaces

Em seu código C#, inclua os namespaces necessários para acessar as funcionalidades do Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Etapa 1: carregar um arquivo 3D

Carregue seu arquivo 3D usando Aspose.3D. Neste exemplo, carregamos um arquivo chamado “test.fbx”:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Etapa 2: definir formato binário personalizado

Defina a estrutura do formato binário personalizado no qual deseja salvar suas malhas 3D. O exemplo usa uma estrutura com MeshBlock, Vertex e Triangle como componentes.

```csharp
// O layout de memória de um vértice é
// posição float[3];
// flutuar[3] normal;
// flutuar[3]uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Etapa 3: abra o arquivo para gravação

Abra um arquivo binário para gravação, onde serão salvas as malhas 3D convertidas:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Etapa 4: iterar por meio de nós e entidades

Visite cada nó na cena 3D e converta entidades de malha para o formato binário personalizado. Ignore luzes, câmeras e outras entidades que não sejam mesh:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (continuar processando)
    }
    return true;
});
```

## Etapa 5: converter e escrever pontos de controle e triângulos

Para cada entidade de malha, converta os pontos de controle no espaço mundial e grave-os no arquivo binário junto com os índices triangulares:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//O layout de memória da malha é:
// float[16] matriz_transformação;
// int vértices_count;
// int índices_contagem;
// vértice[vertices_count] vértices;
// índices ushort[indices_count];


//escrever transformação
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//escreva o número de vértices/índices
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//escrever vértices e índices
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Conclusão

Neste tutorial, abordamos o processo de salvar malhas 3D em um formato binário personalizado usando Aspose.3D para .NET. Esta poderosa biblioteca fornece aos desenvolvedores as ferramentas necessárias para manipular arquivos 3D perfeitamente. Experimente diferentes formatos e configurações para desbloquear todo o potencial do Aspose.3D em seus projetos.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D oferece suporte principalmente a linguagens .NET, mas você pode explorar opções de compatibilidade para outras linguagens.

### P2: Onde posso encontrar exemplos e recursos adicionais?

 A2: O[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18)é um ótimo lugar para encontrar apoio, exemplos e interagir com a comunidade.

### Q3: Existe uma versão de teste disponível para Aspose.3D?

 A3: Sim, você pode obter uma avaliação gratuita em[aqui](https://releases.aspose.com/).

### Q4: Como obtenho uma licença temporária para Aspose.3D?

 A4: Visita[esse link](https://purchase.aspose.com/temporary-license/) para obter uma licença temporária para fins de teste.

### Q5: Posso comprar o Aspose.3D para .NET?

 A5: Sim, você pode comprar Aspose.3D no[página de compra](https://purchase.aspose.com/buy).