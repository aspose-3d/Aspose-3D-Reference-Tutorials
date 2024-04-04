---
title: Aspose.3D SaveOptions를 사용하여 Java에서 3D 파일 저장 최적화
linktitle: Aspose.3D SaveOptions를 사용하여 Java에서 3D 파일 저장 최적화
second_title: Aspose.3D 자바 API
description: Aspose.3D SaveOptions를 사용하여 Java에서 3D 파일 저장을 최적화하는 방법을 알아보세요. 손쉽게 성능을 향상하고 출력을 맞춤화하세요.
type: docs
weight: 16
url: /ko/java/load-and-save/optimize-3d-file-saving/
---
## 소개

Aspose.3D는 개발자가 3D 모델을 원활하게 사용할 수 있도록 지원하는 기능이 풍부한 Java 라이브러리입니다. 3D 파일을 저장할 때 SaveOptions 클래스는 요구 사항에 따라 출력을 미세 조정할 수 있는 다양한 설정을 제공합니다. 이 튜토리얼에서는 다양한 저장 옵션과 이를 활용하여 프로세스를 최적화하는 방법을 살펴보겠습니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  Java용 Aspose.3D: Aspose.3D 라이브러리가 Java 프로젝트에 통합되어 있는지 확인하세요. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/java/).

- Java 개발 환경: 귀하의 컴퓨터에 기능적인 Java 개발 환경을 설정하십시오.

- 문서 디렉터리: 3D 파일을 저장할 디렉터리를 만들고 나중에 사용할 수 있도록 해당 경로를 기록해 둡니다.

## 패키지 가져오기

 Java 프로젝트에서 Aspose.3D 작업에 필요한 패키지를 가져옵니다. 여기에는 다음이 포함됩니다.`Scene` 클래스 및 다양한 SaveOptions 클래스. 다음은 기본 예입니다.

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

이제 각 예를 여러 단계로 나누어 다양한 SaveOptions의 사용법을 보여드리겠습니다.

## 1단계: GLTF SaveOption의 예쁜 인쇄

 그만큼`prettyPrintInGltfSaveOption` 메서드를 사용하면 사람이 쉽게 읽을 수 있도록 들여쓰기된 JSON 콘텐츠가 포함된 GLTF 파일을 생성할 수 있습니다.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // 3D 장면 초기화
    Scene scene = new Scene(new Sphere());
    
    // GLTFSaveOptions 초기화
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // 더 나은 가독성을 위해 예쁜 인쇄를 활성화하세요.
    opt.setPrettyPrint(true);
    
    // 3D 장면 저장
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## 2단계: HTML5 저장 옵션

 그만큼`html5SaveOption` 방법은 사용자 정의 옵션을 포함하여 3D 장면을 HTML5 파일로 저장하는 방법을 보여줍니다.

```java
public static void html5SaveOption() throws IOException {
    // 장면 초기화
    Scene scene = new Scene();
    
    // 원통이 있는 하위 노드 만들기
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //하위 노드의 속성 설정
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // 장면에 조명 추가
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // HTML5SaveOptions 초기화
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // 옵션 사용자 정의(예: 그리드 및 사용자 인터페이스 끄기)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // 장면을 HTML5 파일로 저장
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 다음과 같은 다른 SaveOptions 방법에 대해서도 유사한 분석을 계속합니다.`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , 그리고`drcSaveOptions`.

## 결론

이 포괄적인 튜토리얼을 따라 Aspose.3D SaveOptions를 사용하여 Java에서 3D 파일 저장을 최적화하는 방법을 배웠습니다. GLTF 파일을 예쁘게 인쇄하거나 HTML5 출력을 사용자 정의하는 데 관심이 있다면 Aspose.3D는 3D 그래픽 작업 흐름을 향상시키는 도구를 제공합니다.

## FAQ

### Q1: glTF 파일에 자산을 어떻게 삽입할 수 있나요?

 A1: 자산을 삽입하려면`setEmbedAssets(true)` 의 방법`GltfSaveOptions` 수업.

###  Q2: 이 프로그램의 목적은 무엇입니까?`setPositionBits` method in `DracoSaveOptions`?

 A2:`setPositionBits` 방법은 Draco 압축 알고리즘의 위치에 대한 양자화 비트를 설정합니다.

### Q3: 일반 데이터를 U3D 파일로 내보낼 수 있나요?

 A3: 예, 설정을 통해 일반 데이터를 내보낼 수 있습니다.`setExportNormals(true)` 에서`U3dSaveOptions` 수업.

### Q4: OBJ 내보내기에서 재료 파일 저장을 어떻게 취소합니까?

A4: 활용`setFileSystem(new DummyFileSystem())` 의 방법`ObjSaveOptions` 재료 파일을 삭제하는 클래스입니다.

### Q5: OBJ 파일의 로컬 디렉터리에 종속성을 저장하는 방법이 있습니까?

 A5: 예,`setFileSystem(new LocalFileSystem(MyDir))` 의 방법`ObjSaveOptions` 종속성을 로컬에 저장하는 클래스입니다.