---
title: Aspose.3D를 사용하여 Java의 3D 개체에 PBR 재료 적용
linktitle: Aspose.3D를 사용하여 Java의 3D 개체에 PBR 재료 적용
second_title: Aspose.3D 자바 API
description: Aspose.3D를 사용하여 Java의 3D 개체에 사실적인 PBR 자료를 적용하는 방법을 알아보세요. 물리 기반 렌더링으로 시각적 품질을 향상시킵니다.
type: docs
weight: 10
url: /ko/java/geometry/apply-pbr-materials-to-objects/
---
## 소개

Aspose.3D를 사용하여 Java의 3D 객체에 PBR(물리 기반 렌더링) 자료를 적용하는 방법에 대한 단계별 가이드에 오신 것을 환영합니다. Aspose.3D는 3D 모델 및 장면 작업을 위한 포괄적인 기능을 제공하는 강력한 Java 라이브러리입니다. 이 튜토리얼에서는 실제 조명과 표면 속성을 시뮬레이션하여 3D 개체의 사실성을 향상시키는 PBR 재료를 적용하는 데 중점을 둘 것입니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

1. Java 개발 환경: 시스템에 Java가 설치되어 있는지 확인하십시오.

2.  Aspose.3D 라이브러리: 다음에서 Aspose.3D 라이브러리를 다운로드하여 설치하세요.[다운로드 링크](https://releases.aspose.com/3d/java/).

3.  문서:[선적 서류 비치](https://reference.aspose.com/3d/java/)Aspose.3D를 사용하여 라이브러리 기능에 익숙해지세요.

4.  임시면허(선택) : 면허가 없을 경우 임시면허를 취득할 수 있습니다.[임시 면허증](https://purchase.aspose.com/temporary-license/) 시험용.

## 패키지 가져오기

Java 프로젝트에 Aspose.3D를 사용하는 데 필요한 패키지를 포함하십시오. 코드에 다음 가져오기 문을 추가합니다.

```java
import com.aspose.threed.*;
```

## 1단계: 장면 초기화

Aspose.3D를 사용하여 3D 장면을 만드는 것부터 시작하세요. 장면은 3D 개체의 캔버스 역할을 합니다.

```java
// ExStart:초기화장면
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// 확장:초기화장면
```

## 2단계: PBR 머티리얼 초기화

PBR 재질을 생성하고 금속성 및 거칠기 요소와 같은 속성을 사용자 정의합니다.

```java
// ExStart:초기화PBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

## 3단계: 3D 개체 만들기

PBR 재질이 적용될 3D 개체(예: 상자)를 생성합니다.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

## 4단계: 3D 장면 저장

적용된 PBR 자료를 포함한 3D 장면을 STL과 같은 특정 파일 형식으로 저장합니다.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
//확장:Save3DScene
```

더 복잡한 장면이나 다른 개체에 대해 이 단계를 반복합니다.

## 결론

축하해요! Aspose.3D를 사용하여 Java의 3D 개체에 PBR 자료를 성공적으로 적용했습니다. 이를 통해 3D 모델의 시각적 매력이 향상되어 더욱 사실적이고 시각적으로 놀랍게 만들어집니다.

## FAQ

### Q1: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?

 A1: 네, 가능합니다. 방문하다[구매 페이지](https://purchase.aspose.com/buy) 라이선스 세부정보를 확인하세요.

### Q2: Aspose.3D에 대한 지원을 받으려면 어떻게 해야 합니까?

 A2: 가입하세요[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지역 사회 지원 및 지원을 위해.

### Q3: 무료 평가판이 제공됩니까?

 A3: 예, 다음을 탐색할 수 있습니다.[무료 시험판](https://releases.aspose.com/) 구매하기 전에.

### Q4: Aspose.3D에 대한 자세한 문서는 어디서 찾을 수 있나요?

 A4: 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/java/) 종합적인 안내를 위해.

### Q5: 테스트를 위한 임시 라이센스는 어떻게 얻나요?

 A5: 방문[이 링크](https://purchase.aspose.com/temporary-license/) 임시면허를 취득하기 위해