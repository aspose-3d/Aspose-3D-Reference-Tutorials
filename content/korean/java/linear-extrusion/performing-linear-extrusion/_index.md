---
title: Java용 Aspose.3D에서 선형 압출 수행
linktitle: Java용 Aspose.3D에서 선형 압출 수행
second_title: Aspose.3D 자바 API
description: Java용 Aspose.3D를 사용하여 3D 모델링의 세계를 탐험해보세요. 손쉽게 선형 압출을 수행하는 방법을 알아보세요.
type: docs
weight: 10
url: /ko/java/linear-extrusion/performing-linear-extrusion/
---
## 소개

Java용 Aspose.3D에서 선형 돌출을 수행하는 방법에 대한 포괄적인 튜토리얼에 오신 것을 환영합니다! Java를 사용하여 3D 모델링 기술을 향상시키려는 경우 올바른 위치에 있습니다. 이 튜토리얼에서는 3D 모델링을 위한 강력한 Java 라이브러리인 Aspose.3D를 사용하여 선형 압출을 수행하는 과정을 안내합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

1. Java 개발 환경: 컴퓨터에 Java 개발 환경이 설정되어 있는지 확인하십시오.

2.  Aspose.3D 라이브러리: Aspose.3D 라이브러리를 다운로드하여 설치합니다. 도서관을 찾으실 수 있습니다[여기](https://releases.aspose.com/3d/java/).

## 패키지 가져오기

개발 환경을 설정하고 Aspose.3D 라이브러리를 설치했으면 이제 필요한 패키지를 가져올 차례입니다. Java 코드에 다음을 포함합니다.

```java
import com.aspose.threed.*;
```

명확한 이해를 위해 각 단계를 자세히 살펴보겠습니다.

## 1단계: 문서 디렉터리 설정

문서 디렉터리의 경로를 정의합니다.

```java
String MyDir = "Your Document Directory";
```

이렇게 하면 생성된 3D 모델이 지정된 디렉터리에 저장됩니다.

## 2단계: 기본 모양 초기화

돌출을 위한 기본 프로파일로 직사각형 모양을 만듭니다.

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

필요에 따라 반올림 반경을 조정하여 모양을 사용자 정의합니다.

## 3단계: 선형 압출 수행

기본 프로파일에서 선형 돌출을 수행합니다.

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

여기서는 모양을 10단위로 돌출시키고, 슬라이스 수를 설정하고, 센터링을 활성화하고, 비틀기와 비틀기 오프셋을 적용합니다.

## 4단계: 3D 장면 만들기

3D 장면을 만들고 돌출을 하위 노드로 추가합니다.

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## 5단계: 3D 장면 저장

생성된 3D 장면을 Wavefront OBJ 파일로 저장합니다.

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

이제 Java용 Aspose.3D를 사용하여 선형 압출을 성공적으로 수행했습니다!

## 결론

축하해요! 선형 압출을 수행하기 위해 Java용 Aspose.3D를 활용하는 방법을 배웠습니다. 이 강력한 라이브러리는 3D 모델링 프로젝트에 대한 가능성의 세계를 열어줍니다.

## FAQ

### Q1: Aspose.3D는 모든 Java 버전과 호환됩니까?

A1: Aspose.3D는 Java 1.6 이상 버전에서 작동하도록 설계되었습니다.

### Q2: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?

A2: 예, Aspose.3D는 개인 및 상업용 프로젝트 모두에 사용할 수 있습니다. 라이선스 세부정보를 확인하세요.[여기](https://purchase.aspose.com/buy).

### Q3: Aspose.3D에 대한 지원은 어떻게 받을 수 있나요?

 A3: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지역사회 지원을 원하거나 구매를 고려해보세요.[임시면허](https://purchase.aspose.com/temporary-license/) 프리미엄 지원을 위해.

### Q4: Aspose.3D에 다른 3D 모델링 기능이 있습니까?

 A4: 물론이죠! 광범위한 문서 살펴보기[여기](https://reference.aspose.com/3d/java/) 기능과 예제의 포괄적인 목록을 보려면

### Q5: Aspose.3D에 대한 무료 평가판이 있습니까?

 A5: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).