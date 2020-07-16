from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from basic_app.models import Exam,UserProfileInfo
from basic_app.forms import ExamForm
from django.http import HttpResponse
from django.http import FileResponse, HttpResponseRedirect,HttpResponse
from django.utils.text import slugify
import os,re
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy,reverse
from django.utils import timezone
from basic_app.forms import UserForm,ExamForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

class AboutView(TemplateView):
    template_name='about.html'

class SuccesUploadView(TemplateView):
    template_name='successfull_submission.html'

class ExamListView(ListView):
    model=Exam
    template_name='exam_list.html'

    def get_queryset(self):
        return Exam.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


@login_required
def upload_paper(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            exam=form.save(commit=False)
            exam.name=request.user
            #ExamForm.POST.get['name']=user.username
            exam.save()
            return HttpResponseRedirect(reverse('success_upload'))
    else:
        form = ExamForm()
    return render(request, 'basic_app/upload.html', {'form': form})

class ExamUpdateView(LoginRequiredMixin,UpdateView):#By default template_name=Exam_form.html
    login_url = '/login/'
    redirect_field_name = 'basic_app/successfull_submission.html'

    form_class = ExamForm

    model = Exam    #context_object_name are derived from model name
    #fields will be provided from form_class attr

class DraftListView(LoginRequiredMixin,ListView): #template_name is exam_draft_list.html
    login_url = '/login/'
    redirect_field_name = 'basic_app/successfull_submission.html'

    model = Exam    #context_object_name are derived from model name
    template_name='show_precised_list.html' #not working
    def get_queryset(self):         #in the Exam_draft_list only satisfied condition objects will be passed
        return Exam.objects.filter(published_date__isnull=True).order_by('file')


class ExamDeleteView(LoginRequiredMixin,DeleteView):#By default template_name=exam_confirm_delete.html
    model = Exam    #context_object_name are derived from model name
    #template_name='exam_confirm_delete.html'
    success_url = reverse_lazy('paper_draft_list')


@staff_member_required
def paper_publish(request, pk):
    paper = get_object_or_404(Exam, pk=pk)
    paper.publish()
    return redirect('paper_draft_list')

def download_item(request, pk):
    item = get_object_or_404(Exam, pk=pk)
    file_name, file_extension = 	 os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.file.file,
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.file.name)[:-(len(file_extension))], file_extension)
    return response



def register(request):

        registered=False

        if request.method=="POST":
            user_form=UserForm(data=request.POST)
            user_profile_form=UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and user_profile_form.is_valid():
                user=user_form.save(commit=False)
                user.is_active=False
                user.set_password(user.password)    #hashing
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                 })
                to_email = user_form.cleaned_data.get('email')
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()

                user_profile=user_profile_form.save(commit=False)
                user_profile.user=user
                user_profile.save()
                registered=True
                return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
            else:
                print(user_form.errors)
                print(user_profile_form.errors)
        else:
            user_form=UserForm()
            user_profile_form=UserProfileInfoForm()
        return render(request,'basic_app/registration.html',{'user_form':user_form,'user_profile_form':user_profile_form,'registered':registered})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activated successfully\n<a href="/" %}">Visit Site</a>')
    else:
        return HttpResponse('Activation link is invalid!This problem might be arised due slow internet connetion or link has been broken.Please check whether you can login with the account just created.If not please register again.')

#def show_precised_list(request):
#    return render(request,'basic_app/show_precised_list.html')

class PrescisedListView(ListView,LoginRequiredMixin):
    model=Exam

    template_name='show_precised_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['college'] = self.request.POST.get('college')
        context['branch'] = self.request.POST.get('branch')
        context['semester'] = self.request.POST.get('semester')
        return context

    def get_queryset(self):
        return Exam.objects.filter(published_date__lte=timezone.now(),college=self.kwargs['college'],type=self.kwargs['type'],branch=self.kwargs['branch'],semester=self.kwargs['semester']).order_by('-year','subject')


@login_required
def search_bar_view(request):
    if request.method=="POST":
        college=request.POST['college']
        branch=request.POST['branch']
        sem=request.POST['sem']
        return render(request,'basic_app/notes_or_paper.html',{'college':college,'branch':branch,'sem':sem})
    else:
        return render(request,'basic_app/exam_list.html')

class NotesOrPaperView(TemplateView,LoginRequiredMixin):
    template_name='basic_app/notes_or_paper.html'








def tryit(request):
    return render(request,'basic_app/try.html')








#############################################################
#############################################################
class UploadPaper(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='basic_app/successfull_submission.html'   #not working

    model=Exam
    template_name='upload.html'

    form_class=ExamForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.name = self.request.user.username
        instance.save()


    def get_success_url(self):
        return HttpResponseRedirect(reverse('success_upload'))
