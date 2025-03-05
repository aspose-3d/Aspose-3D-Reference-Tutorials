---
title: Java용 Aspose.3D를 사용하여 선형 돌출에서 슬라이스 지정
linktitle: Java용 Aspose.3D를 사용하여 선형 돌출에서 슬라이스 지정
second_title: Aspose.3D 자바 API
description: Java용 Aspose.3D를 사용하여 선형 돌출에서 슬라이스를 지정하는 방법을 알아보세요. 이 단계별 가이드를 통해 3D 모델링 기술을 향상하세요.
type: docs
weight: 13
url: /ko/java/linear-extrusion/specifying-slices/
---
## 소개

복잡한 3D 모델을 만들려면 창의성 그 이상이 필요한 경우가 많습니다. 이를 위해서는 귀하가 사용할 수 있는 도구에 대한 철저한 이해가 필요합니다. Java용 Aspose.3D는 이 점에서 획기적인 변화를 가져왔습니다. 이 튜토리얼에서는 선형 압출에서 슬라이스를 지정하는 특정 측면에 중점을 둘 것입니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

1. Java 환경: 시스템에 Java 개발 환경이 설정되어 있는지 확인하십시오.
2.  Java용 Aspose.3D: Aspose.3D 라이브러리를 다운로드하고 설치합니다. 필요한 패키지를 찾을 수 있습니다[여기](https://releases.aspose.com/3d/java/).

## 패키지 가져오기

Java 프로젝트에서 Aspose.3D 라이브러리를 가져옵니다. 이는 우리가 작업할 기능에 액세스하는 데 중요합니다. 코드에 다음 import 문을 추가합니다.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

이제 예제를 여러 단계로 나누어 보겠습니다.

## 1단계: 장면 설정

돌출될 기본 프로파일을 초기화합니다. 이 경우`RectangleShape` 지정된 반올림 반경을 사용합니다. 작업할 3D 장면을 만듭니다.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## 2단계: 노드 생성

장면 내에서 왼쪽 및 오른쪽 노드를 생성합니다. 공간적 변화를 위해 왼쪽 노드의 변환을 조정합니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 3단계: 슬라이스를 사용한 선형 돌출

두 노드 모두에서 선형 돌출을 수행하고 각각에 대한 슬라이스 수를 지정합니다. 이것이 바로 마법이 일어나는 곳입니다.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## 4단계: 장면 저장

3D 장면을 원하는 형식(이 경우 Wavefront OBJ 파일)으로 저장합니다.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 결론

축하해요! Java용 Aspose.3D를 사용하여 선형 돌출에서 슬라이스를 지정하는 방법을 성공적으로 배웠습니다. 이 기술은 3D 모델링 여정에 새로운 가능성을 열어줍니다.

## FAQ

### Q1: Java용 Aspose.3D를 어떻게 다운로드할 수 있나요?

 A1: 라이브러리를 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/java/).

### Q2: Aspose.3D에 대한 문서는 어디서 찾을 수 있나요?

 A2: 문서를 참조하세요[여기](https://reference.aspose.com/3d/java/).

### Q3: 무료 평가판이 제공됩니까?

 A3: 예, 무료 평가판을 사용해 볼 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: Aspose.3D에 대한 지원은 어떻게 받을 수 있나요?

 A4: 지원 포럼을 방문하세요.[여기](https://forum.aspose.com/c/3d/18).

### Q5: 임시 라이센스를 구매할 수 있나요?

 A5: 예, 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).