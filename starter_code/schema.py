from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    # Khai báo các trường ở đây...
    document_id: str = Field(...)
    source_type: str = Field(...)
    content: str = Field(...)
    
    # Sử dụng Field với default=None
    # Vì Python 3.10+ hỗ trợ | None, ta dùng nó để thay thế Optional
    author: str | None = Field(default=None)
    category: str | None = Field(default=None)
    timestamp: str | None = Field(default=None)
