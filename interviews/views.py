from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CandidateResponse, InterviewResponse

# Interview questions list
QUESTIONS = [
    "Can you tell me about yourself?",
    "Why are you interested in this role?",
    "What programming languages do you know?",
    "Describe a project you've worked on.",
    "What are your career goals?",
    "Are you familiar with version control like Git?",
    "Do you prefer working in a team or independently?",
    "How do you handle tight deadlines?",
    "Do you have any questions for us?"
]

@api_view(['POST'])
def webhook(request):
    data = request.data

    session_id = data.get("session_id")
    user_input = data.get("user_message", "").strip()

    if not session_id or not user_input:
        return Response({"error": "Missing session_id or user_message"}, status=400)

    # Count how many answers have been recorded for this session
    answered_count = CandidateResponse.objects.filter(session_id=session_id).count()

    # Save candidate's previous answer if it's not the first greeting
    if answered_count > 0 and answered_count <= len(QUESTIONS):
        CandidateResponse.objects.create(
            session_id=session_id,
            question=QUESTIONS[answered_count - 1],
            answer=user_input
        )

    # Determine the next question or finish the interview
    if answered_count < len(QUESTIONS):
        next_question = QUESTIONS[answered_count]
        conversation_end = False
    else:
        next_question = "Thank you! The interview is complete. We will contact you soon."
        conversation_end = True

    # Save bot response for this turn
    InterviewResponse.objects.create(
        session_id=session_id,
        user_message=user_input,
        response=next_question,
        conversation_end=conversation_end
    )

    return Response({
        "response": next_question,
        "conversation_end": conversation_end
    })
