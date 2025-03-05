---
title: 노드 계층 이해
linktitle: 노드 계층 이해
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D의 강력한 기능을 활용해 보세요! 이 단계별 가이드를 통해 노드 계층 구조 조작에 대해 자세히 알아보세요. 멋진 3D 장면을 손쉽게 만들어 보세요.
type: docs
weight: 16
url: /ko/net/geometry-and-hierarchy/node-hierarchy/
---
## 소개

개발자가 .NET 애플리케이션에서 3D 장면 및 모델을 원활하게 작업할 수 있도록 지원하는 강력한 라이브러리인 .NET용 Aspose.3D의 세계에 오신 것을 환영합니다. 이 튜토리얼에서는 Aspose.3D를 사용하여 3D 장면의 노드 계층 구조를 이해하는 복잡한 과정을 살펴보겠습니다. 이 가이드를 마치면 노드를 통해 3D 장면의 구조를 조작하는 방법을 확실하게 이해하여 놀라운 시각적 경험을 만들 수 있습니다.

## 전제 조건

이 3D 여정을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET 라이브러리용 Aspose.3D: Aspose.3D 라이브러리가 .NET 프로젝트에 통합되어 있는지 확인하세요. 아직 이 작업을 수행하지 않았다면 다음 페이지로 이동하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 안내를 위해.

-  라이브러리 다운로드: Aspose.3D 라이브러리를 다운로드하지 않은 경우 다음에서 최신 버전을 다운로드하세요.[다운로드 링크](https://releases.aspose.com/3d/net/) 설명서에 제공된 설치 지침을 따르세요.

-  라이선스 받기: Aspose.3D의 잠재력을 최대한 활용하려면 유효한 라이선스가 필요합니다. 없으신 분들은 얻으시면 됩니다[여기](https://purchase.aspose.com/buy) 또는 다음을 선택하세요.[무료 시험판](https://releases.aspose.com/) 그 능력을 탐구합니다.

-  지원 및 커뮤니티: Aspose.3D 커뮤니티에 가입하세요.[지원 포럼](https://forum.aspose.com/c/3d/18)다른 개발자와 연결하고, 도움을 구하고, 최신 개발 소식을 받아보세요.

-  임시 라이선스(선택 사항): 구매하기 전에 Aspose.3D를 탐색하는 경우[임시 면허증](https://purchase.aspose.com/temporary-license/) 확장된 액세스를 위해.

이제 도구가 준비되었으므로 Aspose.3D를 사용하여 3D 노드 계층 구조를 조작하는 흥미로운 세계를 살펴보겠습니다.

## 네임스페이스 가져오기

.NET 프로젝트에서 Aspose.3D에서 제공하는 기능을 활용하려면 필요한 네임스페이스를 가져와야 합니다. 코드에 다음 줄을 추가합니다.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

이러한 네임스페이스를 사용하면 3D 장면 작업을 위한 필수 클래스 및 메서드에 액세스할 수 있습니다.

## 1단계: 장면 객체 초기화

```csharp
Scene scene = new Scene();
```

 다음을 사용하여 새로운 3D 장면을 생성하는 것으로 시작하십시오.`Scene` 수업.

## 2단계: 하위 노드 생성

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 노드 간 상위-하위 관계를 생성하여 계층적 구조를 구축합니다. 이 예에서는`cube1` 그리고`cube2` 의 하위 노드입니다.`top` 마디.

## 3단계: 메시 생성 및 할당

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 적절한 방법을 사용하여 메쉬를 생성합니다(여기서는`CreateMeshUsingPolygonBuilder`) 이를 하위 노드에 할당합니다.

## 4단계: 번역 설정

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

각 큐브 노드에 대한 변환을 정의하여 3D 공간에 배치합니다.

## 5단계: 상위 노드에 회전 적용

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

상위 노드 회전(`top`), 이 변환이 모든 하위 노드에 어떤 영향을 미치는지 관찰합니다.

## 6단계: 3D 장면 저장

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

출력 디렉터리를 지정하고 3D 장면을 원하는 파일 형식(여기서는 FBX7500ASCII)으로 저장합니다.

## 7단계: 성공 메시지 표시

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

노드 계층 구조 및 저장된 파일 위치가 성공적으로 추가되었음을 사용자에게 알립니다.

## 결론

축하해요! .NET용 Aspose.3D에서 복잡한 3D 노드 계층 구조를 성공적으로 탐색했습니다. 이 튜토리얼에서는 3D 장면을 쉽게 생성, 조작 및 저장하는 방법에 대한 지식을 제공합니다. 여정을 계속하면서 더 많은 기능을 탐색하고 .NET 프로젝트에서 Aspose.3D의 잠재력을 최대한 활용하십시오.

## FAQ

### Q1: 라이선스 없이 .NET용 Aspose.3D를 사용할 수 있나요?

A1: 라이선스로 모든 기능을 잠금 해제할 수 있지만 무료 평가판을 사용하면 제한된 기능으로 Aspose.3D를 탐색할 수 있습니다.

### Q2: 3D 장면 저장을 위해 지원되는 다른 파일 형식이 있습니까?

A2: 예, Aspose.3D는 다양한 형식을 지원합니다. 전체 목록은 설명서를 참조하세요.

### Q3: Aspose.3D 커뮤니티에 어떻게 기여할 수 있나요?

A3: 지원 포럼에 참여하고, 경험을 공유하고, 다른 사람들의 질문을 도와 기여하세요.

### Q4: Aspose.3D는 게임 개발에 적합합니까?

A4: 물론이죠! Aspose.3D는 다목적이며 게임 개발 프로젝트에 통합될 수 있습니다.

### Q5: 임시 라이센스와 정식 라이센스의 차이점은 무엇입니까?

A5: 임시 라이센스는 평가 목적으로 단기 액세스를 제공하는 반면, 정식 라이센스는 무제한 사용을 제공합니다.