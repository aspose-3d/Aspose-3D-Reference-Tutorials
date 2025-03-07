---
title: Aplicando efeito de lente olho de peixe com Aspose.3D para .NET
linktitle: Aplicando efeito de lente olho de peixe a cena 3D
second_title: API Aspose.3D .NET
description: Aprimore suas cenas 3D com Aspose.3D for .NET! Aprenda como aplicar um efeito cativante de lente olho de peixe passo a passo. Baixe Agora!
weight: 12
url: /pt/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aplicando efeito de lente olho de peixe com Aspose.3D para .NET

## Introdução
Você está procurando melhorar o apelo visual de suas cenas 3D? Mergulhe no fascinante mundo dos efeitos de lente olho de peixe com Aspose.3D para .NET. Este tutorial irá guiá-lo passo a passo sobre como aplicar um efeito de lente olho de peixe às suas cenas 3D, dando-lhes uma perspectiva única e cativante.
## Pré-requisitos
Antes de começarmos, certifique-se de ter os seguintes pré-requisitos em vigor:
-  Aspose.3D para .NET: Certifique-se de ter a biblioteca Aspose.3D para .NET instalada. Se não, você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).
-  Exemplo de cena 3D: trabalharemos com um arquivo de amostra de cena 3D (VirtualCity.glb). Você pode usar sua própria cena ou baixar a amostra do[Documentação Aspose.3D](https://reference.aspose.com/3d/net/).
## Importar namespaces
Em seu projeto .NET, inclua os namespaces necessários para acessar as funcionalidades do Aspose.3D. Adicione os seguintes namespaces no início do seu código:
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
## Passo 1: Carregar a Cena 3D
Carregue o arquivo de cena 3D em seu projeto usando o seguinte código:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Etapa 2: configurar câmera e luzes
Crie uma câmera e luzes para aprimorar os aspectos visuais da sua cena. Ajuste parâmetros como NearPlane, FarPlane e RotationMode conforme necessário:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Etapa 3: criar renderizador e destinos de renderização
Configure o renderizador e crie destinos de renderização para mapa de cubo e textura 2D:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Etapa 4: aplicar efeito de lente olho de peixe
Execute o pós-processamento do efeito de lente olho de peixe no mapa do cubo renderizado:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Conclusão
Parabéns! Você aplicou com sucesso um efeito de lente olho de peixe à sua cena 3D usando Aspose.3D para .NET. Experimente diferentes cenas e parâmetros para liberar sua criatividade.
## perguntas frequentes
### Posso aplicar o efeito olho de peixe a qualquer cena 3D?
Sim, você pode aplicar o efeito olho de peixe a qualquer cena 3D. Certifique-se de que a cena esteja devidamente carregada e iluminada para obter os melhores resultados.
### Qual é a importância de ajustar o campo de visão (fov) para 360 graus?
Um campo de visão de 360 graus garante uma projeção esférica completa, criando um impressionante efeito olho de peixe.
### Como posso personalizar a iluminação da minha cena 3D?
Você pode ajustar as propriedades das luzes, como posição, tipo e cor, para obter os efeitos de iluminação desejados.
### Existe um limite para o tamanho da cena 3D que pode ser processada?
O tamanho da cena 3D é limitado principalmente pelos recursos do sistema. Certifique-se de que seu hardware possa lidar com o tamanho da sua cena.
### Posso usar um formato de saída diferente em vez de PNG para o resultado do efeito olho de peixe?
Sim, você pode modificar o código para salvar a saída em diferentes formatos de imagem com base em seus requisitos.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
