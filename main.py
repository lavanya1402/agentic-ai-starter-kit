import logging
from agents.first_agent import run_first_agent
from tools.text_analyzer import basic_text_stats

logging.basicConfig(
    filename="logs/agent_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    user_problem = input("Describe your business or technical problem: ")

    logging.info("User problem received.")
    logging.info(user_problem)

    stats = basic_text_stats(user_problem)
    logging.info(f"Input text stats: {stats}")

    result = run_first_agent(user_problem)

    logging.info("Agent response generated successfully.")
    print("\nStructured Agent Response:\n")
    print(result.model_dump_json(indent=2))
