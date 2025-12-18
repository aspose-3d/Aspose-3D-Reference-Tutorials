---
date: 2025-12-18
description: Aspose.3D for Java를 사용하여 선형 압출에 지면 평면을 추가하고 중심 속성을 설정하는 방법을 단계별 코드 예제와
  함께 배워보세요.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java를 사용한 선형 압출에서 그라운드 플레인 및 컨트롤 센터 추가 방법
url: /ko/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java를 사용한 선형 압출에서 중심 제어

## 소개

Java에서 3D 씬을 구축할 때, **ground plane을 추가**하고 선형 압출에 **center 속성을 정확히 설정**하는 기능은 평범한 프로토타입과 세련된 비주얼 사이의 차이를 만들 수 있습니다. 이 튜토리얼에서는 압출 중심을 제어하고 Aspose.3D for Java를 사용해 ground plane을 추가하는 전체 과정을 단계별로 안내합니다. 왜 이것이 중요한지, 어떻게 설정하는지, 그리고 여러분의 프로젝트에 바로 적용할 수 있는 실행 가능한 코드 샘플을 확인해 보세요.

## 빠른 답변
- **“ground plane을 추가”하면 무엇을 하나요?** 얇은 참조 기하학을 생성하여 압출이 세계 좌표축에 대해 어느 위치에 있는지 시각적으로 확인할 수 있게 해줍니다.  
- **선형 압출의 중심을 어떻게 설정하나요?** `LinearExtrusion` 객체의 `setCenter(boolean)` 메서드를 사용합니다.  
- **샘플을 실행하려면 라이선스가 필요합니까?** 테스트용 임시 라이선스로 실행할 수 있으며, 실제 운영 환경에서는 정식 라이선스가 필요합니다.  
- **저장 형식은 무엇을 사용하나요?** 예제에서는 Wavefront OBJ(`.obj`) 형식으로 저장합니다.  
- **필요한 Java 버전은?** Java 8 이상이면 충분합니다.

## 3D 씬에서 “ground plane을 추가”한다는 의미는?

ground plane을 추가한다는 것은 X‑Z 평면에 얇은 직사각형 기하학(보통 최소 두께의 박스)를 삽입하는 것을 의미합니다. 시각적인 바닥 역할을 하여 다른 객체들의 높이와 정렬을 판단하기 쉽게 만들어 주며, 특히 압출 중심을 실험할 때 유용합니다.

## 선형 압출에 center 속성을 설정해야 하는 이유

기본적으로 선형 압출은 프로파일의 원점에서 시작합니다. `setCenter(true)` 로 center 속성을 설정하면 프로파일이 원점을 기준으로 중앙에 오도록 이동하여, 대칭 디자인이나 여러 객체 간 일관된 정렬이 필요할 때 유용합니다.

## 사전 요구 사항

이 튜토리얼을 시작하기 전에 다음 조건을 준비해 주세요:

