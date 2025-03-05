---
title: Compreendendo a hierarquia de nós
linktitle: Compreendendo a hierarquia de nós
second_title: API Aspose.3D .NET
description: Desbloqueie o poder do Aspose.3D para .NET! Mergulhe na manipulação da hierarquia de nós com este guia passo a passo. Crie cenas 3D impressionantes sem esforço.
type: docs
weight: 16
url: /pt/net/geometry-and-hierarchy/node-hierarchy/
---
## Introdução

Bem-vindo ao mundo do Aspose.3D for .NET, uma biblioteca poderosa que permite aos desenvolvedores trabalhar perfeitamente com cenas e modelos 3D em seus aplicativos .NET. Neste tutorial, nos aprofundaremos nos meandros da compreensão da hierarquia de nós em cenas 3D usando Aspose.3D. Ao final deste guia, você terá uma compreensão sólida de como manipular a estrutura de cenas 3D por meio de nós, permitindo criar experiências visuais impressionantes.

## Pré-requisitos

Antes de embarcarmos nesta jornada 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Biblioteca Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D integrada ao seu projeto .NET. Se você ainda não fez isso, vá até o[documentação](https://reference.aspose.com/3d/net/) para orientação.

-  Baixe a biblioteca: Se você não baixou a biblioteca Aspose.3D, pegue a versão mais recente no[Link para Download](https://releases.aspose.com/3d/net/) e siga as instruções de instalação fornecidas na documentação.

-  Obtenha uma licença: Para desbloquear todo o potencial do Aspose.3D, você precisa de uma licença válida. Se você não tiver um, você pode obtê-lo[aqui](https://purchase.aspose.com/buy) ou opte por um[teste grátis](https://releases.aspose.com/) para explorar suas capacidades.

-  Suporte e comunidade: Junte-se à comunidade Aspose.3D no[Fórum de suporte](https://forum.aspose.com/c/3d/18)para se conectar com outros desenvolvedores, buscar ajuda e ficar atualizado sobre os desenvolvimentos mais recentes.

-  Licença temporária (opcional): Se você estiver explorando o Aspose.3D antes de fazer uma compra, considere obter uma[licença temporária](https://purchase.aspose.com/temporary-license/) para acesso estendido.

Agora que temos nossas ferramentas prontas, vamos mergulhar no emocionante mundo da manipulação de hierarquia de nós 3D usando Aspose.3D.

## Importar namespaces

Em seu projeto .NET, certifique-se de importar os namespaces necessários para aproveitar a funcionalidade fornecida pelo Aspose.3D. Adicione as seguintes linhas ao seu código:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Esses namespaces darão acesso a classes e métodos essenciais para trabalhar com cenas 3D.

## Etapa 1: inicializar o objeto de cena

```csharp
Scene scene = new Scene();
```

 Comece criando uma nova cena 3D usando o`Scene` aula.

## Etapa 2: criar nós filhos

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Estabeleça uma estrutura hierárquica criando relacionamentos pai-filho entre nós. Neste exemplo,`cube1` e`cube2` são nós filhos do`top` nó.

## Etapa 3: criar e atribuir malha

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Gere uma malha usando um método adequado (aqui,`CreateMeshUsingPolygonBuilder`) e atribua-o aos nós filhos.

## Etapa 4: definir traduções

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Defina translações para cada nó do cubo, posicionando-os no espaço 3D.

## Etapa 5: aplicar rotação ao nó pai

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Gire o nó pai (`top`) e observe como essa transformação afeta todos os seus nós filhos.

## Etapa 6: salve a cena 3D

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Especifique o diretório de saída e salve a cena 3D no formato de arquivo desejado (aqui, FBX7500ASCII).

## Etapa 7: exibir mensagem de sucesso

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Informe o usuário sobre a adição bem-sucedida da hierarquia de nós e o local do arquivo salvo.

## Conclusão

Parabéns! Você navegou com sucesso no intrincado mundo da hierarquia de nós 3D no Aspose.3D for .NET. Este tutorial equipou você com o conhecimento necessário para criar, manipular e salvar cenas 3D com facilidade. Conforme você continua sua jornada, explore mais recursos e libere todo o potencial do Aspose.3D em seus projetos .NET.

## Perguntas frequentes

### Q1: Posso usar o Aspose.3D for .NET sem licença?

A1: Embora uma licença desbloqueie todos os recursos, você pode explorar o Aspose.3D com recursos limitados usando a avaliação gratuita.

### P2: Existem outros formatos de arquivo suportados para salvar cenas 3D?

A2: Sim, Aspose.3D suporta vários formatos; consulte a documentação para obter uma lista abrangente.

### Q3: Como posso contribuir com a comunidade Aspose.3D?

A3: Participe do fórum de suporte, compartilhe suas experiências e contribua ajudando outras pessoas com suas dúvidas.

### Q4: O Aspose.3D é adequado para desenvolvimento de jogos?

A4: Com certeza! Aspose.3D é versátil e pode ser integrado em projetos de desenvolvimento de jogos.

### P5: Qual é a diferença entre uma licença temporária e uma licença completa?

R5: Uma licença temporária fornece acesso de curto prazo para fins de avaliação, enquanto uma licença completa oferece uso irrestrito.