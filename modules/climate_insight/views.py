from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import generate_risk_report

class RiskAssessmentView(APIView):
    """
    API view to trigger a climate risk assessment.
    """
    def post(self, request):
        location = request.data.get('location')
        risk_type = request.data.get('risk_type', 'general')
        
        if not location:
            return Response(
                {"error": "Location is required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            report = generate_risk_report(location, risk_type)
            return Response({
                "location": location,
                "risk_type": risk_type,
                "report": report
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
