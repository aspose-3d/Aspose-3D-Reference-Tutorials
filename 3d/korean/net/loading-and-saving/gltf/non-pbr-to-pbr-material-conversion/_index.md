---
title: 비PBR에서 PBR 재질로 변환
linktitle: 비PBR에서 PBR 재질로 변환
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D 살펴보기 - 비PBR 자료를 PBR 자료로 쉽게 변환하세요. 포괄적인 튜토리얼과 강력한 API.
weight: 16
url: /ko/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 비PBR에서 PBR 재질로 변환

## 소개

.NET용 Aspose.3D를 사용하여 비PBR(물리 기반 렌더링)을 PBR 재질로 변환하는 방법에 대한 단계별 가이드에 오신 것을 환영합니다. Aspose.3D는 개발자가 .NET 애플리케이션에서 3D 파일 형식으로 원활하게 작업할 수 있도록 하는 강력한 API입니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET용 Aspose.3D: .NET용 Aspose.3D 라이브러리가 설치되어 있는지 확인하세요. 다운로드 링크를 찾을 수 있습니다[여기](https://releases.aspose.com/3d/net/).

- C#의 기본 이해: 이 자습서에서는 사용자가 C# 프로그래밍에 대한 기본적인 이해를 갖고 있다고 가정합니다.

- IDE(통합 개발 환경): Visual Studio 등 .NET 개발을 위해 선호하는 IDE를 선택합니다.

## 네임스페이스 가져오기

C# 코드에서 필요한 네임스페이스를 가져오는 것부터 시작하세요.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1단계: 새 3D 장면 초기화

다음 코드를 사용하여 새로운 3D 장면을 만드는 것부터 시작하세요.

```csharp
// ExStart:Non_PBRtoPBRMaterial
// 새로운 3D 장면 초기화
var scene = new Scene();
```

## 2단계: 3D 개체 만들기

다음으로 상자와 같은 3D 개체를 만듭니다.

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## 3단계: 재료 변환 구성

비PBR에서 PBR로 변환을 위한 재질 변환 옵션을 설정합니다.

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## 4단계: GLTF 2.0 형식으로 저장

변환된 장면을 GLTF 2.0 형식으로 저장합니다.

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

특정 사용 사례에 필요에 따라 이 단계를 반복하여 각 세부 정보가 올바르게 구성되었는지 확인하세요.

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 Non-PBR을 PBR 자료로 변환하는 방법을 성공적으로 배웠습니다. 이 강력한 도구는 .NET 애플리케이션에서 3D 그래픽 조작에 대한 무한한 가능성을 열어줍니다.

## FAQ

### Q1: Aspose.3D는 모든 3D 파일 형식과 호환됩니까?

A1: 예, Aspose.3D는 광범위한 3D 파일 형식을 지원하여 프로젝트에 유연성을 제공합니다.

### Q2: Aspose.3D를 상업용 애플리케이션으로 사용할 수 있습니까?

 A2: 물론이죠! Aspose.3D는 상용제품이므로 구매가 가능합니다[여기](https://purchase.aspose.com/buy).

### Q3: 테스트하려면 임시 라이센스가 필요합니까?

 A3: 예, 테스트 목적으로 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).

### Q4: Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A4: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.

### Q5: 무료 평가판이 제공됩니까?

 A5: 예, 무료 평가판을 사용해 볼 수 있습니다.[여기](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
