from graph import graph

def run_agent(user_input):
    result = graph.invoke({"input": user_input})
    return result


if __name__ == "__main__":
    print("🤖 Multi-Agent AI System")

    user_input = input("Enter your task: ")

    result = run_agent(user_input)

    print("\n🧠 PLAN:\n")
    print(result["plan"])

    print("\n🔧 TOOL USED:", result["tool"])

    print("\n✅ OUTPUT:\n")
    print(result["output"])