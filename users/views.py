from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm

from .models import User, UserEmailVerification


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'LogIn'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_message = "Вы успешно зарегистрированы"
    success_url = reverse_lazy('users:login')  # reverse_lazy, вместо reverse так как он не работает в классах
    title = 'Register'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class UserEmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):  # Добавляем логику GET запроса для верификации пользователя
        code = kwargs['code']  # kwargs['code'] в данном случае получение из url uuid для верификации
        user = User.objects.get(email=kwargs['email'])  # kwargs['email'] в данном случае получение из url email для
        # верификации
        email_verifications = UserEmailVerification.objects.filter(user=user, code=code)  # выбираем из
        # UserEmailVerification запись с user=user, code=code
        if email_verifications.exists() and not email_verifications.first().is_expired():  # Если запись существует и
            # её срок не истёк, то верифицируем
            user.is_verified_email = True
            user.save()
            return super(UserEmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
