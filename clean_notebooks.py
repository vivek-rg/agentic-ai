import os
import nbformat

def clean_notebooks(folder):
    for file in os.listdir(folder):
        if file.endswith(".ipynb"):
            path = os.path.join(folder, file)
            print(f"Cleaning {file}...")
            nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
            
            # Remove widgets metadata if present
            if "widgets" in nb.metadata:
                del nb.metadata["widgets"]
            
            # Optional: clear outputs
            for cell in nb.cells:
                if "outputs" in cell:
                    cell["outputs"] = []
                if "execution_count" in cell:
                    cell["execution_count"] = None
            
            nbformat.write(nb, path)

folder_path = "."  # current folder
clean_notebooks(folder_path)
print("All notebooks cleaned!")
