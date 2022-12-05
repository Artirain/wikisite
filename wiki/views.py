from audioop import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Wiki, Category
from .forms import WikiForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!!!!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'wiki/register.html', {'form' : form})


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'wiki/login.html', {'form' : form})


def signup(request):
    signup(request)
    if request.user.is_authenticated():
        return redirect('home')
    

def user_logout(request):
    logout(request)
    return redirect('login')


class HomeWiki(ListView): #подкласс класса ListView
    model = Wiki #аналог строки wiki = Wiki.objects.all()
    template_name =  'wiki/home_wiki_list.html'
    context_object_name = 'wiki'
    # extra_context = {'title' : 'Главная'}
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) #взяли что было в переменной контекст
        context['title'] = 'Главная страница' #дополнили данными
        return context

    def get_queryset(self):
        return Wiki.objects.filter(is_published = True) #фильтрация

# def index(request):   #контроллер функции
#     wiki = Wiki.objects.all()

#     context = {
#     'wiki' : wiki, 
#     'title' : 'Список категорий',
#     }

#     return render(request, 'wiki/index.html', context = context) #render использует 3 параметра: request, template name и context

class CategoryWiki(ListView):
    model = Wiki
    template_name =  'wiki/home_wiki_list.html'
    context_object_name = 'wiki' #название объекта
    allow_empty = False #не показываем категории которых нет
    


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) #взяли что было в переменной контекст
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']) #дополнили данными
        return context

    def get_queryset(self):
        return Wiki.objects.filter(category_id = self.kwargs['category_id'], is_published = True) #фильтрация


class ViewWiki(DetailView):
    model = Wiki
    context_object_name = 'wiki_item'
    # pk_url_kwarg = 'wiki_id'
    # template_name =  'wiki/wiki_detail.html'



class CreateWiki(LoginRequiredMixin, CreateView): #класс для создания форм
    form_class = WikiForm
    template_name = 'wiki/add_wiki.html'
    login_url = '/admin/'
    
   
# def get_category(request, category_id):
#     wiki = Wiki.objects.filter(category = category_id) #добавит условие(фильтр)

#     category = Category.objects.get(pk=category_id)
#     return render(request, 'wiki/category.html', {'wiki' : wiki, 'category' : category})

# def view_wiki(request, wiki_id):
#     # wiki_item = Wiki.objects.get(pk=wiki_id)
#     wiki_item = get_object_or_404(Wiki, pk=wiki_id)
#     return render(request, 'wiki/view_wiki.html', {'wiki_item': wiki_item})

def add_wiki(request):
    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            wiki = Wiki.objects.create(**form.cleaned_data) #распаковка словаря, присвоит переменным по ключам их значение
            return redirect(wiki) #после добавления новости будет возвращать юзера на главную страницу
    else:
        form = WikiForm()
        return render(request, 'wiki/add_wiki.html', {'form' : form})
        
