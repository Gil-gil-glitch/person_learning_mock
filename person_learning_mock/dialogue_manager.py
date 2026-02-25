import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TaskPlanner(Node):
    def __init__(self):
        super().__init__('task_planner')

        self.sub_person = self.create_subscription(
            String,
            'tracked_person',
            self.person_callback,
            10)

        self.sub_intent = self.create_subscription(
            String,
            'intent',
            self.intent_callback,
            10)

        self.pub_dialogue = self.create_publisher(String, 'start_dialogue', 10)

    def person_callback(self, msg):
        self.get_logger().info("Approaching person")
        dialogue_msg = String()
        dialogue_msg.data = "greet_person"
        self.pub_dialogue.publish(dialogue_msg)

    def intent_callback(self, msg):
        self.get_logger().info(f"Received intent: {msg.data}")

def main():
    rclpy.init()
    node = TaskPlanner()
    rclpy.spin(node)
    rclpy.shutdown()