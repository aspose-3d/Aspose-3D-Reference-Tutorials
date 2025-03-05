---
title: PDF로 3D 저장
linktitle: PDF로 3D 저장
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 살펴보세요. 원활한 3D 모델링 및 렌더링을 위한 유용한 라이브러리입니다. 3D 모델을 PDF로 손쉽게 저장하세요.
type: docs
weight: 19
url: /ko/net/loading-and-saving/pdf/save-3d-in-pdf/
---
## 소개

.NET용 Aspose.3D 사용에 대한 종합 가이드에 오신 것을 환영합니다! 이 튜토리얼에서는 3D 모델을 PDF 형식으로 저장하는 특정 작업에 중점을 두고 3D 모델을 로드하고 저장하는 과정을 안내합니다. .NET용 Aspose.3D는 3D 파일 작업을 위한 효율적인 도구를 제공하는 강력한 라이브러리로, 해당 분야의 개발자와 매니아에게 필수적인 리소스입니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET용 Aspose.3D: 라이브러리가 설치되어 있는지 확인하세요. 그렇지 않은 경우 다음에서 다운로드할 수 있습니다.[.NET 문서용 Aspose.3D](https://reference.aspose.com/3d/net/).

- 개발 환경: 선호하는 .NET 개발 환경을 설정합니다.

- 3D 개념의 기본 이해: 이 가이드에서는 3D 모델링에 대한 기본 지식을 가정하고 있으므로 기본적인 3D 개념을 숙지하세요.

## 네임스페이스 가져오기

.NET 프로젝트에서 Aspose.3D가 제공하는 기능에 액세스하려면 필요한 네임스페이스를 가져와야 합니다.

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## 1단계: 새 장면 만들기

Aspose.3D 라이브러리를 사용하여 새로운 3D 장면을 초기화하는 것부터 시작하세요. 이는 3D 모델의 기초 역할을 합니다.

```csharp
Scene scene = new Scene();
```

## 2단계: 원통 하위 노드 추가

저장 과정을 보여주기 위해 간단한 3D 모델인 원통을 만들어 보겠습니다. 원통을 장면에 하위 노드로 추가합니다.

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## 3단계: 렌더링 모드 및 조명 구성표 설정

3D 장면에 대한 렌더링 모드와 조명 구성표를 정의합니다. 이 단계에서는 모델의 시각적 모양을 사용자 정의할 수 있습니다.

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## 4단계: PDF 형식으로 저장

마지막으로 출력 디렉터리와 파일 이름을 지정하여 저장 프로세스를 실행합니다. 이 경우 3D 모델을 PDF 형식으로 저장합니다.

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

"Your Output Directory"를 원하는 경로로 바꾸십시오.

## 결론

 축하해요! .NET용 Aspose.3D를 사용하여 간단한 3D 모델을 만들고 PDF 형식으로 저장하는 방법을 성공적으로 배웠습니다. 이는 이 강력한 라이브러리를 통해 달성할 수 있는 작업의 시작일 뿐입니다. 더 많은 기능과 가능성을 살펴보세요.[Aspose.3D 문서](https://reference.aspose.com/3d/net/).

## FAQ

### Q1: Aspose.3D for .NET은 모든 3D 파일 형식과 호환됩니까?

A1: 예, .NET용 Aspose.3D는 광범위한 3D 파일 형식을 지원하여 다양한 산업 표준과의 호환성을 보장합니다.

### Q2: 저장 과정에서 3D 모델의 시각적 측면을 사용자 정의할 수 있습니까?

A2: 물론이죠! 튜토리얼에 표시된 대로 렌더링 모드, 조명 구성표 등을 조정하여 원하는 시각적 결과를 얻을 수 있습니다.

### Q3: .NET용 Aspose.3D에 대한 지원은 어디서 찾을 수 있습니까?

 A3: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) .NET용 Aspose.3D와 관련된 커뮤니티 지원 및 토론을 위해.

### Q4: .NET용 Aspose.3D에 대한 무료 평가판이 있습니까?

 A4: 예, 액세스할 수 있습니다.[무료 시험판](https://releases.aspose.com/) 구매하기 전에 .NET용 Aspose.3D의 기능을 살펴보세요.

### Q5: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A5: 임시 면허를 받으려면 다음을 방문하세요.[이 링크](https://purchase.aspose.com/temporary-license/) 제공된 지침을 따르세요.