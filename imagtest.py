from PIL import Image

#이미지 파일 경로
image_path = '202212008462_500.jpg'

#이미지 열기
image = Image.open(image_path)

info = image.info
print(info)

info['meta']='example meta data'
new_image_path='new_image.jpg'
#이미지 복사
image.save(new_image_path, format='JPEG', **info)