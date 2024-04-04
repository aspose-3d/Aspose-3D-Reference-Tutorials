---
title: 빈 3D 문서 만들기
linktitle: 빈 3D 문서 만들기
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 문서 생성의 세계를 탐험해보세요. 놀라운 3D 장면을 손쉽게 생성, 편집 및 저장하세요.
type: docs
weight: 11
url: /ko/net/loading-and-saving/create-empty-3d-document/
---
## 소개

.NET용 Aspose.3D를 사용하여 3D 문서 생성의 세계에 오신 것을 환영합니다! 이 튜토리얼에서는 3D 문서 로드 및 저장의 기본 사항을 살펴보겠습니다. .NET용 Aspose.3D는 3D 장면 작업을 위한 강력한 도구 세트를 제공하며, 원활하게 시작할 수 있도록 각 단계를 안내합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET용 Aspose.3D: 라이브러리가 설치되어 있는지 확인하세요. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/net/).

## 네임스페이스 가져오기

시작하려면 .NET 프로젝트에서 필요한 네임스페이스를 가져옵니다.

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 로드 및 저장 - 빈 3D 문서 만들기

### 1단계: 출력 디렉터리 설정

```csharp
// 문서 디렉터리의 경로입니다.
var output = "Your Output Directory" + "document.fbx";
```

### 2단계: 빈 3D 문서 만들기

```csharp
// ExStart:CreateEmpty3DDocument

// Scene 클래스의 객체 생성
Scene scene = new Scene();

// 3D 장면 문서를 FBX 형식으로 저장
scene.Save(output);

// ExEnd:CreateEmpty3DDocument
```

### 3단계: 결과 표시

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

축하해요! .NET용 Aspose.3D를 사용하여 첫 번째 빈 3D 문서를 만들었습니다. 이 라이브러리의 잠재력을 최대한 활용하려면 더 많은 특징과 기능을 자유롭게 탐색해 보세요.

## 결론

 이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 빈 3D 문서를 만드는 기본 사항을 다루었습니다. 3D 개발 과정을 계속 진행하면서 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 심층적인 통찰력과 고급 기능을 확인하세요.

## FAQ

### Q1: Aspose.3D for .NET은 초보자에게 적합합니까?

A1: 예, .NET용 Aspose.3D는 사용자 친화적인 인터페이스를 제공하므로 초보자와 숙련된 개발자 모두가 액세스할 수 있습니다.

### Q2: 구매하기 전에 .NET용 Aspose.3D를 사용해 볼 수 있나요?

 A2: 물론이죠! 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q3: .NET용 Aspose.3D에 대한 지원을 어떻게 받을 수 있나요?

 A3: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 도움을 구하고 지역 사회와 연결됩니다.

### Q4: .NET용 Aspose.3D에 임시 라이선스를 사용할 수 있습니까?

 A4: 예, 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).

### Q5: .NET용 Aspose.3D를 어디서 구입할 수 있나요?

 A5: 라이브러리를 구매할 수 있습니다.[여기](https://purchase.aspose.com/buy).