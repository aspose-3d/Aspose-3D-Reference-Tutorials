---
title: 장면의 모든 메시를 재료별로 분할하기
linktitle: 장면의 모든 메시를 재료별로 분할하기
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 메쉬를 재료별로 분할하는 방법을 알아보세요. 3D 모델의 효율적인 구성 및 관리를 위한 단계별 가이드를 따르십시오.
type: docs
weight: 21
url: /ko/net/meshes/split-all-meshes-by-material/
---
## 소개
.NET용 Aspose.3D를 사용하여 3D 장면의 모든 메시를 재료별로 분할하는 방법에 대한 단계별 가이드에 오신 것을 환영합니다. 3D 모델로 작업하고 재료를 기반으로 메시를 효율적으로 구성하려는 경우 이 튜토리얼이 적합합니다. Aspose.3D는 3D 파일 작업을 위한 다양한 기능을 제공하는 강력한 .NET 라이브러리이므로 개발자에게 탁월한 선택입니다.
## 전제 조건
튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.
- C# 프로그래밍 언어에 대한 기본 이해.
- 컴퓨터에 Visual Studio가 설치되어 있습니다.
-  .NET 라이브러리용 Aspose.3D. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).
- 분할하려는 입력 3D 파일(예: "test.fbx")입니다.
## 네임스페이스 가져오기
C# 프로젝트에서 필요한 네임스페이스를 가져오는 것부터 시작하세요.
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 1단계: 3D 파일 로드
```csharp
// 문서 디렉터리의 경로입니다.
string input = RunExamples.GetDataFilePath("test.fbx");
// 3D 파일 로드
Scene scene = new Scene(input);
```
 이 단계에서는 Aspose.3D를 사용하여 3D 파일을 로드합니다.`Scene` 수업.
## 2단계: 모든 메시 분할
```csharp
// 모든 메쉬 분할
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 여기서는`SplitMesh` 의 방법`PolygonModifier` 머티리얼에 따라 모든 메시를 분할하는 클래스입니다.
## 3단계: 분할 장면 저장
```csharp
// 파일을 저장
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
변경 사항을 유지하려면 수정된 장면을 새 파일에 저장하세요.
## 4단계: 성공 메시지 표시
```csharp
// 성공 메시지 표시
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
작업이 성공적으로 완료되었음을 나타내는 성공 메시지를 인쇄합니다.
## 결론
축하해요! .NET용 Aspose.3D를 사용하여 3D 장면의 모든 메시를 재료별로 분할하는 방법을 성공적으로 배웠습니다. 이는 복잡한 3D 모델을 구성하고 관리하는 데 유용한 기술이 될 수 있습니다.
## 자주 묻는 질문
### 1. 다른 프로그래밍 언어와 함께 .NET용 Aspose.3D를 사용할 수 있나요?
Aspose.3D는 기본적으로 .NET용으로 설계되었지만 .NET 언어 바인딩을 통해 다른 언어와의 상호 운용성을 제공합니다.
### 2. 체험판이 있나요?
 예, 무료 평가판에 액세스할 수 있습니다[여기](https://releases.aspose.com/).
### 3. 더 많은 예제와 문서는 어디에서 찾을 수 있나요?
 다음에서 포괄적인 문서를 살펴보세요.[Aspose.3D 문서](https://reference.aspose.com/3d/net/).
### 4. Aspose.3D에 대한 지원은 어떻게 받을 수 있나요?
 방문하다[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.
### 5. 임시면허를 취득할 수 있나요?
 네, 임시면허증을 받으실 수 있습니다[여기](https://purchase.aspose.com/temporary-license/).