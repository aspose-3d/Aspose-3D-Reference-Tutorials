---
title: Executando Extrusão Linear
linktitle: Executando Extrusão Linear
second_title: API Aspose.3D .NET
description: Explore o mundo dos gráficos 3D com Aspose.3D para .NET. Executando extrusão linear neste guia passo a passo.
weight: 12
url: /pt/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Executando Extrusão Linear

## Introdução:

Embarque em uma jornada emocionante no reino dos gráficos 3D com Aspose.3D for .NET, uma potência que eleva seu jogo de desenvolvimento. Neste tutorial, vamos nos aprofundar nos meandros da Extrusão Linear – uma técnica fascinante que dá vida a perfis 2D estáticos, impulsionando-os para o mundo dinâmico do 3D. Vamos abrir a porta para a criatividade e inovação usando Aspose.3D!

## Pré-requisitos:

Antes de mergulhar no mundo encantador da manipulação 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

1. Instalação do Aspose.3D:
   -  Comece baixando e instalando Aspose.3D for .NET em[aqui](https://releases.aspose.com/3d/net/).
   -  Siga as instruções de instalação fornecidas na documentação[aqui](https://reference.aspose.com/3d/net/).

2. Configurando seu ambiente de desenvolvimento:
   - Certifique-se de que seu ambiente de desenvolvimento esteja configurado corretamente com os namespaces necessários para Aspose.3D.

Agora que você está preparado, vamos mergulhar na magia do Aspose.3D!

## Importar namespaces:

Inclua os namespaces essenciais para iniciar sua aventura 3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Esses namespaces estabelecem a base para sua jornada de codificação 3D, fornecendo acesso às ferramentas necessárias para uma integração perfeita das funcionalidades do Aspose.3D.

## Executando Extrusão Linear:

Vamos criar um objeto 3D fascinante por meio de extrusão linear usando Aspose.3D. Siga esses passos:

## Etapa 1: inicializar o perfil base
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Esta etapa configura o perfil 2D que servirá de base para nossa obra-prima 3D. Ajuste os parâmetros conforme necessário para obter a forma e o formato desejados.

## Etapa 2: Extrusão Linear
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Aqui é realizada a Extrusão Linear, pegando o perfil 2D e estendendo-o na terceira dimensão. Experimente parâmetros como 'Slices' e 'Twist' para moldar sua criação.

## Etapa 3: crie uma cena
```csharp
Scene scene = new Scene();
```

Uma tela em branco é criada – uma cena onde seu objeto 3D ganhará vida.

## Etapa 4: adicionar extrusão à cena
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Sua obra-prima extrudada é adicionada como um nó filho à cena.

## Etapa 5: salve a cena 3D
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Por fim, salve sua criação no formato desejado. Neste exemplo, ele é salvo como um arquivo Wavefront OBJ.

Agora, contemple sua maravilha 3D!

## Conclusão:

Parabéns! Você acabou de arranhar a superfície do potencial do Aspose.3D. Este tutorial apenas sugere a vasta paisagem que aguarda sua exploração. Mergulhe na documentação, experimente várias formas e desbloqueie todo o espectro de possibilidades com Aspose.3D for .NET.

## Perguntas frequentes:

### Q1: O Aspose.3D é adequado para iniciantes?

A1: Com certeza! Aspose.3D oferece um ambiente amigável e nosso tutorial orienta você no básico.

### Q2: Posso usar Aspose.3D para projetos comerciais?

 A2: Sim, o Aspose.3D vem com opções de licenciamento para uso pessoal e comercial. Verificar[aqui](https://purchase.aspose.com/buy) para detalhes.

### P3: Como posso obter licenças temporárias para testes?

 A3: Visita[esse link](https://purchase.aspose.com/temporary-license/) para obter licenças temporárias para fins de teste.

### P4: Onde posso encontrar suporte da comunidade?

 A4: Junte-se ao[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para se conectar com uma comunidade vibrante e buscar assistência.

### Q5: Existe um teste gratuito disponível?

 A5: Certamente! Baixe a versão de teste gratuita[aqui](https://releases.aspose.com/) para experimentar os recursos do Aspose.3D em primeira mão.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
