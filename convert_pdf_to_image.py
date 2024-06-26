import os
from pdf2image import convert_from_path


def pdf2images(pdf_file_path, save_imgs_path, img_format='png'):
    """pdf 파일을 image 파일로 변환해주는 함수

    Args:
        pdf_file_path (str): pdf 파일의 경로(.pdf까지의 전체 경로)
        save_imgs_path (str): 이미지 파일을 저장할 폴더의 경로
        img_format (str): 이미지 파일의 포맷 (png, jpg, ...)

    Example:
        p = pdf2images("~/Downloads/llm-bio.pdf", "~/Downloads/lim-bio-imgs")
    """
    pages = convert_from_path(pdf_file_path)
    for i, page in enumerate(pages):
        output_path = os.path.join(save_imgs_path, f'img_{i+1}.png')
        page.save(output_path, 'PNG')
    return None