import tabula

import translate_text as tt

# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("test.pdf", pages='all')
print(type(dfs))
for i in dfs:
    for j in i:
        j = tt.translate_string(j)
    print(i)
# # Read remote pdf into a list of DataFrame
# dfs2 = tabula.read_pdf(
#     "https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
#
# # convert PDF into CSV
# tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')
#
# # convert all PDFs in a directory
# tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')
