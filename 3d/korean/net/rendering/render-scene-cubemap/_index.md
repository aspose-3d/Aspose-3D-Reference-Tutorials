---
title: 6개의 면이 있는 큐브맵으로 장면 렌더링
linktitle: 6개의 면이 있는 큐브맵으로 장면 렌더링
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 멋진 큐브맵을 만드세요. 3D 장면을 매혹적인 6면 큐브맵으로 렌더링하기 위한 단계별 가이드를 따르십시오.
type: docs
weight: 14
url: /ko/net/rendering/render-scene-cubemap/
---
## 소개
.NET용 Aspose.3D를 사용하여 6개의 면이 있는 큐브맵으로 장면을 렌더링하는 방법에 대한 단계별 가이드에 오신 것을 환영합니다. 이 튜토리얼에서는 3D 장면을 렌더링하여 놀라운 큐브맵을 만드는 과정을 안내합니다. Aspose.3D는 3D 그래픽 조작을 단순화하는 강력한 .NET API이며, 이 가이드를 통해 그 기능을 활용하여 매력적인 큐브맵을 만들 수 있습니다.
## 전제 조건
튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.
- C# 및 .NET 개발에 대한 실무 지식.
-  .NET용 Aspose.3D가 설치되었습니다. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/).
- 렌더링을 위한 GLB 형식(예: "VirtualCity.glb")의 3D 장면 파일입니다.
## 네임스페이스 가져오기
C# 코드에서 Aspose.3D에 필요한 네임스페이스를 가져오는 것부터 시작하세요.
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
## 1단계: 장면 로드
다음 코드를 사용하여 3D 장면 파일을 로드합니다.
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2단계: 카메라와 조명 만들기
장면을 비추는 카메라와 두 개의 조명을 만듭니다.
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
## 3단계: 렌더러 및 렌더 대상 생성
깊이 텍스처를 사용하여 렌더러 및 큐브 맵 렌더 대상을 만듭니다.
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## 4단계: 큐브맵 면 저장
큐브맵의 각 면을 지정된 파일 이름으로 디스크에 저장합니다.
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
## 결론
축하해요! .NET용 Aspose.3D를 사용하여 3D 장면을 큐브맵으로 성공적으로 렌더링했습니다. 이 강력한 API를 사용하여 추가 사용자 정의 옵션을 탐색하고 3D 그래픽 프로젝트를 향상시키십시오.
## 자주 묻는 질문
### Q: 다른 3D 파일 형식과 함께 .NET용 Aspose.3D를 사용할 수 있습니까?
예, Aspose.3D는 다양한 3D 파일 형식을 지원하여 프로젝트에 유연성을 제공합니다.
### Q: Aspose.3D에 대한 지원은 어떻게 받을 수 있나요?
 방문하다[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.
### Q: 무료 평가판이 제공됩니까?
 예, 무료 평가판에 액세스할 수 있습니다[여기](https://releases.aspose.com/).
### Q: Aspose.3D를 사용하여 애니메이션이 포함된 장면을 렌더링할 수 있습니까?
전적으로! Aspose.3D는 애니메이션 3D 장면 렌더링을 지원합니다.
### Q: 자세한 문서는 어디서 찾을 수 있나요?
 다음을 참조하세요.[Aspose.3D 문서](https://reference.aspose.com/3d/net/) 자세한 정보를 확인하세요.