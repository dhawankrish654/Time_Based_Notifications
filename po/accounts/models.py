from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class notify(models.Model):
    notif=models.TextField()
    day=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    hrs=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(60)])
    min=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(60)])
    def __str__(self):
        return self.notif
class TblAdp(models.Model):

    city = models.CharField(max_length=30)


    adp_id = models.CharField(max_length=8)
    password = models.CharField(max_length=16)
    dob = models.CharField(max_length=30)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    father_firstname = models.CharField(max_length=50)
    father_lastname = models.CharField(max_length=50)
    nominee_firstname = models.CharField(max_length=50)
    nominee_lastname = models.CharField(max_length=50)
    nominee_gender = models.CharField(max_length=20)
    nominee_dob = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    address_correspondence = models.TextField()
    landmark = models.TextField()
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    id_proof = models.CharField(max_length=30)
    proof_address = models.TextField()
    bank_name = models.CharField(max_length=30)
    account_no = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)
    ifs_code = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)
    success = models.IntegerField()
    verify = models.IntegerField()
    mobile_verify = models.IntegerField()
    new_joining = models.IntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_adp'
class TblCategory(models.Model):

    category = models.CharField(max_length=50,unique=True)

    class Meta:
        managed = False
        db_table = 'tbl_category'
    def __str__(self):
        return self.category
class SubCategories(models.Model):
    sub_category = models.CharField(max_length=30)
    category = models.ForeignKey(TblCategory,to_field='category',on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category
