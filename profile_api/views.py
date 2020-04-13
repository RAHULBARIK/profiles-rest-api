from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiview(APIView):
    """Test API View"""

    def get(self, response, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get,post,put,patch,delete)",
            "Is a similar to a traditional Django VIew",
            "Gives you most control over you application logic",
            "Is mapped manually URLs",
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
