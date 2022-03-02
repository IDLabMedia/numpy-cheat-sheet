

f = open("cheat-sheet.md", "w")

def func_table(fname, desc, note=None, see_also=None):
    desc = desc.replace("np.array", "`np.array`")
    LINK = "https://numpy.org/doc/stable/reference/generated/numpy.%s.html"
    f.write((" | [`np.%s()`](" + LINK + "){target=_blank} | %s") % (fname, fname, desc))
    if note is not None:
        f.write("<br/>*Opmerking*: %s" % note)
    if see_also is not None:
        if not isinstance(see_also, list):
            see_also = [see_also]
        f.write("<br/>*Zie ook*: %s" % ", ".join([("[`np.%s()`](" + LINK + "){target=_blank}") % (x, x) for x in  see_also]))
    f.write("\n")

func = func_table

def for_more(link):
    f.write("Voor meer in deze categorie, vind [het overzicht hier](%s){target=_blank}.\n" % link);

def section(header):
    f.write("\n## %s\n" % header)
def subsection(header):
    f.write("\n### %s\n" % header)

def table_header():
    f.write("| Functie | Beschrijving |\n")
    f.write("|---------|--------------|\n")

section("Basis")

subsection("Hulpfuncties")
table_header()
func("squeeze", "Verandert de shape van een np.array zodat alle dimensies met lengte 1 verdwijnen.")
func("expand_dims", "Voert een nieuwe dimensie van lengte 1 in op de gewenste plaats van de shape van een np.array.",
        note="Dit kan ook met gebruik van `None` in de subscript operator.")

subsection("Wiskundige reducties")
table_header()
func("sum", "Sommeert getallen in een np.array over alle of enkele assen.", note="Bij gebruik lees de _Note_ in de documentatie.")
func("mean", "Berekent het gemiddelde van getallen in een np.array over alle of enkele assen.")
func("var", "Berekent de variantie van getallen in een np.array over alle of enkele assen.")
func("std", "Berekent de standaardafwijking van getallen in een np.array over alle of enkele assen.")
func("count_nonzero", "Telt aantal niet-nul elementen in een np.array over alle of enkele assen.")
func("argmin", "Zoekt de positie het kleinste getal in een np.array over alle of enkele assen.")
func("argmax", "Zoekt de positie het grootste getal in een np.array over alle of enkele assen.")
func("amax", "Geeft het grootste getal over alle of enkele assen.", note="Niet te verwarren met `np.maximum()`.", see_also="maximum")
func("amin", "Geeft het kleinste getal over alle of enkele assen.", note="Niet te verwarren met `np.minimum()`.", see_also="minimum")
for_more("https://numpy.org/doc/stable/reference/routines.math.html")

subsection("Wiskundige berekeningen (elementsgewijs)")
table_header()
func("square", "Berekent het kwadraat van een np.array elementsgewijs.")
func("sqrt", "Berekent de vierkantswortel van een np.array elementsgewijs.")
func("power", "Berekent een machtsverheffing van een np.array elementsgewijs.")
func("maximum", "Berekent elementsgewijs de grootste waarde van de twee inputs.")
func("minimum", "Berekent elementsgewijs de kleinste waarde van de twee inputs.")
func("clip", "Combinatie van `np.maximum` en `np.minimum`: Klemt elementsgewijs de input tussen twee grenzen.")
for_more("https://numpy.org/doc/stable/reference/routines.math.html")

subsection("Array creatie")
table_header()
func("zeros", "Produceert een np.array gevuld met nullen van de gegeven grootte.", see_also="zeros_like")
func("ones", "Produceert een np.array gevuld met énen van de gegeven grootte.", see_also="ones_like")
func("arange", "Genereert een rij getallen met geven startpunt, stapgrootte, en maximale waarde.")
func("linspace", "Genereert een rij getallen met geven startpunt, eindpunt, en aantal gewenste waarden.", note="Werkt ook op tuples.")
for_more("https://numpy.org/doc/stable/reference/routines.array-creation.html")

subsection("Arrays samenvoegen en herhalen")
table_header()
func("stack", "Stapelt verschillende np.arrays samen langsheen een nieuwe dimensie.")
func("concatenate", "Plakt verschillende np.arrays samen langsheen een bestaande dimensie.")
func("tile", "Herhaalt éénzelfde np.array een gegeven aantal keer over bestaande en nieuwe dimensies.", see_also="repeat")
for_more("https://numpy.org/doc/stable/reference/routines.array-manipulation.html")

section("Logische functies")
subsection("Waarheid test functies")
table_header()
func("all", "Controlleert of alle waarden in de np.array gelijk zijn aan `True`.")
func("any", "Controlleert of minstens één waarde in de np.array gelijk zijn aan `True`.")

subsection("Logische operatoren")
table_header()
func("logical_and", "Voert de logische AND operator uit elementsgewijs op de twee inputs.")
func("logical_or", "Voert de logische OR operator uit elementsgewijs op de twee inputs.")
func("logical_xor", "Voert de logische XOR operator uit elementsgewijs op de twee inputs.")
func("logical_not", "Voert de logische NOT operator uit elementsgewijs op de input.")

subsection("Vergelijkingen")
table_header()
func("equal", "Vergelijkt de twee inputs elementsgewijs met de gelijkheids operator.", see_also="not_equal")
func("less", "Vergelijkt de twee inputs elementsgewijs met de kleiner-dan operator.", see_also="less_equal")
func("greater", "Vergelijkt de twee inputs elementsgewijs met de groter-dan operator.", see_also="greater_equal")

section("Lineaire Algebra")
table_header()
func("linalg.inv", "Berekent inverse van een vierkante matrix.", "Werkt op de 2 binnenste dimensies.")
func("linalg.matmul", "Berekent matrix-matrix vermenigvuldiging", "Werkt op de 2 binnenste dimensies van beide inputs.")
for_more("https://numpy.org/doc/stable/reference/routines.linalg.html")

f.close()

import subprocess
process = subprocess.run(["pandoc", "-f", "markdown_phpextra", "-t", "html5", "--standalone", "--css", "pandoc_dark.css", "--metadata", "title='NumPy cheat sheet'", "--toc", "--self-contained", "-o", "cheat-sheet.html", "cheat-sheet.md"])
print("exit-code", process.returncode)

subprocess.run(["mkdir", "-p", "docs/"])
subprocess.run(["cp", "cheat-sheet.html", "docs/index.html"])
