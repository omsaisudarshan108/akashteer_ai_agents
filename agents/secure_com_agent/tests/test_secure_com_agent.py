import unittest
from agents.secure_com_agent.secure_com_agent import SecureComAgent

class TestSecureComAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SecureComAgent()

    def test_send_message(self):
        result = self.agent.send_message(sender_agent_id="agent_A", recipient_agent_id="agent_B", message_content="Hello World")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_receive_message_with_sent_message(self):
        self.agent.send_message(sender_agent_id="agent_C", recipient_agent_id="agent_D", message_content="Test Data")
        messages = self.agent.receive_message(recipient_agent_id="agent_D")
        self.assertIsInstance(messages, list)
        self.assertTrue(len(messages) > 0)
        self.assertIn('content', messages[0])
        self.assertIn('sender', messages[0])
        self.assertIn('timestamp', messages[0])
        self.assertNotIn("no_new_messages", messages[0]['content'])


    def test_receive_message_no_message(self):
        messages = self.agent.receive_message(recipient_agent_id="agent_E_no_message")
        self.assertIsInstance(messages, list)
        self.assertTrue(len(messages) > 0) # Expecting the default message
        self.assertIn('content', messages[0])
        self.assertIn('encrypted_payload_no_new_messages', messages[0]['content'])

if __name__ == '__main__':
    unittest.main()
