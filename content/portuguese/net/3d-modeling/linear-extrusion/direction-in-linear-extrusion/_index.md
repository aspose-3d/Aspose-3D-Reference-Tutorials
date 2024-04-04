---
title: Direção na Extrusão Linear
linktitle: Direção na Extrusão Linear
second_title: API Aspose.3D .NET
description: Desbloqueie o mundo da modelagem 3D com Aspose.3D para .NET. Aprenda a direção da extrusão linear, aumente a criatividade e crie aplicações envolventes sem esforço.
type: docs
weight: 11
url: /pt/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---
## Introdução

No mundo dinâmico do desenvolvimento de software, criar modelos 3D imersivos é uma habilidade indispensável. Aspose.3D for .NET fornece aos desenvolvedores um conjunto robusto de ferramentas para aproveitar o potencial da modelagem 3D em seus aplicativos. Neste tutorial, mergulharemos no intrigante mundo da extrusão linear e exploraremos as nuances do recurso "Direção na extrusão linear".

## Pré-requisitos

Antes de embarcarmos nesta jornada emocionante, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Baixe e instale a biblioteca de[Documentação Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Ambiente de desenvolvimento: certifique-se de ter um ambiente de desenvolvimento .NET funcional configurado.

## Importar namespaces

Em seu projeto .NET, importe os namespaces necessários para acessar a funcionalidade do Aspose.3D. Adicione as seguintes linhas ao início do seu código:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Etapa 1: inicializar o perfil base

Comece inicializando o perfil base a ser extrudado. Neste exemplo, criamos uma forma retangular com raio de arredondamento de 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passo 2: Crie uma cena 3D

Construa a base para sua obra-prima 3D criando uma cena.

```csharp
Scene scene = new Scene();
```

## Etapa 3: criar nós

Gere nós na cena para representar diferentes componentes do seu ambiente 3D.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Etapa 4: Extrusão Linear sem Direção

 Execute a extrusão linear no nó esquerdo usando o`Twist` e`Slices` propriedades.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Etapa 5: Extrusão Linear com Direção

 Amplie as capacidades de extrusão incorporando o`Direction` propriedade no nó direito.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Etapa 6: salve a cena 3D

 Preserve sua criação salvando a cena 3D. Substituir`"Your Output Directory"` com o diretório desejado.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Parabéns! Você implementou com sucesso a extrusão linear com Aspose.3D para .NET, explorando as abordagens tradicional e direcional.

## Conclusão

Neste tutorial, navegamos pelo fascinante reino da modelagem 3D usando Aspose.3D for .NET. A extrusão linear, com e sem direção, abre possibilidades infinitas para desenvolvedores que buscam criar aplicativos visualmente impressionantes. Com Aspose.3D, o poder da modelagem 3D está ao seu alcance.

## Perguntas frequentes

### Q1: Como posso obter uma licença temporária do Aspose.3D for .NET?

 A1: Visita[Aspose Licença Temporária](https://purchase.aspose.com/temporary-license/) para obter uma licença temporária.

### P2: Onde posso encontrar suporte para Aspose.3D?

 A2: Junte-se ao[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para buscar assistência e se conectar com a comunidade.

### Q3: Existe um teste gratuito disponível?

 A3: Sim, explore os recursos com uma avaliação gratuita em[Lançamentos Aspose.3D](https://releases.aspose.com/).

### Q4: Como faço para adquirir o Aspose.3D para .NET?

 A4: Navegue até o[Página de compra do Aspose](https://purchase.aspose.com/buy) para opções de licenciamento e detalhes de compra.

### Q5: Onde posso encontrar documentação detalhada para Aspose.3D for .NET?

 A5: Consulte o abrangente[Documentação Aspose.3D .NET](https://reference.aspose.com/3d/net/) para obter informações detalhadas.