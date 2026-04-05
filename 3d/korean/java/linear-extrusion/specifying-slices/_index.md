---
date: 2026-02-22
description: Aspose.3D for Java를 사용하여 슬라이스가 있는 3D 압출을 만드는 방법을 배웁니다. 이 단계별 가이드는 선형
  압출, 라운딩 반경 설정 및 OBJ 내보내기를 다룹니다.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: 슬라이스와 함께 3D 압출 만들기 – Aspose.3D for Java
url: /ko/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 압출을 슬라이스와 함께 만들기 – Aspose.3D for Java

## 소개

부드럽고 정밀한 **3d extrusion** 객체를 만들어야 한다면, 슬라이스 수를 제어하는 것이 핵심입니다. 이 튜토리얼에서는 Aspose.3D for Java를 사용해 선형 압출을 수행하면서 슬라이스를 지정하는 방법을 단계별로 안내합니다. 슬라이스 수가 왜 중요한지, 라운딩 반경을 설정하는 방법, 그리고 결과를 모든 3D 파이프라인에서 사용할 수 있는 OBJ 파일로 내보내는 방법을 확인하게 됩니다.

## 빠른 답변
- **“slices”가 제어하는 것은 무엇인가요?** 압출 표면을 근사하기 위해 사용되는 중간 단면의 수입니다.  
- **슬라이스 수를 설정하는 메서드는?** `LinearExtrusion.setSlices(int)`  
- **프로파일의 라운딩 반경을 변경할 수 있나요?** 예, `RectangleShape.setRoundingRadius(double)`을 사용합니다.  
- **이 예제에서 사용된 파일 형식은?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **코드를 실행하려면 라이선스가 필요합니까?** 평가용으로는 무료 체험판으로 충분하지만, 상용 환경에서는 상업용 라이선스가 필요합니다.

## 슬라이스가 있는 선형 압출이란?

선형 압출은 2‑D 프로파일(예: 사각형)을 직선으로 늘려 3‑D 솔리드 형태로 만드는 작업입니다. **slices**를 지정하면 Aspose.3D에 몇 개의 중간 단계(단면)를 생성할지 알려주게 되며, 이는 라운드된 사각형과 같은 곡선 가장자리의 부드러움에 직접적인 영향을 줍니다.

## 왜 Java용 Aspose.3D를 사용해 3d extrusion을 만들까요?

* **전체 제어** – 슬라이스 수, 라운딩 반경, 내보내기 형식을 프로그래밍 방식으로 조정할 수 있습니다.  
* **크로스‑플랫폼** – 네이티브 종속성 없이 Java가 지원되는 모든 환경에서 동작합니다.  
* **내보내기 유연성** – OBJ, FBX, STL 등 다양한 형식으로 직접 저장할 수 있습니다.

## 사전 요구 사항

1. **Java Development Kit** – JDK 8 이상이 설치되어 있어야 합니다.  
2. **Aspose.3D for Java** – 공식 사이트에서 라이브러리를 다운로드하세요 [here](https://releases.aspose.com/3d/java/).  
3. 원하는 IDE 또는 텍스트 편집기.

## 패키지 가져오기

프로젝트에 Aspose.3D 네임스페이스를 추가하여 3‑D 모델링 클래스를 사용할 수 있게 합니다.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 단계별 가이드

### 단계 1: 씬 설정 및 프로파일 정의

먼저 `RectangleShape`을 생성하고 **라운딩 반경**을 지정하여 모서리를 부드럽게 만듭니다. 그런 다음 모든 기하학을 담을 새로운 `Scene`을 초기화합니다.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 단계 2: 각 압출을 위한 **자식 노드** 객체 생성

모든 기하학은 `Node` 아래에 존재합니다. 여기서는 저슬라이스 압출용 노드와 고슬라이스 압출용 노드, 두 개의 형제 노드를 생성하고, 결과를 쉽게 비교할 수 있도록 왼쪽 노드를 약간 옆으로 이동시킵니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 단계 3: 선형 압출 수행 및 **슬라이스 설정**

이제 실제로 **3d extrusion** 객체를 생성합니다. `LinearExtrusion` 생성자는 프로파일과 압출 깊이를 매개변수로 받습니다. **익명 내부 클래스**를 사용해 `setSlices`를 호출하여 부드러움을 제어합니다. 왼쪽 노드는 2개의 슬라이스(거친)만 사용하고, 오른쪽 노드는 10개의 슬라이스(부드러운)를 사용합니다.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 단계 4: **OBJ 내보내기** – 씬 저장

마지막으로 씬을 Wavefront OBJ 파일로 저장합니다. 이 형식은 3‑D 편집기와 게임 엔진에서 널리 지원됩니다. 이를 통해 Aspose.3D의 **export obj java** 기능을 확인할 수 있습니다.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 일반적인 문제와 해결책

| 문제 | 발생 원인 | 해결 방법 |
|------|----------|----------|
| **압출이 평평하게 보임** | 슬라이스 수가 1 또는 0으로 설정됨 | `setSlices`가 2 이상 값으로 호출되었는지 확인하십시오. |
| **라운드된 모서리가 들쭉날쭉함** | 슬라이스 수에 비해 라운딩 반경이 너무 작음 | 보다 부드러운 곡선을 위해 반경이나 슬라이스 수 중 하나를 늘리세요. |
| **저장 시 파일을 찾을 수 없음** | `MyDir`이 존재하지 않는 폴더를 가리킴 | 디렉터리를 미리 생성하거나 절대 경로를 사용하십시오. |

## 자주 묻는 질문

**Q: Aspose.3D for Java를 어떻게 다운로드하나요?**  
A: 라이브러리를 [here](https://releases.aspose.com/3d/java/)에서 다운로드할 수 있습니다.

**Q: Aspose.3D 문서는 어디에서 찾을 수 있나요?**  
A: 문서는 [here](https://reference.aspose.com/3d/java/)에서 확인하십시오.

**Q: 무료 체험판이 있나요?**  
A: 예, 무료 체험판을 [here](https://releases.aspose.com/)에서 확인할 수 있습니다.

**Q: Aspose.3D 지원을 어떻게 받을 수 있나요?**  
A: 지원 포럼을 [here](https://forum.aspose.com/c/3d/18)에서 방문하십시오.

**Q: 임시 라이선스를 구매할 수 있나요?**  
A: 예, 임시 라이선스는 [here](https://purchase.aspose.com/temporary-license/)에서 구매할 수 있습니다.

**마지막 업데이트:** 2026-02-22  
**테스트 환경:** Aspose.3D for Java 24.11 (latest at time of writing)  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}