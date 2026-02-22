---
date: 2026-02-22
description: Aspose.3D for Java를 사용하여 선형 압출에서 방향을 설정하고 3D 모델 OBJ를 내보내는 방법을 배워보세요.
  단계별 가이드를 따라하세요.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java를 사용한 선형 압출에서 방향 설정 방법
url: /ko/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java에서 선형 압출의 방향 설정 방법

## 소개

이 포괄적인 튜토리얼에서는 Aspose.3D for Java를 사용하여 선형 압출을 수행할 때 **방향을 설정하는 방법**을 알아볼 수 있습니다. CAD와 유사한 도구를 만들거나 게임 엔진용 기하학을 생성하든, 압출 방향을 제어하면 필요한 정확한 형태를 만들 수 있습니다. 프로파일 초기화부터 결과를 OBJ 파일로 저장하는 단계까지 차근차근 안내하므로 Java에서 직접 **export 3d model obj** 파일을 **내보낼** 수도 있습니다.

## 빠른 답변
- **선형 압출의 주요 클래스는 무엇인가요?** `LinearExtrusion`
- **압출 방향을 정의하는 메서드는?** `setDirection(Vector3 direction)`
- **결과를 OBJ로 내보낼 수 있나요?** Yes, using `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **개발에 라이선스가 필요합니까?** 무료 체험판을 사용할 수 있으며, 제품 환경에서는 라이선스가 필요합니다.
- **어떤 Java IDE가 가장 적합한가요?** IntelliJ IDEA 또는 Eclipse 모두 완벽히 지원됩니다.

## 선형 압출이란?

선형 압출은 사각형이나 원과 같은 2‑D 프로파일을 직선으로 연장하여 3‑D 솔리드를 생성합니다. 기본적으로 압출은 양의 Z‑축을 따라 진행되지만, Aspose.3D에서는 `setDirection` 속성을 사용해 경로를 변경할 수 있습니다.

## 왜 선형 압출에서 방향을 설정해야 할까요?

- 씬 내 기존 객체와 기하학을 정렬하기 위해.
- 추가 변환 단계 없이 기울어진 또는 각진 부품을 만들기 위해.
- 특정 좌표계와 일치해야 하는 모델을 내보내기 위해 (예: 3‑D 프린팅이나 게임 엔진).

## 사전 요구 사항

- Java에 대한 기본 지식.
- Aspose.3D 라이브러리를 설치합니다. [here](https://releases.aspose.com/3d/java/)에서 다운로드할 수 있습니다.
- Eclipse 또는 IntelliJ IDEA와 같은 IDE.

## 패키지 가져오기

먼저, 핵심 3‑D 클래스와 유틸리티 타입을 제공하는 네임스페이스를 가져옵니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 단계 1: 기본 프로파일 초기화

압출될 형태를 생성합니다. 이 예제에서는 가장자리를 부드럽게 만들기 위해 작은 라운딩 반경을 가진 `RectangleShape`을 사용합니다.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 단계 2: 씬 생성

`Scene` 객체는 모든 3‑D 노드, 조명, 카메라 및 재질을 담는 컨테이너 역할을 합니다.

```java
Scene scene = new Scene();
```

## 단계 3: 노드 생성

씬 루트에 두 개의 자식 노드를 추가합니다—왼쪽 압출용과 오른쪽 압출용 각각 하나씩. 오른쪽 노드는 두 객체가 겹치지 않도록 이동됩니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 단계 4: 왼쪽 노드에서 선형 압출 수행

왼쪽 노드에서 기본 Z‑축 방향으로 프로파일을 압출합니다. 또한 전체 360° 트위스트를 추가하고 슬라이스 수를 늘려 메쉬를 부드럽게 합니다.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 단계 5: 방향을 지정하여 오른쪽 노드에서 선형 압출 수행

여기서 **방향을 설정**합니다. `setDirection`에 사용자 정의 `Vector3`을 전달하면 압출이 벡터 (0.3, 0.2, 1)을 따라 진행되어 기울어진 형태가 만들어집니다.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 단계 6: 3D 씬 저장

마지막으로, 씬을 Wavefront OBJ 형식으로 내보냅니다. 이 단계는 **save obj file java** 프로젝트를 보여주며, 결과를 모든 3‑D 뷰어에서 쉽게 확인할 수 있게 합니다.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 일반적인 문제와 해결책

| 문제 | 발생 원인 | 해결 방법 |
|------|----------|----------|
| OBJ 파일이 비어 있음 | 프로파일이 노드에 추가되지 않음 | `createChildNode`가 유효한 노드에서 호출되었는지 확인 |
| 방향이 변경되지 않음 | `setDirection`이 압출이 이미 구성된 후에 호출됨 | 예시와 같이 `LinearExtrusion` 초기화 단계에서 방향을 설정 |
| 저해상도 메쉬 | `setSlices` 값이 너무 낮음 | 슬라이스 수를 늘리세요 (예: 100 이상) |

## 결론

이제 선형 압출에서 **방향을 설정하는 방법**, 트위스트와 슬라이스 설정을 조정하는 방법, 그리고 Aspose.3D for Java를 사용해 **3d model obj** 파일을 **내보내는 방법**을 알게 되었습니다. 이러한 기술을 통해 기하학 생성에 세밀한 제어가 가능해지며, 3‑D 자산을 보다 큰 파이프라인에 쉽게 통합할 수 있습니다.

## FAQ

### Q1: Aspose.3D를 다른 프로그래밍 언어와 함께 사용할 수 있나요?

A1: Aspose.3D는 .NET 및 Java를 포함한 다양한 프로그래밍 언어를 지원합니다.

### Q2. Aspose.3D의 무료 체험판이 있나요?

A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Aspose.3D for Java에 대한 자세한 문서는 어디에서 찾을 수 있나요?

A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: Aspose.3D 지원을 어떻게 받을 수 있나요?

A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Aspose.3D의 임시 라이선스가 제공되나요?

A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**마지막 업데이트:** 2026-02-22  
**테스트 환경:** Aspose.3D for Java (최신 릴리스)  
**작성자:** Aspose