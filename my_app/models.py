from django.db import models
from services.mixin import DateMixin,SlugMixin  
from services.generator import Generator 
from services.uploader import Uploader
from django.contrib.auth import get_user_model 


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)





COUNTRY_CHOICES = (
    ("usa", "Amerika"),
    ("az", "Azerbaijan"),
    ("eu", "Europa"),
    ("as", "Asia"),
    
    
)

User = get_user_model()


# Create your models here.
class Category(SlugMixin,DateMixin):
    name = models.CharField(max_length = 255,verbose_name = 'adi')


    def __str__(self):
        return self.name


    class Meta:
     ordering = ('-created_at',)
     verbose_name = 'category'
     verbose_name_plural = 'categories'


    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Category)
        super(Category, self).save(*args, **kwargs)





class Color(DateMixin,SlugMixin):
      name = models.TextField(verbose_name = 'mehsulun rengi')


      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'reng'
       verbose_name_plural = 'rengler'

      def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Color)
        super(Color, self).save(*args, **kwargs)

        

class Size(DateMixin,SlugMixin):
      name = models.TextField(verbose_name = 'mehsulun olcusu')

      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'olcu'
       verbose_name_plural = 'olculer'

      def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Size)
        super(Size, self).save(*args, **kwargs)


class Product(SlugMixin,DateMixin):
     category = models.ForeignKey(Category,on_delete = models.SET_NULL,null = True,blank = True)
     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     price = models.FloatField(verbose_name ='mehsulun qiymeti')
     description_L = models.TextField(verbose_name = 'kicik movzu')
     description_B = models.TextField(verbose_name = 'boyuk movzu')
     rating = models.FloatField(verbose_name = 'reyting')
     information = models.TextField(verbose_name = 'mehsul haqqinda')
     color = models.ManyToManyField(Color,verbose_name='reng')
     size = models.ManyToManyField(Size,verbose_name= 'olcu')
     is_seen = models.BooleanField(default = False)

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'mehsul'
       verbose_name_plural = 'mehsullar'

     def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Product)
        super(Product, self).save(*args, **kwargs)

    # partniors model yalniz image fild 
    # contact modeli form ve istifadeci yalniz 20 den az yaza bilr subject
    # chekout modeli
    # base.html
        
class Partniors(DateMixin):
      image = models.ImageField(upload_to=Uploader.upload_photo_partniors,null=True,blank=True)
      
      def __str__(self):
        return f'{self.created_at}'

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'partnior sekil'
       verbose_name_plural = 'partnior sekiller'

class Contact(SlugMixin,DateMixin):
       
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    
   
    def __str__(self):
        return self.name
    
    class Meta:

     ordering = ('name',)
     verbose_name = 'contact'
     verbose_name_plural = 'contactlar'

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=20, model_=Contact)
        super(Contact, self).save(*args, **kwargs)   


class Checkout(SlugMixin,DateMixin):
       name = models.CharField(max_length = 255,verbose_name = 'ad')
       surname = models.CharField(max_length = 255,verbose_name = 'soyad')
       email = models.CharField(max_length = 255,verbose_name = 'email')
       phone = models.CharField(max_length = 255, verbose_name = 'telefon')
       adress1 = models.CharField(max_length = 255, verbose_name = 'adress 1')
       adress2 = models.CharField(max_length = 255, verbose_name = 'adress 2')
       country = models.CharField(max_length=255,verbose_name='olke adlari',choices=COUNTRY_CHOICES)
       city = models.CharField(max_length = 255,verbose_name = 'sheher adi')
       state  = models.CharField(max_length = 255,verbose_name = 'dovlet')
       zipcode = models.CharField(max_length = 255, verbose_name = 'olke kodu')

       def __str__(self):
         return self.name
    
       class Meta:
        ordering = ('name',)
        verbose_name = 'checkout'
        verbose_name_plural = 'checkout'
        

       def save(self, *args, **kwargs):
         if not self.slug:
          self.slug = Generator.create_slug_shortcode(size=20, model_=Checkout)
         super(Checkout, self).save(*args, **kwargs)   

class ProductImage(DateMixin):
       image = models.ImageField(upload_to=Uploader.upload_photo_products,null=True,blank=True)
       product = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True,blank = True)

       def __str__(self):
         return self.product.name
    
       class Meta:
        ordering = ('-created_at',)
        verbose_name = 'mehsul shekili'
        verbose_name_plural = 'mehsul shekilleri'



class Comment(DateMixin, SlugMixin):
    text = models.TextField(verbose_name="User's comment")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text[:10]

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Rey"
        verbose_name_plural = "Reyler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Comment)
        super(Comment, self).save(*args, **kwargs)


class SpecialOffer(DateMixin, SlugMixin):
    text = models.TextField(verbose_name="metn")
    discount = models.TextField(verbose_name = 'endirim')
    image = models.ImageField(upload_to=Uploader.upload_photo_special_offer,null=True,blank=True)

    def __str__(self):
        return self.discount

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "xususi teklif"
        verbose_name_plural = "xususi teklifler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=SpecialOffer)
        super(SpecialOffer, self).save(*args, **kwargs)

class Slider(DateMixin):
       image = models.ImageField(upload_to=Uploader.upload_photo_slider,null=True,blank=True)
       title = models.CharField(max_length = 255, verbose_name = 'basliq')
       text = models.TextField(verbose_name="metn")

       def __str__(self):
         return self.title
    
       class Meta:
        ordering = ('-created_at',)
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'


class Basket(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField()
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
          return self.user.first_name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "sebet"
        verbose_name_plural = "sebetler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Basket)
        super(Basket, self).save(*args, **kwargs)
        
class SignUp(DateMixin):
    email = models.CharField(max_length = 255,verbose_name = 'email')

    def __str__(self):
        return self.email
    


class SosialMedia(DateMixin):
    sosial_name = models.CharField(max_length=255,verbose_name='sosial media hesabi',choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name", )
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"
