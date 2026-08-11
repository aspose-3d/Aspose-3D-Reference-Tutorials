---
date: 2026-08-02
description: Aspose.3D for Java를 사용하여 선형 압출에서 압출 방향을 변경하고 OBJ 파일을 내보내는 방법을 배웁니다. 단계별
  가이드를 따라 주세요.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: 압출 방향 변경 – Aspose.3D Java
og_description: Aspose.3D for Java를 사용하여 선형 압출에서 압출 방향을 변경하고 OBJ 파일을 내보냅니다. 이 가이드는
  단계별 코드와 개발자를 위한 팁을 제공합니다.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: 압출 방향 변경 – Aspose.3D Java 튜토리얼
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 3D 모델에서 압출 방향 변경 – Aspose.3D Java
url: /ko/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 모델에서 압출 방향 변경 – Aspose.3D Java

## 소개

이 포괄적인 튜토리얼에서는 Aspose.3D for Java를 사용하여 선형 압출을 수행할 때 **압출 방향을 변경하는 방법**을 알아봅니다. CAD와 유사한 도구를 만들든, 게임 엔진용 에셋을 준비하든, 3D 프린팅용 부품을 생성하든, 압출 방향을 제어하면 필요한 정확한 형태를 만들 수 있습니다. 프로파일 초기화부터 결과를 OBJ 파일로 저장하는 단계까지 차례대로 안내하므로 Java에서 직접 **3D 모델 OBJ** 파일을 **내보낼** 수도 있습니다.

## 빠른 답변
- **선형 압출을 수행하는 클래스는?** `LinearExtrusion`
- **압출 벡터를 설정하는 메서드는?** `setDirection(Vector3 direction)`
- **결과를 OBJ로 저장할 수 있나요?** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **프로덕션에 라이선스가 필요합니까?** 무료 체험을 이용할 수 있으며, 상업적 사용에는 라이선스가 필수입니다.
- **Aspose.3D와 가장 잘 호환되는 IDE는?** IntelliJ IDEA와 Eclipse가 완전히 지원됩니다.

## 선형 압출이란?

선형 압출은 사각형이나 원과 같은 2‑D 스케치를 직선으로 연장하여 3‑D 솔리드를 생성하는 과정입니다. 기본적으로 압출은 양의 Z‑축을 따라 진행되지만, Aspose.3D에서는 `setDirection` 속성을 사용해 경로를 변경할 수 있어 최종 형상을 완전히 제어할 수 있습니다.

## 선형 압출에서 압출 방향을 변경해야 하는 이유

압출 방향을 변경하면 새로운 형상을 기존 객체와 정렬하고, 추가 변환 없이 각진 부품을 만들며, 하위 파이프라인(예: 3‑D 프린터나 게임 엔진)에서 요구하는 좌표계에 맞는 모델을 생성할 수 있습니다. 이를 통해 후처리 단계가 필요 없게 되고, 불필요한 회전을 피하는 방향 벡터를 사용할 경우 파일 크기 오버헤드를 최대 15 %까지 줄일 수 있습니다.

## 사전 요구 사항

