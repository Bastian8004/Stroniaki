from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from django.urls import reverse
import mysite.settings
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import AboutUsForm, ContactFormForm, BlogForm, PostForm
from strona.models import Main, About_us, Blog, Post, Contact

def main(request):
    mains = Main.objects.all().order_by()
    return render(request, 'main.html', {'mains': mains})


def error_404_view(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, '404.html', None, None, 404)


def about_us(request):
    abouts = About_us.objects.all().order_by('-published_date')
    return render(request, 'about_us.html', {'abouts': abouts})


def about_us_new(request):
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            about = form.save(commit=False)
            about.published_date = timezone.now()
            about.save()
            return redirect('about_us')
    else:
        form = AboutUsForm()
    return render(request, 'About/about_new.html', {'form': form})


def about_us_edit(request, pk):
    about = get_object_or_404(About_us, pk=pk)
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.published_date = timezone.now()
            about.save()
            return redirect('about_us')
    else:
        form = AboutUsForm(instance=about)
    return render(request, 'About/about_edit.html', {'form': form})


def about_us_delete(request, pk):
    about = get_object_or_404(About_us, pk=pk)
    about.delete()
    return redirect(reverse('about_us'))


def offers(request):
    return render(request, 'offers.html')


def post_list(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {'blogs': blogs})


def post_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    posts = Post.objects.filter(Blog=blog)

    return render(request, 'Blog/post_detail.html', {
        'blog': blog,
        'posts': posts,
    })


def post_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'Blog/post_new.html', {'form': form})


def post_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'Blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect(reverse('blog'))


def post_post_new(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=blog.pk)
    else:
        form = PostForm()
    return render(request, 'Blog/post_post_new.html', {'form': form, 'blog': blog})


def post_post_edit(request, blog_pk, pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=blog.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog/post_post_edit.html', {'form': form, 'blog': blog})


def post_post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('post_detail_delete'))

def contact_email_created(contact):
    formatted_date = contact.created_date.strftime('%d-%m-%Y')

    subject = f'Stroniaki - Zapytanie - {contact.Subject}'
    message = f"""Imię i nazwisko: {contact.Name}
        Numer telefonu: {contact.Phone}
        Email: {contact.Email}

        Wiadomość: {contact.Message}

        Data: {formatted_date}
        """

    subject_client = f'Stroniaki - Potwierdzenie wysłania wiadomości'
    message_client = f""" Witam, poniżej przesyłam potwierdzenie wysłania wiadomości do nas.

        Szczegóły:

        Temat: {contact.Subject}
        Imię i nazwisko: {contact.Name}
        Numer telefonu: {contact.Phone}
        Email: {contact.Email}

        Wiadomość: {contact.Message}

        Data: {formatted_date}

        Skontaktujemy się z Państwem drogą mailową albo telefoniczną najszybciej jak to będzie możliwe.

        Miłego dnia
        Zespół Stroniaki


        Wiadomość została wygenerowana automatycznie.
            """

    email = EmailMessage(
        subject,
        message,
        mysite.settings.DEFAULT_FROM_EMAIL,
        ['sebastian.paszkowski@uth.pl'],
    )

    email_client = EmailMessage(
        subject_client,
        message_client,
        mysite.settings.DEFAULT_FROM_EMAIL,
        [contact.Email]
    )

    email.send()
    email_client.send()


def send_question_email_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save the form and create the contact object
            contact_email_created(contact)  # Pass the contact object here
            messages.success(request, 'Wiadomość została wysłana. Skontaktujemy się z Tobą!')
            return redirect('contact')
        else:
            print(form.errors)  # Debugging - print any form errors to the console
    else:
        form = ContactFormForm()

    return render(request, 'contact.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact_email_created(contact)  # Zmieniamy na przekazanie obiektu
            messages.success(request, 'Wiadomość została wysłana. Skontaktujemy się z Tobą!')
            return redirect('contact.html')
    else:
        form = ContactFormForm()

    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'form': form, 'contacts': contacts})





