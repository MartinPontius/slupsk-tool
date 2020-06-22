from django.db import models
import pystache


class Kindergartendish(models.Model):
    kindergarten = models.ForeignKey(
        "kindergarten.Kindergarten",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Kindergarten",
        related_name='kindergartendish_kindergarten',
    )
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Choose the particular date",
    )
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name="Enter the name of the dish",
    )
    type = models.CharField(
        choices=(
            ("breakfast", "Breakfast"),
            ("lunch", "Lunch"),
            ("afternoon_tea", "Afternoon tea"),
        ),
        max_length=13,
        null=True,
        blank=True,
        verbose_name="Type of meal",
    )
    waste = models.CharField(
        choices=(
            ("less25", "Less than 25 %"),
            ("25to75", "From 25 % to 75 %"),
            ("more75", "More than 75 %"),
        ),
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Food waste – how much of the dish you have to dump into the garbage?",
    )
    picture = models.ImageField(
        upload_to="kindergartendishs",
        null=True,
        blank=True,
        verbose_name="Picture of the dish",
    )

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "kindergartendish"
        verbose_name_plural = "kindergartendishs"


class Composition(models.Model):
    kindergartendish = models.ForeignKey(
        Kindergartendish,
        on_delete=models.CASCADE,
        related_name="compositions",
    )
    ingredient = models.ForeignKey(
        "ingredient.Ingredient",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Choose an ingredient from the list",
        related_name='kindergartendish_ingredient',
    )
    weight_grams = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Enter the weight of the ingredient (grams)",
    )
    calories = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Enter the number of calories of the ingredient",
    )
    from_producer = models.CharField(
        choices=(
            ("yes", "Yes"),
            ("no", "No"),
            ("uncertain", "Don&#x27;t know"),
        ),
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Was the ingredient bought directly from the producer?",
    )

    class Meta:
        verbose_name = "composition"
        verbose_name_plural = "compositions"
