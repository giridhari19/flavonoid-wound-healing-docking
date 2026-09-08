from pathlib import Path
from rdkit import Chem
from tkinter import filedialog
import tkinter as tk
root=tk.Tk()
root.withdraw()

inp=Path(filedialog.askdirectory( title="select sdfs directory"))
result=inp.parent / "pdbs"
(result).mkdir(parents=True, exist_ok=True)

sdfs=list(inp.glob("*.sdf"))


for sdf in sdfs:
	name=sdf.stem
	supplier=Chem.SDMolSupplier(sdf)
	for i,mol in enumerate(supplier):
		if mol is None:
			print(f"Warning! Couldn't read the {i}th molecule in {name}")
			continue
		Chem.MolToPDBFile(mol, result / (name + ".pdb"))
		

	


