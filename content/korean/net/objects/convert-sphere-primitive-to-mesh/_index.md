---
title: 구형 프리미티브를 메시로 변환
linktitle: 구형 프리미티브를 메시로 변환
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 탐색하고 사용자 정의 메모리 레이아웃을 사용하여 Sphere Mesh를 Triangle Mesh로 쉽게 변환하세요. 원활한 통합을 위한 단계별 가이드를 따르세요.
type: docs
weight: 16
url: /ko/net/objects/convert-sphere-primitive-to-mesh/
---
## 소개
.NET용 Aspose.3D의 강력한 기능을 활용하여 구형 메시를 사용자 정의 메모리 레이아웃이 있는 삼각형 메시로 변환하려고 하시나요? 이 단계별 가이드는 프로세스를 안내하므로 초보자도 쉽게 따라할 수 있습니다. 이 튜토리얼이 끝나면 .NET용 Aspose.3D를 사용하여 이를 달성하는 방법을 확실하게 이해하게 될 것입니다.
## 전제 조건
튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.
- .NET 프로그래밍에 대한 기본 지식.
-  .NET 라이브러리용 Aspose.3D가 설치되었습니다. 다음에서 다운로드할 수 있습니다.[.NET용 Aspose.3D 다운로드 페이지](https://releases.aspose.com/3d/net/).
- C# 프로그래밍 언어에 익숙합니다.
## 네임스페이스 가져오기
C# 프로젝트에서 Aspose.3D 기능을 활용하려면 필요한 네임스페이스를 가져와야 합니다.
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 1단계: 장면 객체 초기화
```csharp
// 장면 객체 초기화
Scene scene = new Scene();
```
## 2단계: 노드 클래스 객체 초기화
```csharp
// 노드 클래스 객체 초기화
Node cubeNode = new Node("sphere");
```
## 3단계: 구형 메시를 형식화된 TriMesh로 변환
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## 4단계: 사용자 정의된 구조로 정점 데이터 가져오기
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## 5단계: 32비트 및 16비트 인덱스 가져오기
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## 6단계: 정점 및 인덱스 데이터를 메모리 스트림에 쓰기
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## 7단계: 노드를 메시 형상으로 지정
```csharp
cubeNode.Entity = sphere;
```
## 8단계: 장면에 노드 추가
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## 9단계: 3D 장면 저장
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## 10단계: 결과 표시
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## MyVertex 샘플 소스 코드
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## 결론
축하해요! .NET용 Aspose.3D를 사용하여 사용자 정의 메모리 레이아웃을 사용하여 구형 메시를 삼각형 메시로 성공적으로 변환했습니다. 이 강력한 라이브러리는 .NET 애플리케이션에서 3D 개체를 조작하는 원활한 방법을 제공합니다.
## 자주 묻는 질문
### Q: 다른 .NET 프레임워크와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?
A: 예, .NET용 Aspose.3D는 다양한 .NET 프레임워크와 호환됩니다.
### Q: .NET용 Aspose.3D에 대한 자세한 문서는 어디서 찾을 수 있나요?
 답: 다음을 참조하세요.[.NET 문서용 Aspose.3D](https://reference.aspose.com/3d/net/) 자세한 정보를 확인하세요.
### Q: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?
 답: 방문하다[이 링크](https://purchase.aspose.com/temporary-license/) 임시면허를 취득하기 위해
### Q: .NET용 Aspose.3D에 사용할 수 있는 샘플 프로젝트가 있습니까?
 A: .NET 문서용 Aspose.3D를 살펴보고[GitHub 저장소](https://github.com/aspose-3d/Aspose.3D-for-.NET) 샘플 프로젝트의 경우.
### Q: .NET용 Aspose.3D 지원을 위한 활발한 커뮤니티가 있습니까?
 A: 네, 가입하세요.[.NET 포럼용 Aspose.3D](https://forum.aspose.com/c/3d/18) 지역사회의 도움을 받으려면.