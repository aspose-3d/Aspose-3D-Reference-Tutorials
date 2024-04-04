---
title: 3D 장면에서 뷰포트 캡처
linktitle: 3D 장면에서 뷰포트 캡처
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 멋진 3D 뷰포트를 캡처하는 방법을 알아보세요. 유연하게 장면을 렌더링하기 위한 단계별 가이드입니다.
type: docs
weight: 11
url: /ko/net/rendering/capture-viewport/
---
## 소개

3D 그래픽 및 시각화 영역에서 뷰포트 캡처는 장면의 깊이와 디테일을 향상시키는 필수 기술입니다. .NET용 Aspose.3D는 3D 장면을 렌더링하고 조작하기 위한 강력한 솔루션을 제공합니다. 이 튜토리얼에서는 Aspose.3D를 사용하여 3D 장면에서 뷰포트를 캡처하는 과정을 안내하므로 놀라운 시각화를 쉽게 만들 수 있습니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET 라이브러리용 Aspose.3D: Aspose.3D 라이브러리가 설치되어 있는지 확인하세요. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).

## 네임스페이스 가져오기

시작하려면 필요한 네임스페이스를 .NET 프로젝트로 가져옵니다.

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

## 1단계: 기존 3D 장면 로드

기존 3D 장면을 프로젝트에 로드하는 것부터 시작하세요. 다음 코드 조각은 이를 보여줍니다.

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## 2단계: 카메라 만들기

다음으로 카메라 인스턴스를 생성하고 위치와 대상을 설정합니다.

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## 3단계: 장면에 조명 추가

광원을 추가하여 장면을 향상시키세요. 아래 코드 조각은 포인트 라이트를 만드는 방법을 보여줍니다.

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## 4단계: 렌더러 및 렌더 대상 구성

렌더러를 설정하고 장면 캡처를 위한 렌더 대상을 만듭니다.

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ...(다음 단계에서 계속)
    }
}
```

## 5단계: 뷰포트 정의 및 렌더링

뷰포트를 정의하고 장면을 렌더링하여 출력 이미지를 생성합니다.

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## 6단계: 뷰포트 수정 및 다시 렌더링

뷰포트를 수정하고 장면을 다시 한 번 렌더링하여 Aspose.3D의 유연성을 보여줍니다.

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

원하는 시각적 효과를 얻으려면 다양한 구성을 계속 실험해 보세요.

## 결론

이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 3D 장면에서 뷰포트를 캡처하는 프로세스를 살펴보았습니다. 강력한 기능을 활용하면 3D 그래픽 프로젝트를 새로운 차원으로 끌어올려 매력적인 시각적 경험을 제공할 수 있습니다.

## FAQ

### Q1: Aspose.3D는 다른 3D 파일 형식과 호환됩니까?

A1: 예, Aspose.3D는 다양한 3D 파일 형식을 지원하므로 다양한 디자인 도구와의 호환성을 보장합니다.

### Q2: Aspose.3D를 게임 개발에 사용할 수 있나요?

A2: Aspose.3D는 주로 그래픽과 시각화를 위해 설계되었지만 그 기능은 게임 개발의 특정 측면을 보완할 수 있습니다.

### Q3: 추가 예제와 문서는 어디에서 찾을 수 있습니까?

 A3: 포괄적인 탐색[Aspose.3D 문서](https://reference.aspose.com/3d/net/) 더 많은 예시와 자세한 정보를 확인하세요.

### Q4: 무료 평가판이 제공됩니까?

 A4: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### 질문 5: 어떻게 도움을 구하거나 커뮤니티에 참여할 수 있나요?

 A5: Aspose.3D 커뮤니티에 가입하세요.[지원 포럼](https://forum.aspose.com/c/3d/18) 지원과 협력을 위해.