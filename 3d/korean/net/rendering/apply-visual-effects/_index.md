---
title: 3D 뷰포트에 시각 효과 적용
linktitle: 3D 뷰포트에 시각 효과 적용
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 시각화의 세계를 탐험해보세요. 단계별 튜토리얼을 통해 장면에 매혹적인 시각 효과를 적용하는 방법을 알아보세요. 픽셀화, 회색조, 가장자리 감지 및 흐림 효과로 프로젝트를 향상시키세요.
type: docs
weight: 10
url: /ko/net/rendering/apply-visual-effects/
---
## 소개

3D 장면의 시각적 매력을 향상시키는 것은 몰입형 경험을 만드는 데 있어 중요한 측면입니다. .NET용 Aspose.3D는 3D 뷰포트에 시각 효과를 적용하는 강력한 도구 세트를 제공합니다. 이 튜토리얼에서는 픽셀화, 회색조, 가장자리 감지 및 흐림을 포함하여 3D 장면에 다양한 효과를 적용하는 과정을 살펴보겠습니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 사항을 확인하세요.

- C# 및 .NET 개발에 대한 실무 지식.
-  .NET 라이브러리용 Aspose.3D가 설치되었습니다. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).
- 실험용 3D 장면 파일(예: "scene.obj")

## 네임스페이스 가져오기

시작하려면 Aspose.3D 및 기타 종속성에 필요한 네임스페이스를 가져옵니다. 코드에 다음 줄을 추가합니다.

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 다음을 사용하여 3D 장면을 로드합니다.`Scene` 수업.

## 2단계: 카메라 만들기

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

카메라 인스턴스를 생성하고 해당 위치와 대상을 설정합니다.

## 3단계: 장면에 조명 추가

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

시각적 효과를 높이기 위해 조명을 도입합니다.

## 4단계: 렌더러 및 렌더 대상 생성

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // 렌더러 설정 구성
    renderer.EnableShadows = false;

    // 렌더 타겟 생성
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // 뷰포트 구성
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // 장면을 텍스처로 렌더링
        renderer.Render(rt);

        // 렌더링된 텍스처를 파일에 저장
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // 후처리 효과를 계속 진행합니다...
    }
}
```

장면을 캡처하기 위해 렌더러와 렌더 대상을 만듭니다.

## 5단계: 후처리 효과 적용

### 5.1단계 픽셀화 효과

```csharp
// 픽셀화 효과 만들기
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

픽셀화 효과를 적용하고 결과를 저장합니다.

### 5.2 단계 그레이스케일 효과

```csharp
// 회색조 효과 만들기
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

회색조 효과를 적용하고 결과를 저장합니다.

### 5.3단계 효과 결합

```csharp
// 회색조와 픽셀화 효과 결합
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

다양한 효과를 결합하여 독특한 결과를 얻으세요.

### 5.4단계 에지 검출 효과

```csharp
// 가장자리 감지 효과 만들기
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

가장자리 감지 효과를 적용하고 결과를 저장합니다.

### 5.5단계 흐림 효과

```csharp
// 흐림 효과 만들기
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

흐림 효과를 적용하고 결과를 저장합니다.

## 결론

3D 뷰포트에서 시각 효과를 실험하면 장면에 깊이와 창의성이 더해집니다. .NET용 Aspose.3D는 이 프로세스를 단순화하여 프로젝트를 향상시킬 수 있는 다양한 후처리 효과를 제공합니다.

## FAQ

### Q1: 여러 효과를 동시에 적용할 수 있나요?

A1: 예. 다양한 후처리 효과를 결합하여 독특하고 복잡한 결과를 얻을 수 있습니다.

### Q2: 시각 효과의 강도를 어떻게 조정할 수 있나요?

A2: 각 효과에는 강도를 제어하기 위해 조정할 수 있는 매개변수가 있을 수 있습니다. 구체적인 내용은 문서를 참고하세요.

### Q3: Aspose.3D는 게임 개발에 적합합니까?

A3: Aspose.3D는 주로 3D 모델링 및 렌더링용으로 설계되었지만 게임 개발의 특정 측면에서 사용될 수 있습니다.

### Q4: 추가 후처리 효과를 사용할 수 있나요?

A4: Aspose.3D는 다양한 내장 후처리 효과를 제공하며, 라이브러리를 사용하여 사용자 정의 효과를 만들 수 있습니다.

### Q5: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?

 A5: 예, Aspose.3D를 상업적 목적으로 사용할 수 있습니다. 다음을 참조하세요.[구매 페이지](https://purchase.aspose.com/buy) 라이선스 세부정보를 확인하세요.