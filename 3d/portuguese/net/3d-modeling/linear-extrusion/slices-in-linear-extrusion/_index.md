---
title: Fatias em Extrusão Linear
linktitle: Fatias em Extrusão Linear
second_title: API Aspose.3D .NET
description: Explore o mundo do design 3D com Aspose.3D para .NET. Crie modelos impressionantes usando nosso tutorial de extrusão linear.
weight: 13
url: /pt/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Fatias em Extrusão Linear

## Introdução

Bem-vindo ao mundo do design 3D usando Aspose.3D para .NET! Quer você seja um desenvolvedor experiente ou esteja apenas começando, este tutorial irá guiá-lo através do processo de criação de visualizações 3D impressionantes usando a poderosa biblioteca Aspose.3D.

## Pré-requisitos

Antes de mergulhar no mundo do design 3D com Aspose.3D, certifique-se de ter os seguintes pré-requisitos:

-  Biblioteca Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/net/).

- Ambiente de Desenvolvimento Integrado (IDE): Use qualquer IDE preferido compatível com desenvolvimento .NET.

- Compreensão básica de C#: Familiarize-se com os fundamentos da linguagem de programação C#.

- Desejo de explorar o design 3D: Paixão por criar modelos 3D visualmente deslumbrantes!

## Importar namespaces

Para iniciar sua jornada de design 3D com Aspose.3D, você precisará importar os namespaces necessários. Isso garante que seu código possa acessar as classes e funcionalidades necessárias.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Extrusão Linear - Fatias em Extrusão Linear

Agora, vamos mergulhar em um exemplo prático – Extrusão Linear com Fatias. Esta técnica permite criar modelos 3D complexos com vários níveis de detalhe.

### Etapa 1: inicializar o perfil base

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Passo 2: Crie uma cena 3D

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Etapa 3: criar nós esquerdo e direito

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Etapa 4: Execute a extrusão linear no nó esquerdo

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Etapa 5: Execute a extrusão linear no nó direito

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Etapa 6: Salvar cena 3D

```csharp
// ExStart:Salvar3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
//ExEnd:Save3DScene
```

## Conclusão

Parabéns! Você aprendeu com sucesso como realizar extrusão linear com fatias usando Aspose.3D para .NET. Este é apenas o começo de sua jornada de design 3D com Aspose.3D - libere sua criatividade e explore as infinitas possibilidades!

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D foi projetado principalmente para .NET, mas você pode explorar opções de interoperabilidade com linguagens como Python usando ligações .NET.

### Q2: Onde posso encontrar documentação detalhada para Aspose.3D for .NET?

 A2: Consulte a documentação[aqui](https://reference.aspose.com/3d/net/) para obter informações detalhadas sobre os recursos e uso do Aspose.3D.

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?

 A3: Sim, você pode fazer seu teste gratuito[aqui](https://releases.aspose.com/)para explorar os recursos da biblioteca antes de fazer uma compra.

### Q4: Como posso obter suporte técnico para Aspose.3D for .NET?

 A4: Visite o fórum Aspose.3D[aqui](https://forum.aspose.com/c/3d/18) buscar assistência e se envolver com a comunidade.

### Q5: Posso usar uma licença temporária para Aspose.3D for .NET?

 A5: Sim, obtenha uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/) para fins de avaliação.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
