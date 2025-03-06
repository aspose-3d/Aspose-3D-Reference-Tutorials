---
title: 상자에 PBR 재질 적용
linktitle: 상자에 PBR 재질 적용
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 그래픽의 세계를 탐험해보세요. 물리 기반 렌더링 자료를 사용하여 몰입형 장면을 쉽게 만들 수 있습니다.
weight: 10
url: /ko/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 상자에 PBR 재질 적용

## 소개

3D 그래픽의 매혹적인 세계에 오신 것을 환영합니다! 이 단계별 가이드에서는 강력한 .NET용 Aspose.3D 라이브러리를 살펴보고 PBR(물리 기반 렌더링) 자료를 사용하여 멋진 3D 장면을 만드는 방법을 알아봅니다. Aspose.3D는 3D 그래픽의 복잡한 프로세스를 단순화하고 개발자에게 가능성의 영역을 열어줍니다.

## 전제 조건

3D 그래픽의 흥미진진한 세계에 뛰어들기 전에 모든 설정이 완료되었는지 확인하겠습니다.

### .NET용 Aspose.3D 다운로드 및 설치

 방문하다[.NET 문서용 Aspose.3D](https://reference.aspose.com/3d/net/) 라이브러리 다운로드 및 설치에 대한 자세한 지침을 참조하세요.

### 라이센스 취득

Aspose.3D의 잠재력을 최대한 활용하려면 유효한 라이센스를 얻으십시오. 임시면허를 취득할 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/) 또는 정식 라이센스를 구매하세요[여기](https://purchase.aspose.com/buy).

## 네임스페이스 가져오기

먼저, .NET용 Aspose.3D의 기능을 활용하려면 필요한 네임스페이스를 가져와야 합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1단계: 장면 초기화

다음 코드 조각을 사용하여 3D 장면을 초기화하는 것부터 시작하세요.

```csharp
Scene scene = new Scene();
```

## 2단계: PBR 머티리얼 초기화

사실적인 렌더링을 달성하기 위해 PBR 재질 개체를 만듭니다.

```csharp
PbrMaterial mat = new PbrMaterial();
```

## 3단계: 재료 속성 설정

재질 특성을 미세 조정하여 거의 금속에 가깝고 매우 거칠게 만듭니다.

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## 4단계: 상자 만들기

PBR 재질이 적용될 상자를 생성합니다.

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## 5단계: 상자에 재료 적용

생성된 상자 노드에 PBR 재질을 할당합니다.

```csharp
boxNode.Material = mat;
```

## 6단계: 3D 장면 저장

원하는 출력 디렉터리를 사용하여 3D 장면을 STL 형식으로 저장합니다.

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

축하해요! .NET용 Aspose.3D를 사용하여 3D 장면의 상자에 PBR 재질을 성공적으로 적용했습니다.

## 결론

.NET용 Aspose.3D를 사용하여 3D 그래픽을 탐험하면 무한한 창의적 가능성의 문이 열립니다. 직관적인 API와 강력한 기능을 통해 시각적으로 멋진 장면을 만드는 것이 개발자에게 즐거운 경험이 됩니다.

## FAQ

### Q1: Aspose.3D는 다른 3D 파일 형식과 호환됩니까?

A1: 예, Aspose.3D는 다양한 3D 파일 형식을 지원하여 프로젝트의 유연성을 보장합니다.

### Q2: Aspose.3D를 상업용 애플리케이션으로 사용할 수 있습니까?

A2: 물론이죠! Aspose.3D는 애플리케이션에 원활하게 통합할 수 있는 상용 라이센스를 제공합니다.

### Q3: 평가판을 사용할 수 있나요?

 A3: 예, 무료 평가판을 다운로드하여 Aspose.3D의 기능을 탐색할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: 커뮤니티 지원과 토론은 어디서 찾을 수 있나요?

 A4: Aspose.3D 커뮤니티에 가입하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지원과 토론을 위해.

### Q5: Aspose.3D에 대한 임시 라이선스를 어떻게 얻나요?

 A5: 임시 라이센스를 얻을 수 있습니다[여기](https://purchase.aspose.com/temporary-license/) 평가 목적으로.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
