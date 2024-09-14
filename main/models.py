from django.db import models
from django.utils.html import mark_safe 

#BANNERS Data
class banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text=models.CharField(max_length=150)
    #Names images after their alt text
    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
    # Returns an HTML <img> tag to display the product's image in the admin interface
    # The image is displayed as a thumbnail with a width of 80 pixels.
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

# Pages for Privacy and Terms Data
class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    def __str__(self):
        return self.title
        
# FAQ Data
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
        
# Services Data
class service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img=models.ImageField(upload_to="services/",null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))
    
# Enquiry Form Data
class Enquiry(models.Model):
    enquirer_name = models.CharField(max_length=150)
    enquirer_email = models.CharField(max_length=150)
    enquiry_message = models.TextField()
    enquiry_dateAndTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enquirer_name
        
class trainer(models.Model):
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True) 
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.TextField()
    is_active=models.BooleanField(default=False)
    detail=models.TextField()
    img=models.ImageField(upload_to="trainers/",null=True)

    def __str__(self):
        return str(self.full_name)
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))


# Assign subscriber to a trainer
class AssignSubscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


# Trainer's Achievements
class TrainerAcheivement(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.DateField(null=True)
    img = models.ImageField(upload_to="trainers_achievments/")
    details = models.TextField()

    def __str__(self):
        return str(self.title)
    
    def image_tag(self):
        if self.img:
            return mark_safe("<img src='%s' width='80'/>" %(self.img.url))
        else:
            return 'no-image'
        

# Trainer's Salary
class TrainerSalary(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    amount_date = models.DateField()
    remarks = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Trainers' Salaries"

    def __str__(self):
        return str(self.trainer.full_name)


# Training Notifications
class TrainerNotification(models.Model):
    notif_msg = models.TextField()

    def __str__(self):
        return str(self.notif_msg)


    def save(self,  *args, **kwargs):
        super(TrainerNotification, self).save(*args, **kwargs)
        channel_layer = get_channel_layer()
        notif = self.notif_msg
        total = TrainerNotification.objects.all().count()
        async_to_sync(channel_layer.group_send) (
            'noti_group_name', {
                'type' : 'send_notificatio',
                'value' : json.dumps({'notif':notif, 'total': total})}
            )



# Notifications - Mark as read by trainer
class NotifTrainerStatus(models.Model):
    notif = models.ForeignKey(TrainerNotification, on_delete=models.CASCADE, related_name='trainernotification')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='trainer')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Trainer Notification Status"


# Subscribers and Admin Messages to Trainer
class TrainerMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Messages for Trainers"
        
    
class mealplan(models.Model):
    #CURRENTLY JUST A NAME BUT WILL ADD SUBSCRIBER ADD ONCE SUBSCRIBER MODEL IS MADE
    subscriber = models.CharField(max_length=100)
    mealchoice = [('B','breakfast'),('L','lunch'),('D','dinner')]
    mealtime = models.CharField(max_length=1,choices=mealchoice,default='B')
    meal = models.CharField(max_length=100)
    trainer = models.ForeignKey(trainer,on_delete=models.CASCADE,related_name='mealplans')


