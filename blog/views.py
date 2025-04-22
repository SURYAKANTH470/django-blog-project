import requests
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.db.models import Q
from django.http import HttpResponse

def test_form_submission(request):
    if request.method == 'POST':
        return HttpResponse("Form submitted successfully!")
    return HttpResponse("This is a test form page.")

def blog_list(request):
    blogs = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        response.raise_for_status()
        countries = response.json()
    except requests.exceptions.RequestException as e:
        countries = []
        print(f"Error fetching countries: {e}")

    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'query': query, 'countries': countries, 'user': request.user}) # Pass the user to the template

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})