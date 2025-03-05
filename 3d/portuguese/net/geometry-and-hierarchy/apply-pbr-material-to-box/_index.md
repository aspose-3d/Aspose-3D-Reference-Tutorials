---
title: Aplicando material PBR à caixa
linktitle: Aplicando material PBR à caixa
second_title: API Aspose.3D .NET
description: Explore o mundo dos gráficos 3D com Aspose.3D para .NET. Crie cenas imersivas sem esforço usando materiais de renderização com base física.
type: docs
weight: 10
url: /pt/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Introdução

Bem-vindo ao fascinante mundo dos gráficos 3D! Neste guia passo a passo, exploraremos a poderosa biblioteca Aspose.3D para .NET e aprenderemos como criar cenas 3D impressionantes usando materiais de renderização baseada em física (PBR). Aspose.3D simplifica o complexo processo de gráficos 3D e abre um mundo de possibilidades para desenvolvedores.

## Pré-requisitos

Antes de mergulharmos no emocionante mundo dos gráficos 3D, vamos garantir que você tenha tudo configurado:

### Baixe e instale Aspose.3D para .NET

 Visite a[Documentação do Aspose.3D para .NET](https://reference.aspose.com/3d/net/) para obter instruções detalhadas sobre como baixar e instalar a biblioteca.

### Adquira uma licença

Para desbloquear todo o potencial do Aspose.3D, obtenha uma licença válida. Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/) ou compre uma licença completa[aqui](https://purchase.aspose.com/buy).

## Importar namespaces

Em primeiro lugar, certifique-se de importar os namespaces necessários para aproveitar os recursos do Aspose.3D for .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Etapa 1: inicializar uma cena

Comece inicializando uma cena 3D usando o seguinte trecho de código:

```csharp
Scene scene = new Scene();
```

## Etapa 2: inicializar o material PBR

Crie um objeto de material PBR para obter uma renderização realista:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Etapa 3: definir propriedades do material

Ajuste as propriedades do material, tornando-o quase metálico e muito áspero:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Etapa 4: crie uma caixa

Gere uma caixa na qual o material PBR será aplicado:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Passo 5: Aplicar Material na Caixa

Atribua o material PBR ao nó de caixa criado:

```csharp
boxNode.Material = mat;
```

## Etapa 6: salve a cena 3D

Salve a cena 3D no formato STL com o diretório de saída desejado:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Parabéns! Você aplicou com sucesso um material PBR a uma caixa em uma cena 3D usando Aspose.3D for .NET.

## Conclusão

Aventurar-se em gráficos 3D com Aspose.3D for .NET abre portas para infinitas possibilidades criativas. Com sua API intuitiva e recursos robustos, a criação de cenas visualmente deslumbrantes torna-se uma experiência agradável para os desenvolvedores.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com outros formatos de arquivo 3D?

A1: Sim, Aspose.3D suporta vários formatos de arquivo 3D, garantindo flexibilidade em seus projetos.

### Q2: Posso usar o Aspose.3D para aplicações comerciais?

A2: Com certeza! Aspose.3D fornece licenças comerciais para integração perfeita em seus aplicativos.

### Q3: Existe uma versão de teste disponível?

 A3: Sim, você pode explorar os recursos do Aspose.3D baixando a versão de avaliação gratuita[aqui](https://releases.aspose.com/).

### P4: Onde posso encontrar suporte e discussões da comunidade?

 A4: Junte-se à comunidade Aspose.3D em[Fóruns Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões.

### Q5: Como obtenho uma licença temporária para Aspose.3D?

 A5: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/) para fins de avaliação.