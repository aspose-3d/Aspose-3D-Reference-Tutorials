---
date: 2025-12-18
description: Aspose.3D for Java를 사용하여 3D 씬을 만들고 OBJ 파일을 저장하는 방법을 배워보세요. 선형 압출 방향에
  대한 단계별 가이드를 따라가세요.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D 씬 만들기 – 압출 방향 설정 Aspose.3D Java
url: /ko/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 씬 만들기 – Extrusion 방향 설정 Aspose.3D Java

## Introduction

이 튜토리얼에서는 Aspose.3D for Java를 사용하여 **3D 씬을 만드는 방법**과 extrusion 방향을 제어하는 방법을 배웁니다. 건축 시각화, 제품 프로토타입, 게임 에셋 등을 제작하든, 선형 extrusion을 마스터하면 복잡한 형태를 빠르게 모델링할 수 있는 유연성을 얻을 수 있습니다. Java에서 노드를 추가하는 단계부터 **3D 모델 obj 파일 내보내기**까지 모든 과정을 차근차근 안내하므로 결과를 즉시 확인할 수 있습니다.

## Quick Answers
- **“create 3d scene”이란 무엇인가요?** Aspose.3D `Scene` 객체를 초기화하여 모든 기하학, 조명 및 카메라를 담는 것을 의미합니다.  
- **Extrusion 방향은 어떻게 설정하나요?** `LinearExtrusion` 인스턴스의 `setDirection(Vector3)` 메서드를 사용합니다.  
- **어떤 포맷으로 내보내야 하나요?** OBJ 포맷(`FileFormat.WAVEFRONTOBJ`)은 3‑D 워크플로우에서 널리 지원됩니다.  
- **Aspose.3D에 라이선스가 필요하나요?** 개발 단계에서는 무료 체험판을 사용할 수 있으며, 실제 서비스에서는 상용 라이선스가 필요합니다.  
- **Java에서 노드를 더 추가할 수 있나요?** 네—`scene.getRootNode().createChildNode()`를 사용해 원하는 만큼 객체를 추가할 수 있습니다.

## What is a “create 3d scene” workflow?

**create 3d scene** 워크플로우는 빈 `Scene` 객체를 시작점으로 삼아, geometry(예: extrusion된 프로파일)를 추가하고, 변환을 적용한 뒤 최종적으로 OBJ와 같은 파일 포맷으로 저장하는 일련의 과정을 말합니다. 이 패턴은 Aspose.3D 기반 대부분의 3‑D 애플리케이션의 핵심 구조입니다.

## Why set extrusion direction?

Extrusion 방향을 설정하면 extrusion 과정에서 형태를 기울이거나 회전, 왜곡시킬 수 있어 후처리 없이도 최종 기하학을 정확히 제어할 수 있습니다. 특히 다음과 같은 경우에 유용합니다.

- 테이퍼드 컬럼이나 맞춤형 파이프 제작.  
- 기계 부품에서 비표준 축에 맞춘 extrusion.  
- 시각 효과를 위한 예술적 형태 생성.

## Prerequisites

시작하기 전에 다음이 준비되어 있어야 합니다.

- 기본 Java 지식.  
- Aspose.3D 라이브러리 설치 – [여기](https://releases.aspose.com/3d/java/)에서 다운로드.  
- Eclipse 또는 IntelliJ IDEA와 같은 IDE.

## Import Packages

먼저 필요한 Aspose.3D 클래스를 임포트합니다:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Extrusion에 사용할 2‑D 프로파일을 생성합니다. 여기서는 둥근 사각형을 예시로 사용합니다:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** 라운딩 반경을 조정하면 extrusion 전 사각형 모서리의 날카로움이나 부드러움을 제어할 수 있습니다.

## Step 2: Create a Scene

이제 우리 객체들을 담을 **3D 씬**을 생성합니다:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

씬의 루트 노드에 두 개의 자식 노드(왼쪽, 오른쪽)를 추가하고, 왼쪽 노드를 약간 옆으로 이동시킵니다:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

왼쪽 노드에서 기본 Z‑축 방향으로 프로파일을 extrusion합니다. 전체 360° 트위스트와 슬라이스 수를 늘려 부드럽게 만듭니다:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

여기서는 **direction 설정 방법**을 보여줍니다. 커스텀 `Vector3`를 제공하여 extrusion을 (0.3, 0.2, 1) 방향으로 기울입니다:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

마지막으로 **OBJ 파일을 저장**하여 어떤 3‑D 뷰어에서도 결과를 확인할 수 있게 합니다:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

생성된 OBJ 파일을 열면 두 개의 extrusion된 사각형을 볼 수 있습니다: 하나는 기본 방향, 다른 하나는 지정한 벡터에 따라 기울어져 있습니다.

## Common Issues and Solutions

| Issue | Reason | Fix |
|-------|--------|-----|
| OBJ 파일이 비어 있음 | 씬이 저장되지 않았거나 경로가 잘못됨 | `MyDir`이 쓰기 가능한 폴더를 가리키는지, 파일 이름이 `.obj`로 끝나는지 확인 |
| Extrusion이 평평해 보임 | `setSlices` 값이 너무 낮음 | 슬라이스 수를 늘림(예: 200)으로 부드러운 기하학 확보 |
| Direction이 적용되지 않음 | Vector가 정규화되지 않음 | 정규화된 `Vector3`를 사용하거나 원하는 기울기에 맞게 값 조정 |

## Frequently Asked Questions

### Q1: Can I use Aspose.3D with other programming languages?
A1: Aspose.3D supports various languages, including .NET and Java.

### Q2: Is there a free trial available for Aspose.3D?
A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Where can I find detailed documentation for Aspose.3D for Java?
A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: How can I get support for Aspose.3D?
A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Are temporary licenses available for Aspose.3D?
A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}