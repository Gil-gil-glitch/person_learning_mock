import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NLPNode(Node):
    def __init__(self):
        super().__init__('nlp_node')

        self.subscription = self.create_subscription(
            String,
            'speech_text',
            self.callback,
            10)

        self.publisher = self.create_publisher(String, 'intent', 10)

    def callback(self, msg):
        intent_msg = String()
        intent_msg.data = "provide_name:John"
        self.get_logger().info("Parsed intent: provide_name")
        self.publisher.publish(intent_msg)

def main():
    rclpy.init()
    node = NLPNode()
    rclpy.spin(node)
    rclpy.shutdown()