import datetime

class SecureComAgent:
    def __init__(self):
        self.messages = {}  # Stores messages, keyed by recipient_agent_id

    def send_message(self, sender_agent_id: str, recipient_agent_id: str, message_content: str) -> str:
        """
        Simulates sending an encrypted message.

        Args:
            sender_agent_id: The ID of the sending agent.
            recipient_agent_id: The ID of the recipient agent.
            message_content: The content of the message.

        Returns:
            A confirmation message.
        """
        if recipient_agent_id not in self.messages:
            self.messages[recipient_agent_id] = []

        # Simulate encryption by adding a prefix
        encrypted_payload = f"encrypted_payload_{message_content[:10]}..."
        
        self.messages[recipient_agent_id].append({
            'sender': sender_agent_id,
            'content': encrypted_payload,
            'timestamp': datetime.datetime.now().isoformat()
        })
        return f"Message from {sender_agent_id} to {recipient_agent_id} sent securely."

    def receive_message(self, recipient_agent_id: str) -> list:
        """
        Simulates receiving encrypted messages for an agent.

        Args:
            recipient_agent_id: The ID of the recipient agent.

        Returns:
            A list of received messages.
        """
        # Return messages for the recipient and clear them (as if they've been read)
        received = self.messages.get(recipient_agent_id, [])
        if recipient_agent_id in self.messages:
            del self.messages[recipient_agent_id] # Or mark as read
        
        if not received: # Return a predefined message if none are available
            return [{
                'sender': 'system_default',
                'content': 'encrypted_payload_no_new_messages...',
                'timestamp': datetime.datetime.now().isoformat()
            }]
        return received
