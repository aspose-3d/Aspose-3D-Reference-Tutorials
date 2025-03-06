---
title: Deslocamento de torção em extrusão linear
linktitle: Deslocamento de torção em extrusão linear
second_title: API Aspose.3D .NET
description: Explore a magia do Aspose.3D para .NET com nosso guia passo a passo sobre Twist Offset em Extrusão Linear. Eleve seus projetos 3D sem esforço.
weight: 15
url: /pt/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Deslocamento de torção em extrusão linear

## Introdução

Bem-vindo ao mundo do Aspose.3D for .NET, uma biblioteca versátil que permite aos desenvolvedores lidar com a manipulação 3D com facilidade. Neste tutorial, nos aprofundaremos em um dos recursos intrigantes - o "Deslocamento de torção na extrusão linear". Se você está pronto para aprimorar suas habilidades de programação 3D, vamos começar!

## Pré-requisitos

Antes de embarcarmos nesta jornada emocionante, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Biblioteca Aspose.3D for .NET: Baixe e instale a biblioteca do[página de lançamento](https://releases.aspose.com/3d/net/).

- Seu ambiente de desenvolvimento: certifique-se de que seu ambiente de desenvolvimento esteja configurado e pronto para funcionar.

## Importar namespaces

Comece importando os namespaces necessários para acessar a funcionalidade fornecida pelo Aspose.3D for .NET. No seu código, isso pode ser parecido com:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Agora, vamos dividir o exemplo em etapas gerenciáveis para dominar o Twist Offset na Extrusão Linear:

## Etapa 1: inicializar o perfil base

Comece criando um perfil base, aqui exemplificado por uma forma retangular com um raio de arredondamento especificado.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Etapa 2: crie uma cena

Gere uma cena 3D para hospedar seus nós e formas.

```csharp
Scene scene = new Scene();
```

## Etapa 3: criar nós

Construa nós dentro da cena, tanto à esquerda quanto à direita.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Etapa 4: Extrusão Linear no Nó Esquerdo

Execute a extrusão linear no nó esquerdo usando a propriedade twist and slices.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Etapa 5: Extrusão Linear no Nó Direito com Deslocamento de Torção

No nó direito, execute a extrusão linear usando a propriedade twist, twist offset e slices.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Etapa 6: Salvar cena 3D

Salve a cena 3D no diretório de saída desejado, especificando o formato do arquivo como WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Parabéns! Você implementou com sucesso o Twist Offset em Linear Extrusion usando Aspose.3D para .NET.

## Conclusão

Neste tutorial, exploramos os poderosos recursos do Aspose.3D para .NET, focando especificamente no Twist Offset na Extrusão Linear. Com essas novas habilidades, você estará bem equipado para infundir dinamismo em seus projetos 3D.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for .NET com outras linguagens de programação?

A1: Aspose.3D oferece suporte principalmente a linguagens .NET, mas Aspose fornece bibliotecas semelhantes para Java e outras plataformas.

### P2: Como obtenho uma licença temporária do Aspose.3D for .NET?

 A2: Visita[esse link](https://purchase.aspose.com/temporary-license/)adquirir uma licença temporária para fins de teste.

### Q3: Existe um fórum da comunidade para Aspose.3D for .NET?

 A3: Com certeza! Junte-se à comunidade em[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para se envolver com outros desenvolvedores e buscar assistência.

### P4: Existem exemplos e documentação adicionais disponíveis?

 A4: Explore o[documentação](https://reference.aspose.com/3d/net/) para guias e exemplos extensos.

### Q5: Onde posso comprar o Aspose.3D para .NET?

 A5: Vá para[esse link](https://purchase.aspose.com/buy) para fazer uma compra e desbloquear todo o potencial do Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
