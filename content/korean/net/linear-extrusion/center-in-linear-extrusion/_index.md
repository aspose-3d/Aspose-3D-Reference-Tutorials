---
title: 선형 돌출의 중심
linktitle: 선형 돌출의 중심
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 모델링의 세계를 탐험해보세요. 선형 압출 기술을 중심으로 멋진 디자인을 만들고 창의력을 발휘해보세요.
type: docs
weight: 10
url: /ko/net/linear-extrusion/center-in-linear-extrusion/
---
## 소개

.NET용 Aspose.3D를 사용한 선형 돌출 마스터링에 대한 포괄적인 가이드에 오신 것을 환영합니다. 3D 모델링 기술을 향상하고 멋진 돌출을 만들고 싶다면 잘 찾아오셨습니다. 이 튜토리얼에서는 선형 압출 기술, 특히 센터링 측면에 초점을 맞춰 디자인을 완전히 새로운 수준으로 끌어올리는 기술을 자세히 살펴보겠습니다.

## 전제 조건

이 흥미진진한 여정을 시작하기 전에 다음과 같은 전제 조건이 갖추어져 있는지 확인하세요.

- C# 프로그래밍 언어에 대한 기본 이해.
- 컴퓨터에 Visual Studio가 설치되어 있습니다.
-  .NET 라이브러리용 Aspose.3D는 다음에서 다운로드할 수 있습니다.[Aspose.3D .NET 문서](https://reference.aspose.com/3d/net/).
-  다음에 대한 액세스 권한이 있는지 확인하십시오.[Aspose.3D .NET 문서](https://reference.aspose.com/3d/net/) 튜토리얼 전반에 걸쳐 참조할 수 있습니다.

## 네임스페이스 가져오기

시작하기 위해 필요한 네임스페이스를 가져오겠습니다. 이는 우리의 3D 모델링 걸작을 위한 토대를 마련할 것입니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 1단계: 기본 프로필 초기화

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2단계: 3D 장면 만들기

```csharp
Scene scene = new Scene();
```

## 3단계: 왼쪽 및 오른쪽 노드 생성

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 4단계: 왼쪽 노드에서 선형 돌출 수행

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 5단계: 참조용 접지면 설정

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 6단계: 오른쪽 노드에서 선형 압출 수행

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 7단계: 참조용 접지면 설정(오른쪽 노드)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 8단계: 3D 장면 저장

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 센터링을 통한 선형 압출 기술을 성공적으로 마스터했습니다. 다양한 매개변수를 자유롭게 실험하고 이 기술이 제공하는 광대한 가능성을 탐색해 보세요.

## FAQ

### Q1: 다른 프로그래밍 언어와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?

A1: Aspose.3D는 주로 C# 및 VB.NET과 같은 .NET 언어를 지원합니다.

### Q2: Aspose.3D 관련 쿼리에 대한 지원은 어디서 찾을 수 있나요?

 A2: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 전담 지원 및 토론을 위해.

### Q3: .NET용 Aspose.3D에 대한 무료 평가판이 있습니까?

 A3: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A4: 임시 라이센스를 취득할 수 있습니다[여기](https://purchase.aspose.com/temporary-license/).

### Q5: .NET용 Aspose.3D 라이선스는 어디서 구입할 수 있나요?

 A5: 라이센스 구매[여기](https://purchase.aspose.com/buy).
