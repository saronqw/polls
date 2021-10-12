from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from PollsApp.models import Poll, Question, Vote, Choice, QuestionType
from PollsApp.permissions import IsAdminOrReadOnly
from PollsApp.serializers import PollSerializer, QuestionSerializer, VoteSerializer, ChoiceSerializer, \
    QuestionTypeSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False)
    def get_active_polls(self, request):
        datetime_now = timezone.now()
        polls = self.get_queryset().filter(start_date__lte=datetime_now, end_date__gte=datetime_now)
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuestionTypeViewSet(viewsets.ModelViewSet):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class UserAnswersView(APIView):

    def get(self, request):
        user = request.user.id
        questions = Vote.objects.all()\
            .values('id', 'user', 'choice__text', 'text', 'question_id', 'question__poll_id')\
            .filter(user_id=user)
        return Response(questions)
