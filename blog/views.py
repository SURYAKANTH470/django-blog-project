from django.shortcuts import render, get_object_or_404
from .models import Blog
import requests  # To make API requests

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    #  API Integration (Example with restcountries.com)
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        response.raise_for_status()  # Raise an exception for bad status codes
        countries_data = response.json()
    except requests.exceptions.RequestException as e:
        countries_data = None
        print(f"Error fetching countries data: {e}")

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'countries': countries_data})