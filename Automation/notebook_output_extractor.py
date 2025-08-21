import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import sys
import base64
from pathlib import Path

def save_notebook_output_to_md(notebook_path, markdown_path):
    """
    Executes a Jupyter Notebook and saves only the cell outputs to a Markdown file.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        print(f"Executing notebook: {notebook_path}...")
        notebook_dir = Path(notebook_path).parent
        preprocessor = ExecutePreprocessor(timeout=600, kernel_name='python3')
        executed_nb, _ = preprocessor.preprocess(nb, {'metadata': {'path': str(notebook_dir)}})
        print("Execution complete.")

        md_outputs = []
        for cell in executed_nb.cells:
            if cell.cell_type == 'code' and hasattr(cell, 'outputs'):
                for output in cell.outputs:
                    if output.output_type == 'stream':
                        md_outputs.append(f"```text\n{output.text.strip()}\n```")
                    elif output.output_type == 'execute_result':
                        if 'text/html' in output.data:
                            md_outputs.append(output.data['text/html'])
                        elif 'text/plain' in output.data:
                            md_outputs.append(f"```text\n{output.data['text/plain'].strip()}\n```")
                    elif output.output_type == 'display_data':
                        if 'image/png' in output.data:
                            png_base64 = output.data['image/png']
                            md_outputs.append(f'![png](data:image/png;base64,{png_base64})')
                        elif 'text/html' in output.data:
                            md_outputs.append(output.data['text/html'])
                        elif 'text/plain' in output.data:
                            md_outputs.append(f"```text\n{output.data['text/plain'].strip()}\n```")
                    elif output.output_type == 'error':
                        traceback = "\n".join(output.traceback)
                        error_message = f"**Error:** {output.ename}\n```bash\n{traceback}\n```"
                        md_outputs.append(error_message)

        print(f"Writing outputs to: {markdown_path}...")
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(f"# Output of `{notebook_path}`\n\n")
            f.write("\n\n---\n\n".join(md_outputs))
        
        print("Successfully saved notebook outputs to markdown file.")

    except FileNotFoundError:
        print(f"Error: The file '{notebook_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_output.py <input_notebook.ipynb> <output_markdown.md>")
        sys.exit(1)
    
    save_notebook_output_to_md(sys.argv[1], sys.argv[2])