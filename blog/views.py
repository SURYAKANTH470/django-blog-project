import requests
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    countries_data = []
    try:
        response = requests.get('https://api.worldbank.org/v2/country?format=json')
        print(f"Response Status Code: {response.status_code}")

        if response.status_code == 200:
            countries_data = response.json()[1]  # The second element contains country data
            print(f"Countries data fetched: {countries_data[:5]}")
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching countries data: {e}")

    if not countries_data:
        print("No countries data available.")

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'countries': countries_data})
