---
title: Java용 Aspose.3D를 사용하여 선형 압출에 비틀기 적용
linktitle: Java용 Aspose.3D를 사용하여 선형 압출에 비틀기 적용
second_title: Aspose.3D 자바 API
description: Java용 Aspose.3D를 사용하여 3D 모델에 변형을 추가하는 방법을 알아보세요. 향상된 선형 압출 효과를 보려면 단계별 가이드를 따르세요.
weight: 14
url: /ko/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java용 Aspose.3D를 사용하여 선형 압출에 비틀기 적용

## 소개

Java용 Aspose.3D를 사용하여 선형 돌출에 비틀림을 적용하는 방법에 대한 단계별 튜토리얼에 오신 것을 환영합니다. Aspose.3D는 개발자가 3D 파일 형식으로 작업할 수 있도록 지원하는 강력한 Java 라이브러리로, 3D 장면 생성, 조작 및 렌더링을 위한 강력한 기능을 제공합니다. 이 튜토리얼에서는 선형 돌출 프로세스 중에 비틀기 효과를 적용하여 3D 모델을 향상시키는 방법을 살펴보겠습니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

- Java 개발 환경: 시스템에 Java가 설치되어 있는지 확인하십시오.
-  Aspose.3D 라이브러리: 다음에서 Java용 Aspose.3D 라이브러리를 다운로드하고 설치합니다.[다운로드 링크](https://releases.aspose.com/3d/java/).
-  문서:[Aspose.3D 문서](https://reference.aspose.com/3d/java/) 종합적인 안내를 위해.

## 패키지 가져오기

코딩 프로세스를 시작하기 전에 필요한 패키지를 Java 프로젝트로 가져옵니다. 이를 수행하는 방법의 예는 다음과 같습니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1단계: 문서 디렉터리 설정

3D 장면이 저장될 문서 디렉터리를 설정하는 것부터 시작하세요.

```java
// ExStart:SetDocument디렉토리
String MyDir = "Your Document Directory";
// ExEnd:SetDocument디렉토리
```

## 2단계: 기본 프로필 초기화

돌출할 기본 프로파일을 초기화합니다. 이 예에서는 반올림 반경이 있는 직사각형 모양을 사용합니다.

```java
// ExStart:기본 프로필 초기화
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:초기화베이스 프로파일
```

## 3단계: 장면 만들기

돌출된 노드를 호스팅할 3D 장면을 만듭니다.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## 4단계: 노드 생성

장면 내에서 왼쪽 및 오른쪽 노드를 만듭니다. 왼쪽 노드의 이동을 조정합니다.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## 5단계: 비틀기를 사용하여 선형 돌출 수행

트위스트 및 슬라이스 속성을 적용하여 왼쪽 및 오른쪽 노드 모두에서 선형 돌출을 수행합니다.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## 6단계: 3D 장면 저장

3D 장면을 Wavefront OBJ 파일 형식으로 저장합니다.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//확장:Save3DScene
```

## 결론

축하해요! Java용 Aspose.3D를 사용하여 선형 돌출에 비틀림을 성공적으로 적용했습니다. 이 튜토리얼에서는 3D 모델링 기능을 향상시키는 데 도움이 되는 자세한 단계별 가이드를 제공했습니다.

## FAQ

### Q1: Java용 Aspose.3D를 사용하여 다른 3D 파일 형식과 작업할 수 있습니까?

A1: 예, Aspose.3D는 다양한 3D 파일 형식을 지원하므로 다양한 파일 형식을 가져오고, 내보내고, 조작할 수 있습니다.

### Q2: Java용 Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A2: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.

### Q3: Aspose.3D for Java에 대한 무료 평가판이 있습니까?

 A3: 예, 다음에서 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: Java용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A4: 임시 라이센스를 받으십시오.[임시 라이센스 페이지](https://purchase.aspose.com/temporary-license/).

### Q5: Java용 Aspose.3D를 어디서 구입할 수 있나요?

 A5: 다음에서 Java용 Aspose.3D를 구입하세요.[구매 페이지](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
