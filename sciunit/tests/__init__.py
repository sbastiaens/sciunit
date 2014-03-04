"""SciUnit tests live in this module."""
<<<<<<< HEAD
import sciunit
import sciunit.capabilities
from sciunit.comparators import ZComparator # Comparators.  
from sciunit.comparators import Z_to_Boolean # Converters.  
from sciunit.scores import BooleanScore # Scores.  

###############
# Dummy Tests #
###############

class PositivityTest(sciunit.Test):
	"""Checks whether the model produces a positive value."""

	required_capabilities = (sciunit.capabilities.ProducesNumber,)

	def _judge(self, model):
		"""The main testing function."""
		data = model.produce_data()
		return BooleanScore(self, model, data > 0, {"data": data})

##############
# Real Tests #
##############

class ComparatorTest(sciunit.Test):
	"""A test class that encourages the use of Comparators."""
	
	def __init__(self,comparator):
		self._comparator = comparator
		"""Comparator class from sciunit.Comparators."""

	def compare(self,model):
		return self.comparator.compare(self,model)

	def set_comparator(self,model,comparator=None):
		if comparator is None:
			comparator = self._comparator
		self.comparator = comparator() # Instantiate the comparator.  
		assert sciunit.Comparator in self.comparator.__class__.mro()


class StandardTest(ComparatorTest):
	"""A base class with logic common to many tests."""
	
	def __init__(self,reference_data,model_args,comparator):
		"""reference_data are summary statistics of reference data.
		model_args are arguments used by the model to run 
		or fit itself."""
		ComparatorTest.__init__(self,comparator)
		self.reference_data.update(reference_data) # Store reference data. 
		self.model_args.update(model_args) # Store model arguments.  
		self.required_capabilities += (sciunit.capabilities.Runnable,)
		
	desc = "N/A"
	"""A test description"""
		
	def pre_checks(self,model):
		"""Checks that the test has everything it needs to run properly."""
		self.set_comparator(model)

	def _judge(self,model):
		"""Runs the test and returns a score."""
		self.pre_checks(model)
		model.run() # Run the model. Implementation guaranteed by Runnable capability.  
		output_data = self.get_model_data(model) # Get the output data.  
		return self.generate_score(model,output_data)

	def get_reference_stats(self):
		"""Takes test reference data and extract reference stats 
		that the Comparator will understand."""
		return {key:value for key,value in self.reference_data.items()} 
		# This example is trivial. In subclasses there would be some 
		# processing or subsetting of the reference_data.

	def get_output_data(self,model):
		"""Extracts and returns a dict of raw data from the model 
		using that model's Capabilities."""
		model_data = {} 
		# Get model_data from the model. 
		# A more detailed implementation is expected in each model.  
		return model_data

	def get_output_stats(self,output_data):
		"""Take model output data and extracts output stats 
		that the Comparator will understand."""
		return {key:value for key,value in output_data.items()} 
		# This example is trivial. In subclasses there would be some 
		# processing or subsetting of the output_data.
		
	def generate_score(self,model,output_data):
		"""Generate a score using some Comparator applied to the model's output data."""
		model.output_stats = self.get_output_stats(output_data)
		self.reference_stats = self.get_reference_stats()
		score = self.compare(model)
		score.related_data = {'output_stats':model.output_stats,
						      'reference_stats':self.reference_stats}
		return score

class ZTest(StandardTest):
	"""A Z-score test."""
	
	def __init__(self,
			     reference_data={},
			     model_args={},
			     threshold=2):
		print "Instantiating a test of %s" % self.desc
		StandardTest.__init__(self,reference_data,model_args,ZComparator)
		self.conversion_params = {'thresh':threshold}
		"""-2 < Z-score < 2 required to get a BooleanScore of True, 
		i.e. to pass the test."""
 
	comparator = ZComparator
	"""Compare the model to the reference and generate a Z-score."""

	converter = Z_to_Boolean
	"""Convert from Z-score (generated by ZComparator) to Boolean score."""  
	
=======
>>>>>>> bf3616fa571baee622a4fa846477760d02179765
