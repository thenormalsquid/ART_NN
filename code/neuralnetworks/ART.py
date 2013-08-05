import numpy


"""
Helper functions
"""
def column(matrix, i):
    return [row[i] for row in matrix]




#perhaps make an ART class in which all of these functions are methods
class ArtBase(object):

    def __init__(self, oinput, weight):
        self.input = oinput
        self.weight = weight

    #may have to change to numpy array if data is large
    def category_activation(self, bias):
        #weight is a list of lists which converts to a matrix 
        #oinput is a vector, which is a list

        """
        ART_Activate_Categories    Activates the categories in an ART network.
           CATEGORYACTIVATION = ART_Activate_Categories(INPUT, WEIGHT, BIAS)
            This function returns a vector of category activations for the given
            input vector, weight matrix, and bias value.
         
            The input parameters are as follows:
            The INPUT is a vector of size NumFeatures that contains the input
            signal into the network. 
            The WEIGHT is a matrix of size NumFeatures-by-NumCategories which holds the weights of the network.
            The BIAS is the constant that is used to differentiate between very
            similar category activation values. The length of the INPUT vector
            must equal the number of rows in the WEIGHT matrix, and the BIAS
            value must be within the range [0, 1] (although values very near
            0 are best).

            The return parameter is as follows:
            The CATEGORYACTIVATION is a vector of size NumCategories that
            holds the activation value for each category. Returns an array.
         """
        num_categories = len(self.weight[0])
        if len(self.input) != len(self.weight):
            return 'The length of the input and rows of the weights do not match.'
        elif bias < 0 or bias > 1:
            return "The bias must be within the range of [0,1]"
        else:
            """
            Calculate the activation for each category.
            This is done according to the following equation:
            Activation(j) = |Input^Weight(j)| / (bias + |Weight(j)|)
            """
            self.category_activation = []
            #weight should be numpy matrix already, but if not, we convert here
            self.weight = numpy.matrix(weight)
            for j in xrange(num_categories):
                arr = self.weight[:,j].tolist()
                col = column(arr,0)
                match_vector = min(self.input, col)
                weight_length = sum(col)
                self.category_activation.append(sum(match_vector)/(bias + weight_length))
            return self.category_activation


        def add_new_category(self):
            """
            Can be called explicitly? ... 
             ART_Add_New_Category    Adds a new category to the given weight matrix.
            RESIZEDWEIGHT = ART_Add_New_Category(WEIGHT)
            This function returns a new weight matrix which is identical to the
            given weight matrix except that it contains one more category which
            is initialized to all 1's.
         
            The input parameter is as follows:
            The WEIGHT is a matrix of size NumFeatures-by-NumCategories which
            holds the weights of the network.
            The return parameter is as follows:
            The RESIZEDWEIGHT is a matrix of size NumFeatures-by-NumCategories+1
            which holds the weights of the old matrix plus a new category of all
            values of 1.
             """
            self.weight = [row.append(1) for row in self.weight]
            return self.weight


        def calculate_match(self, weight_vector):
            """
            Perhaps there is a function that returns a weight_vector this can be applied to
            ART_Calculate_Match    Calculates the match value of an input to a category.
            MATCH = ART_Calculate_Match(INPUT, WEIGHTVECTOR)
            This function returns a value which represents the amount of match
            between the given input and the given category.
         
            The input parameters are as follows:
            The INPUT is a vector of size NumFeatures that contains the input
            signal into the network. The WEIGHTVECTOR is a matrix of size 
            NumFeatures which holds the weights of the network for a given
            category. The length of the INPUT vector must equal the length of
            the WEIGHTVECTOR.

            The return parameter is as follows:
            The MATCH is a measure of the degree of match between the input
            and the current category.
            """
            #weight_vector is a single row matrix
            num_features = len(self.input)
            if num_features == len(weight_vector):
                #Match = |Input^WeightVector| / |Input|
                match_vector = min(self.input, weight_vector)
                input_length = sum(self.input)
                if input_length == 0:
                    match = 0
                else:
                    match = sum(match_vector) / input_length
                return match
            else:
                return "Input and weight_vector lengths don't match"


def categorize(art_network, data):
    """
     ART_Categorize    Uses an ART network to categorize the given input data.
    CATEGORIZATION = ART_Categorize(ART_NETWORK, DATA)
    This function uses an ART network to categorize the given input data with 
    the specified vigilance parameter. Each sample of the data is presented to
    the network, which categorizes each sample. The function returns the 
    categorization of each sample. If the categorization of the sample requires
    that a new category be created, the category for that sample is set to -1.

    The input parameters are as follows:
    The ART_NETWORK is the trained ART network. It should be created with
    ART_Create_Network(). -> most likely object

    The DATA is the categorization data to be presented
    to the network. It is a matrix of size NumFeatures-by-NumSamples. 

    The return parameters are as follows:
    The CATEGORIZATION is a vector of size NumSamples that holds the 
    category in which the ART network placed each sample. -> returns list
    """
    #num_features will go into an art network object > may need to make the object
    if num_features == art_network.num_features:
        if art_network.vigilance <= 0 or art_network.vigilance > 1:
            return "The range must be (0,1)"
        else:



#tests
if __name__ == "__main__":
    oin = [1,2,3,4]
    weight = [[3,5,1,2],[4,5,2,1],[1,2,3,3],[2,3,3,2]]
    bias = 0.1
    print category_activation(oin, weight, bias)