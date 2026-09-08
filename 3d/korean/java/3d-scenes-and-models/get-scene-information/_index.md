---
date: 2026-09-08
description: Aspose.3D를 사용하여 Java에서 단위를 정의하고 씬을 FBX로 내보내는 방법을 배웁니다. 이 단계별 가이드는 애플리케이션
  이름 설정, 측정 단위 지정 및 3D 씬 정보 가져오기를 보여줍니다.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Java에서 FBX 저장 및 3D 씬 정보 가져오는 방법
og_description: Aspose.3D와 함께 Java에서 단위를 정의하고 씬을 FBX로 내보내는 방법을 배웁니다. 이 가이드는 몇 단계로
  애플리케이션 이름 설정, 측정 단위 지정 및 3D 씬 정보 가져오기를 다룹니다.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Java에서 단위를 정의하고 씬을 FBX로 내보내는 방법
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Java에서 단위를 정의하고 씬을 FBX로 내보내는 방법
url: /ko/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java에서 단위를 정의하고 장면을 FBX로 내보내는 방법

## 소개

If you’re looking for a clear, hands‑on guide on **how to define units** and **export a scene to FBX** while extracting useful metadata from your 3D scenes, you’ve come to the right place. In this tutorial we’ll walk through every step using the **Aspose.3D for Java** library: from creating a scene, **setting the application name**, **defining measurement units**, to finally **exporting the scene to FBX**. By the end you’ll have a ready‑to‑use FBX file that carries the asset information you need for downstream pipelines.

## 빠른 답변
- **주요 목표는 무엇입니까?** 맞춤형 자산 정보를 포함하는 FBX 장면을 내보내는 것입니다.  
- **어떤 라이브러리를 사용합니까?** Aspose.3D for Java.  
- **라이선스가 필요합니까?** 개발에는 무료 체험판으로 충분하고, 운영에는 상용 라이선스가 필요합니다.  
- **측정 단위를 변경할 수 있습니까?** 예 – `setUnitName` 및 `setUnitScaleFactor`를 사용하십시오.  
- **출력은 어디에 저장됩니까?** `scene.save(...)`에 지정한 경로에 저장됩니다.  

## 전제 조건

Before we start, make sure you have:

