# 04 — Data cleaning và feature engineering

**Đầu vào:** mô-đun 03. **Đầu ra:** biến raw data thành dataset phân tích/model được và ghi lại quyết định làm sạch.

1. `01_clean_transform.ipynb` — profiling, missing values, duplicates, type coercion, outlier, encode, scale và split an toàn.

Nguyên tắc: tìm hiểu nguyên nhân dữ liệu thiếu trước khi điền; fit scaler/imputer trên train set, rồi mới transform validation/test để tránh leakage.
