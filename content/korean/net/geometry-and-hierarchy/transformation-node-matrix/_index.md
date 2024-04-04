---
title: 변환 매트릭스로 노드 변환
linktitle: 변환 매트릭스로 노드 변환
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 장면에서 노드를 쉽게 변환할 수 있습니다. 튜토리얼을 통해 단계별 노드 변환을 알아보세요.
type: docs
weight: 21
url: /ko/net/geometry-and-hierarchy/transformation-node-matrix/
---
## 소개

3D 그래픽 및 시각화의 동적 영역에서 장면 내의 개체를 조작하는 능력은 중요한 측면입니다. .NET용 Aspose.3D는 개발자가 변환 매트릭스를 사용하여 노드를 원활하게 변환하고 3D 장면에 창의성과 제어 계층을 추가할 수 있도록 지원합니다. 이 튜토리얼에서는 3D 장면에서 노드를 변환하는 과정을 단계별로 안내합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

1.  .NET 라이브러리용 Aspose.3D: .NET 프로젝트에 Aspose.3D 라이브러리가 설치되어 있는지 확인하세요. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/).

2. 개발 환경: 작동하는 .NET 개발 환경을 설정하고, 아직 설정하지 않은 경우 변환을 구현할 새 프로젝트를 만듭니다.

## 네임스페이스 가져오기

필요한 네임스페이스를 .NET 프로젝트로 가져오는 것부터 시작하세요. 이러한 네임스페이스는 3D 장면 조작을 위한 필수 클래스와 메서드를 제공합니다.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

이제 기본 사항을 다루었으므로 변환 프로세스를 단계별 가이드로 나누어 보겠습니다.

## 1단계: 장면 초기화

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// 장면 객체 초기화
Scene scene = new Scene();

```

이 단계에서는 새로운 빈 3D 장면을 만듭니다.

## 2단계: 메시 생성 및 장면에 연결

```csharp
// Common 클래스를 호출하여 폴리곤 빌더 방법을 사용하여 메쉬를 생성하여 메쉬 인스턴스를 설정합니다.
Mesh mesh = (new Box()).ToMesh();

// 메시에 대한 컨테이너 노드를 만듭니다.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

여기서는 폴리곤 빌더 방법을 사용하여 메시를 생성하고 이를 노드에 할당하여 큐브의 지오메트리를 설정합니다.

## 3단계: 사용자 정의 번역 매트릭스 설정

```csharp
// 맞춤 번역 매트릭스 설정
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

노드에 적용되는 특정 변환을 결정하려면 사용자 정의 변환 행렬을 정의하십시오. 원하는 변환에 필요한 대로 행렬 값을 조정합니다.

장면에 큐브 노드를 포함시켜 전체 3D 환경의 일부로 만듭니다.

## 4단계: 장면 저장

```csharp
// 문서 디렉터리의 경로입니다.
var output = "TransformationToNode.fbx";

// 지원되는 파일 형식으로 3D 장면 저장
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

출력 디렉터리와 파일 이름을 지정한 다음 3D 장면을 원하는 파일 형식으로 저장합니다. 이 예에서는 FBX7500ASCII 형식으로 저장합니다.

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 3D 장면에서 변환 매트릭스를 사용하여 노드를 성공적으로 변환했습니다. 이 기능을 통해 다양하고 시각적으로 매력적인 3D 애플리케이션을 사용할 수 있습니다.

## FAQ

### Q1: 3D 그래픽의 변환 행렬이란 무엇입니까?

A1: 변환 행렬은 3D 공간의 객체에 다양한 변환(이동, 회전, 크기 조정)을 적용하는 데 사용되는 수학적 표현입니다.

### Q2: 단일 노드에 여러 변환을 적용할 수 있습니까?

A2: 예, 각 행렬을 곱하고 그 결과를 노드에 적용하여 여러 변환을 결합할 수 있습니다.

### Q3: 3D 장면 저장을 위해 지원되는 다른 파일 형식이 있습니까?

 A3: .NET용 Aspose.3D는 STL, GLTF, OBJ 등을 포함한 다양한 파일 형식을 지원합니다. 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 포괄적인 목록을 보려면

### Q4: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A4: 다음을 방문하세요.[임시 라이센스 페이지](https://purchase.aspose.com/temporary-license/)Aspose 웹사이트에서 평가 목적으로 임시 라이선스를 얻으세요.

### Q5: 어디서 도움을 구하거나 Aspose.3D 커뮤니티에 연결할 수 있나요?

 A5: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) Aspose.3D를 사용하여 질문하고, 경험을 공유하고, 다른 개발자와 연결하세요.