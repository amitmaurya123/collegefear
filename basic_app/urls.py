from django.conf.urls import url
from basic_app import views
urlpatterns=[

    url(r'^$',views.ExamListView.as_view(),name='exam_list'),
    url(r'^register/$',views.register,name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_account, name='activate'),

    url(r'^success_upload/$',views.SuccesUploadView.as_view(),name='success_upload'),


    url(r'^upload_file/',views.upload_paper,name='upload_paper'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^pdf/(?P<pk>\d+)/download/$', views.download_item, name='pdf_download'),
    #url(r'^cv/pdfs/(?P<filename>)/$', 'views.pdf_download',name="pdf_download"),
    #('ques_detail/<int:pk>/',views.ques_detail,name='ques_detail'),
    url(r'^drafts/paper/$', views.DraftListView.as_view(), name='paper_draft_list'),
    url(r'^paper/(?P<pk>\d+)/publish/$', views.paper_publish, name='paper_publish'),
    url(r'^paper/(?P<pk>\d+)/remove/$', views.ExamDeleteView.as_view(), name='paper_remove'),
    url(r'^paper/(?P<pk>\d+)/edit/$', views.ExamUpdateView.as_view(), name='paper_edit'),
    url(r'^search/bar/view',views.search_bar_view,name='search_bar_view'),
    url(r'^try/$',views.tryit,name='try'),

    url(r'^search/bar/(?P<type>[-\w]+)/show/(?P<college>[-\w]+)/(?P<branch>[-\w]+)/(?P<semester>\d+)/$',views.PrescisedListView.as_view(),name='show_precised_list'),
]
