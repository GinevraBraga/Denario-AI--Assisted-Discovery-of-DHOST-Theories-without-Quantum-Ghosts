from denario import Denario, Journal

folder = "./"
INPUT_DATA_DIR = "./"

# set AstroPilot and input text
astro_pilot = Denario(project_dir=folder)
astro_pilot.set_data_description(f"{folder}/horndeski_prompt.md")

# Generate a research idea from the input text
astro_pilot.get_idea_fast(llm='gemini-2.5-flash', verbose=False)
#astro_pilot.get_idea()

# Generate a research plan to carry out the idea
astro_pilot.get_method_fast(llm="gemini-2.5-pro", verbose=False)
#astro_pilot.get_method()

# Follow the research plan, write and execute code, make plots, and summarize the results
astro_pilot.get_results(engineer_model='gemini-2.5-pro', researcher_model='gemini-2.5-pro')
#astro_pilot.get_results()

# Write a paper with [APS (Physical Review Journals)](https://journals.aps.org/) style
astro_pilot.get_paper(journal=Journal.AAS, llm='gemini-2.5-flash', add_citations=False)

