---
date: 2026-03-23
description: Aspose.3D for .NET를 사용하여 슬라이스와 함께 선형 압출하는 방법을 배워보세요. 단계별 코드 예제로 상세한 3D
  모델을 만들 수 있습니다.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET를 사용한 슬라이스와 선형 압출 방법
url: /ko/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET를 사용한 슬라이스 기반 선형 압출 방법

## Introduction

Aspose.3D for .NET를 활용한 3D 디자인 세계에 오신 것을 환영합니다! 이 튜토리얼에서는 모델의 디테일 수준을 제어할 수 있는 **선형 압출**을 슬라이스와 함께 사용하는 방법을 알아봅니다. 숙련된 개발자이든 이제 시작하는 분이든, 단계별로 자세히 안내하고 각 작업의 이유를 설명하며 바로 적용할 수 있는 실용적인 팁을 제공해 드립니다.

## Quick Answers
- **선형 압출에 슬라이스가 무엇인가요?** 2D 프로파일을 3D로 확장하면서 중간에 생성되는 교차‑섹션(슬라이스)의 개수를 지정하는 방법입니다.  
- **왜 슬라이스를 사용하나요?** 슬라이스 수가 많을수록 곡선이 부드러워지고, 슬라이스 수가 적을수록 메쉬가 가벼워집니다.  
- **필수 조건은?** Aspose.3D for .NET, .NET 호환 IDE, 기본 C# 지식.  
- **보통 실행 시간은?** 최신 PC에서 1초 미만으로 샘플이 실행됩니다.  
- **출력 형식은?** 예제는 Wavefront OBJ로 저장하지만, Aspose.3D는 다양한 포맷을 지원합니다.

## What is Linear Extrusion with Slices?

선형 압출은 2‑D 형태(프로파일)를 직선으로 늘려 3‑D 솔리드를 만드는 작업입니다. **Slices** 속성은 압출 시작점과 끝점 사이에 삽입되는 중간 교차‑섹션의 개수를 결정하며, 이는 부드러움과 폴리곤 수에 직접 영향을 줍니다.

## Why Use Slices in Linear Extrusion?

- **메시 밀도 제어:** 시각적 품질과 파일 크기 사이의 균형을 미세 조정합니다.  
- **성능 최적화:** 실시간 애플리케이션에는 슬라이스를 적게, 고해상도 렌더링에는 많이 사용합니다.  
- **창의적 유연성:** 객체마다 다른 슬라이스 수를 적용해 디자인 의도를 강조할 수 있습니다.

## Prerequisites

시작하기 전에 다음을 준비하세요:

