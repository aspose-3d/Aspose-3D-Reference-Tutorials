---
date: 2026-03-26
description: Aspose.3D for .NET을 사용하여 3D 씬에 공급업체 정보를 추가하고 FBX 파일을 저장하는 방법을 배워보세요.
  실행 가능한 코드를 포함한 단계별 가이드를 따라하세요.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Aspose.3D를 사용하여 벤더 정보 추가 및 FBX 씬 저장 방법
url: /ko/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D를 사용하여 벤더 정보 추가 및 FBX 씬 저장 방법

## Introduction

이 포괄적인 튜토리얼에 오신 것을 환영합니다. 여기서는 **벤더** 세부 정보를 3D 씬에 추가하고 Aspose.3D for .NET을 사용하여 **FBX** 파일을 저장하는 방법을 보여줍니다. 건축 시각화, 게임 에셋, 엔지니어링 모델을 만들든, 벤더 및 애플리케이션 메타데이터를 삽입하면 씬이 더 풍부해지고 다운스트림 관리가 쉬워집니다. 단계별로 진행해 보겠습니다.

## Quick Answers
- **“add vendor”(벤더 추가)란 무엇인가요?** 씬의 AssetInfo 블록에 애플리케이션 및 벤더 이름을 저장합니다.  
- **어떤 포맷이 벤더 정보를 지원하나요?** FBX(ASCII 또는 바이너리)는 저장 시 메타데이터를 유지합니다.  
- **FBX를 어떻게 저장하나요?** `scene.Save(path, FileFormat.FBX7500ASCII)` 또는 바이너리 버전을 사용합니다.  
- **라이선스가 필요한가요?** 개발용으로는 무료 체험판을 사용할 수 있으며, 프로덕션에서는 상용 라이선스가 필요합니다.  
- **측정 단위를 변경할 수 있나요?** 예, `AssetInfo.UnitName` 및 `AssetInfo.UnitScaleFactor`를 설정합니다.

## What is “how to add vendor” in a 3D scene?

3D 씬에서 “벤더 추가”란 무엇인가요?  
벤더 정보를 추가한다는 것은 `Scene` 객체의 `AssetInfo` 속성을 채우는 것을 의미합니다. 이러한 속성은 파일과 함께 저장되어 FBX 파일을 사용하는 모든 사람이 어떤 애플리케이션으로 생성되었는지, 벤더가 누구인지 확인할 수 있습니다.

## Why add vendor information?
- **추적 가능성:** 대규모 파이프라인에서 모델의 출처를 빠르게 식별합니다.  
- **규정 준수:** 일부 산업에서는 자산 관리 목적으로 명시적인 벤더 태깅이 필요합니다.  
- **자동화:** 스크립트가 벤더 메타데이터를 기반으로 파일을 필터링하거나 처리할 수 있습니다.

## Prerequisites

- Aspose.3D for .NET이 설치되어 있어야 합니다. [Aspose.3D for .NET 페이지](https://releases.aspose.com/3d/net/)에서 다운로드할 수 있습니다.

## Import Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## How to Add Vendor Information

### Step 1: Initialize a 3D Scene

```csharp
Scene scene = new Scene();
```

`Scene`을 새로 생성하면 작업할 수 있는 깨끗한 캔버스를 얻을 수 있습니다.

### Step 2: Set Application and Vendor Information

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

여기서는 `ApplicationName`과 `ApplicationVendor`에 의미 있는 문자열을 할당하여 **벤더 정보를 추가하는 방법**을 보여줍니다.

### Step 3: Define Measurement Units

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

단위 시스템을 지정하면 FBX 파일을 여는 사람이 차원을 올바르게 해석할 수 있습니다. 이 예제에서는 하나의 “pole”(폴) = 60 cm 로 설정합니다.

## How to Save FBX Scene

### Step 4: Save the Scene (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

이 코드는 FBX 7.5.0 ASCII 버전을 사용하여 **FBX를 저장하는 방법**을 보여줍니다. 바이너리를 원한다면 `FBX7500ASCII`를 `FBX7500Binary`로 교체하면 됩니다.

> **Pro tip:** 선택한 포맷과 일치하도록 파일 확장자 `.fbx`를 유지하세요; 그렇지 않으면 일부 뷰어가 내용을 잘못 해석할 수 있습니다.

### Step 5: Display Success Message

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

친절한 콘솔 메시지는 벤더 메타데이터가 포함된 씬이 디스크에 정상적으로 저장되었음을 확인시켜 줍니다.

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Viewer에 벤더 정보가 표시되지 않음** | 파일을 **FBX ASCII** 또는 **Binary** 형식으로 저장했는지 확인하세요; 일부 오래된 뷰어는 한 형식만 읽습니다. |
| **경로에 공백이 포함됨** | 경로를 따옴표로 감싸거나 `Path.Combine`을 사용해 안전한 파일 경로를 만드세요. |
| **단위 스케일이 잘못 표시됨** | `UnitScaleFactor`를 다시 확인하세요; 이는 미터에 대한 배율입니다. |
| **라이선스 예외 발생** | 테스트용으로 무료 체험판을 사용하고, 프로덕션 빌드에는 정식 라이선스를 획득하세요. |

## Frequently Asked Questions

**Q: Aspose.3D for .NET을 다른 프로그래밍 언어와 함께 사용할 수 있나요?**  
A: Aspose.3D는 주로 .NET 언어를 지원하지만, 다른 언어와의 상호 운용 옵션을 탐색할 수 있습니다.

**Q: Aspose.3D for .NET의 무료 체험판이 있나요?**  
A: 네, 무료 체험판은 [여기](https://releases.aspose.com/)에서 이용할 수 있습니다.

**Q: Aspose.3D 관련 문의에 대한 지원은 어떻게 받나요?**  
A: 커뮤니티와 지원을 위해 [Aspose.3D 포럼](https://forum.aspose.com/c/3d/18)을 방문하세요.

**Q: Aspose.3D for .NET의 임시 라이선스를 구매할 수 있나요?**  
A: 네, 임시 라이선스는 [여기](https://purchase.aspose.com/temporary-license/)에서 구매할 수 있습니다.

**Q: Aspose.3D for .NET의 자세한 문서는 어디에서 찾을 수 있나요?**  
A: 자세한 내용은 [문서](https://reference.aspose.com/3d/net/)를 참고하세요.

---

**마지막 업데이트:** 2026-03-26  
**테스트 환경:** Aspose.3D 24.11 for .NET  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}