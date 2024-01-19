---
title: Renderizando cena em Cubemap com seis faces
linktitle: Renderizando cena em Cubemap com seis faces
second_title: API Aspose.3D .NET
description: Crie mapas de cubos impressionantes com Aspose.3D para .NET. Siga nosso guia passo a passo para renderizar cenas 3D em mapas cúbicos cativantes de seis faces.
type: docs
weight: 14
url: /pt/net/rendering/render-scene-cubemap/
---
## Introdução
Bem-vindo a este guia passo a passo sobre como renderizar uma cena em um mapa cúbico com seis faces usando Aspose.3D para .NET. Neste tutorial, orientaremos você no processo de criação de um mapa cúbico impressionante, renderizando uma cena 3D. Aspose.3D é uma API .NET poderosa que simplifica a manipulação de gráficos 3D e, com este guia, você aproveitará seus recursos para criar mapas de cubos cativantes.
## Pré-requisitos
Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:
- Conhecimento prático de desenvolvimento em C# e .NET.
-  Aspose.3D para .NET instalado. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).
- Um arquivo de cena 3D em formato GLB (por exemplo, "VirtualCity.glb") para renderização.
## Importar namespaces
Comece importando os namespaces necessários para Aspose.3D em seu código C#:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Etapa 1: carregar a cena
Carregue o arquivo de cena 3D usando o seguinte código:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Etapa 2: criar câmera e luzes
Crie uma câmera e duas luzes para iluminar a cena:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Etapa 3: Criar Renderizador e Destino de Renderização
Crie um renderizador e um destino de renderização do mapa de cubo com textura de profundidade:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Etapa 4: salvar faces do Cubemap
Salve cada face do cubemap em disco com nomes de arquivo especificados:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Conclusão
Parabéns! Você renderizou com sucesso uma cena 3D em um mapa de cubo usando Aspose.3D para .NET. Explore outras opções de personalização e aprimore seus projetos gráficos 3D com esta API poderosa.
## perguntas frequentes
### P: Posso usar o Aspose.3D for .NET com outros formatos de arquivo 3D?
Sim, Aspose.3D suporta vários formatos de arquivo 3D, proporcionando flexibilidade em seus projetos.
### P: Como posso obter suporte para Aspose.3D?
 Visite a[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.
### P: Existe um teste gratuito disponível?
 Sim, você pode acessar o teste gratuito[aqui](https://releases.aspose.com/).
### P: Posso renderizar cenas com animações usando Aspose.3D?
Absolutamente! Aspose.3D suporta renderização de cenas 3D animadas.
### P: Onde posso encontrar documentação detalhada?
 Consulte o[Documentação Aspose.3D](https://reference.aspose.com/3d/net/) para obter informações detalhadas.