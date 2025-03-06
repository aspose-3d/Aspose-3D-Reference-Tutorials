---
title: 사용자 정의 바이너리 형식으로 3D 메시 저장
linktitle: 사용자 정의 바이너리 형식으로 3D 메시 저장
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D의 세계를 탐험해 보세요. 사용자 정의 바이너리 형식으로 메시를 저장하는 방법을 알아보세요.
weight: 13
url: /ko/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 사용자 정의 바이너리 형식으로 3D 메시 저장

## 소개

개발자가 쉽게 3D 파일 작업을 할 수 있도록 지원하는 강력한 라이브러리인 .NET용 Aspose.3D의 세계에 오신 것을 환영합니다. 이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 사용자 정의 바이너리 형식으로 3D 메시를 저장하는 프로세스를 자세히 살펴보겠습니다. 이 가이드에서는 귀하가 C#에 대한 기본적인 이해가 있고 Aspose.3D 라이브러리에 익숙하다고 가정합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 사항이 준비되어 있는지 확인하세요.

-  .NET용 Aspose.3D: Aspose.3D 라이브러리가 설치되어 있는지 확인하세요. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).

- 개발 환경: Visual Studio와 같이 선호하는 C# 개발 환경을 설정합니다.

- 3D 파일 입력: 사용자 정의 바이너리 형식으로 변환하려는 3D 파일(예: test.fbx)이 있습니다.

## 네임스페이스 가져오기

C# 코드에 Aspose.3D 기능에 액세스하는 데 필요한 네임스페이스를 포함합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## 1단계: 3D 파일 로드

Aspose.3D를 사용하여 3D 파일을 로드합니다. 이 예에서는 "test.fbx"라는 파일을 로드합니다.

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## 2단계: 사용자 정의 바이너리 형식 정의

3D 메시를 저장할 사용자 정의 바이너리 형식의 구조를 정의합니다. 이 예에서는 MeshBlock, Vertex 및 Triangle이 구성 요소로 포함된 구조를 사용합니다.

```csharp
// 정점의 메모리 레이아웃은 다음과 같습니다.
// float[3] 위치;
// float[3] 보통;
// 플로트[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## 3단계: 쓰기 위해 파일 열기

변환된 3D 메시가 저장될 쓰기용 바이너리 파일을 엽니다.

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## 4단계: 노드 및 엔터티 반복

3D 장면의 각 노드를 방문하여 메시 엔터티를 사용자 정의 바이너리 형식으로 변환합니다. 조명, 카메라 및 기타 메시가 아닌 개체를 무시합니다.

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ...(계속 처리 중)
    }
    return true;
});
```

## 5단계: 제어점과 삼각형 변환 및 쓰기

각 메시 엔터티에 대해 제어점을 월드 공간으로 변환하고 이를 삼각형 인덱스와 함께 바이너리 파일에 씁니다.

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//메시의 메모리 레이아웃은 다음과 같습니다.
// float[16] 변환_매트릭스;
// int vertices_count;
// int index_count;
// 정점[vertices_count] 정점;
// ushort[indices_count] 인덱스;


//쓰기 변환
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//정점/인덱스 수 쓰기
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//정점과 인덱스 쓰기
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## 결론

이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 사용자 정의 바이너리 형식으로 3D 메시를 저장하는 프로세스를 다루었습니다. 이 강력한 라이브러리는 개발자에게 3D 파일을 원활하게 조작하는 데 필요한 도구를 제공합니다. 프로젝트에서 Aspose.3D의 잠재력을 최대한 활용하려면 다양한 형식과 설정을 실험해 보세요.

## 자주 묻는 질문

### Q1: 다른 프로그래밍 언어와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?

A1: Aspose.3D는 주로 .NET 언어를 지원하지만 다른 언어에 대한 호환성 옵션을 탐색할 수도 있습니다.

### Q2: 추가 예제와 리소스는 어디서 찾을 수 있나요?

 A2:[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18)지원과 사례를 찾고 커뮤니티에 참여할 수 있는 좋은 장소입니다.

### Q3: Aspose.3D에 사용할 수 있는 평가판이 있습니까?

 A3: 예, 다음에서 무료 평가판을 받을 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: Aspose.3D에 대한 임시 라이선스를 어떻게 얻나요?

 A4: 방문[이 링크](https://purchase.aspose.com/temporary-license/) 테스트 목적으로 임시 라이센스를 얻으려면.

### Q5: .NET용 Aspose.3D를 구입할 수 있나요?

 A5: 예, Aspose.3D를 다음 사이트에서 구입할 수 있습니다.[구매 페이지](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
