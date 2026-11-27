
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer,RegisterSerializer
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema
from drf_spectacular.openapi import OpenApiParameter

@extend_schema(
    parameters=[
        OpenApiParameter(
            name='page',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Page number',
        )
    ]
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ticket_list(request):

    if request.method == 'GET':

        priority = request.query_params.get('priority')
        ticket_status = request.query_params.get('status')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        tickets = Ticket.objects.filter(user = request.user).order_by('id')

        if priority:
            tickets = tickets.filter(priority=priority)

        if ticket_status:
            tickets = tickets.filter(status=ticket_status)

        if search:
            tickets = tickets.filter(title__icontains=search)   

        allowed_ordering = ['title', 'priority', 'status']

        if ordering and ordering.lstrip('-') in allowed_ordering:
            tickets = tickets.order_by(ordering)   

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(tickets, request)

        serialized = TicketSerializer(page, many=True)
        return paginator.get_paginated_response(serialized.data)      

        

    elif request.method == 'POST':

        ticket = request.data
        
        serialized = TicketSerializer(data=ticket)

        if serialized.is_valid():
            serialized.save(user = request.user)
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def ticket_detail(request, id):

    ticket = get_object_or_404(Ticket, id=id, user=request.user)

    if request.method == 'GET':

        serialized = TicketSerializer(ticket)
        return Response(serialized.data)

    elif request.method == 'PATCH':

        serialized = TicketSerializer(ticket,data=request.data,partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_200_OK)

        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        ticket.delete()
        return Response({'msg': 'Ticket deleted successfully'})


@api_view(['POST'])
def register_user(request):

    user = request.data
    serialized = RegisterSerializer(data=user)

    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data,status=status.HTTP_201_CREATED)

    return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)