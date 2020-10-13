from django.db import models


# Create your models here.
class Attendance(models.Model):
    ATTENDANCE = (('出席', '出席'), ('欠席', '欠席'),)
    name = models.CharField(verbose_name='名前', max_length=50, unique=True)
    attendance = models.CharField(verbose_name='出欠', max_length=2, choices=ATTENDANCE)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return self.name