- 핵심 Java 구문에 대한 탄탄한 이해.  
- **Aspose.3D for Java**를 다운로드하여 프로젝트에 추가하세요 (공식 사이트에서 받을 수 있습니다) [Aspose 3D 다운로드 페이지](https://releases.aspose.com/3d/java/).  
- 선호하는 Java IDE(IntelliJ IDEA, Eclipse, NetBeans 등)를 올바르게 설정하세요.

## 패키지 가져오기

In your Java source file, import the Aspose.3D classes that provide scene handling and file‑format support.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **전문가 팁:** 불필요한 종속성을 피하고 컴파일 시간을 개선하려면 import 목록을 최소화하세요.

## FBX 파일을 저장하는 과정은 무엇입니까?

To save a scene as an FBX file you create a `Scene`, set any desired asset metadata, define the measurement unit, and then call `scene.save(path, FileFormat.FBX7500ASCII)`. This sequence writes geometry, materials, and metadata into an ASCII FBX that can be inspected or imported by downstream tools.

### 단계 1: 3D 장면 초기화

The `Scene` class is Aspose.3D's top‑level container that represents an entire 3D scene, including geometry, lights, cameras, and metadata. First, create an empty `Scene` object. This will be the container for all geometry, lights, cameras, and asset metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Java에서 애플리케이션 이름 설정 방법

The `AssetInfo` object stores metadata such as application name, vendor, and version for the scene. Adding custom metadata helps downstream tools identify the source of the file. Use the `AssetInfo` object to **set the application name** (and vendor) before you save the file.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **왜 중요한가:** 많은 파이프라인이 원본 애플리케이션을 기준으로 자산을 필터링하거나 태그를 붙이므로 이 단계는 대규모 프로젝트에 필수적입니다.

### 단계 3: 측정 단위 정의

The unit system determines the real‑world scale of the scene; Aspose.3D lets you specify a unit name and a scale factor relative to meters. In this example we use an ancient Egyptian unit called “pole” with a custom scale factor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Adjust `unitScaleFactor` to match the real‑world size of your models; 1.0 represents a 1‑to‑1 mapping with the chosen unit.

### 단계 4: 장면을 FBX로 내보내기

Now that the asset information is attached, we save the scene as an FBX file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX, which is handy for debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Replace `"Your Document Directory"` with an absolute path or a path relative to your project's working directory.

## 왜 Aspose.3D로 장면을 FBX로 내보내나요?

Aspose.3D supports **50+ input and output formats** and can process multi‑hundred‑page scenes without loading the entire file into memory, giving you full control over the exported file—metadata, units, and geometry—without needing a heavyweight 3D authoring application. This makes automated asset generation, batch processing, and server‑side conversions fast and reliable.

## 일반적인 사용 사례

- **게임 자산 파이프라인** – 버전 추적을 위해 제작자 정보를 FBX 파일에 직접 삽입합니다.  
- **건축 시각화** – 렌더링 엔진에 가져올 때 스케일 오류를 방지하기 위해 프로젝트별 단위를 저장합니다.  
- **자동 보고** – 다운스트림 분석 도구가 읽을 수 있는 메타데이터와 함께 즉시 FBX 파일을 생성합니다.  
- **클라우드 기반 3D 서비스** – GUI 없이 프로그래밍 방식으로 장면을 생성하고 내보내며, SaaS 플랫폼에 적합합니다.

## 문제 해결 및 팁

| 문제 | 해결책 |
|-------|----------|
| **저장 후 파일을 찾을 수 없음** | `MyDir`이 기존 폴더를 가리키는지와 애플리케이션에 쓰기 권한이 있는지 확인하세요. |
| **외부 뷰어에서 단위가 잘못 표시됨** | `unitScaleFactor`를 다시 확인하세요; 일부 뷰어는 기본 단위로 미터를 기대합니다. |
| **자산 메타데이터 누락** | 저장하기 **전**에 `scene.getAssetInfo()`를 호출했는지 확인하세요; `save()` 후에 변경한 내용은 유지되지 않습니다. |
| **대형 장면에서 성능 병목** | 저장하기 전에 `scene.optimize()`를 사용해 메모리 사용량을 줄이세요. |
| **ASCII FBX가 너무 큼** | `FileFormat.FBX7500`을 사용해 바이너리 FBX로 전환하세요(FAQ 참조). |

## 자주 묻는 질문

**Q:** 출력 형식을 바이너리 FBX로 어떻게 변경합니까?  
**A:** `scene.save(...)`를 호출할 때 `FileFormat.FBX7500ASCII`를 `FileFormat.FBX7500`으로 교체하십시오.

**Q:** 기본 제공 자산 필드 외에 사용자 정의 메타데이터를 추가할 수 있습니까?  
**A:** 예, `scene.getUserData().add("Key", "Value")`를 사용해 추가 키‑값 쌍을 삽입하십시오.

**Q:** Aspose.3D가 OBJ나 GLTF와 같은 다른 내보내기 형식을 지원합니까?  
**A:** 지원합니다. 필요에 따라 `FileFormat` 열거형을 `OBJ` 또는 `GLTF2`로 변경하면 됩니다.

**Q:** 필요한 Java 버전은 무엇입니까?  
**A:** Aspose.3D for Java는 Java 8 이상을 지원합니다.

**Q:** 기존 FBX를 로드하고 자산 정보를 수정한 뒤 다시 저장할 수 있습니까?  
**A:** 물론 가능합니다. `new Scene("input.fbx")`로 파일을 로드하고 `scene.getAssetInfo()`를 수정한 뒤 저장하세요.

---

**마지막 업데이트:** 2026-09-08  
**테스트 환경:** Aspose.3D for Java 24.11  
**작성자:** Aspose

## 관련 튜토리얼

- [3D 파일 크기 줄이기 – Aspose.3D for Java로 장면 압축](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [vector3 색상 설정 방법 Java: Aspose.3D를 사용하여 Java 장면에서 Diffuse 색상을 변경하고 3D 속성을 관리하기](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}