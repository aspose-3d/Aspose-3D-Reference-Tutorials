---
date: 2026-02-25
description: Tìm hiểu cách đảo ngược hệ tọa độ và tùy chỉnh việc nhập 3D bằng Aspose.3D
  LoadOptions trong Java. Hướng dẫn chi tiết từng bước cho 3DS, OBJ, STL, U3D, glTF,
  PLY, X và tùy chọn FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Đảo hệ tọa độ – Tùy chỉnh việc tải tệp 3D trong Java với Aspose.3D
url: /vi/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Đảo Hệ Tọa Độ – Tùy Chỉnh Tải Tệp 3D trong Java với Aspose.3D

Trong bối cảnh thiết kế và phát triển 3D không ngừng thay đổi, **đảo hệ tọa độ** khi nhập mô hình là một yêu cầu phổ biến. Dù bạn đang chuyển đổi tài sản từ hệ phải sang hệ trái hoặc cần căn chỉnh mô hình với quy ước trục của engine, Aspose.3D cho Java cung cấp khả năng kiểm soát chi tiết. Hướng dẫn này sẽ chỉ cho bạn cách **tùy chỉnh nhập 3D** bằng `LoadOptions` của Aspose.3D, bao gồm các định dạng phổ biến nhất như 3DS, OBJ, STL, U3D, glTF, PLY, X và tùy chọn FBX.

## Câu trả lời nhanh
- **Công dụng của “đảo hệ tọa độ” là gì?** Nó hoán đổi các trục X/Y/Z để phù hợp với quy ước hệ tọa độ mục tiêu.  
- **Các định dạng nào hỗ trợ đảo?** Tất cả các định dạng chính (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) đều cung cấp tùy chọn `setFlipCoordinateSystem`.  
- **Có cần thư viện bổ sung không?** Chỉ cần JAR Aspose.3D cho Java; không yêu cầu bộ chuyển đổi bên ngoài.  
- **Có thể tải vật liệu cùng lúc không?** Có — sử dụng `setEnableMaterials(true)` cho tệp OBJ.  
- **Cần giấy phép cho môi trường sản xuất không?** Cần giấy phép Aspose.3D hợp lệ cho các triển khai không dùng bản dùng thử.

## Hệ tọa độ “đảo” là gì?
Đảo hệ tọa độ thay đổi hướng của các trục được mô hình nhập vào sử dụng. Điều này rất quan trọng khi tệp nguồn sử dụng kiểu tay khác (phải vs. trái) so với engine của bạn, tránh việc mô hình bị lật ngược hoặc phản chiếu.

## Tại sao cần tùy chỉnh nhập 3D?
Tùy chỉnh nhập cho phép bạn:
- Bảo tồn các biến đổi hoạt ảnh (`setApplyAnimationTransform`).  
- Xử lý màu đúng (`setGammaCorrectedColor`).  
- Giải quyết đường dẫn tài nguyên bên ngoài qua `getLookupPaths()`.  
- Tối ưu hóa việc sử dụng bộ nhớ bằng cách chỉ tải những gì cần.

## Yêu cầu trước

- Hiểu biết cơ bản về lập trình Java.  
- Đã cài đặt Java Development Kit (JDK).  
- Thư viện Aspose.3D cho Java đã tải xuống. Bạn có thể lấy nó [here](https://releases.aspose.com/3d/java/).  
- Quen thuộc với các định dạng tệp 3D như 3DS, OBJ, STL, U3D, glTF, PLY, X và FBX.

## Nhập Gói

Trong dự án Java của bạn, hãy chắc chắn nhập các gói Aspose.3D cần thiết:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Cách tùy chỉnh nhập 3D bằng LoadOptions

Dưới đây là các đoạn mã từng bước minh họa cách bật tùy chọn **đảo hệ tọa độ** cho mỗi định dạng được hỗ trợ. Các đoạn mã đã sẵn sàng để sao chép vào dự án; chỉ cần thay `"Your Document Directory"` bằng đường dẫn thực tế tới tài sản của bạn.

### Bước 1: Tùy chỉnh tải tệp 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Bước 2: Tùy chỉnh tải tệp OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Bước 3: Tùy chỉnh tải tệp STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Bước 4: Tùy chỉnh tải tệp U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Bước 5: Tùy chỉnh tải tệp glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Bước 6: Tùy chỉnh tải tệp PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Bước 7: Tùy chỉnh tải tệp X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Bước 8: Tùy chỉnh tải tệp FBX (Tùy chọn)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Các vấn đề thường gặp và giải pháp
- **Mô hình xuất hiện bị lật ngược sau khi tải** – Kiểm tra rằng `setFlipCoordinateSystem(true)` đã được đặt cho định dạng đúng.  
- **Vật liệu bị thiếu** – Đối với tệp OBJ, đảm bảo `setEnableMaterials(true)` và các tệp vật liệu (.mtl) nằm trong một trong các đường dẫn lookup.  
- **Tọa độ texture bị ngược** – Đối với glTF, bạn có thể cần `setFlipTexCoordV(true)` bổ sung cho việc đảo các trục.  
- **Lỗi không tìm thấy tệp** – Thêm thư mục chứa tài nguyên bên ngoài (texture, tệp phụ) vào `loadOpts.getLookupPaths()`.

## Kết luận

Bằng cách tận dụng `LoadOptions` của Aspose.3D, bạn có thể **đảo hệ tọa độ** và **tùy chỉnh nhập 3D** cho hầu hết các định dạng chính. Mức độ kiểm soát này loại bỏ nhu cầu viết script xử lý sau và đảm bảo tài sản của bạn được hiển thị đúng từ lần đầu tiên.

## Câu hỏi thường gặp

### Q1: Tôi có thể tìm tài liệu Aspose.3D cho Java ở đâu?
A1: Tài liệu có sẵn [here](https://reference.aspose.com/3d/java/).

### Q2: Làm sao để tải Aspose.3D cho Java?
A2: Bạn có thể tải nó [here](https://releases.aspose.com/3d/java/).

### Q3: Có bản dùng thử miễn phí không?
A3: Có, bạn có thể truy cập bản dùng thử miễn phí [here](https://releases.aspose.com/).

### Q4: Tôi có thể nhận hỗ trợ cho Aspose.3D cho Java ở đâu?
A4: Tham khảo diễn đàn hỗ trợ [here](https://forum.aspose.com/c/3d/18).

### Q5: Có cần giấy phép tạm thời để thử nghiệm không?
A5: Có, hãy lấy giấy phép tạm thời [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Cập nhật lần cuối:** 2026-02-25  
**Kiểm tra với:** Aspose.3D cho Java 24.11 (mới nhất)  
**Tác giả:** Aspose