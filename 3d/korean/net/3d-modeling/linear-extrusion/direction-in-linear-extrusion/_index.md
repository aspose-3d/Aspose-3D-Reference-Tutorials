---
title: 선형 돌출의 방향
linktitle: 선형 돌출의 방향
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 모델링의 세계를 열어보세요. 선형 압출 방향을 배우고, 창의성을 높이고, 몰입형 애플리케이션을 손쉽게 제작해 보세요.
weight: 11
url: /ko/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 선형 돌출의 방향

## 소개

역동적인 소프트웨어 개발 세계에서 몰입형 3D 모델을 만드는 것은 필수적인 기술입니다. .NET용 Aspose.3D는 개발자에게 애플리케이션에서 3D 모델링의 잠재력을 활용할 수 있는 강력한 도구 세트를 제공합니다. 이 튜토리얼에서는 선형 압출의 흥미로운 세계를 탐구하고 "선형 압출의 방향" 기능의 미묘한 차이를 살펴보겠습니다.

## 전제 조건

이 흥미진진한 여정을 시작하기 전에 다음과 같은 전제 조건이 갖추어져 있는지 확인하세요.

-  .NET용 Aspose.3D: 다음에서 라이브러리를 다운로드하고 설치하세요.[Aspose.3D .NET 문서](https://reference.aspose.com/3d/net/).

- 개발 환경: 작동하는 .NET 개발 환경이 설정되어 있는지 확인하세요.

## 네임스페이스 가져오기

.NET 프로젝트에서 Aspose.3D의 기능에 액세스하는 데 필요한 네임스페이스를 가져옵니다. 코드 시작 부분에 다음 줄을 추가합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 1단계: 기본 프로필 초기화

돌출할 기본 프로파일을 초기화하는 것부터 시작합니다. 이 예에서는 반올림 반경이 0.3인 직사각형 모양을 만듭니다.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2단계: 3D 장면 만들기

장면을 만들어 3D 걸작의 기반을 구축하세요.

```csharp
Scene scene = new Scene();
```

## 3단계: 노드 생성

3D 환경의 다양한 구성 요소를 나타내기 위해 장면 내에 노드를 생성합니다.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## 4단계: 방향이 없는 선형 압출

 다음을 사용하여 왼쪽 노드에서 선형 압출을 수행합니다.`Twist` 그리고`Slices` 속성.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 5단계: 방향이 있는 선형 압출

 다음을 통합하여 압출 기능을 확장합니다.`Direction` 오른쪽 노드의 속성입니다.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## 6단계: 3D 장면 저장

 3D 장면을 저장하여 창작물을 보존하세요. 바꾸다`"Your Output Directory"` 원하는 디렉토리로.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

축하해요! .NET용 Aspose.3D를 사용하여 선형 돌출을 성공적으로 구현했으며 기존 접근 방식과 방향 접근 방식을 모두 탐색했습니다.

## 결론

이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 3D 모델링의 매혹적인 영역을 탐색했습니다. 방향이 있거나 없는 선형 압출은 시각적으로 놀라운 응용 프로그램을 만들려는 개발자에게 무한한 가능성을 열어줍니다. Aspose.3D를 사용하면 3D 모델링의 강력한 기능을 손쉽게 사용할 수 있습니다.

## FAQ

### Q1: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A1: 방문[임시 면허를 양도하다](https://purchase.aspose.com/temporary-license/) 임시면허를 취득하기 위해

### Q2: Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A2: 가입하세요[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 도움을 구하고 지역 사회와 연결됩니다.

### Q3: 무료 평가판이 제공됩니까?

 A3: 예, 무료 평가판을 통해 기능을 살펴보세요.[Aspose.3D 릴리스](https://releases.aspose.com/).

### Q4: .NET용 Aspose.3D를 어떻게 구입합니까?

 A4: 다음으로 이동하세요.[구매 페이지 제안](https://purchase.aspose.com/buy) 라이선스 옵션 및 구매 세부정보를 확인하세요.

### Q5: .NET용 Aspose.3D에 대한 자세한 문서는 어디에서 찾을 수 있습니까?

 A5: 포괄적인 내용을 참조하세요.[Aspose.3D .NET 문서](https://reference.aspose.com/3d/net/) 자세한 정보를 확인하세요.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
