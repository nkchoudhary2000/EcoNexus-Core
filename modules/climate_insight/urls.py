from django.urls import path
from .views import RiskAssessmentView

urlpatterns = [
    path('assess-risk/', RiskAssessmentView.as_view(), name='assess_risk'),
]
