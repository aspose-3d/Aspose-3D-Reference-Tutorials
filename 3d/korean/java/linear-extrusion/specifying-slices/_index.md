---
date: 2026-05-24
description: Aspose.3D for Java를 사용하여 Slices와 함께 3d extrusion을 만드는 방법을 배웁니다. 이 단계별
  가이드는 선형 extrusion, 반경 라운딩 설정 및 OBJ 내보내기를 다룹니다.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Slices를 사용한 3D Extrusion 만들기 – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Slices를 사용한 3D Extrusion 만들기 – Aspose.3D for Java
url: /ko/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 슬라이스를 이용한 압출 만들기 – Aspose.3D for Java

## 소개

부드럽고 정밀한 **3D 압출** 객체를 만들고 싶다면, 슬라이스 수를 제어하는 것이 핵심입니다. 이 튜토리얼에서는 Aspose.3D for Java를 사용하여 선형 압출을 수행하면서 슬라이스를 지정하는 방법을 단계별로 안내합니다. 슬라이스 수가 왜 중요한지, 라운딩 반경을 어떻게 설정하는지, 그리고 결과를 OBJ 파일로 내보내어 모든 3‑D 파이프라인에서 사용할 수 있는 방법을 확인하게 됩니다.

## 빠른 답변
- **“슬라이스”가 무엇을 제어하나요?** 압출 표면을 근사하기 위해 사용되는 중간 단면의 수입니다.  
- **어떤 메서드가 슬라이스 수를 설정하나요?** `LinearExtrusion.setSlices(int)`  
- **프로파일의 라운딩 반경을 변경할 수 있나요?** 예, `RectangleShape.setRoundingRadius(double)`을 통해 가능합니다.  
- **이 예제에서 사용된 파일 형식은 무엇인가요?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **코드를 실행하려면 라이선스가 필요합니까?** 평가용으로는 무료 체험판으로 충분하지만, 제품 환경에서는 상용 라이선스가 필요합니다.

`LinearExtrusion.setSlices(int)`는 압출이 생성할 중간 슬라이스의 수를 설정합니다.  
`RectangleShape.setRoundingRadius(double)`는 직사각형 프로파일의 모서리 반경을 정의합니다.

## 슬라이스를 사용한 Java 3D 압출 만들기

2‑D 프로파일을 로드하고, 슬라이스 수를 선택한 뒤, 라운딩 반경을 설정하고 `save`를 호출하면 전체 워크플로우가 몇 줄 안에 끝납니다. Aspose.3D for Java는 기하학 생성, 슬라이스 보간 및 OBJ 내보내기를 자동으로 처리하므로 저수준 메시 계산에 신경 쓰지 않고 시각적 품질에 집중할 수 있습니다.

## 슬라이스가 있는 선형 압출이란?

슬라이스가 있는 선형 압출은 평면 2‑D 형태를 직선으로 따라 스윕하면서 구성 가능한 수의 중간 단면을 생성해 3‑D 솔리드로 변환합니다. 슬라이스 수는 라운드된 모서리와 같은 곡선 가장자리가 얼마나 부드럽게 렌더링되는지를 직접적으로 좌우합니다.

## Java에서 3D 압출을 만들 때 Aspose.3D를 사용하는 이유

Aspose.3D는 모든 압출 매개변수에 대해 **전체 프로그래밍 제어**를 제공하고, **50개 이상의 입출력 형식**(OBJ, FBX, STL, GLTF 등)을 지원하며, 전체 파일을 메모리에 로드하지 않고도 **수백 페이지 모델**을 처리할 수 있습니다. Java가 지원되는 모든 플랫폼에서 실행되며, 네이티브 DLL이 필요 없고, Windows, Linux, macOS 전반에 걸쳐 결정적인 결과를 보장합니다.

## 전제 조건

