
import pdfplumber
import pandas as pd

# Function to extract the table from the PDF and return it as a DataFrame
def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Extract the first page (or any specific page)
        page = pdf.pages[0]  # Change page index if necessary
        table = page.extract_table()

        # Convert the table data to a pandas DataFrame
        df = pd.DataFrame(table[1:], columns=table[0])  # First row is header
    return df
 
# Function to get the middle two sections of the table
def get_middle_two_sections(df):
    # Assuming the table has an even number of columns, split the table into 4 sections
    # Adjust the number of columns based on the actual table structure
    num_columns = len(df.columns)
    
    if num_columns % 2 == 0:
        mid = num_columns // 2
        # Selecting middle two sections (columns)
        middle_section = df.iloc[:, mid-1:mid+1]
    else:
        print("Table has an odd number of columns, cannot extract exactly middle two sections.")
        middle_section = None
    
    return middle_section

# Path to your PDF file
pdf_path = 'your_pdf_file.pdf'
 
# Extract the table from the PDF
df = extract_table_from_pdf(pdf_path)

# Print the full table (optional)
print("Full Table:")
print(df)

# Get the middle two sections of the table
middle_section = get_middle_two_sections(df)

# Print the middle two sections
if middle_section is not None:
    print("Middle Two Sections of the Table:")
    print(middle_section)
