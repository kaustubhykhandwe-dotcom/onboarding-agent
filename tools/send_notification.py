"""
send_notification stub
Pre-built for the Onboarding Agent session.
Do not modify during the live build.

Simulates sending Slack messages and emails.
Always succeeds. Prints to terminal so the audience sees the notification content.
"""

from datetime import datetime


def send_notification(recipient: str, channel: str, subject: str, body: str) -> dict:
    """
    Send a notification via the specified channel.

    In production, this would call:
      - Slack API for slack channel
      - SES or SendGrid for email channel
      - WhatsApp Business API for whatsapp channel

    For the session, this just prints what would be sent.

    Args:
        recipient: email address, Slack user ID, or phone number
        channel:   one of 'email', 'slack', 'whatsapp'
        subject:   subject line for email, ignored for other channels
        body:      message body

    Returns:
        dict with status, channel, recipient, and timestamp
    """
    timestamp = datetime.now().isoformat() + "Z"

    print(f"\n  == NOTIFICATION via {channel.upper()} ==")
    print(f"     To:        {recipient}")
    if channel == 'email' and subject:
        print(f"     Subject:   {subject}")
    print(f"     Body:      {body}")
    print(f"     Timestamp: {timestamp}")
    print(f"  == NOTIFICATION SENT ==\n")

    return {
        "status": "SUCCESS",
        "channel": channel,
        "recipient": recipient,
        "timestamp": timestamp
    }


if __name__ == '__main__':
    result = send_notification(
        recipient="priya.sharma@meridian.com",
        channel="email",
        subject="Action required: Complete onboarding policies",
        body="Hi Priya, please complete your code of conduct acknowledgement to proceed with onboarding."
    )
    print(result)
