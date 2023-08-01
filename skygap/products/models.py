from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from modelcluster.models import ClusterableModel
from wagtail.models import (
    DraftStateMixin,
    Orderable,
    Page,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet


# PAGES
class ProductIndexPage(Page):
    subpage_types = ["ProductPage"]


class ProductPage(Page):
    ajax_template = "products/product_ajax.html"
    code = models.CharField(
        max_length=2,
        unique=True,
        validators=[MinLengthValidator(2)],
        verbose_name="Unique Code",
        help_text="Example: HD (for hoodies)"
    )

    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Product type icon (<sizing guide>)"
    )

    content_panels = Page.content_panels + [
        FieldPanel("code"),
        FieldPanel("icon"),
    ]

    def __str__(self):
        return self.title


@register_snippet
class Product(DraftStateMixin, RevisionMixin, ClusterableModel):
    name = models.CharField(max_length=254)
    type = models.ForeignKey(
        ProductPage,
        on_delete=models.CASCADE,
        verbose_name="Product Type")
    # sizes = ParentalManyToManyField("products.Size")
    # colors = ParentalManyToManyField("products.Color")
    primary_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Primary Thumbnail Image"
    )
    secondary_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Secondary Thumbnail Image"
    )
    price = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=6,
        verbose_name="Starting Price ($)")
    
    # emb_price = models.DecimalField(
    #     blank=True,
    #     null=True,
    #     decimal_places=2,
    #     max_digits=6,
    #     verbose_name="Embroidery Price ($)")
    
    # def main_image(self):
    #     first_image = self.product_images.first()
    #     if first_image:
    #         return first_image.image
    #     else:
    #         return None
    
    panels = [
        FieldPanel("name"),
        FieldPanel("type"),
        FieldPanel("primary_thumbnail"),
        # FieldPanel("secondary_thumbnail"),
        # InlinePanel("product_images", label="Product Images"),
        # MultiFieldPanel(
        #     [
        #         FieldRowPanel(
        #             [
        #                 FieldPanel("colors", widget=forms.CheckboxSelectMultiple),
        #                 FieldPanel("sizes", widget=forms.CheckboxSelectMultiple),
        #             ]
        #         ),
        #     ], heading="Color and Sizing"
        # ),

        # InlinePanel("product_prices", label="Product Prices"),
        FieldPanel("price"),
        # FieldPanel("emb_price"),
    ]

    def __str__(self):
        return self.name
    

@register_snippet
class Size(DraftStateMixin, RevisionMixin, ClusterableModel):
    size = models.CharField(max_length=5)
    description = models.CharField(max_length=254)

    panels = [
        FieldPanel("size"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.size
    

@register_snippet
class Color(DraftStateMixin, RevisionMixin, ClusterableModel):
    color = models.CharField(blank=True, null=True, max_length=254)
    hexcode = models.CharField(blank=True, null=True, max_length=7)

    panels = [
        FieldPanel("color"),
        FieldPanel("hexcode"),
    ]

    def __str__(self):
        if not self.color:
            return self.hexcode
        return self.color
    

# @register_snippet
# class PriceType(DraftStateMixin, RevisionMixin, ClusterableModel):
#     price_type = models.CharField(max_length=254)

#     panels = [
#         FieldPanel("price_type"),
#     ]

#     def __str__(self):
#         return self.price_type
    

# Product Images
class ProductImage(Orderable):
    parent = ParentalKey(
        Product,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='product_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Product images; first image will be thumbnail (<sizing>)"
    )

    panels = [
        FieldPanel('image'),
    ]


# class ProductPrice(Orderable):
#     parent = ParentalKey(
#         Product,
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name='product_prices'
#     )
#     types = models.ForeignKey(
#         "products.PriceType",
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE,
#     )
#     price = models.DecimalField(
#         blank=True,
#         null=True,
#         decimal_places=2,
#         max_digits=6,
#         verbose_name="Price ($)"
#     )

#     panels = [
#         FieldRowPanel(
#             [
#                 FieldPanel("types", widget=forms.Select),
#                 FieldPanel("price"),
#             ]
#         ),
#     ]
