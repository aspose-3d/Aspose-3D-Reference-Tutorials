---
title: Áp dụng vật liệu PBR vào hộp trong cảnh 3D
linktitle: Áp dụng vật liệu PBR vào hộp trong cảnh 3D
second_title: API Aspose.3D .NET
description: Khám phá thế giới đồ họa 3D với Aspose.3D cho .NET. Tạo các cảnh sống động một cách dễ dàng bằng cách sử dụng vật liệu Kết xuất dựa trên vật lý.
type: docs
weight: 10
url: /vi/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Giới thiệu

Chào mừng đến với thế giới đồ họa 3D hấp dẫn! Trong hướng dẫn từng bước này, chúng ta sẽ khám phá thư viện Aspose.3D for .NET mạnh mẽ và tìm hiểu cách tạo cảnh 3D tuyệt đẹp bằng cách sử dụng vật liệu Kết xuất dựa trên vật lý (PBR). Aspose.3D đơn giản hóa quy trình phức tạp của đồ họa 3D và mở ra nhiều khả năng cho các nhà phát triển.

## Điều kiện tiên quyết

Trước khi chúng ta đi sâu vào thế giới đồ họa 3D thú vị, hãy đảm bảo bạn đã thiết lập mọi thứ:

### Tải xuống và cài đặt Aspose.3D cho .NET

 Tham quan[Aspose.3D cho tài liệu .NET](https://reference.aspose.com/3d/net/) để được hướng dẫn chi tiết cách tải và cài đặt thư viện.

### Nhận giấy phép

 Để mở khóa toàn bộ tiềm năng của Aspose.3D, hãy lấy giấy phép hợp lệ. Bạn có thể nhận được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/) hoặc mua giấy phép đầy đủ[đây](https://purchase.aspose.com/buy).

## Nhập không gian tên

Trước tiên, hãy đảm bảo nhập các không gian tên cần thiết để tận dụng các khả năng của Aspose.3D cho .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Bước 1: Khởi tạo một cảnh

Bắt đầu bằng cách khởi tạo cảnh 3D bằng đoạn mã sau:

```csharp
Scene scene = new Scene();
```

## Bước 2: Khởi tạo vật liệu PBR

Tạo một đối tượng vật liệu PBR để đạt được kết xuất chân thực:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Bước 3: Đặt thuộc tính vật liệu

Tinh chỉnh các đặc tính của vật liệu, làm cho nó gần như kim loại và rất thô:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Bước 4: Tạo hộp

Tạo một hộp mà vật liệu PBR sẽ được áp dụng:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Bước 5: Áp dụng vật liệu vào hộp

Gán vật liệu PBR cho nút hộp đã tạo:

```csharp
boxNode.Material = mat;
```

## Bước 6: Lưu cảnh 3D

Lưu cảnh 3D sang định dạng STL với thư mục đầu ra mong muốn:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Chúc mừng! Bạn đã áp dụng thành công vật liệu PBR vào hộp trong cảnh 3D bằng Aspose.3D for .NET.

## Phần kết luận

Khám phá đồ họa 3D với Aspose.3D cho .NET mở ra cánh cửa cho khả năng sáng tạo vô tận. Với API trực quan và các tính năng mạnh mẽ, việc tạo ra những cảnh quay ấn tượng về mặt hình ảnh sẽ trở thành một trải nghiệm thú vị cho các nhà phát triển.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D có tương thích với các định dạng tệp 3D khác không?

Câu trả lời 1: Có, Aspose.3D hỗ trợ nhiều định dạng tệp 3D khác nhau, đảm bảo tính linh hoạt trong các dự án của bạn.

### Câu hỏi 2: Tôi có thể sử dụng Aspose.3D cho các ứng dụng thương mại không?

A2: Chắc chắn rồi! Aspose.3D cung cấp giấy phép thương mại để tích hợp liền mạch vào ứng dụng của bạn.

### Câu 3: Có phiên bản dùng thử không?

Câu trả lời 3: Có, bạn có thể khám phá các khả năng của Aspose.3D bằng cách tải xuống bản dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 4: Tôi có thể tìm sự hỗ trợ và thảo luận của cộng đồng ở đâu?

 A4: Tham gia cộng đồng Aspose.3D tại[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được hỗ trợ và thảo luận.

### Câu hỏi 5: Làm cách nào để có được giấy phép tạm thời cho Aspose.3D?

 A5: Bạn có thể nhận được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/) cho mục đích đánh giá.