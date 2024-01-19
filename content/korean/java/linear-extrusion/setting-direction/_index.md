---
title: Java용 Aspose.3D를 사용하여 선형 돌출의 방향 설정
linktitle: Java용 Aspose.3D를 사용하여 선형 돌출의 방향 설정
second_title: Aspose.3D 자바 API
description: Java용 Aspose.3D를 사용하여 선형 압출을 마스터하세요! 원활한 3D 프로그래밍을 위한 가이드를 따르세요. 지금 다운로드하여 매혹적인 경험을 즐겨보세요.
type: docs
weight: 12
url: /ko/java/linear-extrusion/setting-direction/
---
## 소개

Java용 Aspose.3D를 사용하여 선형 압출 방향 설정에 대한 단계별 가이드에 오신 것을 환영합니다. Aspose.3D는 개발자가 3D 파일 및 장면을 원활하게 작업할 수 있게 해주는 강력한 Java 라이브러리입니다. 이 튜토리얼에서는 선형 압출의 방향을 설정하는 특정 작업에 중점을 두고 3D 프로그래밍 능력을 향상시킵니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

- Java 프로그래밍 언어에 대한 기본 지식.
-  Aspose.3D 라이브러리가 설치되었습니다. 다음에서 다운로드할 수 있습니다.[여기](https://releases.aspose.com/3d/java/).
- Eclipse 또는 IntelliJ와 같은 Java용 통합 개발 환경(IDE)입니다.

## 패키지 가져오기

프로젝트를 시작하려면 필요한 패키지를 가져와야 합니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1단계: 기본 프로필 초기화

 돌출할 기본 프로파일을 초기화하는 것부터 시작합니다. 이 예에서는`RectangleShape` 반올림 반경이 0.3인 경우:

```java
// 문서 디렉터리의 경로입니다.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2단계: 장면 만들기

다음으로 돌출된 개체를 포함하는 3D 장면을 만듭니다.

```java
Scene scene = new Scene();
```

## 3단계: 노드 생성

장면 내에서 왼쪽 및 오른쪽 노드를 만듭니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4단계: 왼쪽 노드에서 선형 돌출 수행

 다음을 사용하여 왼쪽 노드에서 선형 압출을 수행합니다.`LinearExtrusion`트위스트 및 슬라이스와 같은 지정된 매개변수가 있는 클래스:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 5단계: 방향을 사용하여 오른쪽 노드에서 선형 돌출 수행

 오른쪽 노드에서 선형 압출을 수행하여`setDirection` 돌출 방향을 정의하는 속성:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 6단계: 3D 장면 저장

3D 장면을 원하는 파일 형식으로 저장합니다. 이 예에서는 이를 Wavefront OBJ 파일로 저장합니다.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 결론

축하해요! Java용 Aspose.3D를 사용하여 선형 돌출에서 방향을 설정하는 방법을 성공적으로 배웠습니다. 이 튜토리얼은 3D 프로그래밍 기술을 향상시키고 창의적인 프로젝트의 새로운 가능성을 열어줍니다.

## FAQ

### Q1: Aspose.3D를 다른 프로그래밍 언어와 함께 사용할 수 있습니까?

A1: Aspose.3D는 .NET 및 Java를 포함한 다양한 프로그래밍 언어를 지원합니다.

### Q2. Aspose.3D에 대한 무료 평가판이 있습니까?

 A2: 예, 무료 평가판을 통해 Aspose.3D의 기능을 탐색할 수 있습니다.[여기](https://releases.aspose.com/).

### Q3: Java용 Aspose.3D에 대한 자세한 문서는 어디서 찾을 수 있나요?

 A3: 포괄적인 문서를 사용할 수 있습니다.[여기](https://reference.aspose.com/3d/java/).

### Q4: Aspose.3D에 대한 지원은 어떻게 받을 수 있나요?

 A4: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18)도움이나 문의사항이 있으면

### Q5: Aspose.3D에 임시 라이선스를 사용할 수 있나요?

 A5: 예, 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).