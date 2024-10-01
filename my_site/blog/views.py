from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hihking in the mountais",
        "image": "montains.jpg",
        "auth": "lucasoliveira",
        "date": date(2024, 9, 28),
        "title": "Mountain hiking",
        "excert": "ksdnfkjsnfç çsdfçslkdf lsdfjlksdfml ldkjfklsdfmsdjfkls jksdfklsjdflksjd lksjdfhewp9qunfpiq efuhqweopfjwperfnowf efp9wjef0jef=0",
        "content": "lore asjdoifplaslore asjdoifplas çaksldjf quepn q9w8hefpqwo p9mclpkd fpodmcwp ecnjffpioqh9p qp9ueiownk apokdcclksiui iwquhoaipqá oijpjifaçaodqp akjnp fponapkldlore asjdoifplas çaksldjf quepn q9w8hefpqwo p9mclpkd fpodmcwp ecnjffpioqh9p qp9ueiownk apokdcclksiui iwquhoaipqá oijpjifaçaodqp akjnp fponapkld çaksldjf quepn q9w8hefpqwo p9mclpkd fpodmcwp ecnjffpioqh9p qp9ueiownk apokdcclksiui iwquhoaipqá oijpjifaçaodqp akjnp fponapkld"
    }
]

# Create your views here.

def home_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_datails(request, slug):
    return render(request, "blog/post-datail.html")