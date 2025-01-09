import re 
from pathlib import Path

##nu har vi gjort i Jupyter notebook. Här är det enkelt.
## Men här i ett script blir det klurigare pga paths. 
## Run knappen utgår från var vi är i terminalen. Så det är risky?
## Ska vi basera programmet istället relativt var filen finns. I jupyter notebook så löstes detta automatiskt
## detta måste fixa. Använda bibliteket pathlib.

#print("This is the path of this script")
#print(Path(__file__)) # här får vi en absolut path till detta script
## från denna absoluta path kan vi leta fram vår text.

#print("This is the path of this script")
#print(Path(__file__).parent / "data" / "ml_text_raw.txt") # Denna pathen MOTSVARAR det v gjorde i Jupyter Notebook
data_path = Path(__file__).parent / "data" #gör det till en variabel och använder det nedan

with open(data_path / "ml_text_raw.txt", 'r') as file:
    raw_text = file.read()

text_fixed_spacing = re.sub(r"\s+", " ",raw_text)

#then use same code as in Notebook to clean it further
text_fixed_spacing.split(". ")
sentences = [text.strip().capitalize() for text in text_fixed_spacing.split(".")]
sentences = sentences[:-1]

cleaned_text = "\n".join(sentences)

with open("data/cleaned_ml_text_script.txt", "w") as file:
    file.write(cleaned_text)