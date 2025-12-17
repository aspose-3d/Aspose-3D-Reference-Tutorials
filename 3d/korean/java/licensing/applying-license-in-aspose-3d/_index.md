---
date: 2025-12-17
description: Aspose.3D for Java에서 라이선스를 설정하는 방법과 메터링 라이선스를 위한 공개·비공개 키 사용 방법을 배웁니다.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java에서 라이선스 설정 방법 – 완전 가이드
url: /ko/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java에서 라이선스 설정 방법

## 소개

환영합니다! 이 단계별 튜토리얼에서는 Java 애플리케이션에서 Aspose.3D의 **라이선스 설정 방법**을 배우고, **공개·비공개 키를 사용한 메터링 라이선스** 사용법도 익히게 됩니다. Aspose.3D는 3D 파일 형식을 다루는 작업을 간소화하는 강력한 Java 라이브러리이며, 유효한 라이선스를 적용하면 전체 기능을 사용할 수 있습니다. 이 가이드를 마치면 어떤 Java 프로젝트에도 라이선스를 원활히 통합할 수 있게 됩니다.

## 빠른 답변
- **라이선스를 설정하는 기본 방법은 무엇인가요?** `License` 클래스를 사용하고 파일 경로나 스트림을 인자로 `setLicense`를 호출합니다.  
- **스트림에서 라이선스를 로드할 수 있나요?** 예 – `FileInputStream`을 사용하면 완벽히 동작합니다.  
- **공개·비공개 키는 무엇에 사용되나요?** `Metered` 클래스를 통해 메터링 라이선스를 활성화합니다.  
- **개발에 라이선스가 필요합니까?** 테스트용으로는 임시 또는 체험 라이선스로 충분하며, 프로덕션에서는 정식 라이선스가 필요합니다.  
- **지원되는 Java 버전은?** Aspose.3D는 Java 6 이상에서 동작합니다.

## 전제 조건

시작하기 전에 다음을 준비하십시오:

- Java 프로그래밍에 대한 기본 이해.
- 프로젝트에 Aspose.3D 라이브러리를 추가. [release page](https://releases.aspose.com/3d/java/)에서 다운로드하세요.
- 유효한 `.lic` 파일 또는 공개·비공개 메터링 키.

## 패키지 가져오기

Java 소스 파일에 필요한 import 문을 추가하십시오. Aspose.3D JAR가 클래스패스에 포함되어 있는지 확인하세요.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 파일을 사용하여 라이선스 설정 방법

### 단계 1: License 객체 생성

`License` 클래스를 인스턴스화합니다 – 이 객체가 라이선스 정보를 보관합니다.

```java
License license = new License();
```

### 단계 2: 파일에서 라이선스 설정

`.lic` 파일의 상대 경로나 절대 경로를 지정하고 적용합니다.

```java
license.setLicense("Aspose._3D.lic");
```

> **Pro tip:** 라이선스 파일을 소스 제어 디렉터리 밖에 두어 우발적인 노출을 방지하십시오.

## 스트림을 사용하여 라이선스 설정 방법

### 단계 1: License 객체 생성

앞과 같이 새 `License` 인스턴스로 시작합니다.

```java
License license = new License();
```

### 단계 2: 스트림에서 라이선스 설정

`FileInputStream`으로 라이선스 파일을 읽어 `setLicense`에 스트림을 전달합니다. try‑with‑resources 블록이 스트림을 자동으로 닫아줍니다.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## 메터링 라이선스를 위한 공개·비공개 키 사용 방법

### 단계 1: Metered 라이선스 객체 초기화

메터링(사용량 기반) 라이선스를 처리하는 `Metered` 클래스의 인스턴스를 생성합니다.

```java
Metered metered = new Metered();
```

### 단계 2: 공개·비공개 키 설정

Aspose에서 받은 키를 제공하십시오. 이 키들은 라이브러리가 사용량을 라이선스 서버에 보고하도록 합니다.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Warning:** 공개 배포되는 JAR에 비공개 키를 하드코딩하지 마십시오. 안전한 위치나 환경 변수에서 로드하는 것을 고려하세요.

## 일반적인 사용 사례

- **엔터프라이즈 3D 렌더링 파이프라인** – 라이선스 설정 후 고성능 API를 사용할 수 있습니다.
- **자동화 테스트 환경** – 전체 라이선스를 구매하지 않고도 기능을 검증하기 위해 임시 라이선스를 사용합니다(FAQ 참조).
- **메터링 SaaS 솔루션** – 실제 사용량에 따라 고객에게 청구하기 위해 공개·비공개 키를 통합합니다.

## 결론

축하합니다! 이제 파일이나 스트림을 사용해 Java에서 Aspose.3D의 **라이선스 설정 방법**과 메터링 라이선스를 위한 **공개·비공개 키 사용 방법**을 알게 되었습니다. 이 단계들을 따라 하면 Aspose.3D를 어떤 Java 애플리케이션에도 자신 있게 통합하고 3D 처리 기능을 최대한 활용할 수 있습니다.

## 자주 묻는 질문

**Q1: Aspose.3D가 모든 Java 버전과 호환되나요?**  
A1: 예, Aspose.3D는 Java 6 이상 버전에서 동작합니다.

**Q2: 추가 문서는 어디에서 찾을 수 있나요?**  
A2: 문서는 [here](https://reference.aspose.com/3d/java/)에서 확인할 수 있습니다.

**Q3: 구매 전에 Aspose.3D를 체험할 수 있나요?**  
A3: 예, 무료 체험을 [here](https://releases.aspose.com/)에서 확인할 수 있습니다.

**Q4: Aspose.3D 지원을 어떻게 받을 수 있나요?**  
A4: 커뮤니티 및 공식 지원을 위해 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 를 방문하십시오.

**Q5: 테스트에 임시 라이선스가 필요합니까?**  
A5: 예, 임시 라이선스를 [here](https://purchase.aspose.com/temporary-license/)에서 얻을 수 있습니다.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**마지막 업데이트:** 2025-12-17  
**테스트 환경:** Aspose.3D 24.11 for Java  
**작성자:** Aspose  

---