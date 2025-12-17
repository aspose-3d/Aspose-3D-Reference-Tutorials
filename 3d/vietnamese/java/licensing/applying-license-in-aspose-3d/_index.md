---
date: 2025-12-17
description: Tìm hiểu cách thiết lập giấy phép trong Aspose.3D cho Java và cách sử
  dụng khóa công khai và khóa riêng cho giấy phép tính theo mức sử dụng.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cách Đặt Giấy Phép trong Aspose.3D cho Java – Hướng Dẫn Toàn Diện
url: /vi/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách Đặt Giấy Phép trong Aspose.3D cho Java

## Giới thiệu

Chào mừng! Trong hướng dẫn từng bước này, bạn sẽ khám phá **cách đặt giấy phép** cho Aspose.3D trong một ứng dụng Java và cũng học **cách sử dụng khóa công khai và riêng tư** cho giấy phép tính theo mức. Aspose.3D là một thư viện Java mạnh mẽ giúp đơn giản hóa việc làm việc với các định dạng tệp 3D, và một giấy phép hợp lệ sẽ mở khóa toàn bộ tính năng của nó. Khi kết thúc hướng dẫn này, bạn sẽ có thể tích hợp giấy phép một cách liền mạch vào bất kỳ dự án Java nào.

## Câu trả lời nhanh
- **Cách chính để đặt giấy phép là gì?** Sử dụng lớp `License` và gọi `setLicense` với đường dẫn tệp hoặc luồng.  
- **Tôi có thể tải giấy phép từ một luồng không?** Có – `FileInputStream` hoạt động hoàn hảo.  
- **Khóa công khai/riêng tư dùng để làm gì?** Chúng cho phép giấy phép tính theo mức thông qua lớp `Metered`.  
- **Tôi có cần giấy phép cho việc phát triển không?** Giấy phép tạm thời hoặc dùng thử đủ cho việc kiểm tra; giấy phép đầy đủ cần thiết cho môi trường sản xuất.  
- **Các phiên bản Java nào được hỗ trợ?** Aspose.3D hoạt động với Java 6 trở lên.

## Yêu cầu trước

Trước khi bắt đầu, hãy đảm bảo bạn có:

- Kiến thức cơ bản về lập trình Java.  
- Thư viện Aspose.3D đã được thêm vào dự án của bạn. Tải xuống từ [release page](https://releases.aspose.com/3d/java/).  
- Một tệp `.lic` hợp lệ hoặc các khóa metered công khai và riêng tư của bạn.

## Nhập các Gói

Thêm các import cần thiết vào tệp nguồn Java của bạn. Đảm bảo JAR Aspose.3D có trong classpath.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Cách Đặt Giấy Phép Bằng Tệp

### Bước 1: Tạo Đối Tượng License

Khởi tạo lớp `License` – đối tượng này sẽ chứa thông tin giấy phép.

```java
License license = new License();
```

### Bước 2: Đặt Giấy Phép Từ Tệp

Cung cấp đường dẫn tương đối hoặc tuyệt đối tới tệp `.lic` của bạn và áp dụng nó.

```java
license.setLicense("Aspose._3D.lic");
```

> **Mẹo chuyên nghiệp:** Giữ tệp giấy phép ở ngoài thư mục kiểm soát nguồn để tránh việc lộ ra ngoài một cách vô tình.

## Cách Đặt Giấy Phép Bằng Luồng

### Bước 1: Tạo Đối Tượng License

Như trước, bắt đầu với một thể hiện `License` mới.

```java
License license = new License();
```

### Bước 2: Đặt Giấy Phép Từ Luồng

Đọc tệp giấy phép vào một `FileInputStream` và truyền luồng này cho `setLicense`. Khối try‑with‑resources đảm bảo luồng được đóng tự động.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Cách Sử Dụng Khóa Công Khai Riêng Tư cho Giấy Phép Tính Theo Mức

### Bước 1: Khởi Tạo Đối Tượng Metered License

Tạo một thể hiện của lớp `Metered`, lớp này xử lý giấy phép tính theo mức (pay‑as‑you‑go).

```java
Metered metered = new Metered();
```

### Bước 2: Đặt Khóa Công Khai và Riêng Tư

Cung cấp các khóa bạn nhận được từ Aspose. Các khóa này cho phép thư viện báo cáo việc sử dụng trở lại máy chủ giấy phép.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Cảnh báo:** Không bao giờ hard‑code (mã cứng) khóa riêng tư của bạn trong một JAR được phân phối công khai. Hãy cân nhắc tải nó từ một vị trí an toàn hoặc biến môi trường.

## Các Trường Hợp Sử Dụng Thông Thường

- **Enterprise 3D rendering pipelines** – mở khóa các API hiệu năng cao sau khi đặt giấy phép.  
- **Automated testing environments** – sử dụng giấy phép tạm thời (xem FAQ) để xác thực chức năng mà không cần mua giấy phép đầy đủ.  
- **Metered SaaS solutions** – tích hợp khóa công khai/riêng tư để tính phí khách hàng dựa trên mức sử dụng thực tế.

## Kết Luận

Chúc mừng! Bạn giờ đã biết **cách đặt giấy phép** cho Aspose.3D trong Java bằng tệp, luồng, và cách **sử dụng khóa công khai riêng tư** cho giấy phép tính theo mức. Với các bước này, bạn có thể tự tin tích hợp Aspose.3D vào bất kỳ ứng dụng Java nào và tận dụng tối đa khả năng xử lý 3D của nó.

## Câu Hỏi Thường Gặp

**Q1: Aspose.3D có tương thích với mọi phiên bản Java không?**  
A1: Có, Aspose.3D hoạt động với Java 6 và các phiên bản sau.

**Q2: Tôi có thể tìm tài liệu bổ sung ở đâu?**  
A2: Bạn có thể tham khảo tài liệu [tại đây](https://reference.aspose.com/3d/java/).

**Q3: Tôi có thể dùng thử Aspose.3D trước khi mua không?**  
A3: Có, bạn có thể khám phá bản dùng thử miễn phí [tại đây](https://releases.aspose.com/).

**Q4: Làm sao tôi có thể nhận hỗ trợ cho Aspose.3D?**  
A4: Truy cập [Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để nhận hỗ trợ từ cộng đồng và chính thức.

**Q5: Tôi có cần giấy phép tạm thời để thử nghiệm không?**  
A5: Có, hãy lấy giấy phép tạm thời [tại đây](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---