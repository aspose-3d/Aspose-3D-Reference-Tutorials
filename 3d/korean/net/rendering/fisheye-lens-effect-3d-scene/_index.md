---
title: .NET용 Aspose.3D를 사용하여 어안 렌즈 효과 적용
linktitle: 3D 장면에 어안 렌즈 효과 적용
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D로 3D 장면을 향상하세요! 매혹적인 어안 렌즈 효과를 적용하는 방법을 단계별로 알아보세요. 지금 다운로드하세요!
weight: 12
url: /ko/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# .NET용 Aspose.3D를 사용하여 어안 렌즈 효과 적용

## 소개
3D 장면의 시각적 매력을 향상시키고 싶으십니까? .NET용 Aspose.3D를 사용하여 어안 렌즈 효과의 매혹적인 세계에 빠져보세요. 이 튜토리얼에서는 3D 장면에 어안 렌즈 효과를 적용하여 독특하고 매력적인 관점을 제공하는 방법을 단계별로 안내합니다.
## 전제 조건
시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.
-  .NET용 Aspose.3D: .NET용 Aspose.3D 라이브러리가 설치되어 있는지 확인하세요. 그렇지 않은 경우 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).
-  샘플 3D 장면: 샘플 3D 장면 파일(VirtualCity.glb)로 작업하겠습니다. 자신만의 장면을 사용하거나 다음에서 샘플을 다운로드할 수 있습니다.[Aspose.3D 문서](https://reference.aspose.com/3d/net/).
## 네임스페이스 가져오기
.NET 프로젝트에서 Aspose.3D 기능에 액세스하는 데 필요한 네임스페이스를 포함합니다. 코드 시작 부분에 다음 네임스페이스를 추가합니다.
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
## 1단계: 3D 장면 로드
다음 코드를 사용하여 3D 장면 파일을 프로젝트에 로드합니다.
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2단계: 카메라와 조명 설정
장면의 시각적 측면을 향상시키기 위해 카메라와 조명을 만듭니다. 필요에 따라 NearPlane, FarPlane 및 RotationMode와 같은 매개변수를 조정합니다.
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
## 3단계: 렌더러 및 렌더 대상 생성
렌더러를 설정하고 큐브 맵 및 2D 텍스처에 대한 렌더 대상을 만듭니다.
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## 4단계: 어안 렌즈 효과 적용
렌더링된 큐브 맵에서 어안 렌즈 효과 후처리를 실행합니다.
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## 결론
축하해요! .NET용 Aspose.3D를 사용하여 3D 장면에 어안 렌즈 효과를 성공적으로 적용했습니다. 다양한 장면과 매개변수를 실험하여 창의력을 발휘해보세요.
## 자주 묻는 질문
### 3D 장면에 어안 효과를 적용할 수 있나요?
예, 모든 3D 장면에 어안 효과를 적용할 수 있습니다. 최적의 결과를 얻으려면 장면이 제대로 로드되고 조명이 켜져 있는지 확인하세요.
### 시야각(fov)을 360도로 조정하는 것은 무엇을 의미합니까?
360도 시야각은 완벽한 구형 프로젝션을 보장하여 놀라운 어안 효과를 만들어냅니다.
### 3D 장면의 조명을 어떻게 사용자 정의할 수 있나요?
위치, 유형, 색상 등 조명의 속성을 조정하여 원하는 조명 효과를 얻을 수 있습니다.
### 처리할 수 있는 3D 장면의 크기에 제한이 있나요?
3D 장면의 크기는 주로 시스템 리소스에 의해 제한됩니다. 하드웨어가 장면의 크기를 처리할 수 있는지 확인하십시오.
### 어안 효과 결과에 PNG 대신 다른 출력 형식을 사용할 수 있습니까?
예, 요구 사항에 따라 다양한 이미지 형식으로 출력을 저장하도록 코드를 수정할 수 있습니다.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
