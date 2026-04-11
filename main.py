from app.workflow.graph_setup import create_workflow

def main():
    app = create_workflow()
    initial_state = {"messages": []}
    result = app.run(initial_state)
    print(result)
    
if __name__ == "__main__":
    main()
