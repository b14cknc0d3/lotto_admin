from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import status

from rest_framework.response import Response

from .models import *
from .serializers import *
from .permissions import IsAuthenticated, IsAdmin, IsOwner


# Create your views here.

class UserViewSet(DynamicModelViewSet):
    permission_classes = (IsAdmin, IsAuthenticated)
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )


########################################################################################################################

# FOR SARCH ONE L VIEW
class OneLSearchViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = OneL
    queryset = OneL.objects.all()
    serializer_class = OneLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )


# For CRUD VIEWS OF ONE L
class OneLViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = OneL
    queryset = OneL.objects.all()
    serializer_class = OneLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )

    def create(self, request, *args, **kwargs):
        serializer = OneLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reseller=request.user)
            return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = OneL.objects.filter(reseller=request.user)
        serializer = OneLSerializer(queryset, many=True)
        return Response(serializer.data)


##################################################################

class FiveLSearchViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = FiveL
    queryset = FiveL.objects.all()
    serializer_class = FiveLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )


class FiveLViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = FiveL
    queryset = FiveL.objects.all()
    serializer_class = FiveLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )

    def list(self, request, *args, **kwargs):
        queryset = FiveL.objects.filter(reseller=request.user)
        serializer = FiveLSerializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = FiveLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reseller=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#############################################################################################################
class TwoLSearchViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = TwoL
    queryset = TwoL.objects.all()
    serializer_class = TwoLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )


#############################################################################


class TwoLViewSet(DynamicModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    model = TwoL
    queryset = TwoL.objects.all()
    serializer_class = TwoLSerializer
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )

    def list(self, request, *args, **kwargs):
        queryset = TwoL.objects.filter(reseller=request.user)
        serializer = FiveLSerializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = TwoLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reseller=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
###################################################################################################
