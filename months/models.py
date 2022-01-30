from django.db import models

# Create your models here.

class Months(models.Model):
    months=models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'months_table'


class January(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'january_table'



class February(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'february_table'



class March(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'march_table'



class April(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'april_table'



class May(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'may_table'



class June(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'june_table'



class July(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'july_table'



class August(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'august_table'



class September(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'september_table'



class October(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'october_table'



class November(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'november_table'



class December(models.Model):
    date_pk = models.IntegerField(primary_key=True)
    sehri_ends = models.CharField(max_length=8, null=False)
    fajr_starts = models.CharField(max_length=8, null=False)
    fajr_ends = models.CharField(max_length=8, null=False)
    duhur_starts = models.CharField(max_length=8, null=False)
    duhur_ends = models.CharField(max_length=8, null=False)
    asr_starts = models.CharField(max_length=8, null=False)
    asr_ends = models.CharField(max_length=8, null=False)
    maghrib_starts = models.CharField(max_length=8, null=False)
    maghrib_ends = models.CharField(max_length=8, null=False)
    isha_starts = models.CharField(max_length=8, null=False)
    isha_ends = models.CharField(max_length=8, null=False)
    makrooh_morning_starts = models.CharField(max_length=8, null=False)
    makrooh_morning_ends = models.CharField(max_length=8, null=False)
    makrooh_noon_starts = models.CharField(max_length=8, null=False)
    makrooh_noon_ends = models.CharField(max_length=8, null=False)
    makrooh_evening_starts = models.CharField(max_length=8, null=False)
    makrooh_evening_ends = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'december_table'
