from gjango.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="inidex")
]