def responder_bot(text):
    """
    Responder Bot

    A simple keyword-based auto-response function designed for use in customer service automation.

    This function analyzes the given input text for specific keywords ("order", "support", or "refund")
    and returns helpful automated responses based on the matched terms.

    Parameters:
    - text (str): A user message to analyze.

    Returns:
    - str: A combined response message related to any detected keywords.
           If no keywords are found, a default assistance message is returned.

    Example:
    >>> responder_bot("I need support and a refund.")
    'Our support team is here to assist. We have received your refund request. We will process it promptly.'

    Skills demonstrated:
    - String processing and normalization
    - Keyword detection using dictionaries
    - Conditional logic and control flow
    """
    
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
