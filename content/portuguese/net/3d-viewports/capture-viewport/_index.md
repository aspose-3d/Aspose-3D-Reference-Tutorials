---
title: Capturando viewports em cenas 3D
linktitle: Capturando viewports em cenas 3D
second_title: API Aspose.3D .NET
description: Aprenda a capturar viewports 3D impressionantes usando Aspose.3D para .NET. Guia passo a passo para renderizar cenas com flexibilidade.
type: docs
weight: 11
url: /pt/net/3d-viewports/capture-viewport/
---
## Introdução

No domínio dos gráficos e visualização 3D, capturar viewports é uma habilidade essencial que aprimora a profundidade e os detalhes de suas cenas. Aspose.3D for .NET fornece uma solução robusta para renderizar e manipular cenas 3D. Este tutorial irá guiá-lo através do processo de captura de viewports em cenas 3D usando Aspose.3D, permitindo criar visualizações impressionantes com facilidade.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Biblioteca Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/net/).

## Importar namespaces

Para começar, importe os namespaces necessários para o seu projeto .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Etapa 1: carregar uma cena 3D existente

Comece carregando uma cena 3D existente em seu projeto. O trecho de código a seguir demonstra isso:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Etapa 2: crie uma câmera

A seguir, crie uma instância da câmera e defina sua posição e alvo:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Etapa 3: adicione iluminação à cena

Aprimore sua cena adicionando uma fonte de luz. O trecho de código abaixo mostra como criar um ponto de luz:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Etapa 4: configurar o renderizador e o destino de renderização

Configure o renderizador e crie um destino de renderização para capturar a cena:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (continuação nas próximas etapas)
    }
}
```

## Etapa 5: definir viewports e renderizar

Defina viewports e renderize a cena para gerar imagens de saída:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Etapa 6: modificar viewports e renderizar novamente

Modifique as viewports e renderize a cena mais uma vez, demonstrando a flexibilidade do Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Continue experimentando diferentes configurações para obter os efeitos visuais desejados.

## Conclusão

Neste tutorial, exploramos o processo de captura de viewports em cenas 3D usando Aspose.3D for .NET. Aproveitando seus recursos poderosos, você pode elevar seus projetos gráficos 3D a novos patamares, proporcionando experiências visuais cativantes.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com outros formatos de arquivo 3D?

A1: Sim, Aspose.3D suporta vários formatos de arquivo 3D, garantindo compatibilidade com uma ampla gama de ferramentas de design.

### Q2: Posso usar Aspose.3D para desenvolvimento de jogos?

A2: Embora o Aspose.3D seja projetado principalmente para gráficos e visualização, suas funcionalidades podem complementar certos aspectos do desenvolvimento de jogos.

### P3: Onde posso encontrar exemplos e documentação adicionais?

 A3: Explore o abrangente[Documentação Aspose.3D](https://reference.aspose.com/3d/net/) para mais exemplos e informações detalhadas.

### Q4: Existe um teste gratuito disponível?

 A4: Sim, você pode acessar uma avaliação gratuita[aqui](https://releases.aspose.com/).

### P5: Como posso procurar ajuda ou participar na comunidade?

 A5: Junte-se à comunidade Aspose.3D no[Fórum de suporte](https://forum.aspose.com/c/3d/18) para assistência e colaboração.