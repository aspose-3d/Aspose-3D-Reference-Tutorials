---
title: 쿼터니언 연결
linktitle: 쿼터니언 연결
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 장면에서 쿼터니언 조작의 강력한 기능을 살펴보세요. 몰입형 변환을 위해 쿼터니언을 단계별로 연결하는 방법을 알아보세요.
weight: 11
url: /ko/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 쿼터니언 연결

## 소개

.NET용 Aspose.3D를 사용하여 3D 장면에서 쿼터니언을 연결하는 포괄적인 튜토리얼에 오신 것을 환영합니다! 쿼터니언 조작 기술을 향상시키려는 개발자이거나 3D 애호가라면 잘 찾아오셨습니다. 이 튜토리얼에서는 프로세스를 단계별로 안내하여 원활한 학습 경험을 보장합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET 라이브러리용 Aspose.3D: 다음에서 라이브러리를 다운로드하고 설치합니다.[Aspose 웹 사이트](https://releases.aspose.com/3d/net/).
- 개발 환경: .NET용 개발 환경이 작동하는지 확인하세요.

## 네임스페이스 가져오기

.NET 프로젝트에 Aspose.3D의 기능을 활용하는 데 필요한 네임스페이스를 포함하세요.

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## 1단계: 장면 만들기

Aspose.3D 라이브러리를 사용하여 3D 장면을 만드는 것부터 시작하세요. 장면은 쿼터니언 조작을 위한 캔버스 역할을 합니다.

```csharp
Scene scene = new Scene();
```

## 2단계: 쿼터니언 정의

 세 개의 쿼터니언을 정의하고,`q1`, `q2` , 그리고`q3`, 각각은 특정 회전을 나타냅니다.

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## 3단계: 원통 만들기

각각 쿼터니언을 나타내는 세 개의 원통을 만듭니다. 정의된 쿼터니언을 기반으로 회전 및 평행 이동 속성을 설정합니다.

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// q2와 q3에 대해 반복합니다.
```

## 4단계: 파일에 저장

출력 형식과 파일 이름을 지정하여 장면을 파일에 저장합니다.

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## 5단계: 성공 메시지 표시

쿼터니언이 연결되고 파일이 저장되면 파일 경로와 함께 성공 메시지를 인쇄합니다.

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 3D 장면에서 쿼터니언을 연결하는 방법을 성공적으로 배웠습니다. 프로젝트에서 고유한 변환을 달성하기 위해 다양한 쿼터니언 조합을 실험해 보세요.

## FAQ

### Q1: 3D 그래픽의 쿼터니언이란 무엇입니까?

A1: 쿼터니언은 3D 공간에서 회전을 나타내는 데 사용되는 수학적 엔터티로, 다른 회전 표현에 비해 이점을 제공합니다.

### Q2: 다른 .NET 라이브러리와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?

A2: 예, .NET용 Aspose.3D는 다른 .NET 라이브러리와 원활하게 작동하도록 설계되었습니다.

### Q3: .NET용 Aspose.3D에 대한 무료 평가판이 있습니까?

A3: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: .NET용 Aspose.3D에 대한 지원을 어떻게 받을 수 있나요?

 A4: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.

### Q5: .NET용 Aspose.3D의 임시 라이선스를 사용할 수 있나요?

 A5: 예, 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
