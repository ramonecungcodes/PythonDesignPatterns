from abc import ABC, abstractmethod


class DataAnalysisTemplate(ABC):
    @abstractmethod
    def load_input_data(self):
        pass

    def load_AI_data(self):
        print("AI data loaded.")
    
    @abstractmethod
    def transform_data(self):
        pass
    
    def generate_report(self):
        self.load_input_data()
        self.load_AI_data()
        self.transform_data()
        print("Generating report... Done!")


class WebTrafficDataAnalysis(DataAnalysisTemplate):
    def load_input_data(self):
        print("Web logs parsed and data loaded.")
    
    def transform_data(self):
        print("Web data transformed to match AI model input.")


class FootTrafficDataAnalysis(DataAnalysisTemplate):
    def load_input_data(self):
        print("Foot traffic data loaded.")
    
    def transform_data(self):
        print("Foot traffic data has been transformed to match AI model input.")


class PreSalesDataAnalysis(DataAnalysisTemplate):
    def load_input_data(self):
        print("Pre sales data loaded.")
    
    def load_AI_data(self):
        print("AI model has been loaded with additional parameters for sales data.")
    
    def transform_data(self):
        print("Pre sales data has been transformed to match pre sales AI model.")

def demo_template_method_pattern():
    algorithms_to_execute = [WebTrafficDataAnalysis, FootTrafficDataAnalysis, PreSalesDataAnalysis]

    for algorithm in algorithms_to_execute:
        algorithm().generate_report()
        print("")
    

if __name__ == "__main__":
    demo_template_method_pattern()