1. **Java 개발 환경** – 로컬 머신에 Java 개발 환경이 구축되어 있어야 합니다.  
2. **Aspose.3D for Java** – Aspose.3D 라이브러리를 다운로드하고 설치합니다. 라이브러리와 문서는 [여기](https://reference.aspose.com/3d/java/)에서 확인할 수 있습니다.  
3. **문서 디렉터리** – Java 파일을 저장할 디렉터리를 만듭니다. 예를 들어 “Your Document Directory”라고 부르겠습니다.

## 패키지 가져오기

Java 개발 환경에서 Aspose.3D에 필요한 패키지를 가져옵니다. 이렇게 하면 라이브러리에서 제공하는 기능을 코드에서 사용할 수 있습니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1단계: 기본 프로파일 설정

압출할 기본 프로파일을 초기화합니다. 여기서는 반경 0.3의 라운딩이 적용된 사각형 형태를 사용합니다.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2단계: 3D 씬 생성

씬을 생성하여 3D 세계의 기반을 만듭니다.

```java
Scene scene = new Scene();
```

## 3단계: 좌·우 노드 생성

씬 안에 좌측과 우측 노드를 만듭니다. 이 노드들은 3D 객체를 배치할 캔버스 역할을 합니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4단계: 중심 속성이 적용된 선형 압출 (좌측 노드)

좌측 노드에서 **중심을 맞추지 않은** 상태로 선형 압출을 수행하고 슬라이스 수를 3으로 설정합니다. `setCenter(false)` 호출이 바로 **center 속성을 false** 로 설정하는 부분입니다.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 5단계: 참조용 Ground Plane 추가 (좌측 노드)

좌측 노드에 **ground plane을 추가**하여 시각적 기준을 강화합니다. 얇은 박스가 바닥 역할을 하여 압출 높이를 명확히 확인할 수 있습니다.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 6단계: 중심 속성이 적용된 선형 압출 (우측 노드)

이번에는 우측 노드에서 **압출을 중앙에 맞추어** 수행합니다. `setCenter(true)` 호출이 **center 속성을 true** 로 설정하는 예시입니다.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 7단계: 참조용 Ground Plane 추가 (우측 노드)

좌측과 마찬가지로 우측 노드에도 ground plane을 추가해 일관된 시각적 기준을 제공합니다.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 8단계: 3D 씬 저장

3D 씬을 Wavefront OBJ 형식으로 저장하여 표준 3D 뷰어에서 확인할 수 있게 합니다.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 일반적인 문제와 해결 방법

| 문제 | 발생 원인 | 해결 방법 |
|------|-----------|-----------|
| Ground plane이 보이지 않음 | 박스 두께가 뷰어의 스케일에 비해 너무 얇음 | `Box`의 첫 번째 매개변수(두께)를 늘리거나 뷰어에서 줌 아웃합니다. |
| 압출이 위치가 틀어짐 | `setCenter` 값이 의도대로 설정되지 않음 | `setCenter`에 전달된 boolean 값을 다시 확인합니다. |
| 파일이 저장되지 않음 | 디렉터리 경로가 잘못되었거나 쓰기 권한이 없음 | `MyDir`이 존재하고 쓰기 권한이 있는 폴더를 가리키는지 확인합니다. |

## 자주 묻는 질문

**Q1: Aspose.3D for Java를 상업 프로젝트에 사용할 수 있나요?**  
A1: 네, Aspose.3D for Java는 상업적 사용이 가능합니다. 라이선스 상세 내용은 [여기](https://purchase.aspose.com/buy)에서 확인하세요.

**Q2: 무료 체험판이 있나요?**  
A2: 네, Aspose.3D for Java의 무료 체험판은 [여기](https://releases.aspose.com/)에서 이용할 수 있습니다.

**Q3: Aspose.3D for Java에 대한 지원은 어디서 받을 수 있나요?**  
A3: Aspose.3D 커뮤니티 포럼이 지원 및 경험 공유에 좋은 장소입니다. 포럼은 [여기](https://forum.aspose.com/c/3d/18)에서 방문하세요.

**Q4: 테스트용 임시 라이선스가 필요합니까?**  
A4: 네, 테스트용 임시 라이선스가 필요하면 [여기](https://purchase.aspose.com/temporary-license/)에서 발급받을 수 있습니다.

**Q5: 문서는 어디서 찾을 수 있나요?**  
A5: Aspose.3D for Java 문서는 [여기](https://reference.aspose.com/3d/java/)에서 확인할 수 있습니다.

## 결론

선형 압출에서 **center 속성을 제어**하고 Aspose.3D for Java로 **ground plane을 추가**하는 방법을 익히면 3D 그래픽 개발에서 새로운 가능성을 열 수 있습니다. 위 단계들을 따라 하면 중심이 맞춰진 압출, 시각적 기준 평면, OBJ 형식으로의 내보내기를 손쉽게 구현할 수 있습니다. 다양한 프로파일, 슬라이스 수, 변환을 실험해 보면서 프로젝트에 맞는 최적의 결과를 만들어 보세요.

---

**마지막 업데이트:** 2025-12-18  
**테스트 환경:** Aspose.3D 24.11 for Java (작성 시 최신 버전)  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}