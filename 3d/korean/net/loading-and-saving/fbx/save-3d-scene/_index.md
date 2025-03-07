---
title: 3D 장면을 FBX 파일로 저장
linktitle: 3D 장면을 FBX 파일로 저장
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D의 강력한 기능을 살펴보세요. 원활한 3D 장면 조작을 위한 다목적 라이브러리입니다. 쉽게 로드하고, 저장하고, 압축하세요.
weight: 20
url: /ko/net/loading-and-saving/fbx/save-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 장면을 FBX 파일로 저장

## 소개

.NET용 Aspose.3D를 사용하여 3D 장면 조작 영역으로의 흥미로운 여행에 오신 것을 환영합니다! 숙련된 개발자이든 호기심이 많은 팬이든 관계없이 이 튜토리얼은 3D 장면을 손쉽게 로드, 저장 및 압축하는 과정을 안내합니다.

## 전제 조건

3D 장면 조작의 매혹적인 세계에 뛰어들기 전에 다음 전제 조건이 갖추어져 있는지 확인하십시오.

-  .NET용 Aspose.3D: 다음에서 Aspose.3D 라이브러리를 다운로드하고 설치하세요.[다운로드 링크](https://releases.aspose.com/3d/net/).
-  문서화: 포괄적인 설명서를 통해 라이브러리의 기능을 숙지하십시오.[선적 서류 비치](https://reference.aspose.com/3d/net/).
- 출력 디렉터리: 튜토리얼 중에 생성된 출력 파일을 저장할 디렉터리를 설정합니다.

## 네임스페이스 가져오기

필요한 네임스페이스를 .NET 환경으로 가져와 탐색을 시작하겠습니다.

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## 로드 및 저장 - 3D 장면 저장

### 1단계: 3D 문서 로드

```csharp
Scene scene = Scene.FromFile("document.fbx");
```

 이 단계에서는 새로운`Scene` 객체를 만들고 기존 3D 문서를 로드합니다.`FromFile` 방법.

### 2단계: 장면을 스트림에 저장

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

 로드된 3D 장면을 다음을 사용하여 메모리 스트림에 저장합니다.`Save` 메서드를 사용하여 원하는 파일 형식(이 경우 FBX7500ASCII)을 지정합니다.


### 3단계: 장면을 로컬 경로에 저장

```csharp
scene.Save("output_out.fbx", FileFormat.FBX7500ASCII);
```

3D 장면을 로컬 경로에 저장하여 의미 있는 출력 디렉터리와 파일 이름을 제공합니다.

## 압축

이제 3D 장면의 압축 옵션을 살펴보겠습니다.

### 1단계: 3D 문서 로드

```csharp
Scene scene = new Scene("document.fbx");
```

 이전 예와 유사하게 3D 문서를`Scene` 물체.

### 2단계: 압축을 비활성화하고 저장합니다.

```csharp
scene.Save("UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

3D 장면을 저장하는 동안 압축을 비활성화하여 명확한 출력 경로와 파일 이름을 제공합니다.

## 결론

이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 3D 장면을 로드, 저장 및 압축하는 기본 측면을 살펴보았습니다. 이러한 지식으로 무장하면 자신만의 3D 여정을 시작하고 Aspose.3D 영역 내에서 창의적인 가능성을 발휘할 준비가 된 것입니다.

## FAQ

### Q1: Aspose.3D는 다양한 3D 파일 형식과 호환됩니까?

A1: 예, Aspose.3D는 광범위한 3D 파일 형식을 지원하여 프로젝트에 유연성을 제공합니다.

### Q2: Aspose.3D를 다른 .NET 라이브러리와 통합할 수 있습니까?

A2: 물론이죠! Aspose.3D는 다른 .NET 라이브러리와 원활하게 통합되어 애플리케이션의 기능을 향상시킵니다.

### Q3: Aspose.3D에 대한 임시 라이선스를 어떻게 얻을 수 있나요?

 A3: 다음을 방문하세요.[임시 면허증](https://purchase.aspose.com/temporary-license/) Aspose 웹사이트 페이지에서 임시 라이센스를 얻으세요.

### 질문4: 어디에서 도움을 구하거나 커뮤니티와 연결할 수 있나요?

 A4: 활발한 Aspose.3D 커뮤니티에 참여하세요.[법정](https://forum.aspose.com/c/3d/18) 지원을 구하고, 경험을 공유하고, 동료 애호가들과 협력합니다.

### Q5: Aspose.3D에 대한 무료 평가판이 있습니까?

 A5: 네, Aspose.3D의 기능을 탐색해 보세요.[무료 시험판](https://releases.aspose.com/) 오늘!
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
