class Article(models.Model):
    title = models.CharField()


class Comment(models.Model):
    text = models.CharField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


#
class Device(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)


class Card(models.Model):
    objects = models.Manager()
    device = models.ForeignKey(Device, to_field="id", on_delete=models.CASCADE)
    # device_type = models.CharField(max_length=32, unique=True, blank=True, null=True)
    # device_name = models.CharField(max_length=32, unique=True, blank=True, null=True)


Card.objects.annotate(
    device_type=F("card__device__type"),
    # device_name
)

# к примеру в class Card хочу получать из class Devace type и name