1. **Java Development Kit** – JDK 8 이상이 설치되어 있어야 합니다.  
2. **Aspose.3D for Java** – 공식 사이트에서 라이브러리를 다운로드하십시오 [here](https://releases.aspose.com/3d/java/).  
3. 원하는 IDE 또는 텍스트 편집기.

## 패키지 가져오기

프로젝트에 Aspose.3D 네임스페이스를 추가하여 3‑D 모델링 클래스를 사용할 수 있게 합니다.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 단계별 가이드

### 단계 1: 씬 설정 및 프로파일 정의

`RectangleShape`는 2‑D 직사각형 프로파일을 정의하는 클래스입니다.  
먼저 `RectangleShape`를 생성하고 **라운딩 반경**을 지정해 모서리를 부드럽게 만듭니다.  
`Scene`은 모든 노드와 기하학을 담는 루트 컨테이너입니다.  
그 다음 모든 기하학을 보관할 새로운 `Scene`을 초기화합니다.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 단계 2: 각 압출을 위한 자식 노드 객체 생성

`Node`는 기하학 및 변환을 보유할 수 있는 씬 그래프의 요소를 나타냅니다.  
모든 기하학은 `Node` 아래에 존재합니다. 여기서는 저슬라이스 압출용 노드와 고슬라이스 압출용 노드, 두 개의 형제 노드를 생성하고, 결과를 쉽게 비교할 수 있도록 왼쪽 노드를 약간 옆으로 이동합니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 단계 3: 선형 압출 수행 및 슬라이스 설정

`LinearExtrusion`은 프로파일을 선형으로 스윕하여 솔리드를 생성하는 클래스입니다.  
`LinearExtrusion`은 Aspose.3D에서 2‑D 프로파일을 직선을 따라 압출해 솔리드를 만드는 클래스입니다. **익명 내부 클래스**를 사용해 `setSlices`를 호출하여 부드러움을 제어합니다. 왼쪽 노드는 슬라이스 2개(거친)만 사용하고, 오른쪽 노드는 슬라이스 10개(부드러운)를 사용합니다.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 단계 4: OBJ 내보내기 – 씬 저장

마지막으로 씬을 Wavefront OBJ 파일로 저장합니다. 이 형식은 3‑D 편집기와 게임 엔진에서 널리 지원됩니다. 이는 Aspose.3D의 **OBJ Java 내보내기** 기능을 보여줍니다.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 일반적인 문제 및 해결책

| 문제 | 발생 원인 | 해결 방법 |
|------|----------|-----------|
| **압출이 평평하게 보임** | 슬라이스 수가 1 또는 0으로 설정됨 | `setSlices`가 값 ≥ 2로 호출되었는지 확인하십시오. |
| **라운드된 모서리가 들쭉날쭉함** | 슬라이스 수에 비해 라운딩 반경이 너무 작음 | 보다 부드러운 곡선을 위해 반경이나 슬라이스 수 중 하나를 늘리십시오. |
| **저장 시 파일을 찾을 수 없음** | `MyDir`이 존재하지 않는 폴더를 가리킴 | 디렉터리를 미리 생성하거나 절대 경로를 사용하십시오. |

## 자주 묻는 질문

**Q: Aspose.3D for Java를 어떻게 다운로드하나요?**  
A: 라이브러리를 [here](https://releases.aspose.com/3d/java/)에서 다운로드할 수 있습니다.

**Q: Aspose.3D 문서는 어디에서 찾을 수 있나요?**  
A: 문서는 [here](https://reference.aspose.com/3d/java/)에서 확인하십시오.

**Q: 무료 체험판을 이용할 수 있나요?**  
A: 예, 무료 체험판은 [here](https://releases.aspose.com/)에서 확인할 수 있습니다.

**Q: Aspose.3D 지원을 어떻게 받을 수 있나요?**  
A: 지원 포럼은 [here](https://forum.aspose.com/c/3d/18)에서 방문하십시오.

**Q: 임시 라이선스를 구매할 수 있나요?**  
A: 예, 임시 라이선스는 [here](https://purchase.aspose.com/temporary-license/)에서 구입할 수 있습니다.

**마지막 업데이트:** 2026-05-24  
**테스트 환경:** Aspose.3D for Java 24.11 (작성 시 최신 버전)  
**작성자:** Aspose

## 관련 튜토리얼

- [Aspose.3D를 사용한 Java 3D 압출 만들기](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Aspose.3D for Java로 선형 압출 방향 설정 방법](/3d/java/linear-extrusion/setting-direction/)
- [선형 압출에서 트위스트가 적용된 3D 씬 만들기 – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}