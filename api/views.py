from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q, Max

from .models import review
from .serializers import ReviewSerializer


# API view for searching the keyword
class ReviewSearchView(APIView):
    def post(self, request):
        print(request.data)
        searchText = request.data['searchText']

        try:
            # search the keyword in each column and return filtered queryset
            if (len(searchText) > 0):
                find = review.objects.filter(Q(productId__icontains=searchText) |
                                             Q(userId__icontains=searchText) |
                                             Q(profileName__icontains=searchText) |
                                             Q(helpfulness__icontains=searchText) |
                                             Q(score__icontains=searchText) |
                                             Q(time__icontains=searchText) |
                                             Q(summary__icontains=searchText) |
                                             Q(text__icontains=searchText)).distinct()
                # Filter out max score and max helpfulness from the query set
                if (len(find) > 0):
                    max_score = find.aggregate(Max('score'))
                    max_helpfulness = find.aggregate(Max('helpfulness'))
                    data = find.filter(
                        Q(score=max_score['score__max']) & Q(helpfulness=max_helpfulness['helpfulness__max']))
                    serializer = ReviewSerializer(data, many=True)
                    # Return the filtered data
                    return Response({'status': 200, 'find': serializer.data}, status=status.HTTP_200_OK)
                else:
                    # Return if keyword not found
                    return Response({'status': 404, 'responseMessage': 'Keyword not found'},
                                    status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'status': 400, 'responseMessage': 'Search text cannot be empty'},
                                status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'status': 404, 'responseMessage': 'Keyword not found'}, status=status.HTTP_404_NOT_FOUND)
