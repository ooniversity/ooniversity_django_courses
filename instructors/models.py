from django.db import models

class Position(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	#instructor = models.ForeignKey(Instructor)
	def __unicode__(self):
		return self.name

class Address(models.Model):
	line1 = models.CharField(max_length=255)
	line2 = models.CharField(max_length=255)

	def __unicode__(self):
		return self.line1+' '+self.line2

class Instructor(models.Model):
	# we have id = autofill, prime key
	name = models.CharField(verbose_name=u'Instructor Name',max_length=255, help_text="This is name description")
	surname = models.CharField(max_length=255)
	date_of_birthday = models.DateField()
	email = models.EmailField(unique=True, blank=True)
	phone = models.CharField(max_length=15, null=True)
	#null=True = not set === svojstvo of DB
	#blank=True = can be empty str === for validation
	course = models.CharField(max_length=255)
	#linkein = models.URLField(unique=True, null=True)
	slug = models.SlugField(unique=True)#, default=0)
	#photo = models.FileField()
	#photo = models.ImageField() #needs Pillow
	 #description = models.TextField()
	#age = models.IntegerField()
	#sulary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	#= AutoField(primary_key=True)
	#= PrimaryField - defoltnuy id
	#= BooleanField()
	is_active = models.BooleanField(default=True)#, null=True, blank=True)
	#= DateTimeField()
	#gender = models.CharField(max_length=1, choices = (('M','Male'), ('F','Female'))) # first => in DB... secont for export in anywhere, adminpanel
	#gender = models.IntegerField(default=1, choices = (('1','Male'), ('2','Female'))) # first => in DB... secont for export in anywhere, adminpanel
	#created_date = models.DateField(auto_now_add=True, null=True)
	#edited_date = models.DateField(auto_now=True, null=True)

	position = models.ForeignKey(Position)
		#max_length=10, 
		#	choices=(("instructor","Instructor"),("assistant","Assistant")), default="instructor")
	courses = models.ManyToManyField(Course)
	address = models.OneToOneField(Address, blank=True, null=True)


	def __unicode__(self):
		return self.name+' '+self.surname