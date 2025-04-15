def responder_bot(text):
    keywords = {
        "order": "Thank you for placing your order with us.",
        "support": "Our support team is here to assist.",
        "refund": "We have received your refund request. We will process it promptly.",
    }

    text = text.lower()
    responses = []  # Start empty!

    for keyword in keywords:
        if keyword in text:
            responses.append(keywords[keyword])

    if responses:
        return " ".join(responses)
    else:
        return "Thank you for your message. How can we assist you today?"
