from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BusquedaPostForm


def inicio(request):
    posts = Post.objects.filter(publicado=True)[:6]
    return render(request, 'blog/inicio.html', {'posts': posts})


def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'Post "{post.titulo}" creado exitosamente.')
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})


def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            messages.success(request, f'Autor "{autor}" registrado.')
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'blog/form_autor.html', {'form': form})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat = form.save()
            messages.success(request, f'Categoría "{cat.nombre}" creada.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'blog/form_categoria.html', {'form': form})


def buscar(request):
    form = BusquedaPostForm(request.GET or None)
    resultados = []
    busqueda_realizada = False
    if form.is_valid():
        consulta = form.cleaned_data.get('consulta', '')
        categoria = form.cleaned_data.get('categoria')
        busqueda_realizada = True
        resultados = Post.objects.filter(publicado=True)
        if consulta:
            resultados = resultados.filter(titulo__icontains=consulta) | \
                         resultados.filter(contenido__icontains=consulta)
        if categoria:
            resultados = resultados.filter(categoria=categoria)
        resultados = resultados.distinct()
    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados,
        'busqueda_realizada': busqueda_realizada,
    })