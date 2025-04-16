from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import tempfile
import os
from pdf2image import convert_from_path

router = APIRouter(prefix='/pdftopng')

@router.post("/")
async def pdftopng(file: UploadFile = File(...)):
    # 创建临时文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        # 保存上传的PDF文件
        content = await file.read()
        tmp_pdf.write(content)
        tmp_pdf_path = tmp_pdf.name
    
    # 转换为PNG
    images = convert_from_path(tmp_pdf_path)
    
    # 保存第一页为PNG
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_png:
        images[0].save(tmp_png.name, "PNG")
        tmp_png_path = tmp_png.name
    
    # 清理临时PDF文件
    os.unlink(tmp_pdf_path)
    
    # 返回PNG文件
    return FileResponse(
        tmp_png_path,
        media_type="image/png",
        filename="converted.png"
    )