from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, RedirectView
from django.contrib import messages
# Create your views here.
from accounts.forms import SignUpForm
from accounts.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'avatar',
    )
    success_url = reverse_lazy('index')
    template_name = 'my_profile.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    template_name = 'sign_up.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm

    def form_valid(self, form):
        messages.info(self.request, 'Thank for sign up! Please, check your email.')
        return super().form_valid(form)


class ActivateUserView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(User, username=username, is_active=False)

        user.is_active = True

        # update_fields - save only needed(minimum) fields
        user.save(update_fields=('is_active', ))

        messages.info(self.request, 'Your Account is activated!')

        return super().get_redirect_url(*args, **kwargs)
