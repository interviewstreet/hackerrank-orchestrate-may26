from dotenv import load_dotenv
from pathlib import Path
import os
import click

from llm.llm import LLM
from llm.template import template

from embeddings.embeddings import Data, Embeddings
from loader.loader import walk_data_files, open_ticket_file
from writer.writer import write_output, parse_response

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
data_folder_path = os.environ.get("DATA_FOLDER")
support_ticket_file_path = os.environ.get("SUPPORT_TICKETS")
output_file_path = os.environ.get("OUTPUT_FILE")

if api_key is None:
    raise ValueError(f"api key does not exist {api_key}")

if data_folder_path is None:
    raise ValueError(f"invalid data folder path {data_folder_path}")

if support_ticket_file_path is None:
    raise ValueError(f"invalid support_tickets file path {support_ticket_file_path}")

if output_file_path is None:
    raise ValueError(f"No output_file_path provided {output_file_path}")

BASE = Path(__file__).parent.parent
# sample data/support ticket folder/files
data_folder = BASE / data_folder_path
support_tickets_file = BASE / support_ticket_file_path
output_file = BASE / output_file_path

# initiate the embeddings class
embeddings_class = Embeddings()

# initiate the llm class
llm_class = LLM(api_key)

# get data files
data_files = walk_data_files(str(data_folder))
# get support_tickets
support_tickets = open_ticket_file(str(support_tickets_file))

# main command  
@click.command()
def run():
    responses = []
    # load or create embeddings from the data files
    embeddings_class.load_or_create_embeddings(data_files)
    # for each support ticket in the support tickets, create a match list with the embeddings
    for ticket in support_tickets:
        # get a sorted list of similarity scores with data with a limit (default 10)
        sims: list[tuple[float, Data]] = embeddings_class.match_support_ticket(ticket)
        # unite all the data in a string to pass into the LLM
        data_string = ""
        for pair in sims:
            data_string += f"{pair[1]}\n"
        # get a response for each query from the llm
        query = f"{ticket.get('issue', '')} {ticket.get('company', '')} {ticket.get('subject', '')}"
        res = llm_class.get_response(template(query, data_string))
    #   # parse each response into a json object and push it into the responses
        responses.append(parse_response(res))
    # write responses to a csv file
    write_output(output_file, responses)

if __name__ == "__main__":
    run()
