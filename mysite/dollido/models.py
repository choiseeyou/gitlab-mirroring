from django.db import models

# Create your models here.
class Lost(models.Model):
    image = models.FileField('사진 등록',upload_to='lost_image', blank=True)
    item = models.CharField('분실물 이름', max_length=200)
    description = models.CharField('특이사항',max_length=500, default='')
    create_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.item
    class Meta:
        db_table = 'lost_item'
  

class ApiListId(models.Model):
  # API list primary key
  atcId = models.CharField(max_length=30, primary_key=True)
  # 물품명
  fdPrdtNm = models.CharField(max_length=500, null=True, default = '')
  # 분실물 이미지 명
  fdFilePathImg = models.CharField(max_length=300)
  # 게시제목
  fdSbjt = models.CharField(max_length=500)
  # 보관 장소
  depPlace = models.CharField(max_length=30)
  # 습득일자  
  fdYmd = models.DateField(max_length=10, null = True)
  # 카테고리 (외래키)
  # category = models.ForeignKey(Category, on_delete=models.CASCADE)
  category = models.CharField(max_length=20)
  # 색상명
  clrNm = models.CharField(max_length=10)