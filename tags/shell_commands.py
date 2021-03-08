from tags.models import Tag

qs = Tag.objects.all()
print(qs)
black =Tag.objects.last()
black.title
black.slug

black.products

black.products.all()

black.products.all().first()

exit()

from products.models import Product

qs = Product.objects.all()
print(qs)
tshirt.title =qs.first()
tshirt.description

tshirt.tag

tshirt.tags

tshirt.tag_set

tshirt.tag_set.all()

tshirt.tag_set.filter(title__icontains='black')
