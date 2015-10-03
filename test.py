import cherrypy
 
# import our dna translation code
import translator
 
class MyWebApp:
     
    # the index method just displays a form
    def index(self):
        return """
            <form action="do_translate" method="get">
                Type your DNA sequence:
                <input type="text" name="dna_sequence"/>
                <input type="submit" value="Translate!">
            </form>
 
        """
    index.exposed = True   
 
    # here is the translate method
    def do_translate(self, dna_sequence):
        # use the imported function to carry out the translation
        # repr() gives us a string representation of a list
	dna_sequence = dna_sequence.replace(" ", "")
	print dna_sequence
        return repr(translator.translate_dna_3frame(dna_sequence))
    do_translate.exposed = True
 
cherrypy.quickstart(MyWebApp())
