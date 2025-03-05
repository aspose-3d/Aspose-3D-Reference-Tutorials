---
title: Java용 Aspose.3D를 사용하여 선형 압출의 중심 제어
linktitle: Java용 Aspose.3D를 사용하여 선형 압출의 중심 제어
second_title: Aspose.3D 자바 API
description: Aspose.3D를 사용하여 Java에서 3D 그래픽의 세계를 탐험해보세요. 선형 압출에서 중심을 쉽게 제어할 수 있습니다.
type: docs
weight: 11
url: /ko/java/linear-extrusion/controlling-center/
---
## 소개

3D 그래픽 및 Java 프로그래밍 세계에서 선형 돌출의 중심을 제어하는 것은 프로젝트에서 원하는 효과를 얻는 데 중요한 역할을 합니다. Aspose.3D for Java는 이러한 작업을 원활하게 처리할 수 있는 강력한 툴킷을 제공합니다. 이 튜토리얼에서는 Java용 Aspose.3D를 사용하여 선형 압출에서 중심을 제어하는 과정을 자세히 살펴보고 원활하고 포괄적인 이해를 보장하기 위해 각 단계를 세분화합니다.

## 전제 조건

이 튜토리얼 여정을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

1. Java 개발 환경: 컴퓨터에 Java 개발 환경이 설정되어 있는지 확인하십시오.

2.  Java용 Aspose.3D: Aspose.3D 라이브러리를 다운로드하고 설치합니다. 라이브러리와 해당 문서를 찾을 수 있습니다[여기](https://reference.aspose.com/3d/java/).

3. 문서 디렉터리: Java 문서를 저장할 디렉터리를 만듭니다. 이를 "문서 디렉토리"라고 부르겠습니다.

## 패키지 가져오기

Java 개발 환경에서 Aspose.3D에 필요한 패키지를 가져옵니다. 이렇게 하면 코드가 라이브러리에서 제공하는 기능에 액세스할 수 있습니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1단계: 기본 프로필 설정

돌출할 기본 프로파일을 초기화합니다. 이 예에서는 반올림 반경이 0.3인 직사각형 모양을 사용합니다.

```java
// 문서 디렉터리의 경로입니다.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2단계: 3D 장면 만들기

장면을 만들어 3D 세계의 기반을 구축하세요.

```java
Scene scene = new Scene();
```

## 3단계: 왼쪽 및 오른쪽 노드 생성

장면 내에서 왼쪽 및 오른쪽 노드를 설정합니다. 이러한 노드는 3D 개체의 캔버스 역할을 합니다.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4단계: 중심 속성을 사용한 선형 돌출

왼쪽 노드에 중심을 맞추지 않고 선형 압출을 수행하고 슬라이스 수를 3으로 설정합니다.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 5단계: 참조용 접지면 설정

왼쪽 노드에 접지면을 추가하여 시각적 표현을 향상시킵니다.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 6단계: 중심 속성을 사용한 선형 돌출(오른쪽 노드)

오른쪽 노드에서 선형 돌출을 수행합니다. 이번에는 돌출을 중심으로 하고 슬라이스 수를 다시 3으로 설정합니다.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 7단계: 참조용 접지면 설정(오른쪽 노드)

왼쪽 노드와 유사하게 참조용으로 오른쪽 노드에 접지면을 추가합니다.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 8단계: 3D 장면 저장

3D 장면을 Wavefront OBJ 형식으로 저장합니다.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 결론

Java용 Aspose.3D를 사용하여 선형 압출에서 중심을 제어하면 3D 그래픽 개발에 흥미로운 가능성이 열립니다. 이 단계별 가이드를 따라 Java 프로젝트에서 원하는 시각적 효과를 얻을 수 있도록 center 속성을 조작하는 방법을 배웠습니다.

## FAQ

### Q1: 상용 프로젝트에서 Java용 Aspose.3D를 사용할 수 있습니까?

 A1: 예, Java용 Aspose.3D는 상업용으로 사용할 수 있습니다. 라이선스에 대한 자세한 내용을 보려면 다음을 방문하세요.[여기](https://purchase.aspose.com/buy).

### Q2: 무료 평가판을 이용할 수 있나요?

 A2: 예, Java용 Aspose.3D 무료 평가판을 탐색할 수 있습니다.[여기](https://releases.aspose.com/).

### Q3: Java용 Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A3: Aspose.3D 커뮤니티 포럼은 지원을 구하고 경험을 공유할 수 있는 좋은 장소입니다. 포럼 방문[여기](https://forum.aspose.com/c/3d/18).

### Q4: 테스트하려면 임시 라이센스가 필요합니까?

A4: 예, 테스트 목적으로 임시 라이센스가 필요한 경우 임시 라이센스를 얻을 수 있습니다.[여기](https://purchase.aspose.com/temporary-license/).

### Q5: 문서는 어디서 찾을 수 있나요?

 A5: Java용 Aspose.3D 문서를 사용할 수 있습니다.[여기](https://reference.aspose.com/3d/java/).