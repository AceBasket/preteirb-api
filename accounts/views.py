from .serializers import AccountSerializer
from rest_framework import generics, permissions, status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiTypes, inline_serializer


class CreateAccountView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Create a new user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate a token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Return the token as a response
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)


class ManageAccountView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogInView(generics.GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        responses={
            status.HTTP_200_OK: inline_serializer(
                name='TokenResponse',
                fields={
                    'token': serializers.CharField(),
                    'id': serializers.CharField(),
                    'username': serializers.CharField()
                }
            ),
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name='ErrorResponse',
                fields={
                    'error': serializers.CharField()
                }
            )
        },
    )
    def post(self, request, *args, **kwargs):
        """ Log in a user """
        # Get the username and password from request
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated
        if user:
            # Generate a token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Return the token as a response
            return Response({
                'token': token.key,
                'id': user.pk,
                'username': user.username
            }, status=status.HTTP_200_OK)
        else:
            # Return an error message
            return Response({
                'error': 'Wrong Credentials'
            }, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(generics.GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=None,
        responses={204: None},
    )
    def post(self, request, *args, **kwargs):
        """ Log out a user """
        # Get the user from request
        user = request.user

        # Delete the token of the user
        Token.objects.filter(user=user).delete()

        # Return a success message
        return Response(status=status.HTTP_204_NO_CONTENT)
