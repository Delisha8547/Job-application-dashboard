def classify_email(text):
    text = text.lower()

    rejection_keywords = [
        "unfortunately",
        "we regret",
        "not moving forward",
        "not successful",
        "unsuccessful",
        "decided to proceed with other candidates",
        "position has been filled",
        "after careful consideration",
        "we will not be progressing",
        "we won't be progressing"
    ]

    assessment_keywords = [
        "assessment",
        "coding test",
        "online test",
        "technical test",
        "assignment"
    ]

    interview_keywords = [
        "interview",
        "schedule a call",
        "meeting",
        "video call",
        "discussion"
    ]

    if any(keyword in text for keyword in rejection_keywords):
        return "Rejected"
    elif any(keyword in text for keyword in assessment_keywords):
        return "Assessment"
    elif any(keyword in text for keyword in interview_keywords):
        return "Interview"
    else:
        return "No Response"

