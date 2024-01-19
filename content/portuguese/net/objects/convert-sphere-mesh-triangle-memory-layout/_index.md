---
title: Convertendo malha de esfera em malha triangular com layout de memória personalizado
linktitle: Convertendo malha de esfera em malha triangular com layout de memória personalizado
second_title: API Aspose.3D .NET
description: Explore o Aspose.3D para .NET e converta facilmente Sphere Mesh em Triangle Mesh com layout de memória personalizado. Siga nosso guia passo a passo para uma integração perfeita.
type: docs
weight: 15
url: /pt/net/objects/convert-sphere-mesh-triangle-memory-layout/
---
## Introdução
Você está procurando aproveitar o poder do Aspose.3D for .NET para converter uma Sphere Mesh em uma Triangle Mesh com um layout de memória personalizado? Este guia passo a passo orientará você durante o processo, facilitando o acompanhamento até mesmo para iniciantes. Ao final deste tutorial, você terá um conhecimento sólido de como conseguir isso usando Aspose.3D for .NET.
## Pré-requisitos
Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:
- Conhecimento básico de programação .NET.
-  Biblioteca Aspose.3D para .NET instalada. Você pode baixá-lo no[Página de download do Aspose.3D para .NET](https://releases.aspose.com/3d/net/).
- Familiaridade com a linguagem de programação C#.
## Importar namespaces
Em seu projeto C#, certifique-se de importar os namespaces necessários para aproveitar a funcionalidade Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Runtime.InteropServices;
```
## Etapa 1: inicializar o objeto de cena
```csharp
// Inicializar objeto de cena
Scene scene = new Scene();
```
## Etapa 2: inicializar o objeto de classe do nó
```csharp
// Inicializar objeto de classe Node
Node cubeNode = new Node("sphere");
```
## Etapa 3: converter malha de esfera em TriMesh digitado
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Etapa 4: obter dados de vértice em estrutura personalizada
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Etapa 5: obtenha índices de 32 e 16 bits
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Etapa 6: gravar dados de vértice e índice no fluxo de memória
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Etapa 7: apontar o nó para a geometria da malha
```csharp
cubeNode.Entity = sphere;
```
## Etapa 8: adicionar nó à cena
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Etapa 9: Salvar cena 3D
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Etapa 10: exibir resultados
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```
## Conclusão
Parabéns! Você converteu com sucesso uma malha de esfera em uma malha de triângulo com um layout de memória personalizado usando Aspose.3D para .NET. Esta poderosa biblioteca fornece uma maneira perfeita de manipular objetos 3D em seus aplicativos .NET.
## Perguntas frequentes
### P: Posso usar o Aspose.3D for .NET com outras estruturas .NET?
R: Sim, o Aspose.3D for .NET é compatível com vários frameworks .NET.
### P: Onde posso encontrar documentação detalhada do Aspose.3D for .NET?
 R: Consulte o[Documentação do Aspose.3D para .NET](https://reference.aspose.com/3d/net/) para obter informações detalhadas.
### P: Como posso obter uma licença temporária do Aspose.3D for .NET?
 Uma visita[esse link](https://purchase.aspose.com/temporary-license/) para obter uma licença temporária.
### P: Há algum projeto de amostra disponível para Aspose.3D for .NET?
 R: Explore a documentação do Aspose.3D for .NET e[Repositório GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) para projetos de amostra.
### P: Existe uma comunidade ativa para suporte ao Aspose.3D for .NET?
 R: Sim, junte-se ao[Fórum Aspose.3D para .NET](https://forum.aspose.com/c/3d/18) para obter ajuda da comunidade.