- Aspose.3D for .NET Library – [여기](https://releases.aspose.com/3d/net/)에서 다운로드합니다.  
- C#를 지원하는 IDE(Visual Studio, Rider, VS Code 등).  
- C# 문법 및 객체‑지향 개념에 대한 기본 지식.  
- 3‑D 기하학을 실험해보고 싶은 호기심!

## Import Namespaces

핵심 Aspose.3D 클래스를 사용하기 위해 네임스페이스를 가져옵니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

간단한 직사각형 형태를 만들고 모서리가 완전히 날카롭지 않도록 작은 라운딩 반경을 적용합니다.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Step 2: Create a 3D Scene

`Scene`은 모든 노드, 메쉬, 조명 및 카메라를 담는 컨테이너 역할을 합니다.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Step 3: Add Left and Right Nodes

씬의 루트 아래에 두 개의 형제 노드를 생성합니다. 왼쪽 노드에는 슬라이스 수를 낮게, 오른쪽 노드에는 높게 설정해 시각적 차이를 비교할 수 있게 합니다.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Step 4: Perform Linear Extrusion on the Left Node (Low Detail)

여기서는 **2개의 슬라이스**만 사용해 직사각형을 압출합니다. 거친 메쉬가 생성되어 빠른 미리보기에 적합합니다.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Step 5: Perform Linear Extrusion on the Right Node (High Detail)

이번에는 **10개의 슬라이스**를 사용해 훨씬 부드러운 결과를 얻습니다. 기하학이 더 섬세해지는 것을 확인하세요.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Step 6: Save the 3D Scene

마지막으로 씬을 OBJ 파일로 저장합니다. `"Your Output Directory"`를 실제 머신에 존재하는 유효한 경로로 교체하세요.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **파일이 생성되지 않음** | 출력 경로가 잘못되었거나 쓰기 권한이 없습니다. | 절대 경로를 사용하고 폴더가 존재하는지 확인합니다. |
| **오브젝트가 평면처럼 보임** | `Slices`가 1 또는 0으로 설정되었습니다. | 최소 2 이상의 `Slices` 값을 지정해 눈에 보이는 압출을 만들세요. |
| **예상치 못한 기하학** | 라운딩 반경이 직사각형 크기에 비해 너무 큽니다. | `RoundingRadius`를 직사각형 가장 작은 변의 절반보다 작은 값으로 조정합니다. |

## Frequently Asked Questions

**Q: 압출 방향을 바꿀 수 있나요?**  
A: 네. 노드의 `Transform` 속성을 사용해 압출된 기하학을 회전하거나 이동한 뒤 저장하면 됩니다.

**Q: Aspose.3D가 다른 압출 타입을 지원하나요?**  
A: 물론입니다. `LinearExtrusion` 외에도 `RevolveExtrusion`, `SweepExtrusion` 등을 사용할 수 있습니다.

**Q: 어떤 파일 포맷으로 내보낼 수 있나요?**  
A: Aspose.3D는 OBJ, STL, FBX, 3MF, Collada 등 다양한 포맷을 지원합니다. `FileFormat` 열거형을 변경하면 됩니다.

**Q: 프로그래밍적으로 재질을 설정할 방법이 있나요?**  
A: 있습니다. 노드를 만든 뒤 해당 노드의 `Entity` 컬렉션에 `Material`을 할당하면 됩니다.

**Q: 슬라이스 수가 메모리 사용량에 어떤 영향을 미치나요?**  
A: 슬라이스가 많을수록 정점과 면의 수가 증가해 메모리 소비가 비례적으로 늘어납니다. 목표 플랫폼에 맞는 최적점을 찾기 위해 프로파일링을 활용하세요.

## Original FAQ's

### Q1: Aspose.3D for .NET를 다른 프로그래밍 언어와 함께 사용할 수 있나요?

A1: Aspose.3D는 주로 .NET용으로 설계되었지만, .NET 바인딩을 이용해 Python 등 다른 언어와의 상호 운용성을 탐색할 수 있습니다.

### Q2: Aspose.3D for .NET에 대한 자세한 문서는 어디서 찾을 수 있나요?

A2: Aspose.3D의 기능과 사용법에 대한 심층 정보를 보려면 [여기](https://reference.aspose.com/3d/net/)의 문서를 참고하세요.

### Q3: Aspose.3D for .NET의 무료 체험판이 있나요?

A3: 네, 라이브러리 기능을 구매 전 체험하려면 [여기](https://releases.aspose.com/)에서 무료 체험판을 받아보세요.

### Q4: Aspose.3D for .NET에 대한 기술 지원은 어떻게 받을 수 있나요?

A4: 지원이 필요하면 Aspose.3D 포럼 [여기](https://forum.aspose.com/c/3d/18)에서 문의하고 커뮤니티와 소통하세요.

### Q5: Aspose.3D for .NET의 임시 라이선스를 사용할 수 있나요?

A5: 네, 평가용으로 [여기](https://purchase.aspose.com/temporary-license/)에서 임시 라이선스를 발급받을 수 있습니다.

## Conclusion

이제 Aspose.3D for .NET를 사용해 슬라이스와 함께 **선형 압출**하는 방법을 익혔으며, 슬라이스 수에 따른 영향을 확인하고 작업을 내보내는 방법을 배웠습니다. 다른 프로파일을 실험하고 `Slices` 값을 조정하며, 재질이나 조명을 통합해 프로덕션 수준의 3‑D 에셋을 만들어 보세요.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}