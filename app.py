def predict_action(command: str) -> str:
    command = command.lower()

    if "pick" in command or "grab" in command:
        return "机器人动作：抓取物体"
    elif "move" in command or "go" in command:
        return "机器人动作：移动到目标位置"
    elif "open" in command:
        return "机器人动作：打开物体"
    elif "put" in command or "place" in command:
        return "机器人动作：放置物体"
    else:
        return "机器人动作：暂时无法识别"


if __name__ == "__main__":
    print("=== Mini VLA Docker Demo ===")
    print("输入一条机器人指令，例如：pick up the red cup")
    print("输入 exit 退出程序")

    while True:
        user_input = input("\n请输入指令：")

        if user_input.lower() == "exit":
            print("程序结束")
            break

        action = predict_action(user_input)
        print(action)