"""Module providing an example of the Template Method design pattern."""


from abc import ABC, abstractmethod


class DataAnalysisTemplate(ABC):
    """Provides an interface for providing various types of data analysis"""

    @abstractmethod
    def load_input_data(self):
        """Provides for data to be loaded into the instance"""

    # pylint: disable=locally-disabled, invalid-name
    def load_AI_data(self):
        """Loads an generic AI model by default in this example"""
        print("AI data loaded.")

    @abstractmethod
    def transform_data(self):
        """
        Allows data to be transformed using the loaded data, AI model, and 
        potentially other sources
        """

    def generate_report(self):
        """Generates output that human consumers can read/understand based on transformed data"""

        self.load_input_data()
        self.load_AI_data()
        self.transform_data()
        print("Generating report... Done!")


class WebTrafficDataAnalysis(DataAnalysisTemplate):
    """Provides ability to perform analysis on web server logs"""

    def load_input_data(self):
        print("Web logs parsed and data loaded.")

    def transform_data(self):
        print("Web data transformed to match AI model input.")


class FootTrafficDataAnalysis(DataAnalysisTemplate):
    """Provides ability to perform analysis on retail foot traffic"""

    def load_input_data(self):
        print("Foot traffic data loaded.")

    def transform_data(self):
        print("Foot traffic data has been transformed to match AI model input.")


class PreSalesDataAnalysis(DataAnalysisTemplate):
    """Provides ability to perform analysis on pre sales data gathered by marketing department"""
    def load_input_data(self):
        print("Pre sales data loaded.")

    def load_AI_data(self):
        print("AI model has been loaded with additional parameters for sales data.")

    def transform_data(self):
        print("Pre sales data has been transformed to match pre sales AI model.")

def demo_template_method_pattern():
    """Demo the Template Method design pattern as implemented using the classes above"""
    algorithms_to_execute = [WebTrafficDataAnalysis, FootTrafficDataAnalysis, PreSalesDataAnalysis]

    for algorithm in algorithms_to_execute:
        algorithm().generate_report()
        print("")


if __name__ == "__main__":
    demo_template_method_pattern()