- Java에 대한 기본 지식.
- Aspose.3D 라이브러리가 설치되어 있어야 합니다. [here](https://releases.aspose.com/3d/java/)에서 다운로드할 수 있습니다. 모든 Aspose 릴리스는 메인 페이지 [here](https://releases.aspose.com/)에서 확인할 수 있습니다.
- Eclipse 또는 IntelliJ IDEA와 같은 IDE.

## 패키지 가져오기

`com.aspose.threed` 네임스페이스는 핵심 3‑D 클래스와 유틸리티 타입을 제공합니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 단계 1: 기본 프로파일 초기화

`RectangleShape` 클래스는 압출될 2‑D 프로파일을 생성합니다. 작은 라운딩 반경을 지정하면 가장자리가 부드럽게 보입니다.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 단계 2: 씬 생성

`Scene` 클래스는 Aspose.3D의 최상위 컨테이너로, 모든 3‑D 노드, 조명, 카메라 및 재질을 포함합니다.

```java
Scene scene = new Scene();
```

## 단계 3: 노드 생성

`Node`는 씬 그래프에서 객체를 나타내며, 기하학, 변환 및 기타 속성을 연결할 수 있게 해줍니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 단계 4: 왼쪽 노드에 선형 압출 수행

`LinearExtrusion`은 압출 작업을 수행하여 2‑D 프로파일을 3‑D 메시로 변환합니다.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 단계 5: 방향을 지정하여 오른쪽 노드에 선형 압출 수행

여기서는 **압출 방향을 변경**합니다. `setDirection`에 사용자 정의 `Vector3`를 전달하면 압출이 벡터 (0.3, 0.2, 1)을 따라 진행되어 씬 좌표계에 맞는 기울어진 형태를 만들 수 있습니다.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 단계 6: 3D 씬 저장

`save` 메서드는 씬을 지정된 형식의 파일로 저장합니다.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 일반적인 문제 및 해결책

| 문제 | 발생 원인 | 해결 방법 |
|------|----------|----------|
| OBJ 파일이 비어 있음 | 프로파일이 노드에 추가되지 않음 | `createChildNode`가 유효한 노드에서 호출되었는지 확인 |
| 방향이 변경되지 않음 | `setDirection`이 압출이 이미 구성된 후에 호출됨 | 예시와 같이 `LinearExtrusion` 초기화 단계에서 방향을 설정 |
| 저해상도 메쉬 | `setSlices` 값이 너무 낮음 | 슬라이스 수를 늘리세요(예: 100 이상) |

## 결론

이제 선형 압출에서 **압출 방향을 변경하는 방법**, 트위스트와 슬라이스 설정을 조정하는 방법, 그리고 Aspose.3D for Java를 사용해 **3D 모델 OBJ** 파일을 **내보내는 방법**을 알게 되었습니다. 이러한 기술을 통해 기하학 생성에 세밀한 제어가 가능해지며, 3‑D 에셋을 대규모 파이프라인에 쉽게 통합할 수 있습니다.

## 자주 묻는 질문

**Q:** Aspose.3D를 다른 프로그래밍 언어와 함께 사용할 수 있나요?  
**A:** 네—Aspose.3D는 .NET 및 Java용 API를 제공하여 크로스‑플랫폼 개발이 가능합니다.

**Q:** Aspose.3D의 무료 체험판이 있나요?  
**A:** 물론입니다. 전체 기능을 무료 체험판으로 확인하려면 [here](https://releases.aspose.com/)를 방문하세요.

**Q:** Aspose.3D for Java에 대한 자세한 문서는 어디서 찾을 수 있나요?  
**A:** 포괄적인 레퍼런스는 [here](https://reference.aspose.com/3d/java/)에서 확인할 수 있습니다.

**Q:** Aspose.3D 지원을 어떻게 받을 수 있나요?  
**A:** 커뮤니티와 제품 팀의 도움을 받으려면 공식 [Aspose.3D forum](https://forum.aspose.com/c/3d/18) 를 방문하세요.

**Q:** 테스트용 임시 라이선스가 제공되나요?  
**A:** 네—임시 라이선스는 [here](https://purchase.aspose.com/temporary-license/)에서 받을 수 있습니다.

**마지막 업데이트:** 2026-08-02  
**테스트 환경:** Aspose.3D for Java (latest release)  
**작성자:** Aspose

{{< blocks/products/products-backtop-button >}}

## 관련 튜토리얼

- [형상 압출 방법 - Java에서 선형 압출로 3D 모델 만들기](/3d/java/linear-extrusion/)
- [Aspose.3D를 사용한 Java 3D 압출 생성](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D 그래픽 튜토리얼 – 선형 압출에서 중심 제어](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}